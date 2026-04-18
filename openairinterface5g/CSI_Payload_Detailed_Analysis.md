# OAI CSI UCI Payload 상세 코드 추적 분석 보고서

## 목적
OAI UE에서 PUCCH로 전송되는 CSI UCI payload의 bitmap(필드별 bit length + bit order + padding)이 실제로 어떻게 계산/패킹되는지 코드를 직접 따라가며 확인하고, RTD가 가정한 13bit(RI2 + PMI6 + CQI4 + pad1)와 불일치가 발생하는 정확한 지점을 라인 단위로 특정.

---

## 1. Entry Point 및 호출 흐름

### 1.1 호출 흐름 다이어그램

```
nr_get_csi_measurements() [nr_ue_procedures.c:2681]
  └─> nr_get_csi_payload() [nr_ue_procedures.c:2857]
      └─> get_csirs_RI_PMI_CQI_payload() [nr_ue_procedures.c:2994]
          ├─> csi_report->csi_meas_bitlen.* (이미 계산됨)
          ├─> nr_get_csi_bitlen() [nr_mac_common.c:4794] (PUCCH 전송 시)
          └─> reverse_bits() [nr_common.c:167]
```

### 1.2 상위 호출자

**1단계: CSI 스케줄링**
- **파일**: `openair2/LAYER2/NR_MAC_UE/nr_ue_procedures.c`
- **함수**: `nr_get_csi_measurements()` (라인 2681)
- **호출 위치**: `nr_ue_pucch_scheduler()` → `nr_get_csi_measurements()` (라인 1740)

**2단계: CSI Payload 생성**
- **파일**: `openair2/LAYER2/NR_MAC_UE/nr_ue_procedures.c`
- **함수**: `nr_get_csi_payload()` (라인 2857)
- **호출 위치**: `nr_get_csi_measurements()` → `nr_get_csi_payload()` (라인 2721, 2730)

**3단계: RI/PMI/CQI Payload 생성**
- **파일**: `openair2/LAYER2/NR_MAC_UE/nr_ue_procedures.c`
- **함수**: `get_csirs_RI_PMI_CQI_payload()` (라인 2994)
- **호출 위치**: `nr_get_csi_payload()` → `get_csirs_RI_PMI_CQI_payload()` (라인 2885)

### 1.3 CSI Bitlen 사전 계산 (초기화 시)

**파일**: `openair2/LAYER2/NR_MAC_COMMON/nr_mac_common.c`
- **함수**: `compute_csi_bitlen()` (라인 4676)
- **호출 위치**: `config_ue.c:2497` (RRC 설정 수신 시)
- **내용**: 모든 RI 값에 대해 bitlen을 미리 계산하여 `csi_report_template[]`에 저장

---

## 2. Bit Length 계산 경로 추적

### 2.1 PUCCH Periodic CSI 전송 시 Part-1/Part-2 Bitlen 결정

**파일**: `openair2/LAYER2/NR_MAC_UE/nr_ue_procedures.c`
**함수**: `get_csirs_RI_PMI_CQI_payload()`
**라인**: 3039-3047

```c
else {  // PUCCH 전송 (mapping_type != ON_PUSCH)
  p1_bits = nr_get_csi_bitlen(csi_report);  // 라인 3040
  padding_bitlen = p1_bits - (cri_bitlen + ri_bitlen + pmi_x1_bitlen + pmi_x2_bitlen + cqi_bitlen);  // 라인 3041
  // Part-2는 사용되지 않음 (p2_bits = 0)
}
```

**확인 사항**:
- ✅ **a) p1_bits = nr_get_csi_bitlen(csi_report) 호출됨** (라인 3040)
- ✅ **b) Part-2는 PUCCH에서 0으로 고정** (라인 3066에서 `p2_bits = 0`으로 초기화, PUCCH 경로에서는 설정 안 됨)

### 2.2 nr_get_csi_bitlen() 내부 로직

**파일**: `openair2/LAYER2/NR_MAC_COMMON/nr_mac_common.c`
**함수**: `nr_get_csi_bitlen()`
**라인**: 4794-4828

