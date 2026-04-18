# OAI 채널을 Sionna로 대체하는 방안

## 개요

이 문서는 OpenAirInterface (OAI)의 채널 기능을 Sionna의 채널 모델로 대체하는 방법을 제안합니다. Sionna는 3GPP TR 38.901 표준 기반의 정교한 채널 모델을 제공하며, TensorFlow 기반으로 GPU 가속을 지원합니다.

## 목차

1. [OAI와 Sionna 채널 비교](#1-oai와-sionna-채널-비교)
2. [대체 방법](#2-대체-방법)
3. [방법별 상세 구현](#3-방법별-상세-구현)
4. [권장 방법](#4-권장-방법)
5. [구현 예시](#5-구현-예시)
6. [고려사항](#6-고려사항)

---

## 1. OAI와 Sionna 채널 비교

### 1.1 OAI 채널 특징

- **구현 언어**: C/C++
- **채널 모델**: 간단한 모델 (AWGN, Rayleigh 등)
- **최적화**: 실시간 시뮬레이션에 최적화
- **인터페이스**: C 함수 기반
- **제한사항**: 
  - 제한적인 채널 모델
  - 3GPP 표준 모델 미지원
  - GPU 가속 제한적

### 1.2 Sionna 채널 특징

- **구현 언어**: Python (TensorFlow)
- **채널 모델**: 
  - 3GPP TR 38.901 표준 모델 (TDL, CDL, UMi, UMa, RMa)
  - Rayleigh Block Fading
  - AWGN
  - 외부 CIR 데이터셋 지원
- **최적화**: 
  - GPU 가속 지원
  - 배치 처리 최적화
  - JIT 컴파일 지원
- **인터페이스**: Python 클래스 기반
- **장점**:
  - 표준 기반 정교한 채널 모델
  - 높은 성능 (GPU 활용)
  - 유연한 확장성

### 1.3 비교표

| 항목 | OAI | Sionna |
|------|-----|--------|
| 채널 모델 다양성 | 제한적 | 매우 다양 (3GPP 표준) |
| 성능 | CPU 최적화 | GPU 가속 가능 |
| 표준 준수 | 부분적 | 3GPP TR 38.901 완전 준수 |
| 배치 처리 | 제한적 | 완전 지원 |
| 확장성 | 낮음 | 높음 |
| 실시간 처리 | 우수 | 배치 처리에 최적화 |

---

## 2. 대체 방법

### 2.1 방법 1: 직접 통합 (Direct Integration)

**개념**: Sionna 채널 모델을 OAI 코드베이스에 직접 통합

**장점**:
- 완전한 통합
- 최소한의 인터페이스 오버헤드
- 성능 최적화 가능

**단점**:
- OAI 코드베이스 수정 필요
- Python-C 바인딩 필요
- 유지보수 복잡도 증가

**적용 시나리오**:
- OAI 코드베이스를 직접 수정할 수 있는 경우
- 장기적인 통합이 필요한 경우

### 2.2 방법 2: 하이브리드 방식 (Hybrid Approach)

**개념**: Sionna로 채널 계수를 사전 생성하고, OAI에서 사용

**장점**:
- OAI 코드베이스 수정 최소화
- 채널 생성과 시뮬레이션 분리
- 구현이 상대적으로 간단

**단점**:
- 사전 생성된 채널 데이터 필요
- 메모리 사용량 증가
- 동적 채널 변경 제한적

**적용 시나리오**:
- 채널이 사전에 알려진 경우
- 오프라인 시뮬레이션
- 채널 데이터를 파일로 저장/로드하는 경우

### 2.3 방법 3: 래퍼 인터페이스 (Wrapper Interface)

**개념**: Sionna 채널을 OAI 인터페이스로 래핑하는 C 확장 모듈 생성

**장점**:
- OAI 인터페이스 유지
- Python-C 바인딩으로 통합
- 유연한 채널 모델 선택

**단점**:
- Python-C 바인딩 구현 필요
- 런타임 오버헤드 존재
- 디버깅 복잡도 증가

**적용 시나리오**:
- OAI 인터페이스를 유지해야 하는 경우
- 다양한 채널 모델을 동적으로 선택해야 하는 경우

### 2.4 방법 4: 외부 서비스 (External Service)

**개념**: Sionna 채널을 독립적인 서비스로 실행하고, OAI와 통신

**장점**:
- 완전한 분리
- 독립적인 확장 가능
- 다양한 언어/플랫폼 지원

**단점**:
- 네트워크 통신 오버헤드
- 복잡한 아키텍처
- 실시간 처리에 부적합할 수 있음

**적용 시나리오**:
- 마이크로서비스 아키텍처
- 분산 시뮬레이션
- 클라우드 기반 시뮬레이션

---

## 3. 방법별 상세 구현

### 3.1 방법 1: 직접 통합

#### 3.1.1 Python-C 바인딩 (Cython 사용)

```python
# sionna_channel_wrapper.pyx
import numpy as np
cimport numpy as np
from sionna.phy.channel import GenerateOFDMChannel, ApplyOFDMChannel

cdef class SionnaChannelWrapper:
    cdef object channel_model
    cdef object ofdm_channel_gen
    cdef object apply_channel
    
    def __init__(self, channel_model, resource_grid):
        self.channel_model = channel_model
        self.ofdm_channel_gen = GenerateOFDMChannel(
            channel_model, resource_grid
        )
        self.apply_channel = ApplyOFDMChannel()
    
    def generate_channel(self, int batch_size):
        """채널 주파수 응답 생성"""
        h_freq = self.ofdm_channel_gen(batch_size)
        return h_freq.numpy()
    
    def apply_channel_to_signal(self, 
                                 np.ndarray x,
                                 np.ndarray h_freq,
                                 float noise_power):
        """신호에 채널 적용"""
        import tensorflow as tf
        x_tf = tf.convert_to_tensor(x, dtype=tf.complex64)
        h_tf = tf.convert_to_tensor(h_freq, dtype=tf.complex64)
        y = self.apply_channel(x_tf, h_tf, noise_power)
        return y.numpy()
```

#### 3.1.2 C 인터페이스

```c
// sionna_channel_c.h
#ifndef SIONNA_CHANNEL_C_H
#define SIONNA_CHANNEL_C_H

#ifdef __cplusplus
extern "C" {
#endif

typedef struct {
    void* wrapper;  // Python 객체 포인터
} SionnaChannel;

// 채널 생성기 초기화
SionnaChannel* sionna_channel_init(const char* model_type,
                                    double carrier_freq,
                                    int num_subcarriers,
                                    double subcarrier_spacing);

// 채널 주파수 응답 생성
int sionna_generate_channel(SionnaChannel* channel,
                            int batch_size,
                            double* h_real, double* h_imag);

// 채널 적용
int sionna_apply_channel(SionnaChannel* channel,
                         double* x_real, double* x_imag,
                         double* h_real, double* h_imag,
                         double noise_power,
                         double* y_real, double* y_imag);

// 리소스 해제
void sionna_channel_free(SionnaChannel* channel);

#ifdef __cplusplus
}
#endif

#endif // SIONNA_CHANNEL_C_H
```

### 3.2 방법 2: 하이브리드 방식

#### 3.2.1 채널 사전 생성 스크립트

```python
# generate_channel_dataset.py
import numpy as np
import tensorflow as tf
import h5py
from sionna.phy.channel.tr38901 import UMi, Antenna, PanelArray
from sionna.phy.channel import GenerateOFDMChannel
from sionna.phy.ofdm import ResourceGrid
from sionna.sys import gen_hexgrid_topology

def generate_channel_dataset(output_file, num_samples, batch_size):
    """채널 데이터셋 사전 생성"""
    
    # 리소스 그리드 설정
    rg = ResourceGrid(
        num_ofdm_symbols=14,
        fft_size=1024,
        subcarrier_spacing=15e3
    )
    
    # 안테나 배열 설정
    ut_array = Antenna(
        polarization="single",
        polarization_type="V",
        antenna_pattern="omni",
        carrier_frequency=3.5e9
    )
    
    bs_array = PanelArray(
        num_rows_per_panel=4,
        num_cols_per_panel=4,
        polarization='dual',
        polarization_type='VH',
        antenna_pattern='38.901',
        carrier_frequency=3.5e9
    )
    
    # 채널 모델 생성
    channel_model = UMi(
        carrier_frequency=3.5e9,
        o2i_model='low',
        ut_array=ut_array,
        bs_array=bs_array,
        direction='downlink',
        enable_pathloss=True,
        enable_shadow_fading=True
    )
    
    # 토폴로지 생성 및 설정
    topology = gen_hexgrid_topology(
        batch_size=batch_size,
        num_rings=1,
        num_ut_per_sector=3,
        scenario='umi',
        min_bs_ut_dist=10.0,
        max_bs_ut_dist=200.0,
        los=True,
        return_grid=True
    )
    
    channel_model.set_topology(*topology)
    
    # OFDM 채널 생성기
    ofdm_channel_gen = GenerateOFDMChannel(
        channel_model=channel_model,
        resource_grid=rg,
        normalize_channel=False
    )
    
    # HDF5 파일 생성
    with h5py.File(output_file, 'w') as f:
        # 데이터셋 생성
        h_freq_dset = f.create_dataset(
            'h_freq',
            shape=(num_samples, 1, 1, 1, 1, 14, 1024),
            dtype=np.complex64
        )
        
        # 채널 생성
        for i in range(0, num_samples, batch_size):
            current_batch = min(batch_size, num_samples - i)
            h_freq = ofdm_channel_gen(current_batch)
            h_freq_np = h_freq.numpy()
            
            h_freq_dset[i:i+current_batch] = h_freq_np
            
            print(f"Generated {i+current_batch}/{num_samples} samples")

if __name__ == "__main__":
    generate_channel_dataset(
        output_file="channel_dataset.h5",
        num_samples=1000,
        batch_size=32
    )
```

#### 3.2.2 OAI에서 채널 데이터 로드

```c
// oai_channel_loader.c
#include <hdf5.h>
#include "oai_channel.h"

typedef struct {
    hid_t file_id;
    hid_t dataset_id;
    int current_index;
    int total_samples;
} ChannelDataset;

ChannelDataset* load_channel_dataset(const char* filename) {
    ChannelDataset* ds = malloc(sizeof(ChannelDataset));
    
    ds->file_id = H5Fopen(filename, H5F_ACC_RDONLY, H5P_DEFAULT);
    ds->dataset_id = H5Dopen2(ds->file_id, "/h_freq", H5P_DEFAULT);
    
    // 데이터셋 크기 확인
    hid_t space_id = H5Dget_space(ds->dataset_id);
    hsize_t dims[7];
    H5Sget_simple_extent_dims(space_id, dims, NULL);
    ds->total_samples = dims[0];
    ds->current_index = 0;
    
    H5Sclose(space_id);
    
    return ds;
}

void get_channel_response(ChannelDataset* ds, 
                          complex_t* h_freq,
                          int num_subcarriers) {
    hsize_t start[7] = {ds->current_index, 0, 0, 0, 0, 0, 0};
    hsize_t count[7] = {1, 1, 1, 1, 1, 14, num_subcarriers};
    
    hid_t memspace = H5Screate_simple(7, count, NULL);
    hid_t filespace = H5Dget_space(ds->dataset_id);
    H5Sselect_hyperslab(filespace, H5S_SELECT_SET, start, NULL, count, NULL);
    
    H5Dread(ds->dataset_id, H5T_NATIVE_COMPLEX, memspace, 
            filespace, H5P_DEFAULT, h_freq);
    
    H5Sclose(memspace);
    H5Sclose(filespace);
    
    ds->current_index = (ds->current_index + 1) % ds->total_samples;
}
```

### 3.3 방법 3: 래퍼 인터페이스

#### 3.3.1 Python 래퍼 서버

```python
# sionna_channel_server.py
import socket
import pickle
import numpy as np
import tensorflow as tf
from sionna.phy.channel.tr38901 import UMi
from sionna.phy.channel import GenerateOFDMChannel, ApplyOFDMChannel
from sionna.phy.ofdm import ResourceGrid

class SionnaChannelServer:
    def __init__(self, port=8888):
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('localhost', port))
        self.socket.listen(1)
        
        # 채널 모델 초기화
        self.setup_channel_model()
    
    def setup_channel_model(self):
        """채널 모델 초기화"""
        rg = ResourceGrid(
            num_ofdm_symbols=14,
            fft_size=1024,
            subcarrier_spacing=15e3
        )
        
        channel_model = UMi(
            carrier_frequency=3.5e9,
            o2i_model='low',
            ut_array=Antenna(...),
            bs_array=PanelArray(...),
            direction='downlink'
        )
        
        self.ofdm_channel_gen = GenerateOFDMChannel(
            channel_model, rg
        )
        self.apply_channel = ApplyOFDMChannel()
    
    def handle_request(self, conn):
        """요청 처리"""
        data = conn.recv(4096)
        request = pickle.loads(data)
        
        if request['type'] == 'generate_channel':
            batch_size = request['batch_size']
            h_freq = self.ofdm_channel_gen(batch_size)
            response = {'h_freq': h_freq.numpy()}
        
        elif request['type'] == 'apply_channel':
            x = tf.convert_to_tensor(request['x'], dtype=tf.complex64)
            h_freq = tf.convert_to_tensor(request['h_freq'], dtype=tf.complex64)
            no = request.get('noise_power', 0.0)
            y = self.apply_channel(x, h_freq, no)
            response = {'y': y.numpy()}
        
        conn.send(pickle.dumps(response))
        conn.close()
    
    def run(self):
        """서버 실행"""
        print(f"Sionna Channel Server listening on port {self.port}")
        while True:
            conn, addr = self.socket.accept()
            self.handle_request(conn)

if __name__ == "__main__":
    server = SionnaChannelServer()
    server.run()
```

#### 3.3.2 C 클라이언트

```c
// sionna_channel_client.c
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <string.h>
#include <stdio.h>

int request_channel(int socket_fd, int batch_size, 
                    complex_t* h_freq, int h_freq_size) {
    // 요청 생성 및 전송
    // 응답 수신 및 파싱
    // h_freq에 데이터 복사
    return 0;
}
```

---

## 4. 권장 방법

### 4.1 시나리오별 권장 방법

#### 시나리오 1: 오프라인 시뮬레이션
**권장**: 방법 2 (하이브리드 방식)
- 채널을 사전 생성하여 저장
- OAI에서 파일로 로드
- 구현이 간단하고 안정적

#### 시나리오 2: 실시간 시뮬레이션 (단일 시스템)
**권장**: 방법 3 (래퍼 인터페이스)
- Python-C 바인딩 사용
- 런타임에 채널 생성
- OAI 인터페이스 유지

#### 시나리오 3: 장기 통합 프로젝트
**권장**: 방법 1 (직접 통합)
- 완전한 통합
- 최적의 성능
- 유지보수 가능

#### 시나리오 4: 분산/클라우드 시뮬레이션
**권장**: 방법 4 (외부 서비스)
- 마이크로서비스 아키텍처
- 독립적인 확장
- 다양한 플랫폼 지원

### 4.2 일반적인 권장사항

**단기적 접근 (빠른 프로토타이핑)**:
- 방법 2 (하이브리드 방식) 사용
- 채널 데이터를 HDF5나 NumPy 형식으로 저장
- OAI에서 간단한 로더 구현

**중기적 접근 (안정적인 통합)**:
- 방법 3 (래퍼 인터페이스) 사용
- Cython 또는 ctypes로 Python-C 바인딩
- 점진적인 통합 및 테스트

**장기적 접근 (완전한 통합)**:
- 방법 1 (직접 통합) 고려
- OAI 코드베이스에 Sionna 채널 모듈 통합
- 성능 최적화 및 테스트

---

## 5. 구현 예시

### 5.1 간단한 통합 예시 (방법 2 기반)

```python
# oai_sionna_channel_bridge.py
"""
OAI와 Sionna 채널을 연결하는 브리지 모듈
"""
import numpy as np
import tensorflow as tf
from sionna.phy.channel.tr38901 import UMi, Antenna, PanelArray
from sionna.phy.channel import GenerateOFDMChannel
from sionna.phy.ofdm import ResourceGrid
from sionna.sys import gen_hexgrid_topology

class OAISionnaChannelBridge:
    """OAI 채널 인터페이스를 Sionna로 대체"""
    
    def __init__(self, config):
        """
        Parameters
        ----------
        config : dict
            채널 설정
            - carrier_frequency: 반송파 주파수 [Hz]
            - num_subcarriers: 서브캐리어 수
            - subcarrier_spacing: 서브캐리어 간격 [Hz]
            - num_ofdm_symbols: OFDM 심볼 수
            - scenario: 시나리오 타입 ('umi', 'uma', 'rma')
        """
        self.config = config
        self._setup_channel_model()
    
    def _setup_channel_model(self):
        """채널 모델 초기화"""
        # 리소스 그리드
        self.rg = ResourceGrid(
            num_ofdm_symbols=self.config['num_ofdm_symbols'],
            fft_size=self.config['num_subcarriers'],
            subcarrier_spacing=self.config['subcarrier_spacing']
        )
        
        # 안테나 배열
        ut_array = Antenna(
            polarization="single",
            polarization_type="V",
            antenna_pattern="omni",
            carrier_frequency=self.config['carrier_frequency']
        )
        
        bs_array = PanelArray(
            num_rows_per_panel=4,
            num_cols_per_panel=4,
            polarization='dual',
            polarization_type='VH',
            antenna_pattern='38.901',
            carrier_frequency=self.config['carrier_frequency']
        )
        
        # 채널 모델
        scenario_map = {
            'umi': UMi,
            'uma': UMa,
            'rma': RMa
        }
        
        ChannelModel = scenario_map.get(
            self.config.get('scenario', 'umi'),
            UMi
        )
        
        self.channel_model = ChannelModel(
            carrier_frequency=self.config['carrier_frequency'],
            o2i_model='low',
            ut_array=ut_array,
            bs_array=bs_array,
            direction='downlink',
            enable_pathloss=True,
            enable_shadow_fading=True
        )
        
        # 토폴로지 설정
        topology = gen_hexgrid_topology(
            batch_size=1,
            num_rings=1,
            num_ut_per_sector=3,
            scenario=self.config.get('scenario', 'umi'),
            min_bs_ut_dist=10.0,
            max_bs_ut_dist=200.0,
            los=True,
            return_grid=True
        )
        
        self.channel_model.set_topology(*topology)
        
        # OFDM 채널 생성기
        self.ofdm_channel_gen = GenerateOFDMChannel(
            channel_model=self.channel_model,
            resource_grid=self.rg,
            normalize_channel=False
        )
    
    def generate_channel(self, batch_size=1):
        """
        채널 주파수 응답 생성
        
        Parameters
        ----------
        batch_size : int
            배치 크기
        
        Returns
        -------
        h_freq : np.ndarray
            채널 주파수 응답
            Shape: [batch_size, num_rx, num_rx_ant, num_tx, num_tx_ant, 
                    num_ofdm_symbols, num_subcarriers]
        """
        h_freq = self.ofdm_channel_gen(batch_size)
        return h_freq.numpy()
    
    def save_channel_to_file(self, filename, num_samples, batch_size=32):
        """
        채널 데이터를 파일로 저장
        
        Parameters
        ----------
        filename : str
            출력 파일명
        num_samples : int
            생성할 샘플 수
        batch_size : int
            배치 크기
        """
        import h5py
        
        with h5py.File(filename, 'w') as f:
            # 첫 번째 배치로 차원 확인
            h_sample = self.generate_channel(batch_size)
            shape = h_sample.shape
            
            # 데이터셋 생성
            h_freq_dset = f.create_dataset(
                'h_freq',
                shape=(num_samples,) + shape[1:],
                dtype=np.complex64
            )
            
            # 채널 생성 및 저장
            for i in range(0, num_samples, batch_size):
                current_batch = min(batch_size, num_samples - i)
                h_freq = self.generate_channel(current_batch)
                h_freq_dset[i:i+current_batch] = h_freq
        
        print(f"Saved {num_samples} channel samples to {filename}")

# 사용 예시
if __name__ == "__main__":
    config = {
        'carrier_frequency': 3.5e9,
        'num_subcarriers': 1024,
        'subcarrier_spacing': 15e3,
        'num_ofdm_symbols': 14,
        'scenario': 'umi'
    }
    
    bridge = OAISionnaChannelBridge(config)
    
    # 채널 생성
    h_freq = bridge.generate_channel(batch_size=1)
    print(f"Channel shape: {h_freq.shape}")
    
    # 파일로 저장
    bridge.save_channel_to_file(
        filename="oai_channel_dataset.h5",
        num_samples=1000,
        batch_size=32
    )
```

### 5.2 C 인터페이스 예시

```c
// oai_sionna_channel.h
#ifndef OAI_SIONNA_CHANNEL_H
#define OAI_SIONNA_CHANNEL_H

#include <complex.h>
#include <stdint.h>

// 채널 초기화
int oai_sionna_channel_init(const char* config_file);

// 채널 주파수 응답 생성
int oai_sionna_generate_channel(
    uint32_t batch_size,
    complex_t* h_freq,  // 출력: [batch, rx, rx_ant, tx, tx_ant, symbols, subcarriers]
    uint32_t* dims     // 출력: 차원 정보
);

// 채널 데이터 로드 (하이브리드 방식)
int oai_sionna_load_channel_dataset(const char* filename);

// 다음 채널 샘플 가져오기
int oai_sionna_get_next_channel(
    complex_t* h_freq,
    uint32_t* dims
);

// 리소스 해제
void oai_sionna_channel_cleanup(void);

#endif // OAI_SIONNA_CHANNEL_H
```

---

## 6. 고려사항

### 6.1 성능 고려사항

1. **GPU 활용**
   - Sionna는 TensorFlow 기반으로 GPU 가속 지원
   - 대량의 채널 생성 시 GPU 사용 권장
   - CPU-GPU 메모리 전송 최소화

2. **배치 처리**
   - Sionna는 배치 처리에 최적화
   - 여러 채널을 한 번에 생성하는 것이 효율적
   - OAI에서 배치 단위로 처리하도록 설계

3. **메모리 관리**
   - 채널 데이터는 메모리 집약적
   - 필요시 스트리밍 방식 사용
   - 메모리 풀링 고려

### 6.2 호환성 고려사항

1. **데이터 형식**
   - Sionna: TensorFlow 텐서 (complex64/complex128)
   - OAI: C 배열 (complex_t)
   - 변환 오버헤드 최소화 필요

2. **인덱싱**
   - Sionna: [batch, rx, rx_ant, tx, tx_ant, symbols, subcarriers]
   - OAI: 일반적으로 [symbols, subcarriers, antennas]
   - 차원 변환 함수 필요

3. **정밀도**
   - Sionna: float32 (single) 또는 float64 (double)
   - OAI: 일반적으로 float 또는 double
   - 정밀도 일치 확인

### 6.3 구현 고려사항

1. **에러 처리**
   - Python-C 바인딩에서 예외 처리
   - 메모리 할당 실패 처리
   - 잘못된 입력 검증

2. **스레드 안전성**
   - 멀티스레드 환경에서의 안전성
   - GIL (Global Interpreter Lock) 고려
   - 동시성 제어

3. **버전 관리**
   - Sionna 버전 업데이트 대응
   - API 변경사항 추적
   - 호환성 테스트

### 6.4 테스트 전략

1. **단위 테스트**
   - 각 채널 모델별 테스트
   - 인터페이스 함수 테스트
   - 에러 케이스 테스트

2. **통합 테스트**
   - OAI와 Sionna 통합 테스트
   - 엔드투엔드 시뮬레이션
   - 성능 벤치마크

3. **검증**
   - 3GPP 표준 준수 검증
   - 기존 OAI 채널과 비교
   - 수치적 정확도 검증

---

## 7. 마이그레이션 로드맵

### Phase 1: 준비 단계 (1-2주)
- [ ] Sionna 환경 설정
- [ ] OAI 코드베이스 분석
- [ ] 채널 인터페이스 정의
- [ ] 프로토타입 구현

### Phase 2: 구현 단계 (2-4주)
- [ ] 선택한 방법으로 구현
- [ ] 단위 테스트 작성
- [ ] 기본 기능 구현

### Phase 3: 통합 단계 (2-3주)
- [ ] OAI와 통합
- [ ] 통합 테스트
- [ ] 성능 최적화

### Phase 4: 검증 단계 (1-2주)
- [ ] 기능 검증
- [ ] 성능 벤치마크
- [ ] 문서화

---

## 8. 참고 자료

### 8.1 Sionna 관련
- Sionna 공식 문서: https://nvlabs.github.io/sionna/
- 채널 모델 API: `doc/source/phy/api/channel.wireless.rst`
- 튜토리얼: `tutorials/phy/Realistic_Multiuser_MIMO_Simulations.ipynb`

### 8.2 OAI 관련
- OpenAirInterface 공식 사이트: https://openairinterface.org/
- OAI 채널 구현 문서

### 8.3 통합 관련
- Python-C 바인딩: Cython, ctypes, cffi
- HDF5 문서: https://www.hdfgroup.org/
- TensorFlow C API: https://www.tensorflow.org/install/lang_c

---

## 9. 요약

OAI의 채널 기능을 Sionna로 대체하는 가장 적합한 방법은 **사용 시나리오에 따라 다릅니다**:

1. **오프라인 시뮬레이션**: 하이브리드 방식 (방법 2) - 가장 간단하고 안정적
2. **실시간 시뮬레이션**: 래퍼 인터페이스 (방법 3) - 균형잡힌 접근
3. **장기 프로젝트**: 직접 통합 (방법 1) - 최적의 성능
4. **분산 시스템**: 외부 서비스 (방법 4) - 확장성 우수

**일반적인 권장사항**:
- 단기: 하이브리드 방식으로 빠른 프로토타이핑
- 중기: 래퍼 인터페이스로 안정적인 통합
- 장기: 직접 통합으로 완전한 최적화

각 방법은 장단점이 있으므로, 프로젝트의 요구사항, 시간 제약, 리소스를 고려하여 선택하는 것이 중요합니다.
