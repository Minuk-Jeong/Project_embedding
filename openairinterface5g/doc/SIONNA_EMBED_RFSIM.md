### 목적

`nr-softmodem`/`nr-uesoftmodem`가 사용하는 `rfsimulator` 디바이스 안에서 **Python을 임베딩**해 Sionna가 만든 **복소수 MIMO 채널 행렬 H**를 생성하고, 이를 **실제 IQ 샘플에 곱해 적용**하는 POC입니다.

### 핵심 요약 (지금 구현된 상태)

- **MIMO H 생성**: `sionna-main/oai_channel_embed.py` (`get_h_flat()`)
- **H 적용 위치**: `radio/rfsimulator/simulator.c`의 “no channel modeling” 경로에서 MIMO 합성 시 `y += H * x` 복소수 곱 적용
- **활성화**: 환경변수 `OAI_SIONNA_RFSIM_APPLY=1`
- **2x2 설정**: gNB conf의 RU `nb_tx/nb_rx` + 논리 포트(`pdsch_AntennaPorts_*`, `pusch_AntennaPorts`)까지 같이 맞춰야 UE가 PBCH를 정상 디코드

---

### 빌드

프로젝트 루트에서:

```bash
cd /home/lab/바탕화면/Project_embedding/openairinterface5g
./cmake_targets/build_oai --gNB --nrUE --ninja --cmake-opt "-DOAI_PYTHON_EMBED=ON" -w SIMU
```

---

### gNB 설정 파일 분리 (SISO / 2x2)

- **SISO(기본)**: `targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.band78.fr1.106PRB.pci0.rfsim.conf`
- **2x2**: `targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.band78.fr1.106PRB.pci0.rfsim.2x2.conf`

2x2에서 UE가 PBCH를 정상 디코드하려면, **RU 물리 체인(`nb_tx/nb_rx`) + 논리 포트(`pdsch_AntennaPorts_*`, `pusch_AntennaPorts`, `maxMIMO_Layers`)**가 함께 맞아야 합니다. 위 2x2 conf에 반영되어 있습니다.

---

### 실행 (Baseline, 채널 적용 OFF)

#### gNB

```bash
./cmake_targets/ran_build/build/nr-softmodem \
  -O targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.band78.fr1.106PRB.pci0.rfsim.2x2.conf \
  --gNBs.[0].min_rxtxtime 6 --rfsim --noS1 2>&1 | tee gnb.log
```

#### UE (2x2)

```bash
./cmake_targets/ran_build/build/nr-uesoftmodem \
  --rfsim --noS1 --rfsimulator.serveraddr 127.0.0.1 \
  --ue-nb-ant-rx 2 --ue-nb-ant-tx 2 \
  -C 3619200000 -r 106 --numerology 1 --band 78 --ssb 516 2>&1 | tee ue.log
```

---

### 실행 (Sionna 채널 적용 ON)

`rfsimulator`에서 채널을 적용하려면 **gNB/UE 둘 다** 동일 환경변수를 켜는 것을 권장합니다.

권장 환경변수:

- `OAI_SIONNA_RFSIM_APPLY=1`: 적용 ON
- `OAI_SIONNA_RX_ANT=2`, `OAI_SIONNA_TX_ANT=2`: H 크기(기본은 OAI의 rx/tx 채널 수)
- `OAI_SIONNA_DIAG_ONLY=1`: 초기 안정화를 위해 **대각만 적용**(기본 ON)
- `OAI_SIONNA_SCALE=1.0`: 스케일(기본 1.0)
- `OAI_SIONNA_UPDATE_US=5000000`: H 갱신 주기(us, 기본 5초). 갱신할 때마다 `[SIONNA][RFSIM] Updated H` 로그 1줄.

#### TDL (`OAI_SIONNA_CHANNEL_FAMILY=TDL`) 추가 옵션

Sionna `TDL` 생성자 인자를 환경변수로 넘길 수 있습니다 (`oai_channel_embed.py`).

