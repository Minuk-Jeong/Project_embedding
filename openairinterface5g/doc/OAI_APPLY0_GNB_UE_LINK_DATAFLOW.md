# OAI `APPLY=0` 시 gNB↔UE 링크 신호처리: IFFT/FFT/컨볼루션

이 문서는 rfsimulator에서 `OAI_SIONNA_RFSIM_APPLY=0` (즉 Sionna 평탄 `H` 적용이 꺼짐)인 상태에서, gNB와 UE가 링크되며 실제 IQ가 처리되는 과정을 **수식 관점**과 **근거 코드 조각** 관점으로 정리합니다.

핵심은 아래 3개 구간입니다.

1. gNB: OFDM 변조(주파수→시간)에서 **IFFT**와 **CP 삽입**
2. rfsimulator: 채널 모델 옵션에 따라
   - `chanmod` 활성: **FIR 컨볼루션**(`rxAddInput`)
   - `chanmod` 비활성: **단순 MIMO 믹싱 + AWGN**
3. UE: OFDM 수신(시간→주파수)에서 **FFT(dft 호출)**와 이후 채널 추정/보정

---

## 0. 용어/전제

- `APPLY=0`은 rfsimulator에서 Sionna가 만든 평탄 MIMO 행렬 `H`를 곱하지 않는다는 의미입니다.
- gNB/UE의 OFDM IFFT/FFT는 `APPLY`와 무관하게 PHY 내부에서 항상 수행됩니다.
- rfsimulator에서 “컨볼루션이 있냐/없냐”는 `OAI_SIONNA`와 별개로, 주로 `rfsimulator` 실행 옵션에 포함된 `chanmod` 여부에 따라 결정됩니다.

---

## 1) gNB: OFDM 변조 = IFFT + CP 삽입

### 수식(개념)

OFDM 한 심볼에서, 주파수 영역(리소스 그리드) 샘플 `X[k]`를 시간 영역 샘플 `x[n]`로 바꾸는 과정은 일반적으로 IFFT로 표현됩니다.

```text
x[n] = sum_{k=0}^{N-1} X[k] * exp(j*2*pi*k*n/N) / N,  n=0..N-1
```

그 다음 CP(사이클릭 프리픽스)를 추가해서 길이를 늘립니다.

```text
x_cp[n] = x[n - Ncp],  n=0..Ncp-1
```

### 근거 코드 (OAI)

`openair1/PHY/MODULATION/ofdm_mod.c`의 `PHY_ofdm_mod()`에서 `idft()`(IFFT 엔진)를 호출하고, `CYCLIC_PREFIX`일 때 CP를 복사합니다.

```text
openair1/PHY/MODULATION/ofdm_mod.c
  idft(idft_size, (int16_t *)&input[i * fftsize], (int16_t *)output_ptr, 1);
  memcpy((void *)&output_ptr[-nb_prefix_samples],
         (void *)&output_ptr[fftsize - nb_prefix_samples],
         nb_prefix_samples * sizeof(c16_t));
```

그리고 `do_OFDM_mod()`에서 각 안테나/슬롯에 대해 `PHY_ofdm_mod(..., CYCLIC_PREFIX)`를 반복 호출합니다.

```text
openair1/PHY/MODULATION/ofdm_mod.c
  PHY_ofdm_mod((int *)&txdataF[aa][slot_offset_F],
               (int *)&txdata[aa][slot_offset],
               frame_parms->ofdm_symbol_size,
               12,                 // number of symbols
               frame_parms->ofdm_symbol_size>>2, // CP length
               CYCLIC_PREFIX);
```

---

## 2) rfsimulator: IQ 채널 처리 (APPLY=0 기준)

rfsimulator는 gNB로부터 받은 시간영역 IQ를 UE 쪽으로 전달하기 전에, 채널 모델/잡음을 적용합니다.

`APPLY=0`이면, rfsimulator의 Sionna 스레드/평탄 H 적용은 켜지지 않아서 `rfsimulator_read()` 내부의 `#ifdef OAI_PYTHON_EMBED` 조건이 만족되지 않습니다.
따라서 `no channel modeling` 경로에서 **Sionna 곱셈이 아니라 legacy 단순 믹싱 계수**가 사용됩니다(아래 2-A).

### 2-A) `chanmod` 비활성: 컨볼루션 없음, 단순 MIMO 믹싱 + AWGN

#### 수식(코드가 하는 일)

`ptr->channel_model == NULL`이면 아래와 같은 “복소 샘플 더하기(믹싱)”가 일어납니다.

```text
acc = sum_{tx} coeff(tx, rx) * x_tx[n]
y_rx[n] = clamp(int16(acc_real), int16(acc_imag)) + (필요시 noise)
```

그리고 rfsimulator가 `num_chanmod_channels == 0`일 때는 전역 noise 파라미터로 **AWGN을 시간 샘플 레벨에서 더합니다.**

