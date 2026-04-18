# Sionna 다경로 → OAI `chanmod` FIR 연동 계획 (6하 원칙)

평탄 복소 행렬 \(H\) 대신, Sionna(`oai_channel_embed.py`)에서 얻은 **다경로 계수·지연**을 **이산 FIR 탭**으로 바꾸고, OAI rfsimulator의 **`rxAddInput` 선형 컨볼루션 경로**(`chanmod` 활성)에서 쓰기 위한 작업을 6하 원칙으로 정리한다.

---

## 1. 무엇을 (What)

| 항목 | 설명 |
|------|------|
| **입력** | Python 측에서 TDL/CDL 등으로 얻은 경로별 복소 이득 \(a_p\) 및 지연 \(\tau_p\) (초), 또는 동등한 다경로 스냅샷. |
| **중간 산출** | rfsimulator IQ와 동일한 **샘플레이트 \(f_s\)** 기준의 **FIR 탭** \(h[\ell]\) (MIMO면 안테나 쌍 \((r,t)\)마다 길이 \(L\) 벡터). |
| **출력·효과** | `channel_desc_t`가 가리키는 **`ch`** 버퍼를 해당 탭으로 채우거나 갱신하여, **`rxAddInput()`** 이 **이산 선형 컨볼루션**을 수행하도록 한다. |
| **하지 않을 것** | 평탄 \(H\) 경로(`OAI_SIONNA_RFSIM_APPLY`, `sionna_h_flat`)와 **동시에** 같은 스트림에 이중 적용하지 않는다. |

---

## 2. 왜 (Why)

| 이유 | 설명 |
|------|------|
| **물리적 정합** | 실제 다경로는 **지연 확산**을 통해 **주파수 선택적 페이딩·ISI**를 만든다. 샘플별 \(y = Hx\)인 평탄 모델은 **한 순간의 MIMO 결합**에 가깝고, **탭 지연 구조**가 없다. |
| **OAI 네이티브 경로 재사용** | `chanmod` ON 시 FIR·`random_channel` 계열이 이미 존재하므로, **검증된 컨볼루션 루프**를 재사용할 수 있다. |
| **비교 실험** | 동일 시나리오에서 **평탄 \(H\)** vs **FIR**의 BLER/CSI/동기 등 차이를 명확히 볼 수 있다. |

---

## 3. 누가 (Who)

| 역할 | 담당 |
|------|------|
| **채널 합성·양자화** | Python(`oai_channel_embed.py` 확장 또는 별도 모듈) 또는 C(스냅샷 파일 로드 후 탭 빌드). |
| **런타임 주입** | OAI 빌드 담당자: `radio/rfsimulator/simulator.c`, 필요 시 `apply_channelmod.c` / `random_channel.c` 인터페이스 확장. |
| **설정·실행** | 실험 담당: gNB/UE conf에서 `chanmod`·`channelmod` 블록, `OAI_SIONNA_RFSIM_APPLY=0` 등 상호 배타 조건 정리. |

---

## 4. 어디서 (Where)

| 위치 | 역할 |
|------|------|
| **`sionna-main/oai_channel_embed.py`** | `get_h_flat()` 이전 단계의 `a`, `tau` 접근·노출, 또는 **탭 직접 생성 함수** 추가. |
| **`radio/rfsimulator/simulator.c`** | 소켓 수신 버퍼 → `rxAddInput` 호출 전, `ptr->channel_model` 및 **`ch`** 갱신 지점(또는 별도 훅). |
| **`radio/rfsimulator/apply_channelmod.c`** | `rxAddInput()` — **변경 최소화**가 이상적(입력 탭만 맞추면 됨). |
| **`openair1/SIMULATION/TOOLS/random_channel.c`** | 참고: TDL-A~E의 `tdlModel`·탭 생성 로직; **외부 탭과의 일관성** 비교용. |
| **설정** | `targets/.../CONF/channelmod_*.conf` — `type`·`model_name`·`ds_tdl` 등; **외부 탭 모드**면 새 `type` 또는 telnet/런타임 API 검토. |
| **문서** | 본 파일, 기존 `doc/SIONNA_EMBED_RFSIM.md` / `doc/SIONNA_RFSIM_CONCEPT_AND_PATHS.md` 와 상호 링크 권장. |

