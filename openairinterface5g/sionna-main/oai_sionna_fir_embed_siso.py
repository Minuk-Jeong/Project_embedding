#!/usr/bin/env python3
# SPDX-License-Identifier: Apache-2.0
"""
SISO(1x1) 전용 Sionna FIR 임베드 모듈.

rfsimulator에서 OAI_SIONNA_FIR_MODULE=oai_sionna_fir_embed_siso 로 지정하면
이 모듈의 get_fir_snapshot()을 호출한다.
"""

from __future__ import annotations

import os
from typing import List, Optional

import numpy as np

import oai_sionna_fir_taps as fir_taps

_inited = False
_seq = 0
_sync_cache_seq: int = -1
_sync_cache_list: Optional[List] = None


def _fir_sync_path() -> str:
    return os.getenv("OAI_SIONNA_FIR_SYNC_FILE", "").strip()


def _read_fir_snapshot_v1(path: str) -> list:
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
    # SISO 전용 모듈: 인자를 받아도 항상 1x1로 동작
    global _inited
    _ = (num_rx_ant, num_tx_ant, kwargs)
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
    반환 포맷: [seq, L, nr, nt, fs_hz, re, im, ...]
    순서: tx -> rx -> tap, 파일 v1과 동일
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
        family, 1, 1, fs_hz, fc_hz, l_cap, tdl_ts_idx, tdl_num_ts
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