#### 근거 코드 (단순 믹싱)

`openairinterface5g/radio/rfsimulator/simulator.c`에서 `else { // no channel modeling }` 블록과 그 내부 믹싱/클램프가 구현되어 있습니다.

```text
radio/rfsimulator/simulator.c
  // no channel modeling
  for (int a_tx = 0; a_tx < nbAnt_tx; a_tx++) {
    const sample_t x = ptr->circularBuf[((firstIndex + i) * nbAnt_tx + a_tx) % CirSize];

    // APPLY=0이면 여기의 Sionna 경로는 비활성이고,
    // 아래 legacy simple MIMO mixing이 실행됩니다.
    uint32_t ant_diff = abs(a_tx - a_rx);
    double coeff = ant_diff ? (0.2 / ant_diff) : 1.0;
    acc_r += (int32_t)lround((double)x.r * coeff);
    acc_i += (int32_t)lround((double)x.i * coeff);
  }

  out[i].r = (int16_t)acc_r;
  out[i].i = (int16_t)acc_i;
```

#### 근거 코드 (AWGN 추가)

`num_chanmod_channels == 0`이면 `OAI_RFSIM_AWGN_DBFS` 또는 기본 noise로 noise를 샘플에 더합니다.

```text
radio/rfsimulator/simulator.c
  if (num_chanmod_channels == 0) {
    int dbfs = get_noise_power_dBFS();
    const char *awgn_env = getenv("OAI_RFSIM_AWGN_DBFS");
    if (awgn_env != NULL && awgn_env[0] != '\0')
      dbfs = atoi(awgn_env);

    const int16_t noise_power =
      (int16_t)(32767.0 / powf(10.0, .05 * (float)(-dbfs)));

    for (int a = 0; a < nbAnt; a++) {
      for (int i = 0; i < nsamps; i++) {
        out[i].r = (int16_t)((int32_t)out[i].r +
                              (int32_t)lroundf((float)noise_power * gaussZiggurat(0.0, 1.0)));
        out[i].i = (int16_t)((int32_t)out[i].i +
                              (int32_t)lroundf((float)noise_power * gaussZiggurat(0.0, 1.0)));
      }
    }
  }
```

---

### 2-B) `chanmod` 활성: FIR 컨볼루션(경로 탭) + (선택) 도플러 위상 + 잡음

`rfsimulator` 실행 시 `rfsimulator.options`에 `chanmod`가 포함되면 rfsimulator는 채널모델을 초기화하고(`init_channelmod`, `load_channellist`) `ptr->channel_model != NULL`가 됩니다.

```text
radio/rfsimulator/simulator.c
  else if (strcmp(rfsimu_params[p].strlistptr[i], "chanmod") == 0) {
    init_channelmod();
    load_channellist(...);
    rfsimulator->channelmod = true;
  }
```

이 경우 rfsimulator는 `rfsimulator_read()`에서 `rxAddInput()`을 호출해, 채널 디스크립터의 탭 배열(`channelDesc->ch[...]`)을 이용한 **컨볼루션**을 수행합니다.

#### 수식(코드가 하는 일)

`rxAddInput()`의 핵심은 각 출력 샘플에 대해 탭 인덱스 `l`을 순회하며, 입력 `x[idx]`와 탭 `h[l]`를 복소 곱 후 합산하는 것입니다.

```text
y[n] = sum_{tx} pathLoss * sum_{l=0}^{L-1} h_{rx,tx}[l] * x_tx[n - l] + noise
```

#### 근거 코드 (컨볼루션 루프)

`radio/rfsimulator/apply_channelmod.c`의 `rxAddInput()`에서 아래 구간이 FIR 컨볼루션의 본체입니다.

```text
radio/rfsimulator/apply_channelmod.c
  for (int txAnt=0; txAnt < nbTx; txAnt++) {
    const struct complexd *channelModel = channelDesc->ch[rxAnt+(txAnt*channelDesc->nb_rx)];
    for (int l = 0; l < (int)channelDesc->channel_length; l++) {
      ...
      const struct complex16 tx16 = input_sig[idx];

      rx_tmp.r += tx16.r * channelModel[l].r - tx16.i * channelModel[l].i;
      rx_tmp.i += tx16.i * channelModel[l].r + tx16.r * channelModel[l].i;
    }
  }

  out_ptr->r += rx_tmp.r * pathLossLinear + noise_per_sample * gaussZiggurat(0.0, 1.0);
  out_ptr->i += rx_tmp.i * pathLossLinear + noise_per_sample * gaussZiggurat(0.0, 1.0);
```

또한 `channelDesc->Doppler_phase_inc != 0`이면, 누적된 복소 샘플 `rx_tmp`에 대해 도플러 위상회전을 곱합니다.