```c
uint16_t nr_get_csi_bitlen(nr_csi_report_t *csi_report)
{
  // ...
  csi_meas_bitlen = &(csi_report->csi_meas_bitlen);
  uint16_t temp_bitlen;
  for (int i = 0; i < 8; i++) {  // 라인 4815: 모든 RI 값(1~8)에 대해
    temp_bitlen = (csi_meas_bitlen->cri_bitlen+           // 라인 4816
                   csi_meas_bitlen->ri_bitlen+
                   csi_meas_bitlen->li_bitlen[i]+
                   csi_meas_bitlen->cqi_bitlen[i]+
                   csi_meas_bitlen->pmi_x1_bitlen[i]+      // 라인 4820
                   csi_meas_bitlen->pmi_x2_bitlen[i]);
    if(temp_bitlen > max_bitlen)                          // 라인 4822
      max_bitlen = temp_bitlen;                           // 라인 4823
  }
  csi_bitlen += max_bitlen;                                // 라인 4825
  return csi_bitlen;
}
```

**핵심 발견**:
- ✅ **"max_over_all_RI(...)" 기반 길이 산정 존재** (라인 4815-4825)
- 모든 RI 값(1~8)에 대해 bitlen을 계산하고, **최대값을 선택**하여 payload 길이로 사용
- 이로 인해 실제 RI 값과 무관하게 **가장 큰 RI의 bitlen이 사용됨**

### 2.3 compute_csi_bitlen() 내부 필드별 Bitlen 계산

**파일**: `openair2/LAYER2/NR_MAC_COMMON/nr_mac_common.c`
**함수**: `compute_csi_bitlen()`
**라인**: 4676-4792

**cri_RI_PMI_CQI 케이스** (라인 4774-4778):
```c
case (NR_CSI_ReportConfig__reportQuantity_PR_cri_RI_PMI_CQI):
  csi_report->csi_meas_bitlen.cri_bitlen = ceil(log2(nb_resources));  // 라인 4775
  csi_report->csi_meas_bitlen.ri_restriction = compute_ri_bitlen(csi_reportconfig, csi_report);  // 라인 4776
  compute_cqi_bitlen(csi_reportconfig, csi_report->csi_meas_bitlen.ri_restriction, csi_report);  // 라인 4777
  compute_pmi_bitlen(csi_reportconfig, csi_report->csi_meas_bitlen.ri_restriction, csi_report);  // 라인 4778
```

**규칙**:
1. **CRI bitlen**: `ceil(log2(nb_resources))` (라인 4775)
2. **RI bitlen**: `compute_ri_bitlen()` 호출 (라인 4776)
3. **CQI bitlen**: `compute_cqi_bitlen()` 호출 (라인 4777)
4. **PMI bitlen**: `compute_pmi_bitlen()` 호출 (라인 4778)

---

## 3. RI Bitlen 계산 로직

### 3.1 compute_ri_bitlen() 함수

**파일**: `openair2/LAYER2/NR_MAC_COMMON/nr_mac_common.c`
**함수**: `compute_ri_bitlen()`
**라인**: 4291-4343

### 3.2 typeI_SinglePanel_ri_Restriction 해석

**라인 4315**:
```c
uint8_t ri_restriction = type1single->typeI_SinglePanel_ri_Restriction.buf[0];
```

**라인 4329-4333** (4 ports, two_one 케이스):
```c
nb_allowed_ri = number_of_bits_set(ri_restriction);  // 라인 4329: 비트마스크에서 1인 비트 개수 계산
ri_bitlen = ceil(log2(nb_allowed_ri));               // 라인 4330: 허용된 RI 개수의 log2
ri_bitlen = ri_bitlen < 2 ? ri_bitlen : 2;          // 라인 4332: 상한 2bit cap
csi_report->csi_meas_bitlen.ri_bitlen = ri_bitlen;   // 라인 4333
```

**예시**:
- `ri_Restriction = 00001111` (비트 0,1,2,3이 1) → `nb_allowed_ri = 4` → `ceil(log2(4)) = 2` → **ri_bitlen = 2**
- `ri_Restriction = 00000001` (비트 0만 1) → `nb_allowed_ri = 1` → `ceil(log2(1)) = 0` → **ri_bitlen = 0**

**4 ports 조건에서 ri_bitlen 상한**:
- ✅ **2bit cap 존재** (라인 4332: `ri_bitlen = ri_bitlen < 2 ? ri_bitlen : 2`)
- 4 ports (two_one 또는 four_one)인 경우 최대 2bit

