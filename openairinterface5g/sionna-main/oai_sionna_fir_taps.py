#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""
Sionna TDL (or Rayleigh block) → 이산 FIR 탭 h[l] 생성 → OAI rfsimulator chanmod용 스냅샷 파일.

`oai_channel_embed.py`는 수정하지 않는다. 이 모듈만으로 TDL을 호출하고,
다경로 계수를 샘플 인덱스로 양자화해 `channel_desc_t::ch`와 동일한 순서로 v1 스냅샷을 쓴다.

OAI rfsimulator 측 FIR은 `OAI_SIONNA_FIR_EMBED=1`(in-process)이 기본 경로다.
gNB·UE가 **같은** 탭을 쓰려면 `OAI_SIONNA_FIR_SYNC_FILE`을 동일 경로로 두고, 이 스크립트로
그 파일을 주기적으로 갱신하면 `oai_sionna_fir_embed`가 seq를 읽어 `channel_desc_t::ch`에 반영한다.
기본 동작은 sleep 없이 Sionna를 매 스텝 호출해 파일을 갱신한다. `--period` / OAI_SIONNA_FIR_PERIOD_S 로 스로틀 가능.

파일 포맷 v1 (텍스트):
  v1
  <seq>
  <L> <nr> <nt> <fs_hz>
  # 이후 nt * nr * L 줄: 각 줄 re im (double)
  # 순서: tx=0..Nt-1, rx=0..Nr-1, l=0..L-1  → C에서 ch[rx + tx*nb_rx][l]
