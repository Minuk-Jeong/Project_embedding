"""
oai_channel_embed.get_h_flat() 결과에 대한 지표 (실험·로그 상관용).

기존 oai_channel_embed.py 는 수정하지 않고, 이 모듈에서 import 해서 쓴다.
"""

from __future__ import annotations

import math


def frobenius_norm_from_flat(h_flat: list[float]) -> float:
    """
    h_flat: [re00, im00, re01, im01, ...] (복소 행렬 row-major)
    반환: ||H||_F (실수; 각 원소는 re+j im)
    """
    if len(h_flat) % 2 != 0:
        raise ValueError("h_flat length must be even")
    s = 0.0
    for i in range(0, len(h_flat), 2):
        re = h_flat[i]
        im = h_flat[i + 1]
        s += re * re + im * im
    return math.sqrt(s)


def h00_from_flat(h_flat: list[float]) -> tuple[float, float]:
    """첫 원소 (0,0) 의 (re, im)."""
    if len(h_flat) < 2:
        raise ValueError("h_flat too short")
    return float(h_flat[0]), float(h_flat[1])


def metrics_line(h_flat: list[float]) -> str:
    """로그 한 줄용 문자열."""
    nf = frobenius_norm_from_flat(h_flat)
    re00, im00 = h00_from_flat(h_flat)
    return f"||H||_F={nf:.6f} H00={re00:.6f}+j{im00:.6f}"


def sample_metrics_from_embed() -> str:
    """oai_channel_embed 가 초기화된 뒤 한 번 호출."""
    import oai_channel_embed as oce

    hf = oce.get_h_flat()
    return metrics_line(hf)
