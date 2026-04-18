"""
Python 코드를 C로 변환하는 예제

이 파일은 Python 버전의 간단한 수치 계산 함수들을 포함합니다.
각 함수에 대해 C 버전도 제공됩니다.
"""

import numpy as np


def compute_sum(arr):
    """배열의 모든 원소를 합산"""
    total = 0.0
    for i in range(len(arr)):
        total += arr[i]
    return total


def compute_dot_product(a, b):
    """두 벡터의 내적 계산"""
    if len(a) != len(b):
        raise ValueError("벡터 길이가 일치하지 않습니다")
    
    result = 0.0
    for i in range(len(a)):
        result += a[i] * b[i]
    return result


def matrix_multiply(A, B):
    """행렬 곱셈 (간단한 버전)"""
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])
    
    if cols_A != rows_B:
        raise ValueError("행렬 차원이 맞지 않습니다")
    
    # 결과 행렬 초기화
    C = [[0.0 for _ in range(cols_B)] for _ in range(rows_A)]
    
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    
    return C


def fibonacci(n):
    """피보나치 수열 계산 (재귀 버전)"""
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)


def fibonacci_iterative(n):
    """피보나치 수열 계산 (반복 버전 - 더 빠름)"""
    if n <= 1:
        return n
    
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# 테스트 코드
if __name__ == "__main__":
    # compute_sum 테스트
    arr = [1.0, 2.0, 3.0, 4.0, 5.0]
    print(f"합계: {compute_sum(arr)}")
    
    # compute_dot_product 테스트
    a = [1.0, 2.0, 3.0]
    b = [4.0, 5.0, 6.0]
    print(f"내적: {compute_dot_product(a, b)}")
    
    # matrix_multiply 테스트
    A = [[1.0, 2.0], [3.0, 4.0]]
    B = [[5.0, 6.0], [7.0, 8.0]]
    C = matrix_multiply(A, B)
    print(f"행렬 곱셈 결과: {C}")
    
    # fibonacci 테스트
    n = 10
    print(f"피보나치({n}) = {fibonacci_iterative(n)}")