"""

from __future__ import annotations

import argparse
import math
import os
import tempfile
import time
from typing import Optional, Tuple

import numpy as np

try:
    import tensorflow as tf
except ImportError as e:  # pragma: no cover
    raise SystemExit("TensorFlow required: pip install tensorflow") from e


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


def _resolve_throttle_s(cli_period: Optional[float]) -> float:
    """0 = no sleep (run Sionna back-to-back). >0 = sleep that many seconds between writes."""
    if cli_period is not None:
        return max(0.0, float(cli_period))
    v = os.getenv("OAI_SIONNA_FIR_PERIOD_S", "").strip()
    if v:
        try:
            return max(0.0, float(v))
        except ValueError:
            pass
    return 0.0


def _resolve_log_seq_mod() -> int:
    """Print producer-side Updated H once per seq modulo N."""
    v = os.getenv("OAI_SIONNA_LOG_SEQ_MOD", "").strip()
    if not v:
        v = os.getenv("OAI_SIONNA_LOG_EVERY_UPDATES", "").strip()
    try:
        n = int(v) if v else 100
    except ValueError:
        n = 100
    return max(1, n)


def multipath_to_fir_taps(
    a_rx_tx_p: np.ndarray,
    tau_p: np.ndarray,
    fc_hz: float,
    fs_hz: float,
    l_cap: int,
) -> np.ndarray:
    """
    경로별 복소 이득 a[rx,tx,p], 지연 tau[p] (초) → FIR h[tx,rx,l].

    탭 l = round(tau_p * fs); 계수에 exp(-j 2π fc τ) 곱해 베이스밴드 위상 정합.
    """
    if l_cap < 1:
        raise ValueError("l_cap must be >= 1")
    nr, nt, npath = a_rx_tx_p.shape
    if tau_p.shape != (npath,):
        raise ValueError(f"tau_p shape {tau_p.shape} != ({npath},)")
    h = np.zeros((nt, nr, l_cap), dtype=np.complex128)
    for rx in range(nr):
        for tx in range(nt):
            for p in range(npath):
                delay_s = float(tau_p[p])
                lidx = int(round(delay_s * fs_hz))
                if lidx < 0 or lidx >= l_cap:
                    continue
                phase = np.exp(-1j * 2.0 * math.pi * fc_hz * delay_s)
                h[tx, rx, lidx] += np.complex128(a_rx_tx_p[rx, tx, p]) * phase
    return h.astype(np.complex64)


def write_fir_snapshot_v1(path: str, taps_nt_nr_l: np.ndarray, seq: int, fs_hz: float) -> None:
    """taps_nt_nr_l: complex64 (Nt, Nr, L). Write temp file then os.replace (atomic on POSIX)."""
    nt, nr, L = taps_nt_nr_l.shape
    d = os.path.dirname(os.path.abspath(path)) or "."
    fd, tmp = tempfile.mkstemp(prefix=".oai_fir_", suffix=".tmp", dir=d, text=True)
    try:
        with os.fdopen(fd, "w", encoding="ascii") as f:
            f.write("v1\n")
            f.write(f"{seq}\n")
            f.write(f"{L} {nr} {nt} {fs_hz}\n")
            for tx in range(nt):
                for rx in range(nr):
                    for ell in range(L):
                        z = taps_nt_nr_l[tx, rx, ell]
                        f.write(f"{float(np.real(z))} {float(np.imag(z))}\n")
        os.replace(tmp, path)
        tmp = ""
    finally:
        if tmp:
            try:
                os.unlink(tmp)
            except OSError:
                pass


def run_tdl_once(
    num_rx: int,
    num_tx: int,
    fs_hz: float,
    fc_hz: float,
    l_cap: int,
    time_step_index: int,
    num_time_steps: int,
) -> Tuple[np.ndarray, np.ndarray]:
    from sionna.channel.tr38901 import TDL

    model = os.getenv("OAI_SIONNA_TDL_MODEL", "A")
    delay_spread = _env_float("OAI_SIONNA_DELAY_SPREAD_S", 100e-9)
    max_spd_raw = os.getenv("OAI_SIONNA_MAX_SPEED_MPS", "").strip()
    max_speed = None if max_spd_raw == "" else float(max_spd_raw)

    tdl = TDL(
        model=model,
        delay_spread=delay_spread,
        carrier_frequency=fc_hz,
        num_sinusoids=_env_int("OAI_SIONNA_TDL_NUM_SINUSOIDS", 20),
        min_speed=_env_float("OAI_SIONNA_MIN_SPEED_MPS", 0.0),
        max_speed=max_speed,
        num_rx_ant=num_rx,
        num_tx_ant=num_tx,
    )
    h, tau = tdl(batch_size=1, num_time_steps=num_time_steps, sampling_frequency=fs_hz)
    ts_idx = int(time_step_index) % int(num_time_steps)
    # a: [B, num_rx_link, num_rx_ant, num_tx_link, num_tx_ant, P, T]
    a0 = h[0, 0, :, 0, :, :, ts_idx].numpy()
    tau0 = tau[0, 0, 0, :].numpy()
    return a0, tau0


def run_rayleigh_block_once(num_rx: int, num_tx: int) -> Tuple[np.ndarray, np.ndarray]:
    from sionna.channel import RayleighBlockFading

    ch = RayleighBlockFading(num_rx=1, num_rx_ant=num_rx, num_tx=1, num_tx_ant=num_tx)
    h, _tau = ch(batch_size=1, num_time_steps=1)
    # h: [B, num_rx, num_rx_ant, num_tx, num_tx_ant, 1, T]
    h0 = h[0, 0, :, 0, :, 0, 0].numpy()
    a0 = np.zeros((num_rx, num_tx, 1), dtype=np.complex128)
    for rx in range(num_rx):
        for tx in range(num_tx):
            a0[rx, tx, 0] = h0[rx, tx]
    tau0 = np.zeros((1,), dtype=np.float64)
    return a0, tau0


def build_taps_from_sionna(
    family: str,
    num_rx: int,
    num_tx: int,
    fs_hz: float,
    fc_hz: float,
    l_cap: int,
    tdl_ts_idx: int,
    tdl_num_ts: int,
) -> np.ndarray:
    family_u = family.strip().upper()
    if family_u == "TDL":
        a0, tau0 = run_tdl_once(num_rx, num_tx, fs_hz, fc_hz, l_cap, tdl_ts_idx, tdl_num_ts)
    elif family_u == "RAYLEIGH_BLOCK":
        a0, tau0 = run_rayleigh_block_once(num_rx, num_tx)
    else:
        raise ValueError(f"Unsupported OAI_SIONNA_CHANNEL_FAMILY={family}")
    if a0.ndim != 3:
        raise RuntimeError(f"unexpected a shape {a0.shape}")
    taps = multipath_to_fir_taps(a0.astype(np.complex128), tau0, fc_hz, fs_hz, l_cap)
    scale = _env_float("OAI_SIONNA_FIR_SCALE", 1.0)
    if scale != 1.0:
        taps = (taps * np.float32(scale)).astype(np.complex64)
    return taps


def main() -> None:
    tf.config.run_functions_eagerly(True)
    tf.config.threading.set_intra_op_parallelism_threads(1)
    tf.config.threading.set_inter_op_parallelism_threads(1)
    try:
        tf.config.set_visible_devices([], "GPU")
    except Exception:
        pass

    ap = argparse.ArgumentParser(
        description="Write v1 FIR snapshot for OAI_SIONNA_FIR_SYNC_FILE (Sionna TDL / Rayleigh)."
    )
    ap.add_argument("--out", default="/tmp/oai_rfsim_fir.txt", help="Path (often same as OAI_SIONNA_FIR_SYNC_FILE)")
    ap.add_argument(
        "--period",
        type=float,
        default=None,
        metavar="SEC",
        help="Optional throttle: sleep SEC after each write (default 0 = continuous). Env OAI_SIONNA_FIR_PERIOD_S.",
    )
    ap.add_argument("--once", action="store_true", help="Single write and exit")
    args = ap.parse_args()

    throttle_s = _resolve_throttle_s(args.period)
    num_rx = _env_int("OAI_SIONNA_RX_ANT", 1)
    num_tx = _env_int("OAI_SIONNA_TX_ANT", 1)
    fs_hz = _env_float("OAI_SIONNA_SAMPLING_HZ", 61.44e6)
    fc_hz = _env_float("OAI_SIONNA_CARRIER_HZ", 3.6192e9)
    l_cap = _env_int("OAI_SIONNA_FIR_L_CAP", 64)
    family = os.getenv("OAI_SIONNA_CHANNEL_FAMILY", "TDL")
    tdl_ts_idx = _env_int("OAI_SIONNA_TDL_TIME_STEP_INDEX", 0)
    tdl_num_ts = max(1, _env_int("OAI_SIONNA_TDL_NUM_TIME_STEPS", 1))
    log_seq_mod = _resolve_log_seq_mod()

    mode = f"throttle_s={throttle_s}" if throttle_s > 0 else "continuous (no sleep between Sionna steps)"
    print(
        f"[oai_sionna_fir_taps] out={args.out} {mode} once={args.once} -> sync file seq advances for FIR embed",
        flush=True,
    )
    seq = 0
    while True:
        taps = build_taps_from_sionna(family, num_rx, num_tx, fs_hz, fc_hz, l_cap, tdl_ts_idx, tdl_num_ts)
        write_fir_snapshot_v1(args.out, taps, seq, fs_hz)
        if args.once or (seq % log_seq_mod == 0):
            z00 = taps[0, 0, 0] if taps.size > 0 else np.complex64(0.0 + 0.0j)
            extra = ""
            if num_rx >= 2 and num_tx >= 2 and taps.shape[0] >= 2 and taps.shape[1] >= 2:
                z11 = taps[1, 1, 0]
                extra = (
                    f" H[1,1]={float(np.real(z11)):.6f} + j{float(np.imag(z11)):.6f}"
                )
            print(
                "[SIONNA][FIR_PRODUCER] Updated H "
                f"seq={seq} ({num_rx}x{num_tx}), "
                f"H[0,0]={float(np.real(z00)):.6f} + j{float(np.imag(z00)):.6f}"
                f"{extra} "
                f"(L={taps.shape[2]}, out={args.out})",
                flush=True,
            )
        seq += 1
        if args.once:
            break
        if throttle_s > 0:
            time.sleep(throttle_s)
        else:
            try:
                os.sched_yield()
            except AttributeError:
                pass


if __name__ == "__main__":
    main()
