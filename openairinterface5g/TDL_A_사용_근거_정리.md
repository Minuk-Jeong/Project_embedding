# TDL-A 모델 사용 근거 정리

본 문서는 `gnb_4x4_tdl_dynamic_l2.log`, `ue_4x4_tdl_dynamic_l2.log` 및 실제 사용된 conf 파일을 기준으로,
"현재 테스트가 rfsimulator chanmod + TDL-A 모델로 실행되었는지"를 검증한 결과를 정리한다.

## 1) 실행 명령 근거 (gNB/UE)

### gNB 실행 로그
- 파일: `gnb_4x4_tdl_dynamic_l2.log`
- 핵심 라인:
  - `CMDLINE: "./nr-softmodem" "--rfsim" "--noS1" "-O" ".../gnb.sa.band78.fr1.106PRB.pci0.rfsim.4x4.chanmod_tdl_a_layer2_dynamic.conf" ...`
- 해석:
  - gNB가 문제의 conf(`...4x4.chanmod_tdl_a_layer2_dynamic.conf`)를 실제로 로드함.

### UE 실행 로그
- 파일: `ue_4x4_tdl_dynamic_l2.log`
- 핵심 라인:
  - `CMDLINE: "./nr-uesoftmodem" "--rfsim" ... "--ue-nb-ant-rx" "4" "--ue-nb-ant-tx" "4" ...`
  - `Connection to 127.0.0.1:4043 established`
- 해석:
  - UE는 rfsim 클라이언트로 gNB rfsim 서버에 정상 접속했고, 4x4 안테나 옵션으로 동작함.

## 2) gNB conf 근거 (chanmod + 동적 TDL-A include)

- 파일: `targets/PROJECTS/GENERIC-NR-5GC/CONF/gnb.sa.band78.fr1.106PRB.pci0.rfsim.4x4.chanmod_tdl_a_layer2_dynamic.conf`
- 핵심 설정:
  - `rfsimulator.options = ("chanmod");`
  - `@include "channelmod_rfsimu_tdl_a_dynamic.conf"`
  - `nb_tx = 4`, `nb_rx = 4`
  - `maxMIMO_layers = 2`
- 해석:
  - rfsim의 채널모델 경로(`chanmod`)를 활성화했고, 동적 TDL-A 모델 정의 파일을 직접 include함.
  - 물리 4x4, 스케줄링 2-layer 프로파일이 동시에 설정됨.

## 3) TDL-A 채널 정의 근거 (모델 파일)

- 파일: `targets/PROJECTS/GENERIC-NR-5GC/CONF/channelmod_rfsimu_tdl_a_dynamic.conf`
- 핵심 설정:
  - `modellist = "modellist_rfsimu_tdl_a_dyn"`
  - `model_name = "rfsimu_channel_enB0"`, `type = "TDL_A"`
  - `model_name = "rfsimu_channel_ue0"`, `type = "TDL_A"`
  - `forgetfact = 0.2`
  - `ds_tdl = 300e-9`
- 해석:
  - DL/UL 양방향 채널 모델이 모두 `type = "TDL_A"`로 명시됨.
  - `forgetfact`, `ds_tdl`가 포함된 동적 프로파일임.

## 4) 런타임(OCM) 근거: 실제 TDL-A 모델 할당 로그

- 파일: `gnb_4x4_tdl_dynamic_l2.log`
- 핵심 라인:
  - `Model rfsimu_channel_enB0 type TDL_A allocated from config file, list modellist_rfsimu_tdl_a_dyn`
  - `Model rfsimu_channel_ue0 type TDL_A allocated from config file, list modellist_rfsimu_tdl_a_dyn`
  - `Random channel rfsimu_channel_ue0 in rfsimulator activated`
- 해석:
  - 단순히 conf에 적힌 것이 아니라, OCM에서 실제로 TDL_A 타입을 읽어 채널 객체를 생성/활성화했음.
  - 이 로그가 TDL-A 적용의 가장 직접적인 런타임 증거임.

## 5) 2-layer 적용 근거

- 파일: `gnb_4x4_tdl_dynamic_l2.log`
- 핵심 라인:
  - `... maxMIMO_Layers 2 ...`
- 해석:
  - 이전에 파라미터명 불일치(`maxMIMO_Layers` vs `maxMIMO_layers`)로 미적용되던 상태가 해결되었고,
    해당 실행에서는 2-layer 값이 실제로 파싱/적용되었음.

## 6) 최종 결론

아래 3단계를 모두 만족하므로, 본 테스트는 "rfsimulator chanmod 기반의 TDL-A 모델"로 실행된 것이 맞다.

1. gNB conf에서 `options=("chanmod")` + 동적 TDL-A 파일 include
2. 모델 파일에서 DL/UL 모두 `type="TDL_A"` 정의
3. gNB 런타임 OCM 로그에서 `type TDL_A allocated ...` 확인

또한 동일 실행에서 `maxMIMO_Layers 2`가 로그에 출력되어 2-layer 설정도 적용되었다.
