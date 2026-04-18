# Sionna–rfsimulator: 패치·통합 TODO (`SIONNA_RFSIM_CONCEPT_AND_PATHS.md` 기준)

기존 트리의 **`radio/rfsimulator/simulator.c`**, **`oai_channel_embed.py`** 등은 **이 체크리스트만으로는 수정하지 않는다.**  
아래는 **향후 통합** 또는 **검증** 시 따라갈 작업 목록이며, 참조용 코드는 `contrib/oai_sionna_rfsim/` 에 둔다.

---

## 문서·스크립트 (완료 시 체크)

- [ ] `doc/SIONNA_RFSIM_CONCEPT_AND_PATHS.md` 와 본 TODO를 팀 내 공유 경로에 두었는지
- [ ] 실험 시 `scripts/source_rfsim_sionna_env.sh` 로 환경을 고정할지 결정
- [ ] 로그 상관 분석에 `sionna-main/oai_rfsim_metrics.py` 사용 여부

---

## 빌드·실행 (매 실험)

- [ ] `cmake` 에 `-DOAI_PYTHON_EMBED=ON` 으로 `librfsimulator` 빌드
- [ ] `ninja rfsimulator` (및 필요 시 `nr-softmodem` / `nr-uesoftmodem`)
- [ ] 실행 cwd = **프로젝트 루트** (`sionna-main`, `sionna-main/src` 가 상대 경로로 보이게)
- [ ] `LD_LIBRARY_PATH` 에 빌드 산출물 디렉터리 포함

---

## 경로 A — `apply_channelmod.c` / `rxAddInput()` (chanmod)

**현재 POC는 여기를 쓰지 않는다.** 다탭 FIR을 Sionna로 채우려면 이쪽이 대상이다.

- [ ] `rxAddInput()` 실제 시그니처·순환 버퍼 인덱스와 외부 가이드의 예시 코드 대조
- [ ] Python 임베딩을 A에 넣을 경우 **`simulator.c` 쪽과 이중 `Py_Initialize` 방지** 설계
- [ ] `channel_desc_t` 를 탭으로 채우는 Python API (`get_taps` 등) 명세
- [ ] `CMakeLists.txt` 에 `apply_channelmod` 타깃에 Python 링크 추가 (통합 시)

---

## 경로 B — `simulator.c` / `rfsimulator_read()` (chanmod 없음, **현 POC**)

- [ ] `OAI_SIONNA_RFSIM_APPLY` / `OAI_SIONNA_*` 환경변수를 실험마다 기록
- [ ] UE-only vs 양쪽 APPLY 실험 목적에 맞게 env 정리 (로그 매칭 기대치)
- [ ] `OAI_SIONNA_UPDATE_US` 스윕으로 SINR 출렁임 vs H 갱신 주기 확인

---

## FIR 완전 대체 (장기)

- [ ] Sionna 출력 → `channelDesc->ch[rx,tx][l]` 매핑 규칙 확정
- [ ] 또는 공유 메모리/파일로 탭 스냅샷 + `rxAddInput` 읽기

---

## 참조 코드 (새 파일만, 저장소 `contrib/`)

| 경로 | 용도 |
|------|------|
| `contrib/oai_sionna_rfsim/oai_sionna_bridge.h` | 향후 C 측 브리지 API 스케치 |
| `contrib/oai_sionna_rfsim/oai_sionna_bridge_stub.c` | 링크 없이 컴파일 가능한 스텁 |
| `contrib/oai_sionna_rfsim/README.md` | 통합 시 주의사항 |
| `sionna-main/oai_rfsim_metrics.py` | `get_h_flat` 결과의 노름 등 |
| `scripts/source_rfsim_sionna_env.sh` | 공통 env |

---

## 완료 기준 (POC)

- [ ] APPLY 0 vs 1 에서 동작 차이가 명확히 재현되는지
- [ ] `Updated H` 와 UE 측 지표를 같은 실험 프로토콜으로 수집했는지
