#!/usr/bin/env python3
"""
Minimal run: 3GPP TDL + OFDMChannel (time-varying taps / Doppler via speed range).

Usage (from repo root):
  PYTHONPATH=sionna-main/src python3 sionna-main/scripts/sionna_advanced_channel_demo.py

Or after: pip install -e sionna-main
  python3 sionna-main/scripts/sionna_advanced_channel_demo.py
"""
from __future__ import annotations

import os
import sys

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_SRC = os.path.join(_ROOT, "src")
if _SRC not in sys.path:
    sys.path.insert(0, _SRC)

import tensorflow as tf


def main() -> None:
    tf.config.run_functions_eagerly(True)

    from sionna.phy.ofdm import ResourceGrid
    from sionna.phy.channel.tr38901 import TDL
    from sionna.phy.channel import OFDMChannel

    batch = 1
    fft_size = 64
    num_ofdm_symbols = 14
    subcarrier_spacing = 30e3
    carrier_frequency = 3.5e9
    delay_spread = 100e-9
    min_speed = 0.0
    max_speed = 30.0
    num_tx_ant = 2
    num_rx_ant = 2

    tdl = TDL(
        "A",
        delay_spread=delay_spread,
        carrier_frequency=carrier_frequency,
        min_speed=min_speed,
        max_speed=max_speed,
        num_rx_ant=num_rx_ant,
        num_tx_ant=num_tx_ant,
    )

    rg = ResourceGrid(
        num_ofdm_symbols=num_ofdm_symbols,
        fft_size=fft_size,
        subcarrier_spacing=subcarrier_spacing,
        num_tx=1,
        num_streams_per_tx=num_tx_ant,
        cyclic_prefix_length=rg_cp_len(fft_size, subcarrier_spacing),
    )

    channel = OFDMChannel(tdl, rg, return_channel=True)

    x = tf.complex(
        tf.random.normal([batch, 1, num_tx_ant, num_ofdm_symbols, fft_size]),
        tf.random.normal([batch, 1, num_tx_ant, num_ofdm_symbols, fft_size]),
    )
    x = x * tf.cast(tf.math.rsqrt(tf.reduce_mean(tf.abs(x) ** 2)), x.dtype)

    no = tf.constant(1e-3, tf.float32)
    y, h_freq = channel(x, no=no)

    p_in = float(tf.reduce_mean(tf.abs(x) ** 2))
    p_out = float(tf.reduce_mean(tf.abs(y) ** 2))
    p_h = float(tf.reduce_mean(tf.abs(h_freq) ** 2))

    print("Sionna advanced channel demo (TDL-A + OFDMChannel)")
    print(f"  carrier={carrier_frequency/1e9:.2f} GHz, SCS={subcarrier_spacing/1e3:.0f} kHz")
    print(f"  delay_spread={delay_spread*1e9:.0f} ns, speed [{min_speed},{max_speed}] m/s (Doppler range)")
    print(f"  MIMO {num_tx_ant}x{num_rx_ant}, FFT={fft_size}, symbols={num_ofdm_symbols}")
    print(f"  E[|x|^2]={p_in:.4f}, E[|y|^2]={p_out:.4f}, E[|H|^2]={p_h:.4f} (with noise no={float(no):g})")
    print("OK.")


def rg_cp_len(fft_size: int, scs: float) -> int:
    """Normal CP length for 30 kHz-ish numerology (same idea as LTE/NR short CP)."""
    # Sionna ResourceGrid expects cyclic_prefix_length; use ~7% of FFT for demo
    return max(fft_size // 8, 4)


if __name__ == "__main__":
    main()
