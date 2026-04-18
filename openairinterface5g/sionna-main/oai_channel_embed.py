import os
import threading
import math

import numpy as np
import tensorflow as tf

"""
OAI에서 Python 임베딩으로 import해서 호출하는 모듈.

핵심 포인트:
- 프로세스 시작 시 1회 init() 호출로 Sionna 채널 객체를 생성/캐시
- 이후 get_coeff() / get_h_flat()로 계수 또는 MIMO H 평탄 벡터 반환

TDL 전체 옵션은 환경변수로 (Sionna TDL __init__ 대응):
  OAI_SIONNA_TDL_NUM_SINUSOIDS, OAI_SIONNA_TDL_LOS_AO_DEG / _RAD,
  OAI_SIONNA_PRECISION, OAI_SIONNA_TDL_{RX,TX,SPATIAL}_CORR_NPY,
  OAI_SIONNA_TDL_NUM_TIME_STEPS, OAI_SIONNA_TDL_TIME_STEP_MODE, _TIME_STEP_INDEX,
  OAI_SIONNA_MAX_SPEED_MPS 비우면 max_speed=None.

주의:
- TensorFlow/Sionna 초기화 비용이 크므로 매 호출마다 import/객체 생성하지 않도록 설계
- OAI rfsim은 get_h_flat()의 주파수 평탄 H만 사용; 서브캐리어 전역은 Sionna OFDM 경로 별도.
"""

_lock = threading.Lock()
_inited = False
_chan = None
_num_rx_ant = 1
_num_tx_ant = 1
_channel_family = "RAYLEIGH_BLOCK"
_carrier_frequency_hz = 3.6192e9
_sampling_frequency_hz = 61.44e6
# get_h_flat()마다 증가; TDL/CDL + OAI_SIONNA_TDL_TIME_STEP_MODE=cycle 일 때만 사용
_tdl_time_step_cycle = 0


def _env_float(name: str, default: float) -> float:
    v = os.getenv(name)
    if v is None or v == "":
        return float(default)
    try:
        return float(v)
    except ValueError:
        return float(default)


def _env_int(name: str, default: int) -> int:
    v = os.getenv(name)
    if v is None or v == "":
        return int(default)
    try:
        return int(v)
    except ValueError:
        return int(default)


def _optional_precision():
    """Sionna TDL/CDL `precision`: None | 'single' | 'double'."""
    v = os.getenv("OAI_SIONNA_PRECISION", "").strip().lower()
    if v in ("single", "double"):
        return v
    return None


def _tdl_los_aoa_radians() -> float:
    """
    LoS TDL 모델의 도래각 [rad]. Sionna 기본은 pi/4.
    `OAI_SIONNA_TDL_LOS_AO_DEG`가 있으면 도 단위, 없으면 `OAI_SIONNA_TDL_LOS_AO_RAD`(기본 pi/4).
    """
    deg = os.getenv("OAI_SIONNA_TDL_LOS_AO_DEG", "").strip()
    if deg:
        try:
            return float(deg) * math.pi / 180.0
        except ValueError:
            pass
    return _env_float("OAI_SIONNA_TDL_LOS_AO_RAD", math.pi / 4.0)


def _load_complex_matrix_npy(path: str):
    """
    .npy에 complex64/complex128 또는 (re,im) 실수 쌍이 저장된 경우 로드.
    실패 시 None.
    """
    if not path or not path.strip():
        return None
    path = path.strip()
    if not os.path.isfile(path):
        print(f"[OAI_SIONNA] warning: corr matrix file missing: {path}")
        return None
    try:
        arr = np.load(path, allow_pickle=False)
    except OSError as e:
        print(f"[OAI_SIONNA] warning: np.load failed {path}: {e}")
        return None
    if arr.dtype.kind == "c":
        return tf.constant(arr, dtype=tf.complex64)
    if arr.ndim == 3 and arr.shape[-1] == 2:
        return tf.complex(
            tf.constant(arr[..., 0], dtype=tf.float32),
            tf.constant(arr[..., 1], dtype=tf.float32),
        )
    print(f"[OAI_SIONNA] warning: unsupported array dtype/shape in {path}")
    return None


def _make_single_pol_array(num_ant: int, carrier_frequency_hz: float):
    # Build a simple omni single-polarized array with num_ant elements.
    from sionna.phy.channel.tr38901 import PanelArray
    return PanelArray(
        num_rows_per_panel=1,
        num_cols_per_panel=1,
        polarization="single",
        polarization_type="V",
        antenna_pattern="omni",
        carrier_frequency=carrier_frequency_hz,
        num_rows=1,
        num_cols=int(num_ant),
    )