---

## 4. PMI Bitlen 계산 로직 (가장 중요)

### 4.1 compute_pmi_bitlen() 함수

**파일**: `openair2/LAYER2/NR_MAC_COMMON/nr_mac_common.c`
**함수**: `compute_pmi_bitlen()`
**라인**: 4596-4634

**RI별 PMI bitlen 배열 채우기** (라인 4599-4625):
```c
for(int i = 0; i < 8; i++) {  // RI = i+1 (1~8)
  csi_report->csi_meas_bitlen.pmi_x1_bitlen[i] = 0;
  csi_report->csi_meas_bitlen.pmi_x2_bitlen[i] = 0;
  if (codebookConfig == NULL || ((ri_restriction >> i) & 0x01) == 0)  // 라인 4602
    return;  // RI i+1이 허용되지 않으면 스킵
  else {
    // set_bitlen_size_singlepanel() 호출 (라인 4621)
    set_bitlen_size_singlepanel(&csi_report->csi_meas_bitlen, n1, n2, o1, o2, i + 1, type1->codebookMode);
  }
}
```

### 4.2 set_bitlen_size_singlepanel() 함수

**파일**: `openair2/LAYER2/NR_MAC_COMMON/nr_mac_common.c`
**함수**: `set_bitlen_size_singlepanel()`
**라인**: 4462-4593

### 4.3 RI=1 vs RI=2 PMI Bitlen 차이

#### RI=1 케이스 (라인 4467-4493)

**4 ports, n1=2, n2=1, o1=4, o2=1, codebookMode=1인 경우**:
```c
case 1:
  if(n2 > 1) {  // n2=1이므로 else 경로
    // ...
  }
  else{  // 라인 4480
    if (codebook_mode == 1) {  // 라인 4481
      csi_bitlen->pmi_i11_bitlen[i] = ceil(log2(n1 * o1));  // 라인 4482: ceil(log2(2*4)) = 3
      csi_bitlen->pmi_i12_bitlen[i] = ceil(log2(n2 * o2));  // 라인 4483: ceil(log2(1*1)) = 0
      csi_bitlen->pmi_x2_bitlen[i] = 2;                     // 라인 4484: 2bit
    }
  }
  csi_bitlen->pmi_i13_bitlen[i] = 0;  // 라인 4492: RI=1에서는 i13 없음
```

**결과**: `pmi_i11_bitlen[0] = 3`, `pmi_i12_bitlen[0] = 0`, `pmi_x2_bitlen[0] = 2`, `pmi_i13_bitlen[0] = 0`
- **총 PMI bitlen**: 3 + 0 + 2 = **5bit** (RTD 가정 6bit와 다름!)

**4 ports, n1=4, n2=1, o1=4, o2=1, codebookMode=1인 경우 (four_one)**:
```c
case 1:
  else{  // 라인 4480
    if (codebook_mode == 1) {  // 라인 4481
      csi_bitlen->pmi_i11_bitlen[i] = ceil(log2(n1 * o1));  // 라인 4482: ceil(log2(4*4)) = 4
      csi_bitlen->pmi_i12_bitlen[i] = ceil(log2(n2 * o2));  // 라인 4483: ceil(log2(1*1)) = 0
      csi_bitlen->pmi_x2_bitlen[i] = 2;                     // 라인 4484: 2bit
    }
  }
```

**결과**: `pmi_i11_bitlen[0] = 4`, `pmi_i12_bitlen[0] = 0`, `pmi_x2_bitlen[0] = 2`
- **총 PMI bitlen**: 4 + 0 + 2 = **6bit** (RTD 가정과 일치하지만, 이는 특수 케이스)

#### RI=2 케이스 (라인 4494-4535)

**4 ports, n1=2, n2=1, codebookMode=1인 경우**:
```c
case 2:
  if(n1 * n2 == 2) {  // 라인 4495: 2*1 = 2
    if (codebook_mode == 1) {  // 라인 4496
      csi_bitlen->pmi_i11_bitlen[i] = ceil(log2(n1 * o1));  // 라인 4497: ceil(log2(2*4)) = 3
      csi_bitlen->pmi_i12_bitlen[i] = ceil(log2(n2 * o2));  // 라인 4498: ceil(log2(1*1)) = 0
      csi_bitlen->pmi_x2_bitlen[i] = 1;                     // 라인 4499: 1bit (RI=2에서는 2bit → 1bit로 감소)
    }
    csi_bitlen->pmi_i13_bitlen[i] = 1;  // 라인 4506: RI=2에서 i13 추가 (1bit)
  }
```

