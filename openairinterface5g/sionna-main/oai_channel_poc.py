import os
import sys

import numpy as np
import tensorflow as tf

"""
Sionna의 RayleighBlockFading 채널을 사용해
단일 complex 채널 계수 1개를 생성하고,
OAI 프로젝트 루트에 텍스트 파일로 저장하는 스크립트입니다.

- 경로: ~/바탕화면/Project_embedding/openairinterface5g/sionna-main/oai_channel_poc.py
- 출력 파일: ../channel_coeff.txt
"""


def _make_sionna_channel():
  r"""
  Rayleigh block-fading SISO(1x1) 채널 하나를 생성해서
  complex 계수 텐서 H를 반환합니다.
  """

  # pip로 설치된 sionna 패키지를 사용
  from sionna.channel import RayleighBlockFading

  # TensorFlow 2.x 즉시 실행 모드 보장
  tf.config.run_functions_eagerly(True)

  # SISO: num_tx=1, num_rx=1, 안테나는 1x1
  num_tx = 1
  num_rx = 1
  num_tx_ant = 1
  num_rx_ant = 1

  # RayleighBlockFading은 (num_rx, num_rx_ant, num_tx, num_tx_ant)를 인자로 받고,
  # 호출 시 (batch_size, num_time_steps)를 받습니다.
  chan = RayleighBlockFading(num_rx=num_rx,
                             num_rx_ant=num_rx_ant,
                             num_tx=num_tx,
                             num_tx_ant=num_tx_ant)

  batch_size = 1
  num_time_steps = 1

  # h: [B, num_rx, num_rx_ant, num_tx, num_tx_ant, 1, num_time_steps]
  h, _ = chan(batch_size=batch_size, num_time_steps=num_time_steps)

  return h


def main():
  # Sionna 채널에서 complex 계수 1개 추출
  h = _make_sionna_channel()

  # shape: [1, num_rx, num_tx] 이라고 가정하고 첫 번째 계수만 사용
  h0 = h[0, 0, 0]
  h_real = float(tf.math.real(h0).numpy())
  h_imag = float(tf.math.imag(h0).numpy())

  # 출력 파일 경로: sionna-main 기준 상위 디렉토리(OAI 루트)로 올라가서 channel_coeff.txt 생성
  script_dir = os.path.dirname(os.path.abspath(__file__))
  project_root = os.path.abspath(os.path.join(script_dir, ".."))
  out_path = os.path.join(project_root, "channel_coeff.txt")

  # 디렉토리가 존재한다고 가정 (OAI 루트)
  with open(out_path, "w") as f:
    f.write(f"{h_real} {h_imag}\n")

  print(f"[oai_channel_poc] Wrote channel coefficient to {out_path}: {h_real} {h_imag}")


if __name__ == "__main__":
  main()