def init(seed: int | None = None,
         num_rx: int = 1,
         num_tx: int = 1,
         num_rx_ant: int = 1,
         num_tx_ant: int = 1):
    """
    Sionna RayleighBlockFading 채널 객체를 1회 생성합니다.
    """
    global _inited, _chan, _num_rx_ant, _num_tx_ant
    global _channel_family, _carrier_frequency_hz, _sampling_frequency_hz
    with _lock:
        if _inited:
            return True

        if seed is not None:
            tf.random.set_seed(int(seed))

        # eager 모드 보장 (디버깅 및 임베딩 POC 안정성)
        tf.config.run_functions_eagerly(True)
        
        # Python 임베딩 환경에서 TensorFlow 스레드 충돌 방지
        # intra/inter-op parallelism을 1로 제한하여 스레드 풀 생성을 최소화
        tf.config.threading.set_intra_op_parallelism_threads(1)
        tf.config.threading.set_inter_op_parallelism_threads(1)
        # GPU 사용 비활성화 (임베딩 환경에서는 CPU만 사용)
        tf.config.set_visible_devices([], 'GPU')

        _num_rx_ant = int(num_rx_ant)
        _num_tx_ant = int(num_tx_ant)
        _carrier_frequency_hz = _env_float("OAI_SIONNA_CARRIER_HZ", 3.6192e9)
        _sampling_frequency_hz = _env_float("OAI_SIONNA_SAMPLING_HZ", 61.44e6)
        _channel_family = os.getenv("OAI_SIONNA_CHANNEL_FAMILY", "RAYLEIGH_BLOCK").strip().upper()

        if _channel_family == "TDL":
            from sionna.phy.channel.tr38901 import TDL

            max_spd_raw = os.getenv("OAI_SIONNA_MAX_SPEED_MPS", "").strip()
            if max_spd_raw == "":
                max_speed_arg = None
            else:
                try:
                    max_speed_arg = float(max_spd_raw)
                except ValueError:
                    max_speed_arg = 0.0

            spatial = _load_complex_matrix_npy(os.getenv("OAI_SIONNA_TDL_SPATIAL_CORR_NPY", ""))
            rx_corr = _load_complex_matrix_npy(os.getenv("OAI_SIONNA_TDL_RX_CORR_NPY", ""))
            tx_corr = _load_complex_matrix_npy(os.getenv("OAI_SIONNA_TDL_TX_CORR_NPY", ""))
            if spatial is not None:
                rx_corr = None
                tx_corr = None

            tdl_kw = dict(
                model=os.getenv("OAI_SIONNA_TDL_MODEL", "A"),
                delay_spread=_env_float("OAI_SIONNA_DELAY_SPREAD_S", 100e-9),
                carrier_frequency=_carrier_frequency_hz,
                num_sinusoids=_env_int("OAI_SIONNA_TDL_NUM_SINUSOIDS", 20),
                los_angle_of_arrival=_tdl_los_aoa_radians(),
                min_speed=_env_float("OAI_SIONNA_MIN_SPEED_MPS", 0.0),
                max_speed=max_speed_arg,
                num_rx_ant=_num_rx_ant,
                num_tx_ant=_num_tx_ant,
                spatial_corr_mat=spatial,
                rx_corr_mat=rx_corr,
                tx_corr_mat=tx_corr,
                precision=_optional_precision(),
            )
            _chan = TDL(**tdl_kw)
        elif _channel_family == "CDL":
            from sionna.phy.channel.tr38901 import CDL
            direction = os.getenv("OAI_SIONNA_DIRECTION", "downlink").strip().lower()
            bs_array = _make_single_pol_array(_num_tx_ant, _carrier_frequency_hz)
            ut_array = _make_single_pol_array(_num_rx_ant, _carrier_frequency_hz)
            max_spd_c = os.getenv("OAI_SIONNA_MAX_SPEED_MPS", "").strip()
            if max_spd_c == "":
                max_cdl = None
            else:
                try:
                    max_cdl = float(max_spd_c)
                except ValueError:
                    max_cdl = 0.0
            _chan = CDL(
                model=os.getenv("OAI_SIONNA_CDL_MODEL", "A"),
                delay_spread=_env_float("OAI_SIONNA_DELAY_SPREAD_S", 100e-9),
                carrier_frequency=_carrier_frequency_hz,
                ut_array=ut_array,
                bs_array=bs_array,
                direction=direction if direction in ("uplink", "downlink") else "downlink",
                min_speed=_env_float("OAI_SIONNA_MIN_SPEED_MPS", 0.0),
                max_speed=max_cdl,
                precision=_optional_precision(),
            )
        else:
            from sionna.phy.channel import RayleighBlockFading
            _channel_family = "RAYLEIGH_BLOCK"
            _chan = RayleighBlockFading(
                num_rx=int(num_rx),
                num_rx_ant=_num_rx_ant,
                num_tx=int(num_tx),
                num_tx_ant=_num_tx_ant,
            )

        print(
            f"[OAI_SIONNA] init family={_channel_family} rx_ant={_num_rx_ant} tx_ant={_num_tx_ant} "
            f"fc={_carrier_frequency_hz}Hz fs={_sampling_frequency_hz}Hz"
        )

        _inited = True
        return True