**결과**: `pmi_i11_bitlen[1] = 3`, `pmi_i12_bitlen[1] = 0`, `pmi_x2_bitlen[1] = 1`, `pmi_i13_bitlen[1] = 1`
- **총 PMI bitlen**: 3 + 0 + 1 + 1 = **5bit**

**4 ports, n1=2, n2=2, codebookMode=1인 경우**:
```c
case 2:
  else {  // 라인 4508: n1*n2 != 2
    if(n2 > 1) {  // 라인 4509: n2=2
      if (codebook_mode == 1) {  // 라인 4510
        csi_bitlen->pmi_i11_bitlen[i] = ceil(log2(n1 * o1));  // 라인 4511: ceil(log2(2*4)) = 3
        csi_bitlen->pmi_i12_bitlen[i] = ceil(log2(n2 * o2));  // 라인 4512: ceil(log2(2*4)) = 3
        csi_bitlen->pmi_x2_bitlen[i] = 1;                     // 라인 4513: 1bit
      }
    }
    csi_bitlen->pmi_i13_bitlen[i] = 2;  // 라인 4533: RI=2에서 i13 추가 (2bit)
  }
```

**결과**: `pmi_i11_bitlen[1] = 3`, `pmi_i12_bitlen[1] = 3`, `pmi_x2_bitlen[1] = 1`, `pmi_i13_bitlen[1] = 2`
- **총 PMI bitlen**: 3 + 3 + 1 + 2 = **9bit** (RTD 가정 6bit와 크게 다름!)

### 4.4 pmi_x1_bitlen 계산

**파일**: `openair2/LAYER2/NR_MAC_COMMON/nr_mac_common.c`
**라인**: 4592

```c
csi_bitlen->pmi_x1_bitlen[i] = csi_bitlen->pmi_i11_bitlen[i] + csi_bitlen->pmi_i12_bitlen[i] + csi_bitlen->pmi_i13_bitlen[i];
```

**확인**:
- ✅ **pmi_x1_bitlen은 i11 + i12 + i13의 합**으로 계산됨
- ✅ **실제 패킹에서는 사용됨** (라인 3041, 3042, 3043에서 padding 계산 및 shift에 사용)

### 4.5 RTD 가정(PMI_i2=2bit, PMI_i11=4bit → 총 6bit)이 성립하지 않는 이유

#### (1) i11/i12 존재 여부
- **코드 근거**: `set_bitlen_size_singlepanel()`에서 `pmi_i11_bitlen`과 `pmi_i12_bitlen`을 별도로 계산 (라인 4470-4488)
- **실제**: i11과 i12는 **별도 필드**이며, i1은 이 둘을 합친 값이 아님 (i1은 별도로 측정됨)

#### (2) i2 bitlen
- **코드 근거**: `pmi_x2_bitlen[ri]`는 RI에 따라 **1bit 또는 2bit**로 변함
  - RI=1: `pmi_x2_bitlen[0] = 2` (라인 4484)
  - RI=2: `pmi_x2_bitlen[1] = 1` (라인 4499, 4513)
- **RTD 가정**: 항상 2bit (잘못된 가정)

#### (3) rank>1 추가 항목(i13 등)
- **코드 근거**: RI=2 이상에서 `pmi_i13_bitlen` 추가
  - RI=2, n1*n2=2: `pmi_i13_bitlen[1] = 1` (라인 4506)
  - RI=2, n1*n2>2: `pmi_i13_bitlen[1] = 2` (라인 4533)
- **RTD 가정**: i13 미고려 (잘못된 가정)

#### (4) codebookMode=1 영향
- **코드 근거**: `codebook_mode == 1`과 `codebook_mode != 1`에서 bitlen 계산식이 다름
  - Mode 1: `ceil(log2(n1 * o1))` (라인 4470, 4482)
  - Mode != 1: `ceil(log2(n1 * o1 / 2))` (라인 4475, 4487)
- **RTD 가정**: codebookMode 고려 안 함

---

