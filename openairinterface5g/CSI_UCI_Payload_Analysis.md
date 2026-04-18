# OAI CSI UCI Payload 구조 분석 보고서

## 개요
본 문서는 OAI (OpenAirInterface)에서 생성하는 CSI UCI Payload의 실제 구조를 코드 분석을 통해 확인한 결과입니다.
분석 기준: `cri_RI_PMI_CQI`, Type-I Single Panel, 4 ports, wideband PMI/CQI, periodic PUCCH report

---

## 1. CSI Report Payload 구성 (비트 단위)

### 1.1 총 비트 수
**PUCCH 전송 시 (periodic report):**
- **Part-1 비트 수**: `nr_get_csi_bitlen(csi_report)` 함수로 계산
- **Part-2 비트 수**: **항상 0** (PUCCH에서는 Part-2 미사용)

**실제 Part-1 비트 수 계산식:**
```
p1_bits = max_over_all_RI(CRI + RI + PMI_i1 + PMI_i2 + CQI + Padding)
```

### 1.2 필드별 비트 구성

#### CRI (CSI-RS Resource Indicator)
- **포함 여부**: **항상 0bit로 인코딩됨**
- **코드 위치**: `nr_ue_procedures.c:3042`
  ```c
  temp_payload_1 = (0/*mac->csi_measurements.cri*/ << ...) | ...
  ```
- **설명**: `cri_RI_PMI_CQI` 설정에서도 CRI는 **항상 0으로 하드코딩**되어 payload에 포함되지만, 실제 CRI 값은 전송되지 않음
- **CRI bitlen 계산**: `cri_bitlen = ceil(log2(nb_resources))` (단, nb_resources=1이면 0bit)

#### RI (Rank Indicator)
- **비트 수**: **RI 값에 따라 가변** (1~2bit)
- **코드 위치**: `nr_mac_common.c:4291-4342` (`compute_ri_bitlen`)
- **계산 방식**:
  - 4 ports인 경우: `ri_bitlen = min(ceil(log2(nb_allowed_ri)), 2)`
  - `typeI_SinglePanel_ri_Restriction` 비트마스크에서 허용된 RI 개수 계산
  - 예: `ri_Restriction = 00001111` (RI 1,2,3,4 허용) → `nb_allowed_ri = 4` → `ri_bitlen = 2`
  - 예: `ri_Restriction = 00000001` (RI 1만 허용) → `ri_bitlen = 0` (RI=1 고정)

#### PMI (Precoding Matrix Indicator)
- **비트 수**: **RI 값에 따라 크게 변함**
- **코드 위치**: `nr_mac_common.c:4462-4560` (`set_bitlen_size_singlepanel`)
- **구성 요소**:
  - `pmi_i11_bitlen[ri]`: i1의 첫 번째 부분 (가변)
  - `pmi_i12_bitlen[ri]`: i1의 두 번째 부분 (가변, n2>1일 때만)
  - `pmi_x2_bitlen[ri]`: i2 (2bit 또는 4bit)
- **실제 사용**: 코드에서는 `i1`과 `i2`로 저장됨
  ```c
  mac->csirs_measurements.i1  // i11과 i12를 합친 값
  mac->csirs_measurements.i2  // i2 값
  ```

**RI=1, 4 ports, codebookMode=1인 경우:**
- `pmi_i11_bitlen[0] = ceil(log2(n1 * o1))` (예: n1=2, o1=4 → 3bit)
- `pmi_i12_bitlen[0] = ceil(log2(n2 * o2))` (예: n2=2, o2=4 → 3bit)
- `pmi_x2_bitlen[0] = 2bit`
- **총 PMI 비트 수**: 3 + 3 + 2 = **8bit** (RTD의 6bit 가정과 다름!)

**RI=2, 4 ports, codebookMode=1인 경우:**
- `pmi_i11_bitlen[1] = ceil(log2(n1 * o1))` (예: 3bit)
- `pmi_i12_bitlen[1] = ceil(log2(n2 * o2))` (예: 3bit)
- `pmi_x2_bitlen[1] = 1bit`
- `pmi_i13_bitlen[1] = 2bit` (rank=2일 때 추가)
- **총 PMI 비트 수**: 3 + 3 + 1 + 2 = **9bit**

**중요**: `pmi_x1_bitlen`은 사용되지 않음. 실제로는 `pmi_i11_bitlen + pmi_i12_bitlen`이 사용됨.

#### CQI (Channel Quality Indicator)
- **비트 수**: **4bit 고정** (RI 값과 무관)
- **코드 위치**: `nr_mac_common.c:4659`
  ```c
  csi_report->csi_meas_bitlen.cqi_bitlen[i] = 4;
  ```

#### Padding
- **존재 여부**: **있음** (PUCCH 전송 시)
- **비트 수**: 가변
- **계산식**: 
  ```c
  padding_bitlen = p1_bits - (cri_bitlen + ri_bitlen + pmi_x1_bitlen + pmi_x2_bitlen + cqi_bitlen)
  ```
