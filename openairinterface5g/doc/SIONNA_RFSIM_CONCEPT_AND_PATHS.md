# Sionna–OAI rfsimulator 연동: 목적과 실제 코드 경로

외부에서 본 “패치 가이드”류 문서는 **의도(무엇을 하려는지)** 는 옳을 수 있으나, **파일명·함수명·삽입 위치**가 저장소 버전과 어긋나기 쉽다. 여기서는 **맥락만 공유**하고, **이 브랜치에서 실제로 쓰는 경로**만 정리한다.

실행·빌드·환경변수 예시는 `doc/SIONNA_EMBED_RFSIM.md`를 본다.

---

## 1. 하려는 일 (개념)

- **1단계 목표**: OAI가 기대하는 **다탭 FIR 전체**를 한 번에 바꾸지 않고, **시점별 평탄 MIMO 채널** \(H\) 를 받아 **IQ에 곱한다**.

\[
y_r[i] \approx \sum_t H_{r,t}\, x_t[i]
\]

- OAI 네이티브 multipath는 대략 다음 형태의 **시간 영역 컨볼루션**이다 (`channel_length` 탭).

\[
y_r[i] = \sum_t \sum_l h_{r,t}[l]\, x_t[\,\text{지연된 샘플}\,]
\]

- Python `get_h_flat()` 이 주는 것은 **탭 벡터가 아니라 (rx,tx) 복소 행렬**이므로, 위 둘은 **1:1 대응이 아니다**. “`l=0`만 있는 특수 FIR”에 가깝게 해석할 때만 평탄 \(H\) 주입과 맞물린다.

---

## 2. OAI rfsimulator 안의 **두 갈래** (혼동 방지)

| 구분 | 언제 타나 | 채널 적용 코드 | 특징 |
|------|-----------|----------------|------|
| **A. chanmod ON** | `--rfsimulator.options chanmod` + channelmod 설정 | `radio/rfsimulator/apply_channelmod.c` 의 `rxAddInput()` | `channel_desc_t`, `channelDesc->ch[·][l]`, **순환 버퍼 인덱스**로 **다탭** 처리 |
| **B. chanmod OFF** | chanmod 없음 (Sionna flat POC가 주로 여기) | `radio/rfsimulator/simulator.c` 의 `rfsimulator_read()` 내부 MIMO 루프 | **평탄 \(H\)** 또는 레거시 실수 믹싱 |

**같은 “Sionna를 OAI에 붙인다”라도, A와 B는 파일이 다르다.**  
다른 문서에서 `rxAddInput()`만 말하거나 `rfsimulator_read_beams()` 같은 이름을 쓰면, **이 트리와 맞지 않을 수 있다.**

---

## 3. 이 저장소에서의 **실제 구현 (B 경로)**

- **Python 임베딩**: `radio/rfsimulator/simulator.c`  
  - `maybe_start_sionna_embed_rfsim()` — `OAI_SIONNA_RFSIM_APPLY=1` 일 때 스레드 기동  
  - `sys.path`에 **`…/sionna-main`** 과 **`…/sionna-main/src`** ( `sionna.phy` 로딩용 )  
  - 모듈명: **`oai_channel_embed`** (`import` 이름 = `sionna-main/oai_channel_embed.py`)  
  - `init()` 은 kwargs로 `num_rx_ant`, `num_tx_ant` 등 전달 (C에서 `PyDict` 사용)

- **Sionna 쪽**: `sionna-main/oai_channel_embed.py`  
  - `get_h_flat()` — C가 주기적으로 호출해 `double` 배열로 복사  
  - `OAI_SIONNA_CHANNEL_FAMILY` 등으로 `RAYLEIGH_BLOCK` / `TDL` / `CDL` 선택 가능  
  - TDL/CDL는 내부적으로 다경로 계수를 쓰지만, **OAI로 넘기기 전에 협대역 등가 행렬로 합산**하는 층이 있음 (FIR 탭 그대로가 아님)

- **H 적용**: `simulator.c` 의 `rfsimulator_read()` — **chanmod 없을 때** `ptr->channel_model == NULL` 분기에서  
  `t->sionna_h_flat` 과 `nbAnt`, `nbAnt_tx` 로 **복소 곱** (`OAI_SIONNA_DIAG_ONLY` 등)

- **빌드**: `-DOAI_PYTHON_EMBED=ON`, 타깃 `librfsimulator` ( `ninja rfsimulator` )

---

## 4. A 경로 (`apply_channelmod.c`)를 고치는 설계와의 관계

- **개념상** “`rxAddInput()`에서 외부 \(H\)로 탭 루프를 대체”는 가능하지만,  
  - 실제 `rxAddInput()` 시그니처는 **`const c16_t *input_sig`** 한 포인터 + **CirSize** 기반 인덱싱이며,  
  - 가이드에 흔한 **`c16_t **input_sig`** 형태와 다르다.  
- **이미 `simulator.c`에 Python이 있으면**, A에 또 `Py_Initialize`를 넣을 경우 **중복 초기화·GIL** 문제를 설계로 막아야 한다.

즉 **“무엇을 하려는지”는 이해하고**, **구체 패치는 A/B 중 하나를 택해 일관되게** 가는 것이 안전하다.

---

## 5. 아직 대체하지 않는 것

- **`channelDesc->ch[rx,tx][l]` 전체 FIR** 을 Sionna가 매 스텝 채우는 방식은 **현재 B 경로 POC에 없음**.  
- 완전 대체를 하려면 예를 들어:  
  - Python에서 **탭 + 지연**을 내보내 OAI `channel_desc_t`에 채우거나,  
  - `rxAddInput()`이 읽을 공유 버퍼를 두거나,  
  - OAI 네이티브 TDL(`random_channel.c`) + chanmod만 쓰고 Sionna는 오프라인 검증 등.

---

## 6. 실험 시 기억할 점

- **UE만 `OAI_SIONNA_RFSIM_APPLY=1`**: DL 수신만 Sionna, gNB 쪽에는 `Updated H` 로그가 안 나오는 것이 정상이다.  
- **양쪽 다 1**: 서로 **독립 스레드**에서 H를 뽑으면 로그가 **매칭되지 않는다** (의도한 바가 아니면 UE-only 또는 shared file 등).

---

## 7. 요약

| 질문 | 이 저장소 기준 답 |
|------|------------------|
| 평탄 \(H\) 주입이 multipath FIR을 **완전 대체**하나? | **아니오.** 개념은 “협대역 등가”에 가깝다. |
| 코드는 어디? | 주로 **`simulator.c` + `oai_channel_embed.py`**, chanmod 경로는 **`apply_channelmod.c`**. |
| 실행 문서? | **`doc/SIONNA_EMBED_RFSIM.md`** |

이 파일은 **다운로드 폴더의 구 가이드와의 차이**를 줄이기 위한 **개념·경로 정합**용이며, 빌드 명령의 유일한 근거로 삼지 않는다 (프로젝트 `CMakeLists`·`cmake_targets`를 따른다).