## 5. CRI 포함 여부 확인

### 5.1 CRI Bitlen 계산

**파일**: `openair2/LAYER2/NR_MAC_COMMON/nr_mac_common.c`
**라인**: 4775

```c
csi_report->csi_meas_bitlen.cri_bitlen = ceil(log2(nb_resources));
```

**결과**:
- `nb_resources = 1` → `cri_bitlen = ceil(log2(1)) = 0` → **payload에 포함 안 됨**
- `nb_resources > 1` → `cri_bitlen > 0` → **payload에 자리표시자 포함**

### 5.2 CRI 실제 Payload 인코딩

**파일**: `openair2/LAYER2/NR_MAC_UE/nr_ue_procedures.c`
**라인**: 3042

```c
temp_payload_1 = (0/*mac->csi_measurements.cri*/ << (cqi_bitlen + pmi_x2_bitlen + pmi_x1_bitlen + padding_bitlen + ri_bitlen)) |
```

**확인**:
- ✅ **nb_resources==1이면 cri_bitlen=0이라 payload에 안 들어감** (shift 크기가 0)
- ✅ **nb_resources>1이면 cri_bitlen>0인데 값은 0으로 하드코딩됨** (주석 `/*mac->csi_measurements.cri*/`는 실제로 0)

---

## 6. Payload Bit Packing 순서 + reverse_bits 적용

### 6.1 reverse_bits 적용 전 비트 배치

**파일**: `openair2/LAYER2/NR_MAC_UE/nr_ue_procedures.c`
**라인**: 3042-3046

```c
temp_payload_1 = (0/*CRI*/ << (cqi_bitlen + pmi_x2_bitlen + pmi_x1_bitlen + padding_bitlen + ri_bitlen)) |
                 (ri << (cqi_bitlen + pmi_x2_bitlen + pmi_x1_bitlen + padding_bitlen)) |
                 (i1 << (cqi_bitlen + pmi_x2_bitlen)) |
                 (i2 << (cqi_bitlen)) |
                 (cqi);
```

**비트 배치 (LSB → MSB, reverse_bits 적용 전)**:
```
[LSB] CQI(cqi_bitlen) | i2(pmi_x2_bitlen) | i1(pmi_x1_bitlen) | Padding(padding_bitlen) | RI(ri_bitlen) | CRI(cri_bitlen) [MSB]
```

**예시 (RI=1, 4 ports, n1=2, n2=1, codebookMode=1, nb_resources=1)**:
- CRI: 0bit (cri_bitlen=0)
- RI: 2bit (ri_bitlen=2, ri_Restriction=00001111)
- Padding: 가변 (p1_bits - (0+2+5+4) = p1_bits - 11)
- i1: 3bit (pmi_i11_bitlen=3, pmi_i12_bitlen=0, pmi_i13_bitlen=0 → pmi_x1_bitlen=3)
- i2: 2bit (pmi_x2_bitlen=2)
- CQI: 4bit

**비트 배치**:
```
[LSB] CQI[3:0] | i2[1:0] | i1[2:0] | Padding | RI[1:0] [MSB]
```

### 6.2 reverse_bits 적용

**파일**: `openair2/LAYER2/NR_MAC_UE/nr_ue_procedures.c`
**라인**: 3049

```c
temp_payload_1 = reverse_bits(temp_payload_1, p1_bits);
```

**reverse_bits() 함수**:
**파일**: `common/utils/nr/nr_common.c`
**라인**: 167-187

```c
uint64_t reverse_bits(uint64_t in, int n_bits)
{
  // n_bits만큼의 비트를 역순으로 뒤집음
  // 예: n_bits=10, in=10 0000 1111 → return=11 1100 0001
}
```

### 6.3 reverse_bits 적용 후 최종 전송 비트 순서

**최종 전송 순서 (MSB → LSB, reverse_bits 적용 후)**:
```
[MSB] CRI(cri_bitlen) | RI(ri_bitlen) | Padding(padding_bitlen) | i1(pmi_x1_bitlen) | i2(pmi_x2_bitlen) | CQI(cqi_bitlen) [LSB]
```

**예시 (위와 동일 조건)**:
```
[MSB] RI[1:0] | Padding | i1[2:0] | i2[1:0] | CQI[3:0] [LSB]
```

