# Python to C 변환 예제

이 디렉토리에는 Python 코드를 C로 변환하는 다양한 방법의 예제가 포함되어 있습니다.

## 파일 구조

- `python_to_c_example.py`: 원본 Python 코드
- `python_to_c_example.c`: 수동으로 변환한 C 코드
- `Makefile`: C 코드 컴파일을 위한 Makefile
- `cython_example.pyx`: Cython을 사용한 변환 예제
- `setup_cython.py`: Cython 모듈 빌드 스크립트
- `test_cython.py`: Cython 예제 테스트 스크립트

## 사용 방법

### 1. Python 버전 실행

```bash
python3 python_to_c_example.py
```

### 2. C 버전 컴파일 및 실행

```bash
# 컴파일
make

# 실행
make run

# 또는 직접 실행
./python_to_c_example
```

### 3. Cython 버전 사용

```bash
# Cython 설치 (필요한 경우)
pip install cython numpy

# Cython 모듈 컴파일
python setup_cython.py build_ext --inplace

# 테스트 실행
python test_cython.py
```

## 성능 비교

일반적으로 다음과 같은 성능 차이를 기대할 수 있습니다:

- **Python**: 가장 느림, 하지만 개발이 쉽고 유연함
- **Cython**: Python보다 10-100배 빠름 (타입 힌트 사용 시)
- **C**: 가장 빠름, 하지만 개발 시간이 오래 걸림

## 주의사항

1. **메모리 관리**: C 코드에서는 메모리 할당/해제를 수동으로 관리해야 합니다.
2. **타입 안정성**: C는 타입 체크가 엄격하므로 주의가 필요합니다.
3. **플랫폼 호환성**: C 코드는 플랫폼별로 컴파일이 필요할 수 있습니다.

## 추가 학습 자료

- [Cython 공식 문서](https://cython.readthedocs.io/)
- [Python C API](https://docs.python.org/3/c-api/)
- [GCC 컴파일러 가이드](https://gcc.gnu.org/onlinedocs/)
