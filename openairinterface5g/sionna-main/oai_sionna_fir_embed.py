#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""
Sionna → FIR 탭 → OAI chanmod (in-process).

rfsimulator가 OAI_PYTHON_EMBED 빌드이고 OAI_SIONNA_FIR_EMBED=1 일 때 이 모듈을 import하여
get_fir_snapshot()으로 탭을 넘긴다. 수학은 oai_sionna_fir_taps.build_taps_from_sionna 와 동일.

실행 cwd가 저장소 루트가 아닐 때(예: cmake_targets/ran_build/build)는 환경변수
OAI_SIONNA_REPO_ROOT=/절대경로/openairinterface5g 를 설정해 sionna-main/ 을 찾게 한다.

gNB/UE가 **같은** FIR을 쓰려면 프로세스가 둘이라 각자 Sionna RNG가 갈라진다.
OAI_SIONNA_FIR_SYNC_FILE=/path/to/v1.txt 를 gNB·UE **동일 경로**로 두고,
oai_sionna_fir_taps.py 로 그 파일의 seq를 갱신하면 양쪽이 같은 스냅샷을 읽는다.

MIMO(Nt×Nr)는 OAI_SIONNA_RX_ANT / OAI_SIONNA_TX_ANT(또는 rfsimulator가 넘기는 init 인자)와
conf RU의 nb_rx/nb_tx·chanmod `channel_desc` 차원이 일치해야 한다 (`rfsim_apply_embedded_fir_taps` 검사).
"""

from __future__ import annotations

import os
from typing import List, Optional

import numpy as np

import oai_sionna_fir_taps as fir_taps

_inited = False
_seq = 0
_num_rx = 1
_num_tx = 1
_sync_cache_seq: int = -1
_sync_cache_list: Optional[List] = None


def _fir_sync_path() -> str:
    return os.getenv("OAI_SIONNA_FIR_SYNC_FILE", "").strip()


def _read_fir_snapshot_v1(path: str) -> list:
    """v1 텍스트 스냅샷 읽기 (write_fir_snapshot_v1 과 동일 포맷). seq 동일 시 캐시 반환."""
    global _sync_cache_seq, _sync_cache_list
    with open(path, "r", encoding="ascii") as f:
        if f.readline().strip() != "v1":
            raise ValueError("FIR sync file: expected v1")
        seq = int(f.readline().strip())
        if seq == _sync_cache_seq and _sync_cache_list is not None:
            return _sync_cache_list
        parts = f.readline().split()
        if len(parts) < 4:
            raise ValueError("FIR sync file: bad L nr nt fs line")
        L, nr, nt, fs_hz = int(parts[0]), int(parts[1]), int(parts[2]), float(parts[3])
        ncoef = nt * nr * L
        out: list = [seq, L, nr, nt, fs_hz]
        for _ in range(ncoef):
            line = f.readline()
            if not line:
                raise ValueError("FIR sync file: short coefficient data")
            re_im = line.split()
            if len(re_im) < 2:
                raise ValueError("FIR sync file: bad tap line")
            out.append(float(re_im[0]))
            out.append(float(re_im[1]))
        _sync_cache_seq = seq
        _sync_cache_list = out
        return out


def init(num_rx_ant: int = 1, num_tx_ant: int = 1, **kwargs):
    global _inited, _num_rx, _num_tx
    _num_rx = int(num_rx_ant)
    _num_tx = int(num_tx_ant)
    if _inited:
        return
    if _fir_sync_path():
        _inited = True
        return
    import tensorflow as tf

    tf.config.run_functions_eagerly(True)
    tf.config.threading.set_intra_op_parallelism_threads(1)
    tf.config.threading.set_inter_op_parallelism_threads(1)
    try:
        tf.config.set_visible_devices([], "GPU")
    except Exception:
        pass
    _inited = True


def get_fir_snapshot():
    """
    C(rfsimulator)가 기대하는 리스트:
      [seq, L, nr, nt, fs_hz, re, im, ...]  (tx, rx, l 순, 파일 v1과 동일)
    """
    global _seq
    sp = _fir_sync_path()
    if sp:
        return _read_fir_snapshot_v1(sp)

    fs_hz = fir_taps._env_float("OAI_SIONNA_SAMPLING_HZ", 61.44e6)
    fc_hz = fir_taps._env_float("OAI_SIONNA_CARRIER_HZ", 3.6192e9)
    l_cap = fir_taps._env_int("OAI_SIONNA_FIR_L_CAP", 64)
    family = os.getenv("OAI_SIONNA_CHANNEL_FAMILY", "TDL")
    tdl_ts_idx = fir_taps._env_int("OAI_SIONNA_TDL_TIME_STEP_INDEX", 0)
    tdl_num_ts = max(1, fir_taps._env_int("OAI_SIONNA_TDL_NUM_TIME_STEPS", 1))

    taps = fir_taps.build_taps_from_sionna(
        family, _num_rx, _num_tx, fs_hz, fc_hz, l_cap, tdl_ts_idx, tdl_num_ts
    )
    nt, nr, L = taps.shape
    cur = _seq
    _seq += 1

    out: list = [cur, L, nr, nt, fs_hz]
    for tx in range(nt):
        for rx in range(nr):
            for ell in range(L):
                z = taps[tx, rx, ell]
                out.append(float(np.real(z)))
                out.append(float(np.imag(z)))
    return out