### 6.4 RTD 디코더 파싱 순서

**코드 기준 판단**:
- OAI는 reverse_bits를 적용하므로, **RTD는 역순으로 파싱해야 함**
- 즉, **LSB부터 CQI → i2 → i1 → Padding → RI → CRI 순서로 파싱**해야 OAI와 일치

---

## 7. 최종 PUCCH Payload 합성 (ACK/SR/CSI)

### 7.1 PUCCH Payload 최종 합성 코드

**파일**: `openair2/LAYER2/NR_MAC_UE/nr_ue_procedures.c`
**라인**: 1743 (Format 2), 1778 (Format 3), 1796 (Format 4)

**Format 2 예시** (라인 1743):
```c
pucch_pdu->payload = (pucch->csi_part1_payload << (pucch->n_harq + pucch->n_sr)) | 
                     (pucch->sr_payload << pucch->n_harq) | 
                     pucch->ack_payload;
```

**비트 배치 (LSB → MSB)**:
```
[LSB] ACK(n_harq) | SR(n_sr) | CSI(p1_bits) [MSB]
```

### 7.2 RTD가 CSI만 떼어낼 때 필요한 정보

**필요한 정보**:
1. **CSI 시작 위치**: `n_harq + n_sr` 비트 이후
2. **CSI 길이**: `p1_bits` (또는 `pucch->n_csi`)
3. **비트 순서**: reverse_bits가 적용되었으므로 역순 파싱 필요

**코드 근거**:
- `pucch->n_csi = csi.p1_bits` (라인 2722, 2731)
- `pucch->csi_part1_payload`는 이미 reverse_bits가 적용된 상태 (라인 3049)

---

## 8. 재현 조건 기준 실제 Payload Bitlen 계산

### 8.1 시나리오
- Type-I Single Panel, 4 ports (n1_n2 four_one)
- codebookMode=1
- wideband PMI/CQI
- periodic PUCCH report
- ri_Restriction=00001111 (RI 1..4 허용)
- nb_resources=1 (CRI bitlen=0)

### 8.2 n1, n2, o1, o2 계산

**파일**: `openair2/LAYER2/NR_MAC_COMMON/nr_mac_common.c`
**함수**: `get_n1n2_o1o2_singlepanel()`
**라인**: 4391-4395

```c
case (NR_CodebookConfig__codebookType__type1__subType__typeI_SinglePanel__nrOfAntennaPorts__moreThanTwo__n1_n2_PR_four_one_TypeI_SinglePanel_Restriction):
  *n1 = 4;
  *n2 = 1;
  *o1 = 4;
  *o2 = 1;
```

**결과**: `n1=4`, `n2=1`, `o1=4`, `o2=1`

### 8.3 RI=1일 때 p1_bits 계산

#### CRI bitlen
- `cri_bitlen = ceil(log2(1)) = 0`

#### RI bitlen
- `ri_Restriction = 00001111` → `nb_allowed_ri = 4` → `ri_bitlen = min(ceil(log2(4)), 2) = 2`

#### PMI bitlen (RI=1)
- `pmi_i11_bitlen[0] = ceil(log2(4*4)) = 4` (라인 4482)
- `pmi_i12_bitlen[0] = ceil(log2(1*1)) = 0` (라인 4483)
- `pmi_x2_bitlen[0] = 2` (라인 4484)
- `pmi_i13_bitlen[0] = 0` (라인 4492)
- `pmi_x1_bitlen[0] = 4 + 0 + 0 = 4` (라인 4592)
- **총 PMI bitlen**: 4 + 2 = **6bit**

#### CQI bitlen
- `cqi_bitlen[0] = 4` (라인 4659)

#### 총 bitlen (RI=1)
- `p1_bits = max_over_all_RI(0 + 2 + 0 + 4 + 6 + 4) = 16bit` (최대값은 RI=1이 아닐 수 있음)

**실제 계산**: `nr_get_csi_bitlen()`은 모든 RI에 대해 계산하므로, RI=2,3,4도 확인 필요.

### 8.4 RI=2일 때 p1_bits 계산

