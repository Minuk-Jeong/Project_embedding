# Python 코드를 C로 변환하는 방법 가이드

## 개요
Python 코드를 C로 변환하는 여러 방법과 각 방법의 장단점을 설명합니다.

## 방법 1: Cython 사용 (권장)

### 장점
- Python 코드를 거의 그대로 사용 가능
- 타입 힌트만 추가하면 성능 향상
- Python과 C의 하이브리드 접근 가능

### 설치
```bash
pip install cython
```

### 예제: Python 함수를 Cython으로 변환

**원본 Python 코드 (example.py)**
```python
def compute_sum(arr):
    total = 0
    for i in range(len(arr)):
        total += arr[i]
    return total
```

**Cython 버전 (example.pyx)**
```cython
# example.pyx
cimport numpy as np
import numpy as np

def compute_sum(double[:] arr):
    cdef double total = 0.0
    cdef int i
    for i in range(arr.shape[0]):
        total += arr[i]
    return total
```

**setup.py**
```python
from setuptools import setup
from Cython.Build import cythonize
import numpy

setup(
    ext_modules = cythonize("example.pyx"),
    include_dirs=[numpy.get_include()]
)
```

**컴파일**
```bash
python setup.py build_ext --inplace
```

## 방법 2: Nuitka 사용

### 장점
- 전체 애플리케이션을 독립 실행 파일로 변환
- Python 런타임 없이 실행 가능

### 설치
```bash
pip install nuitka
```

### 사용법
```bash
# 단일 파일 컴파일
python -m nuitka example.py

# 최적화 옵션 포함
python -m nuitka --standalone --onefile example.py
```

## 방법 3: 수동 변환

### Python과 C의 주요 차이점

| Python | C |
|--------|---|
| 동적 타입 | 정적 타입 선언 필요 |
| 자동 메모리 관리 | 수동 메모리 관리 (malloc/free) |
| 리스트, 딕셔너리 등 내장 자료구조 | 배열, 구조체 사용 |
| 예외 처리 | 에러 코드 반환 |

### 변환 예제

**Python 코드**
```python
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

def compute_fibonacci_list(n):
    result = []
    for i in range(n):
        result.append(fibonacci(i))
    return result
```

**C 코드**
```c
#include <stdio.h>
#include <stdlib.h>

int fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n-1) + fibonacci(n-2);
}

int* compute_fibonacci_list(int n) {
    int* result = (int*)malloc(n * sizeof(int));
    if (result == NULL) {
        return NULL;  // 메모리 할당 실패
    }
    
    for (int i = 0; i < n; i++) {
        result[i] = fibonacci(i);
    }
    
    return result;
}

void free_fibonacci_list(int* arr) {
    free(arr);
}

int main() {
    int n = 10;
    int* fib_list = compute_fibonacci_list(n);
    
    if (fib_list != NULL) {
        for (int i = 0; i < n; i++) {
            printf("%d ", fib_list[i]);
        }
        printf("\n");
        free_fibonacci_list(fib_list);
    }
    
    return 0;
}
```

## 방법 4: 하이브리드 접근 (Python + C 확장)

### ctypes 사용

**C 코드 (libexample.c)**
```c
#include <stdio.h>

double compute_sum(double* arr, int n) {
    double total = 0.0;
    for (int i = 0; i < n; i++) {
        total += arr[i];
    }
    return total;
}
```

**컴파일**
```bash
gcc -shared -o libexample.so -fPIC libexample.c
```

**Python에서 사용**
```python
import ctypes
import numpy as np

# 라이브러리 로드
lib = ctypes.CDLL('./libexample.so')

# 함수 시그니처 정의
lib.compute_sum.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_int]
lib.compute_sum.restype = ctypes.c_double

# 사용
arr = np.array([1.0, 2.0, 3.0, 4.0], dtype=np.float64)
result = lib.compute_sum(arr.ctypes.data_as(ctypes.POINTER(ctypes.c_double)), len(arr))
print(result)  # 10.0
```

## 방법 5: CFFI (C Foreign Function Interface) 사용

### 설치
```bash
pip install cffi
```

### 예제

**example_build.py**
```python
from cffi import FFI

ffi = FFI()
ffi.cdef("""
    double compute_sum(double* arr, int n);
""")

# C 소스 코드
ffi.set_source("_example",
    """
    double compute_sum(double* arr, int n) {
        double total = 0.0;
        for (int i = 0; i < n; i++) {
            total += arr[i];
        }
        return total;
    }
    """)

if __name__ == "__main__":
    ffi.compile()
```

**사용**
```python
from _example import ffi, lib
import numpy as np

arr = np.array([1.0, 2.0, 3.0, 4.0], dtype=np.float64)
result = lib.compute_sum(ffi.cast("double*", arr.ctypes.data), len(arr))
print(result)
```

## Sionna 프로젝트에 적용하기

### 고려사항
1. **TensorFlow 의존성**: Sionna는 TensorFlow 기반이므로, TensorFlow 연산을 C로 변환하는 것은 매우 복잡합니다.
2. **권장 접근**: 핵심 수치 계산 알고리즘만 C로 변환하고, TensorFlow 연산은 그대로 유지
3. **성능 최적화**: GPU 연산이 필요한 부분은 CUDA를 사용하는 것이 더 효과적일 수 있습니다.

### 예제: 간단한 수치 함수 변환

**Python (numerics.py에서 추출한 예제)**
```python
def simple_compute(x, y):
    return x * y + x**2
```

**C 버전**
```c
double simple_compute(double x, double y) {
    return x * y + x * x;
}
```

## 선택 가이드

| 상황 | 권장 방법 |
|------|----------|
| 빠른 프로토타이핑 | Cython |
| 독립 실행 파일 필요 | Nuitka |
| 최대 성능 필요 | 수동 C 변환 |
| 기존 C 라이브러리 활용 | ctypes 또는 CFFI |
| TensorFlow 연산 포함 | 하이브리드 (핵심 부분만 C) |

## 참고 자료

- [Cython 공식 문서](https://cython.readthedocs.io/)
- [Nuitka 공식 문서](https://nuitka.net/)
- [Python C API](https://docs.python.org/3/c-api/)
- [CFFI 문서](https://cffi.readthedocs.io/)

## 주의사항

1. **메모리 관리**: C에서는 malloc/free를 수동으로 관리해야 합니다.
2. **타입 안정성**: C는 타입 체크가 엄격하므로 주의가 필요합니다.
3. **디버깅**: C 코드 디버깅은 Python보다 어려울 수 있습니다.
4. **호환성**: 플랫폼별 컴파일이 필요할 수 있습니다.
