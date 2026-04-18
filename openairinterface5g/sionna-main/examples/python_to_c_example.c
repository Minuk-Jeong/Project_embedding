/*
 * Python 코드를 C로 변환한 예제
 * 
 * 이 파일은 python_to_c_example.py의 C 버전입니다.
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* 배열의 모든 원소를 합산 */
double compute_sum(double* arr, int n) {
    double total = 0.0;
    for (int i = 0; i < n; i++) {
        total += arr[i];
    }
    return total;
}

/* 두 벡터의 내적 계산 */
double compute_dot_product(double* a, double* b, int n) {
    double result = 0.0;
    for (int i = 0; i < n; i++) {
        result += a[i] * b[i];
    }
    return result;
}

/* 행렬 곱셈 (간단한 버전) */
void matrix_multiply(double** A, double** B, double** C, 
                     int rows_A, int cols_A, int rows_B, int cols_B) {
    if (cols_A != rows_B) {
        fprintf(stderr, "행렬 차원이 맞지 않습니다\n");
        return;
    }
    
    // 결과 행렬 초기화
    for (int i = 0; i < rows_A; i++) {
        for (int j = 0; j < cols_B; j++) {
            C[i][j] = 0.0;
        }
    }
    
    for (int i = 0; i < rows_A; i++) {
        for (int j = 0; j < cols_B; j++) {
            for (int k = 0; k < cols_A; k++) {
                C[i][j] += A[i][k] * B[k][j];
            }
        }
    }
}

/* 피보나치 수열 계산 (재귀 버전) */
int fibonacci(int n) {
    if (n <= 1) {
        return n;
    }
    return fibonacci(n-1) + fibonacci(n-2);
}

/* 피보나치 수열 계산 (반복 버전 - 더 빠름) */
int fibonacci_iterative(int n) {
    if (n <= 1) {
        return n;
    }
    
    int a = 0, b = 1;
    for (int i = 2; i <= n; i++) {
        int temp = a + b;
        a = b;
        b = temp;
    }
    return b;
}

/* 동적 2D 배열 할당 */
double** allocate_matrix(int rows, int cols) {
    double** matrix = (double**)malloc(rows * sizeof(double*));
    if (matrix == NULL) {
        return NULL;
    }
    
    for (int i = 0; i < rows; i++) {
        matrix[i] = (double*)malloc(cols * sizeof(double));
        if (matrix[i] == NULL) {
            // 이전에 할당한 메모리 해제
            for (int j = 0; j < i; j++) {
                free(matrix[j]);
            }
            free(matrix);
            return NULL;
        }
    }
    return matrix;
}

/* 동적 2D 배열 해제 */
void free_matrix(double** matrix, int rows) {
    if (matrix == NULL) {
        return;
    }
    
    for (int i = 0; i < rows; i++) {
        free(matrix[i]);
    }
    free(matrix);
}

/* 테스트 코드 */
int main() {
    printf("=== Python to C 변환 예제 ===\n\n");
    
    // compute_sum 테스트
    double arr[] = {1.0, 2.0, 3.0, 4.0, 5.0};
    int n = sizeof(arr) / sizeof(arr[0]);
    printf("합계: %.2f\n", compute_sum(arr, n));
    
    // compute_dot_product 테스트
    double a[] = {1.0, 2.0, 3.0};
    double b[] = {4.0, 5.0, 6.0};
    int vec_len = sizeof(a) / sizeof(a[0]);
    printf("내적: %.2f\n", compute_dot_product(a, b, vec_len));
    
    // matrix_multiply 테스트
    int rows_A = 2, cols_A = 2;
    int rows_B = 2, cols_B = 2;
    
    double** A = allocate_matrix(rows_A, cols_A);
    double** B = allocate_matrix(rows_B, cols_B);
    double** C = allocate_matrix(rows_A, cols_B);
    
    if (A == NULL || B == NULL || C == NULL) {
        fprintf(stderr, "메모리 할당 실패\n");
        return 1;
    }
    
    // 행렬 A 초기화
    A[0][0] = 1.0; A[0][1] = 2.0;
    A[1][0] = 3.0; A[1][1] = 4.0;
    
    // 행렬 B 초기화
    B[0][0] = 5.0; B[0][1] = 6.0;
    B[1][0] = 7.0; B[1][1] = 8.0;
    
    matrix_multiply(A, B, C, rows_A, cols_A, rows_B, cols_B);
    
    printf("행렬 곱셈 결과:\n");
    for (int i = 0; i < rows_A; i++) {
        for (int j = 0; j < cols_B; j++) {
            printf("%.2f ", C[i][j]);
        }
        printf("\n");
    }
    
    // fibonacci 테스트
    int fib_n = 10;
    printf("피보나치(%d) = %d\n", fib_n, fibonacci_iterative(fib_n));
    
    // 메모리 해제
    free_matrix(A, rows_A);
    free_matrix(B, rows_B);
    free_matrix(C, rows_A);
    
    return 0;
}