#### PMI bitlen (RI=2, n1=4, n2=1)
- `n1 * n2 = 4 * 1 = 4` (라인 4495 조건 `n1*n2==2` 불만족)
- `n2 = 1` (라인 4509 조건 `n2>1` 불만족)
- `else` 경로 (라인 4521):
  - `pmi_i11_bitlen[1] = ceil(log2(4*4)) = 4` (라인 4523)
  - `pmi_i12_bitlen[1] = ceil(log2(1*1)) = 0` (라인 4524)
  - `pmi_x2_bitlen[1] = 1` (라인 4525)
  - `pmi_i13_bitlen[1] = 2` (라인 4533)
  - `pmi_x1_bitlen[1] = 4 + 0 + 2 = 6` (라인 4592)
  - **총 PMI bitlen**: 6 + 1 = **7bit**

#### 총 bitlen (RI=2)
- `p1_bits = max_over_all_RI(0 + 2 + 0 + 4 + 7 + 4) = 17bit`

### 8.5 최종 결과

**RI=1**: `p1_bits = 16bit` (예상, 실제는 max_over_all_RI 결과)
**RI=2**: `p1_bits = 17bit` (예상, 실제는 max_over_all_RI 결과)

**실제 p1_bits**: `nr_get_csi_bitlen()`이 모든 RI에 대해 최대값을 반환하므로, **RI=2의 17bit가 사용됨**

---

## 9. RTD 13bit 가정이 깨지는 결정적 코드 라인 3곳

### 9.1 PMI Bitlen 가변이 결정되는 라인

**파일**: `openair2/LAYER2/NR_MAC_COMMON/nr_mac_common.c`
**라인**: 4462-4593 (`set_bitlen_size_singlepanel()`)

**이유**:
- RI 값에 따라 `pmi_i11_bitlen[ri]`, `pmi_i12_bitlen[ri]`, `pmi_x2_bitlen[ri]`, `pmi_i13_bitlen[ri]`가 모두 달라짐
- RTD 가정(PMI 6bit 고정)과 완전히 불일치

### 9.2 Padding 가변이 결정되는 라인

**파일**: `openair2/LAYER2/NR_MAC_UE/nr_ue_procedures.c`
**라인**: 3041

```c
padding_bitlen = p1_bits - (cri_bitlen + ri_bitlen + pmi_x1_bitlen + pmi_x2_bitlen + cqi_bitlen);
```

**이유**:
- `p1_bits`는 `nr_get_csi_bitlen()`에서 **max_over_all_RI**로 계산되므로, 실제 RI 값과 무관하게 최대값 사용
- 실제 RI의 bitlen이 작으면 padding이 커짐
- RTD 가정(padding 1bit 고정)과 불일치

### 9.3 reverse_bits 적용 라인

**파일**: `openair2/LAYER2/NR_MAC_UE/nr_ue_procedures.c`
**라인**: 3049

```c
temp_payload_1 = reverse_bits(temp_payload_1, p1_bits);
```

**이유**:
- 비트 순서가 완전히 역순으로 뒤집힘
- RTD가 순차적으로 파싱하면 필드 순서가 완전히 어긋남

---

## 10. 호출 흐름 다이어그램 (텍스트)

```
nr_ue_pucch_scheduler() [nr_ue_scheduler.c:1717]
  └─> nr_get_csi_measurements() [nr_ue_procedures.c:2681]
      └─> nr_get_csi_payload() [nr_ue_procedures.c:2857]
          └─> get_csirs_RI_PMI_CQI_payload() [nr_ue_procedures.c:2994]
              ├─> csi_report->csi_meas_bitlen.* (사전 계산됨, compute_csi_bitlen()에서)
              │   ├─> compute_ri_bitlen() [nr_mac_common.c:4291]
              │   ├─> compute_pmi_bitlen() [nr_mac_common.c:4596]
              │   │   └─> set_bitlen_size_singlepanel() [nr_mac_common.c:4462]
              │   └─> compute_cqi_bitlen() [nr_mac_common.c:4636]
              ├─> nr_get_csi_bitlen() [nr_mac_common.c:4794] (PUCCH 전송 시)
              │   └─> max_over_all_RI 계산 (라인 4815-4825)
              ├─> Payload 패킹 (라인 3042-3046)
              └─> reverse_bits() [nr_common.c:167] (라인 3049)
```

---

## 11. RI=1 / RI=2 Payload Bitmap 표

### 11.1 RI=1 Payload Bitmap (4 ports, n1=4, n2=1, codebookMode=1, nb_resources=1)