```text
radio/rfsimulator/apply_channelmod.c
  if (channelDesc->Doppler_phase_inc != 0.0) {
    double complex out = in * cexp(Doppler_phase_cur * I);
    rx_tmp.r = creal(out);
    rx_tmp.i = cimag(out);
    Doppler_phase_cur += channelDesc->Doppler_phase_inc;
  }
```

---

## 3) UE: OFDM 수신에서 FFT(dft 호출)

### 수식(개념)

UE는 CP를 제거한 후 FFT로 주파수 영역 심볼을 얻습니다.

```text
Y[k] = sum_{n=0}^{N-1} y[n] * exp(-j*2*pi*k*n/N)
```

여기서 `y[n]`은 rfsimulator를 거친 시간영역 수신 샘플입니다.

### 근거 코드 (front_end_fft)

UE FEP(Front-End Processor)의 `front_end_fft()`에서 `dft()`(FFT 엔진)를 호출합니다.

`openair1/PHY/MODULATION/slot_fep.c`의 아래 구간이 “시간 샘플을 dft로 바꿔 주파수 심볼을 만든다”는 핵심입니다.

```text
openair1/PHY/MODULATION/slot_fep.c
  int s = frame_parms->ofdm_symbol_size;
  dft_size_idx_t dftsizeidx = get_dft(s);

  ...
  unsigned int nb_prefix_samples = (no_prefix ? 0 : frame_parms->nb_prefix_samples);
  ...
  rx_offset = sample_offset + slot_offset + nb_prefix_samples0 + subframe_offset - SOFFSET;

  ...
  dft(dftsizeidx,
      (int16_t *)&common_vars->rxdata[aa][rx_offset % frame_length_samples],
      (int16_t *)&common_vars->common_vars_rx_data_per_thread[threadId]
        .rxdataF[aa][frame_parms->ofdm_symbol_size*symbol],
      1);
```

`front_end_fft()`는 `rx_offset` 계산에 `nb_prefix_samples`(CP 길이)와 관련된 항이 포함되므로, `dft`에 들어가는 입력은 “CP 제거 후 OFDM 심볼 구간”이 되도록 설계되어 있습니다.

참고로 `slot_fep.c`에는 입력 정렬 상태에 따라 `tmp_dft_in`을 거쳐 `dft()`를 호출하는 분기도 존재합니다.
```text
openair1/PHY/MODULATION/slot_fep.c
  if ((rx_offset&7)!=0) {
    memcpy((void *)tmp_dft_in,
           (void *)&common_vars->rxdata[aa][rx_offset % frame_length_samples],
           frame_parms->ofdm_symbol_size*sizeof(int));
    dft(dftsizeidx,(int16_t *)tmp_dft_in,
        (int16_t *)&common_vars->common_vars_rx_data_per_thread[threadId]
          .rxdataF[aa][frame_parms->ofdm_symbol_size*symbol],1);
  } else {
    dft(dftsizeidx,
        (int16_t *)&common_vars->rxdata[aa][(rx_offset) % frame_length_samples],
        (int16_t *)&common_vars->common_vars_rx_data_per_thread[threadId].rxdataF[aa]
          [frame_parms->ofdm_symbol_size*symbol],1);
  }
```

---

## 4) 정리: APPLY=0에서 전체 체인(요약 수식)

`APPLY=0`이고 rfsimulator에서 `chanmod`가 꺼져 있다면(예: Sionna flat-H만 끄고, RF 시뮬레이터는 단순 믹싱만 하는 구성),

1. gNB:
   ```text
   x[n] = IDFT{X[k]}
   x_cp = CP_insert(x)
   ```
2. rfsimulator:
   ```text
   y_rx[n] = sum_{tx} coeff(tx,rx) * x_tx[n] + w[n]
   ```
3. UE:
   ```text
   Y[k] = FFT{y[n]}  (CP 제거 후 dft 입력)
   ```

반대로 `chanmod`가 켜져 있다면,

2. rfsimulator:
   ```text
   y_rx[n] = sum_{tx} pathLoss * sum_{l=0}^{L-1} h_{rx,tx}[l] * x_tx[n-l] + w[n]
   ```

로 바뀝니다.

---

## (선택) 다음 확인 포인트

- 지금 실행 스크립트에서 `rfsimulator.options chanmod`가 켜져 있는지 확인해 주세요.
  - 켜져 있으면 컨볼루션(`rxAddInput`)이 수행됩니다.
  - 꺼져 있으면 단순 믹싱+AWGN(`num_chanmod_channels == 0` 경로)이 수행됩니다.
- UE 로그에서 `dft`/`slot_fep` 단계의 타이밍 및 잡음 영향을 함께 관측하면, SINR 출렁임의 원인을 “컨볼루션 탭 변화 vs 단순 H(혹은 믹싱 계수) 변화”로 분리할 수 있습니다.

