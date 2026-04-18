# cython_example.pyx
# Cython을 사용한 Python to C 변환 예제

# C 표준 라이브러리 함수 사용
cimport cython
from libc.math cimport sqrt, pow

# 타입 힌트를 사용하여 성능 향상
@cython.boundscheck(False)  # 경계 검사 비활성화 (성능 향상)
@cython.wraparound(False)   # 음수 인덱스 비활성화
def compute_sum_cython(double[:] arr):
    """배열의 모든 원소를 합산 (Cython 버전)"""
    cdef double total = 0.0
    cdef int i
    cdef int n = arr.shape[0]
    
    for i in range(n):
        total += arr[i]
    
    return total


@cython.boundscheck(False)
@cython.wraparound(False)
def compute_dot_product_cython(double[:] a, double[:] b):
    """두 벡터의 내적 계산 (Cython 버전)"""
    cdef double result = 0.0
    cdef int i
    cdef int n = a.shape[0]
    
    if n != b.shape[0]:
        raise ValueError("벡터 길이가 일치하지 않습니다")
    
    for i in range(n):
        result += a[i] * b[i]
    
    return result


@cython.boundscheck(False)
@cython.wraparound(False)
def vector_norm_cython(double[:] vec):
    """벡터의 노름 계산 (Cython 버전)"""
    cdef double result = 0.0
    cdef int i
    cdef int n = vec.shape[0]
    
    for i in range(n):
        result += vec[i] * vec[i]
    
    return sqrt(result)


@cython.boundscheck(False)
@cython.wraparound(False)
def compute_power_cython(double[:] arr, double power):
    """배열의 각 원소를 거듭제곱 (Cython 버전)"""
    cdef int i
    cdef int n = arr.shape[0]
    cdef double[:] result = arr.copy()  # 메모리 뷰 복사
    
    for i in range(n):
        result[i] = pow(arr[i], power)
    
    return result
