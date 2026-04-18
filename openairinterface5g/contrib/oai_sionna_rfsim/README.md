# OAI rfsimulator — Sionna 브리지 (참조용, 비통합)

이 디렉터리는 **`librfsimulator`에 아직 연결되지 않는다.**  
`doc/SIONNA_RFSIM_CONCEPT_AND_PATHS.md` 에 적힌 **두 갈래(chanmod / 비 chanmod)** 를 나중에 정리해 넣을 때 참고할 **헤더·스텁**만 둔다.

## 파일

- `oai_sionna_bridge.h` — C 측에서 기대할 수 있는 **최소 API** (이름·역할 명세).
- `oai_sionna_bridge_stub.c` — 실제 Python 호출 없음; **빌드 검증용** 스텁.
- `Makefile` — `make` 로 스텁만 컴파일해 문법 확인 (메인 OAI CMake와 무관).

## 실제 동작 코드 위치 (이 저장소)

- Python 임베딩·스레드·`sys.path`: `radio/rfsimulator/simulator.c`
- 평탄 H 적용: 동 파일 `rfsimulator_read()` 의 chanmod 없음 분기
- `get_h_flat()` 등: `sionna-main/oai_channel_embed.py`

## 통합 시 할 일 (요약)

1. 이 헤더 API를 **`simulator.c`의 기존 구현과 합치거나** 중복을 제거한다.
2. `apply_channelmod.c` 에 넣을 경우 **GIL·단일 `Py_Initialize`** 를 설계한다.
3. 메인 `CMakeLists.txt` 에 소스 추가는 **별 커밋**으로 한다.