- **목적**: PUCCH Format 2/3/4의 최소 payload 크기 요구사항 충족

### 1.3 Payload Bit Mapping (PUCCH)

**비트 순서 (LSB → MSB, reverse_bits 적용 전):**
```
[LSB] CQI(4bit) | i2(pmi_x2_bitlen) | i1(pmi_i11+i12_bitlen) | Padding | RI(ri_bitlen) | CRI(cri_bitlen) [MSB]
```

**실제 인코딩 코드** (`nr_ue_procedures.c:3042-3046`):
```c
temp_payload_1 = (0/*CRI*/ << (cqi_bitlen + pmi_x2_bitlen + pmi_x1_bitlen + padding_bitlen + ri_bitlen)) |
                 (ri << (cqi_bitlen + pmi_x2_bitlen + pmi_x1_bitlen + padding_bitlen)) |
                 (i1 << (cqi_bitlen + pmi_x2_bitlen)) |
                 (i2 << (cqi_bitlen)) |
                 (cqi);
```

**중요**: 인코딩 후 `reverse_bits(temp_payload_1, p1_bits)`로 **비트 순서가 반전**됨!

**최종 전송 순서 (reverse_bits 적용 후, MSB → LSB):**
```
[MSB] CRI | RI | i1 | i2 | CQI [LSB]
```

---

## 2. RI에 따른 PMI 비트수 변화

### 2.1 답변
**예, RI 값에 따라 PMI bit 수가 크게 달라집니다.**

### 2.2 상세 설명
- **PMI 비트 수는 RI 인덱스를 배열 인덱스로 사용**:
  ```c
  int pmi_x1_bitlen = csi_report->csi_meas_bitlen.pmi_x1_bitlen[mac->csirs_measurements.ri];
  int pmi_x2_bitlen = csi_report->csi_meas_bitlen.pmi_x2_bitlen[mac->csirs_measurements.ri];
  ```
- **RI=1과 RI=2의 PMI 비트 수가 다름** (위 예시 참조)
- **RTD의 가정 (항상 6bit)은 잘못됨**

### 2.3 typeI_SinglePanel_ri_Restriction 영향
- **직접적 영향**: 허용된 RI 값의 개수에 따라 `ri_bitlen` 결정
- **간접적 영향**: 각 RI 값에 대해 PMI bitlen이 별도로 계산됨
- **코드 위치**: `nr_mac_common.c:4315, 4602`
  ```c
  uint8_t ri_restriction = type1single->typeI_SinglePanel_ri_Restriction.buf[0];
  if (((ri_restriction >> i) & 0x01) == 0)  // RI i+1이 허용되지 않으면
    csi_report->csi_meas_bitlen.pmi_x2_bitlen[i] = 0;  // PMI bitlen = 0
  ```

---

## 3. CRI 처리 방식

### 3.1 답변
**CRI는 UCI payload에 포함되지만, 항상 0으로 인코딩됩니다.**

### 3.2 상세 설명
- **코드 위치**: `nr_ue_procedures.c:3042`
  ```c
  temp_payload_1 = (0/*mac->csi_measurements.cri*/ << ...) | ...
  ```
- **CRI bitlen 계산**: `cri_bitlen = ceil(log2(nb_resources))`
  - `nb_resources = 1`인 경우: `cri_bitlen = 0`
  - `nb_resources > 1`인 경우: `cri_bitlen > 0`이지만 **값은 항상 0**
- **RTD의 가정 (CRI 미포함)과의 차이**:
  - OAI는 CRI bitlen이 0이 아닌 경우에도 **0 값을 인코딩**
  - RTD가 CRI를 완전히 생략한다면, **비트 위치가 어긋날 수 있음**

### 3.3 실제 동작
- **nb_resources = 1**: CRI bitlen = 0 → payload에 CRI 없음 (RTD와 일치)
- **nb_resources > 1**: CRI bitlen > 0 → payload에 CRI 자리표시자 있음 (값은 0)

---

## 4. CSI Part-1 / Part-2 분리 여부

### 4.1 답변
**PUCCH 전송 시에는 Part-1만 사용되고, Part-2는 항상 0입니다.**

### 4.2 상세 설명
- **코드 위치**: `nr_ue_procedures.c:3039-3047`
  ```c
  else {  // PUCCH 전송 (mapping_type != ON_PUSCH)
    p1_bits = nr_get_csi_bitlen(csi_report);
    // ... Part-1 인코딩 ...
    // Part-2는 사용되지 않음
  }
  ```
- **PUSCH 전송 시**: Part-1과 Part-2로 분리
  ```c
  if (mapping_type == ON_PUSCH) {
    p1_bits = cri_bitlen + ri_bitlen + cqi_bitlen;
    p2_bits = pmi_x1_bitlen + pmi_x2_bitlen;
    // Part-1: CRI + RI + CQI
    // Part-2: PMI (i1 + i2)
  }
  ```
- **PUCCH 전송 시**: 모든 필드가 Part-1에 포함
  ```c
  else {
    p1_bits = nr_get_csi_bitlen(csi_report);  // 모든 필드 포함
    p2_bits = 0;  // Part-2 미사용
  }
  ```