| 환경변수 | 의미 |
|----------|------|
| `OAI_SIONNA_TDL_MODEL` | A–E, A30, B100, C300 |
| `OAI_SIONNA_DELAY_SPREAD_S` | RMS 지연 확산 [s] |
| `OAI_SIONNA_MIN_SPEED_MPS` / `OAI_SIONNA_MAX_SPEED_MPS` | 도플러용 속도 [m/s]. **`MAX`를 비우면** Sionna와 같이 `max_speed=None`(min과 동일) |
| `OAI_SIONNA_TDL_NUM_SINUSOIDS` | SoS 개수 (기본 20) |
| `OAI_SIONNA_TDL_LOS_AO_DEG` 또는 `OAI_SIONNA_TDL_LOS_AO_RAD` | LoS 도래각 (LoS 프로파일일 때) |
| `OAI_SIONNA_PRECISION` | `single` / `double` (비우면 Sionna 전역 기본) |
| `OAI_SIONNA_TDL_RX_CORR_NPY` / `OAI_SIONNA_TDL_TX_CORR_NPY` | 수신/송신 **공간 상관** 행렬, `numpy.save`한 `.npy` (복소 또는 `[...,2]` re/im) |
| `OAI_SIONNA_TDL_SPATIAL_CORR_NPY` | 전체 `num_rx*num_tx` 크기 상관행렬. 지정 시 Rx/Tx 개별 행렬은 무시 |
| `OAI_SIONNA_TDL_NUM_TIME_STEPS` | TDL `__call__`의 시간 스텝 수 (기본 1) |
| `OAI_SIONNA_TDL_TIME_STEP_MODE` | `fixed`: `OAI_SIONNA_TDL_TIME_STEP_INDEX` 스텝만 사용 / `cycle`: `get_h_flat` 호출마다 0…N-1 순환 |

OAI rfsim 쪽은 여전히 **캐리어 한 점에서 합친 평탄 MIMO `H`** 만 씁니다. **서브캐리어별 주파수 응답·OFDM 그리드 전체**는 Sionna `OFDMChannel` 등을 **별도 스크립트**에서 돌려야 합니다.

#### gNB

```bash
OAI_SIONNA_RFSIM_APPLY=1 OAI_SIONNA_RX_ANT=2 OAI_SIONNA_TX_ANT=2 \
OAI_SIONNA_DIAG_ONLY=1 OAI_SIONNA_SCALE=1.0 OAI_SIONNA_UPDATE_US=5000000 \
./cmake_targets/ran_build/build/nr-softmodem \
  -O targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.band78.fr1.106PRB.pci0.rfsim.2x2.conf \
  --gNBs.[0].min_rxtxtime 6 --rfsim --noS1 2>&1 | tee gnb_sionna.log
```

#### UE

```bash
OAI_SIONNA_RFSIM_APPLY=1 OAI_SIONNA_RX_ANT=2 OAI_SIONNA_TX_ANT=2 \
OAI_SIONNA_DIAG_ONLY=1 OAI_SIONNA_SCALE=1.0 OAI_SIONNA_UPDATE_US=5000000 \
./cmake_targets/ran_build/build/nr-uesoftmodem \
  --rfsim --noS1 --rfsimulator.serveraddr 127.0.0.1 \
  --ue-nb-ant-rx 2 --ue-nb-ant-tx 2 \
  -C 3619200000 -r 106 --numerology 1 --band 78 --ssb 516 2>&1 | tee ue_sionna.log
```

---

### 로그로 확인할 것

- `gnb*.log` / `ue*.log`:
  - `[SIONNA][RFSIM] Enabled: applying Sionna H to samples (H=2x2)`
  - `[SIONNA][RFSIM] Updated H (2x2), H[0,0]=...`
- UE:
  - `Initial sync: pbch decoded sucessfully`
  - `UE 0 RNTI ... stats ...` (접속 유지)

---

### 다음 단계(확장 아이디어)

- `OAI_SIONNA_DIAG_ONLY=0`로 **full 2x2 mixing** 활성화
- Sionna 모델 변경(예: TDL/CDL) 및 **다중탭/지연**을 `apply_channelmod.c` 경로로 확장
- 채널을 slot/frame 경계에 맞춰 갱신하도록 타이밍 정교화