---

## 5. 언제 (When)

| 시점 | 동작 |
|------|------|
| **초기화** | rfsimulator 연결·`channel_model` 할당 직후, 첫 `rxAddInput` 전에 **기준 탭** 로드 가능 여부 확정. |
| **주기 갱신** | Sionna 시간 스텝·서브프레임 단위와 맞춰 **탭 세트 재계산** (느린 페이딩) 또는 **고정 탭** (스냅샷 실험). |
| **도플러/시변** | (선택) 탭 위상·크기를 매 블록 갱신하거나, OAI `rxAddInput`의 **도플러 위상 항**과 역할 분담을 문서화하여 **이중 계산** 방지. |
| **배타 조건** | `chanmod` ON → **`sionna_apply` OFF**; 반대로 평탄 \(H\) 실험 시 **`channel_model == NULL`**. |

---

## 6. 어떻게 (How)

### 6.1 알고리즘 개요

1. **스케일 정합**  
   - IQ 스트림 샘플레이트 \(f_s\) = rfsimulator `sample_rate` 와 동일해야 함.  
   - \(\tau_p\) → 샘플 지연 \(d_p = \mathrm{round}(\tau_p \cdot f_s)\)` (또는 **분수 지연**이면 인접 탭에 분할 에너지).

2. **탭 적재**  
   - 각 \((r,t)\): \(h[\ell] \leftarrow \sum_{p:\, d_p = \ell} \tilde{a}_{p,r,t}\) 형태로 합산.  
   - \(\tilde{a}\)에는 캐리어·베이스밴드에 맞는 위상을 포함(현재 `get_h_flat()`의 `exp(-j2\pi f_c \tau)`와 **동일 물리를 탭별로 분산**하는지 일관성 유지).

3. **에너지·정규화**  
   - 합 전력·클리핑(`int16`)과 맞게 스케일 조정; 기존 `random_channel` 출력과 비교 가능하면 좋음.

4. **OAI 측 연결**  
   - **옵션 A**: conf의 TDL 대신 **“외부 탭 파일/공유 메모리”**를 읽는 `channel_desc` 초기화 분기 추가.  
   - **옵션 B**: telnet/`channelmod` 명령 확장으로 탭 업데이트(복잡도 높음).  
   - **옵션 C**: 짧은 주기로 Python이 탭을 파일에 쓰고 C가 `load_*` 후 `memcpy`로 `ch` 갱신(POC에 적합).

5. **검증**  
   - `chanmod`만 켠 OAI 네이티브 TDL-A와 **동일 \(f_s\), 유사 PDP**일 때 스펙트럼·상관이 비슷한지 확인.  
   - 평탄 \(H\) 경로와 **교차 비활성화** 후 단일 경로만 켜서 로그·성능 비교.

### 6.2 리스크·주의

- **CP 길이 vs 채널 길이**: 탭이 길면 ISI·ICI가 커져 UE 동기 한계를 넘을 수 있음.  
- **1×1 최적화 경로**: `simulator.c`의 `nbAnt_tx == 1 && nb_cnx == 1` 분기는 **복사만** 할 수 있어, MIMO FIR 실험 시 안테나 수·연결 수 조건 확인.  
- **스레드 안전**: `sionna_h_flat`과 같이 **mutex** 하에 탭 버퍼 갱신.

---

## 요약 표

| 6하 | 한 줄 |
|-----|--------|
| **무엇을** | 다경로 \((a,\tau)\) → 이산 FIR → `rxAddInput` 컨볼루션. |
| **왜** | 지연 확산·선택적 페이딩을 평탄 \(H\)보다 잘 반영. |
| **누가** | Python/C 개발·실험 담당이 역할 분담. |
| **어디서** | `oai_channel_embed.py`, `simulator.c`, conf, (필요 시) 탭 파일 규약. |
| **언제** | 초기화·주기 갱신; `chanmod`/`sionna_apply` 배타. |
| **어떻게** | 지연 양자화 → 탭 합성 → `ch` 주입 → 검증. |

---

*본 문서는 설계·태스크 분해용이며, 구현 시 실제 API·심볼 이름은 해당 브랜치 소스에 맞게 조정한다.*