### 4.3 RTD 처리 방법
- **PUCCH Format 2/3/4**: Part-1 payload만 디코딩하면 됨
- **Part-2는 무시해도 됨** (항상 0)

---

## 5. 실제 전송된 CSI UCI Payload 덤프

### 5.1 디버그 로그 활성화
코드에 이미 디버그 로그가 포함되어 있습니다:
- **파일**: `nr_ue_procedures.c:3051-3059`
- **로그 레벨**: `LOG_D` (DEBUG)

**로그 출력 내용:**
```
cri_bitlen = X
ri_bitlen = X
pmi_x1_bitlen = X
pmi_x2_bitlen = X
cqi_bitlen = X
csi_part1_payload = 0xXXXXXXXX
csi_part2_payload = 0xXXXXXXXX
part1_bits = X
part2_bits = X
```

### 5.2 로그 활성화 방법
1. **컴파일 시**: `-DLOG_D` 플래그 사용 (또는 기본적으로 활성화됨)
2. **런타임**: 로그 레벨을 DEBUG로 설정
3. **확인 위치**: `nr_ue_procedures.c:3051-3059`

### 5.3 추가 덤프 포인트
**PUCCH 인코딩 직전** (`nr_ue_procedures.c:1743, 1778, 1796`):
```c
pucch_pdu->payload = (pucch->csi_part1_payload << (pucch->n_harq + pucch->n_sr)) | 
                     (pucch->sr_payload << pucch->n_harq) | 
                     pucch->ack_payload;
```
이 시점에서 `pucch->csi_part1_payload`를 로그로 출력하면 최종 payload 확인 가능.

---

## 6. 요약 확인 질문 (Yes/No)

### 6.1 OAI는 해당 RRC 설정에서 CSI payload 길이를 고정 13bit로 보장하나요?
**No.** 
- Payload 길이는 RI 값, 안테나 포트 수, codebook mode에 따라 가변
- 예: RI=1, 4 ports → 약 13-15bit (padding 포함)
- 예: RI=2, 4 ports → 약 15-17bit

### 6.2 RI 값에 따라 PMI bit 수가 변하지 않나요?
**No.**
- **RI 값에 따라 PMI bit 수가 크게 변함**
- RI=1: 약 8bit (i11 + i12 + i2)
- RI=2: 약 9bit (i11 + i12 + i2 + i13)

### 6.3 CRI는 UCI payload에 포함되지 않나요?
**부분적으로 Yes.**
- CRI bitlen이 0이면 포함되지 않음 (nb_resources=1인 경우)
- CRI bitlen > 0이면 자리표시자로 포함되지만 **값은 항상 0**

### 6.4 RTD가 가정한 (RI2 + PMI6 + CQI4 + pad1) 구조가 OAI 구현과 일치하나요?
**No.**
- **PMI는 6bit 고정이 아님** (RI에 따라 8-9bit 이상)
- **Padding은 가변** (최소 payload 크기 요구사항에 따라)
- **CRI는 조건부 포함** (nb_resources > 1이면 포함, 값은 0)

---

## 7. RTD Mismatch 원인 분석

### 7.1 주요 불일치 사항
1. **PMI 비트 수**: RTD는 6bit 고정 가정, OAI는 RI에 따라 8-9bit 이상
2. **CRI 처리**: RTD는 완전 생략 가정, OAI는 bitlen > 0이면 자리표시자 포함
3. **비트 순서**: OAI는 `reverse_bits` 적용 → RTD가 역순으로 파싱해야 할 수 있음

### 7.2 해결 방안
1. **PMI 비트 수**: RI 값에 따라 동적으로 계산
2. **CRI 처리**: CRI bitlen 확인 후, bitlen > 0이면 자리표시자 비트 스킵
3. **비트 순서**: `reverse_bits` 적용 여부 확인 필요

---

## 8. 참고 코드 위치

### 주요 함수
- `get_csirs_RI_PMI_CQI_payload()`: `nr_ue_procedures.c:2994`
- `compute_csi_bitlen()`: `nr_mac_common.c:4676`
- `compute_pmi_bitlen()`: `nr_mac_common.c:4596`
- `set_bitlen_size_singlepanel()`: `nr_mac_common.c:4462`
- `compute_ri_bitlen()`: `nr_mac_common.c:4291`
- `nr_get_csi_bitlen()`: `nr_mac_common.c:4794`

### 주요 구조체
- `CSI_Meas_bitlen_t`: `nr_mac.h:495-506`
- `csi_payload_t`: `mac_defs.h:490-495`

---

## 9. 결론

OAI의 CSI UCI Payload 구조는 RTD의 가정과 여러 부분에서 다릅니다:
- **PMI는 RI에 따라 가변** (6bit 고정 아님)
- **CRI는 조건부 포함** (값은 항상 0)
- **비트 순서는 reverse_bits 적용됨**

RTD 디코더를 수정하여 OAI의 실제 payload 구조에 맞춰야 합니다.
