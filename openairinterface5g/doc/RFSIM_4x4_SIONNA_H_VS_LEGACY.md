# RFSimulator 4×4: Sionna H 적용 시 vs 기존(레거시) 경로 비교

이 문서는 **OpenAirInterface `radio/rfsimulator/simulator.c`** 기준으로, **다중 안테나(예: 4×4)이고 `chanmod`가 꺼진 경우** 수신 `trx_read`에서 **소켓으로 받은 IQ**를 PHY로 넘기기 직전에 어떻게 달라지는지 정리한다.

---

## 공통 전제

- **역할**: gNB는 서버, UE는 클라이언트 등으로 TCP에 IQ를 주고받는다.
- **송신(`trx_write`)**: Sionna와 무관하게 **원본 IQ를 소켓으로 보낸다** (채널은 수신 쪽에서 적용).
- **수신(`rfsimulator_read`)**: 상대가 보낸 샘플이 **`ptr->circularBuf` (순환 버퍼)** 에 쌓이고, 안테나 수에 따라 **MIMO 믹싱 분기**로 들어간다.
- **4×4**: `nbAnt_tx == 4`, `nbAnt == 4` 이므로 **SiSo용 `memcpy` 최적화 분기가 아닌** 일반 MIMO 루프를 탄다.
- **`ptr->channel_model != NULL`**: rfsimulator 옵션으로 **chanmod**를 켠 경우 **다른 경로(`rxAddInput`)** 로 가며, 아래 Sionna/레거시 분기와는 별개다. (Sionna 실험은 보통 chanmod 없이 진행한다.)

---

## 기존 경로 (레거시 MIMO 믹싱, Sionna 미적용)

**조건**: `OAI_SIONNA_RFSIM_APPLY`가 1이 아니거나, 빌드에 `OAI_PYTHON_EMBED`가 없거나, `sionna_h_flat`/안테나 수 조건이 맞지 않으면 **레거시 `else` 분기**로 떨어진다.

**처리 내용** (복소 샘플이지만 계수는 **실수 스칼라**):

- 송신 안테나 `a_tx`, 수신 안테나 `a_rx`에 대해  
  `ant_diff = |a_tx - a_rx|`  
  `coeff = (ant_diff == 0) ? 1.0 : (0.2 / ant_diff)`
- 각 샘플에 대해  
  `acc_r += x.r * coeff`  
  `acc_i += x.i * coeff`  
  즉 **위상 회전 없이**, 안테나 인덱스 차이에 따른 **고정된 실수 이득**만 곱해 더한다.
- **물리적 Rayleigh/복소 MIMO 채널 모델이 아니다.** rfsim 내부에서 안테나 간 에너지를 나누기 위한 **휴리스틱**에 가깝다.

**코드 위치**: `simulator.c` 내 `rfsimulator_read`, 주석 `Legacy simple MIMO mixing (real scalar)`.

---

## Sionna H 적용 경로

**조건** (동시 만족):

- 빌드: `OAI_PYTHON_EMBED`
- 런타임: `OAI_SIONNA_RFSIM_APPLY=1`
- `t->sionna_h_flat` 유효, `sionna_rx_ant >= nbAnt`, `sionna_tx_ant == nbAnt_tx` (4×4면 둘 다 4)

**H의 출처**:

- **임베딩**: 백그라운드 스레드가 Python 모듈 `oai_channel_embed`의 `get_h_flat()`을 주기적으로 호출한다. 내부는 Sionna **`RayleighBlockFading`** (블록 페이딩).
- **공유 파일**: `OAI_SIONNA_SHARED_FILE`이 설정되면 같은 스레드가 파일 스냅샷을 읽어 `sionna_h_flat`을 갱신한다 (별도 producer 권장).

**처리 내용** (시간 영역, **샘플마다**):

- 인덱스: `(a_rx, a_tx)` → `base = 2 * (a_rx * nbAnt_tx + a_tx)`  
  `h_re, h_im` = `sionna_h_flat[base]`, `sionna_h_flat[base+1]` (row-major 복소 행렬)
- 정규화: `norm = sqrt(nbAnt_tx)`  
  실제 사용 계수: `h * (sionna_scale / norm)` (`OAI_SIONNA_SCALE`, 기본 1.0)
- **`OAI_SIONNA_DIAG_ONLY=1`**(기본값에 가깝게 쓰이는 경우): `a_rx != a_tx`이면 해당 항목 **스킵** → 사실상 **대각 성분만** 사용.
- 각 샘플에 대해 **복소 곱** 누적:  
  `acc_r += x.r * h_re - x.i * h_im`  
  `acc_i += x.r * h_im + x.i * h_re`  
  즉 **\(y \mathrel{+}= h_{rx,tx} \cdot x_{tx}\)** 형태.

**코드 위치**: 같은 함수 내 `#ifdef OAI_PYTHON_EMBED` 블록, 주석 `y += h * x (complex multiply)`.

---

## 한눈에 보는 차이

| 항목 | 레거시 | Sionna H |
|------|--------|----------|
| 계수 | 실수, `|a_tx-a_rx|` 기반 고정 규칙 | 복소, **Rayleigh(임베딩/파일)** 로 뽑은 \(H\) |
| 위상 | 없음 (`x.i`에 같은 실수만 곱함) | 있음 (복소 곱) |
| 시간 변화 | 믹싱 규칙 고정 | `OAI_SIONNA_UPDATE_US` 등으로 **H 주기적 갱신** |
| 4×4 교차항 | 항상 존재(계수만 다름) | `DIAG_ONLY` 시 **비대각 0** |
| PHY CSI | 수신 파형이 레거시 믹싱 결과 | 수신 파형이 **H 적용 후** 결과 → CSI-RS 추정값에 **간접 반영** |

---

## 잡음 (`OAI_RFSIM_AWGN_DBFS`)

- **chanmod 없음**일 때, 선택적으로 수신 버퍼에 AWGN을 더하는 확장 경로가 있다.
- **레거시/Sionna 공통**으로, 해당 블록이 실행되면 **믹싱 이후** 샘플에 가우시안 잡음이 가해진다.
- 값이 **더 0에 가까울수록** 잡음이 세지고, **환경 변수 미설정**이면 이 경로는 동작하지 않는다(기본).

---

## 검증 시 유의사항

- **“적용 여부”**: 로그 `[SIONNA][RFSIM] Enabled` / `Updated H` (또는 shared `seq`) 와 OFF 시 부재로 1차 확인.
- **“수학적 일치”**: 동일 스냅샷의 전체 `H`와 소수 샘플 `x`로 \(Hx\)를 오프라인 재현해 비교하는 방식이 직접적이다.
- **“3GPP 동일 채널”**: 본 구현은 **시간 영역 평탄 MIMO**에 가깝고, OFDM 부캐리어별 주파수 선택 페이딩 전체를 재현한다고 보긴 어렵다.

---

## 참고 파일

- `radio/rfsimulator/simulator.c` — `rfsimulator_read`, `maybe_start_sionna_embed_rfsim`, `sionna_embed_loop_rfsim`
- `sionna-main/oai_channel_embed.py` — `RayleighBlockFading`, `get_h_flat()`
