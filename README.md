[README.md](https://github.com/user-attachments/files/26849221/README.md)
# Project_embedding

OpenAirInterface5G(OAI) 기반 NR 시뮬레이션·채널 모델(rfsimulator, `chanmod`, Sionna 연동 등) 실험용 워크스페이스입니다.  
핵심 소스 트리는 **`openairinterface5g/`** 디렉터리에 있습니다.

## 저장소 구조 (요약)

```
Project_embedding/
├── README.md                 # 본 문서
└── openairinterface5g/       # OAI RAN 소스 (5G gNB / nrUE, rfsimulator 등)
    ├── cmake_targets/        # 빌드 스크립트 `build_oai`
    ├── doc/BUILD.md          # OAI 공식 빌드 상세
    ├── targets/PROJECTS/GENERIC-NR-5GC/CONF/   # 실험용 gNB/UE conf
    ├── sionna-main/          # Sionna 관련 스크립트(해당 빌드에 쓰는 경우)
    └── tools/matlab/         # 로그 파싱·BLER 플롯 등 MATLAB 유틸
```

## 지원 환경

- **OS**: Ubuntu 22.04 / 24.04 (x86_64) 권장. OAI 공식 문서도 이 환경을 기준으로 합니다.
- **디스크**: 전체 클론·빌드·CPM 캐시 기준 **수십 GB** 여유 권장.
- **메모리**: 링크 최적화(LTO) 등에 따라 **16 GB 이상**이 안전합니다.

## 사전 준비

```bash
sudo apt-get update
sudo apt-get install -y git curl ca-certificates
```

저장소를 새로 받는 경우:

```bash
git clone <본인-GitHub-저장소-URL> Project_embedding
cd Project_embedding
```

이미 `openairinterface5g`만 있는 경우에는 해당 폴더로 이동하면 됩니다.

```bash
cd openairinterface5g
```

## 최초 빌드 (상세)

아래는 **RF 시뮬레이터(rfsimulator)로 gNB / nrUE를 돌리기 위한 최소 빌드**를 기준으로 합니다.  
USRP 등 실제 SDR을 쓰려면 `-w USRP` 및 추가 패키지가 필요합니다([`doc/BUILD.md`](openairinterface5g/doc/BUILD.md)).

### 1단계: OAI 디렉터리로 이동

```bash
cd /path/to/Project_embedding/openairinterface5g/cmake_targets
```

(경로는 본인 PC의 `Project_embedding` 위치에 맞게 바꿉니다.)

### 2단계: 의존성 일괄 설치 (`-I`)

**최초 1회**(또는 OAI가 요구하는 패키지가 바뀐 뒤) 실행합니다. `sudo` 권한이 필요합니다.

rfsimulator 위주로 가볍게 가려면 **`-w SIMU`** 를 붙입니다.

```bash
./build_oai -I -w SIMU
```

- `-I` : OAI 빌드에 필요한 패키지 설치(컴파일러, cmake, ASN.1 도구 등).
- `-w SIMU` : RF 시뮬레이터 관련 의존 위주(USRP UHD 등은 이 단계에서 강하게 끌어오지 않도록 분리).

선택적으로 문서에 나온 **선택 패키지**까지 깔 수 있습니다.

```bash
./build_oai -I --install-optional-packages -w SIMU
```

설치가 오래 걸리거나 특정 패키지에서 멈추면, 터미널 전체 로그를 저장한 뒤 `doc/BUILD.md`의 해당 절을 참고하세요.

### 3단계: RAN 실행 파일 빌드

**ninja** 사용을 권장합니다(재빌드 속도).

```bash
./build_oai --ninja -w SIMU --gNB --nrUE
```

- `--gNB` : `nr-softmodem` 및 관련 라이브러리.
- `--nrUE` : `nr-uesoftmodem`.
- `-w SIMU` : rfsimulator 디바이스 등 시뮬 경로 포함.

LTE까지 필요하면 `--eNB --UE` 등을 추가할 수 있습니다.

**완전히 깨끗이 다시 빌드**할 때는 `-c` 로 cmake 캐시를 지운 뒤 같은 명령을 다시 실행합니다.

```bash
./build_oai -c --ninja -w SIMU --gNB --nrUE
```

### 4단계: 빌드 결과 확인

성공 시 바이너리는 `openairinterface5g/cmake_targets/ran_build/build/` 아래에 생성됩니다.

저장소 루트(`Project_embedding/`)에 있다면:

```bash
ls -la openairinterface5g/cmake_targets/ran_build/build/nr-softmodem
ls -la openairinterface5g/cmake_targets/ran_build/build/nr-uesoftmodem
```

이미 `openairinterface5g/cmake_targets/` 안에 있다면:

```bash
ls -la ran_build/build/nr-softmodem
ls -la ran_build/build/nr-uesoftmodem
```

### 5단계: 실행 시 라이브러리 경로(권장)

빌드 산출물이 있는 디렉터리에서 실행할 때, 링커가 공유 라이브러리를 찾을 수 있도록:

```bash
cd /path/to/Project_embedding/openairinterface5g/cmake_targets/ran_build/build
export LD_LIBRARY_PATH=/path/to/Project_embedding/openairinterface5g/cmake_targets/ran_build/build:${LD_LIBRARY_PATH}
```

저장소에 `oaienv` 스크립트가 있다면 OAI 문서대로 `source oaienv` 후 실행하는 방법도 있습니다.

### 6단계: 동작 확인(예: rfsim)

gNB / nrUE는 사용 중인 **conf 파일 경로**에 맞게 조정합니다. 예시는 저장소의 `targets/PROJECTS/GENERIC-NR-5GC/CONF/` 아래 문서·메모와 동일한 패턴으로 두면 됩니다.

```bash
cd /path/to/Project_embedding/openairinterface5g/cmake_targets/ran_build/build
./nr-softmodem -O ../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/<사용할-gNB.conf> --rfsim
```

```bash
./nr-uesoftmodem --rfsim --rfsimulator.serveraddr 127.0.0.1 \
  -O ../../../targets/PROJECTS/GENERIC-NR-5GC/CONF/<사용할-UE.conf> \
  ... 주파수·PRB 등 ...
```

## 빌드 문제가 날 때

1. **`./build_oai -h`** 로 옵션 확인.
2. OAI 공식 절차: **[`openairinterface5g/doc/BUILD.md`](openairinterface5g/doc/BUILD.md)** (cmake 직접 실행, ASN.1, UHD 등).
3. **asn1c** 관련 오류는 BUILD.md의 “Installing (new) asn1c from source” 절을 따릅니다.
4. **CMake/CPM 캐시**: `~/.cache/cpm` 용량·네트워크 이슈가 있으면 BUILD.md의 CPM 설명을 참고합니다.

## 참고 링크 (OAI 업스트림)

- [OAI 문서 인덱스](openairinterface5g/doc/README.md)
- [빌드(BUILD.md)](openairinterface5g/doc/BUILD.md)
- [모뎀 실행(RUNMODEM)](openairinterface5g/doc/RUNMODEM.md)

---

본 README는 **GitHub에 올린 `Project_embedding` 루트**에서 처음 환경을 잡는 분을 위한 요약입니다.  
세부 옵션·타깃 OS는 항상 `openairinterface5g/doc/` 내용을 우선합니다.
