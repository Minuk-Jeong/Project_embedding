"""
Cython 예제 테스트 스크립트
"""

import numpy as np

# Cython 모듈 import (컴파일 후)
try:
    import cython_example
    print("Cython 모듈 로드 성공!\n")
except ImportError:
    print("Cython 모듈을 먼저 컴파일해야 합니다:")
    print("  python setup_cython.py build_ext --inplace\n")
    exit(1)

# 테스트 데이터
arr = np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype=np.float64)
a = np.array([1.0, 2.0, 3.0], dtype=np.float64)
b = np.array([4.0, 5.0, 6.0], dtype=np.float64)
vec = np.array([3.0, 4.0], dtype=np.float64)

print("=== Cython 예제 테스트 ===\n")

# compute_sum_cython 테스트
result = cython_example.compute_sum_cython(arr)
print(f"합계: {result}")

# compute_dot_product_cython 테스트
result = cython_example.compute_dot_product_cython(a, b)
print(f"내적: {result}")

# vector_norm_cython 테스트
result = cython_example.vector_norm_cython(vec)
print(f"벡터 노름: {result} (예상: 5.0)")

# compute_power_cython 테스트
result = cython_example.compute_power_cython(arr, 2.0)
print(f"제곱 결과: {result}")

print("\n모든 테스트 완료!")