def get_coeff() -> tuple[float, float]:
    """
    RayleighBlockFading에서 complex 계수 1개를 생성해서 (re, im)로 반환합니다.
    """
    global _inited, _chan
    if not _inited or _chan is None:
        # 기본 init
        init()

    # h: [B, num_rx, num_rx_ant, num_tx, num_tx_ant, 1, T]
    h, _ = _chan(batch_size=1, num_time_steps=1)
    h0 = h[0, 0, 0, 0, 0, 0, 0]
    re = float(tf.math.real(h0).numpy())
    im = float(tf.math.imag(h0).numpy())
    return re, im


def get_shape() -> tuple[int, int]:
    """
    현재 채널 행렬의 (num_rx_ant, num_tx_ant)를 반환합니다.
    """
    global _inited, _chan, _num_rx_ant, _num_tx_ant
    if not _inited or _chan is None:
        init()
    return int(_num_rx_ant), int(_num_tx_ant)


def get_h_flat() -> list[float]:
    """
    MIMO 채널 행렬을 row-major로 평탄화해서 반환합니다.
    반환 형식: [re00, im00, re01, im01, ..., re(R-1,T-1), im(R-1,T-1)]
    """
    global _inited, _chan, _num_rx_ant, _num_tx_ant
    if not _inited or _chan is None:
        init()

    if _channel_family == "RAYLEIGH_BLOCK":
        # h: [B, num_rx, num_rx_ant, num_tx, num_tx_ant, 1, T]
        h, _ = _chan(batch_size=1, num_time_steps=1)
        h_eff = h[0, 0, :, 0, :, 0, 0]
    else:
        # a: [B, num_rx, num_rx_ant, num_tx, num_tx_ant, num_paths, num_time_steps]
        # tau: [B, num_rx, num_tx, num_paths]
        global _tdl_time_step_cycle
        num_ts = max(1, _env_int("OAI_SIONNA_TDL_NUM_TIME_STEPS", 1))
        mode = os.getenv("OAI_SIONNA_TDL_TIME_STEP_MODE", "fixed").strip().lower()
        if mode == "cycle":
            ts_idx = _tdl_time_step_cycle % num_ts
            _tdl_time_step_cycle += 1
        else:
            ts_idx = _env_int("OAI_SIONNA_TDL_TIME_STEP_INDEX", 0) % num_ts
        a, tau = _chan(
            batch_size=1,
            num_time_steps=num_ts,
            sampling_frequency=_sampling_frequency_hz,
        )
        a0 = a[0, 0, :, 0, :, :, ts_idx]  # [rx_ant, tx_ant, num_paths]
        tau0 = tau[0, 0, 0, :]           # [num_paths]
        arg = -2.0 * math.pi * _carrier_frequency_hz * tau0
        phase = tf.exp(tf.complex(tf.zeros_like(arg), arg))
        h_eff = tf.reduce_sum(a0 * phase[tf.newaxis, tf.newaxis, :], axis=-1)

    out: list[float] = []
    for r in range(_num_rx_ant):
        for t in range(_num_tx_ant):
            hij = h_eff[r, t]
            out.append(float(tf.math.real(hij).numpy()))
            out.append(float(tf.math.imag(hij).numpy()))
    return out


def get_coeff_text() -> str:
    """
    C에서 디버그용으로 문자열 형태가 편할 때 사용: "re im"
    """
    re, im = get_coeff()
    return f"{re} {im}"