**reverse_bits 적용 전 (LSB → MSB)**:
| 필드 | Bitlen | 비트 위치 (LSB 기준) |
|------|--------|---------------------|
| CQI | 4 | [3:0] |
| i2 | 2 | [5:4] |
| i1 | 4 | [9:6] |
| Padding | 가변 | [p1_bits-3:p1_bits-ri_bitlen-1] |
| RI | 2 | [p1_bits-1:p1_bits-2] |
| CRI | 0 | - |

**reverse_bits 적용 후 (MSB → LSB)**:
| 필드 | Bitlen | 비트 위치 (MSB 기준) |
|------|--------|---------------------|
| CRI | 0 | - |
| RI | 2 | [p1_bits-1:p1_bits-2] |
| Padding | 가변 | [p1_bits-3:p1_bits-ri_bitlen-1] |
| i1 | 4 | [9:6] |
| i2 | 2 | [5:4] |
| CQI | 4 | [3:0] |

### 11.2 RI=2 Payload Bitmap (동일 조건)

**reverse_bits 적용 전 (LSB → MSB)**:
| 필드 | Bitlen | 비트 위치 (LSB 기준) |
|------|--------|---------------------|
| CQI | 4 | [3:0] |
| i2 | 1 | [4] |
| i1 | 6 | [10:5] (i11=4 + i13=2) |
| Padding | 가변 | [p1_bits-3:p1_bits-ri_bitlen-1] |
| RI | 2 | [p1_bits-1:p1_bits-2] |
| CRI | 0 | - |

**reverse_bits 적용 후 (MSB → LSB)**:
| 필드 | Bitlen | 비트 위치 (MSB 기준) |
|------|--------|---------------------|
| CRI | 0 | - |
| RI | 2 | [p1_bits-1:p1_bits-2] |
| Padding | 가변 | [p1_bits-3:p1_bits-ri_bitlen-1] |
| i1 | 6 | [10:5] |
| i2 | 1 | [4] |
| CQI | 4 | [3:0] |

---

## 12. 결론

### 12.1 RTD 13bit 가정과의 불일치 요약

1. **PMI bitlen 가변**: RI, 안테나 구성, codebookMode에 따라 5~9bit로 변함 (RTD 가정 6bit 고정과 불일치)
2. **Padding 가변**: max_over_all_RI 기반 계산으로 실제 RI와 무관하게 최대값 사용 (RTD 가정 1bit 고정과 불일치)
3. **비트 순서 역전**: reverse_bits 적용으로 RTD가 역순 파싱 필요

### 12.2 RTD 디코더 수정 필요 사항

1. **PMI bitlen 동적 계산**: RI 값에 따라 i11, i12, i13, i2 bitlen을 별도 계산
2. **Padding 동적 계산**: 실제 payload 길이에서 필드별 bitlen을 빼서 계산
3. **비트 순서 역순 파싱**: LSB부터 CQI → i2 → i1 → Padding → RI → CRI 순서로 파싱

---

## 부록: 주요 코드 라인 참조

| 항목 | 파일 | 함수 | 라인 |
|------|------|------|------|
| Entry Point | nr_ue_procedures.c | get_csirs_RI_PMI_CQI_payload | 2994 |
| Part-1 bitlen 계산 | nr_ue_procedures.c | get_csirs_RI_PMI_CQI_payload | 3040 |
| max_over_all_RI | nr_mac_common.c | nr_get_csi_bitlen | 4815-4825 |
| RI bitlen 계산 | nr_mac_common.c | compute_ri_bitlen | 4291-4343 |
| PMI bitlen 계산 | nr_mac_common.c | set_bitlen_size_singlepanel | 4462-4593 |
| pmi_x1_bitlen 계산 | nr_mac_common.c | set_bitlen_size_singlepanel | 4592 |
| CRI bitlen 계산 | nr_mac_common.c | compute_csi_bitlen | 4775 |
| Payload 패킹 | nr_ue_procedures.c | get_csirs_RI_PMI_CQI_payload | 3042-3046 |
| reverse_bits 적용 | nr_ue_procedures.c | get_csirs_RI_PMI_CQI_payload | 3049 |
| PUCCH 합성 | nr_ue_procedures.c | nr_ue_configure_pucch | 1743, 1778, 1796 |
