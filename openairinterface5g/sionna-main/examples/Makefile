# Python to C 변환 예제를 컴파일하기 위한 Makefile

CC = gcc
CFLAGS = -Wall -Wextra -O2 -std=c99
TARGET = python_to_c_example
SOURCE = python_to_c_example.c

# 기본 타겟
all: $(TARGET)

# 실행 파일 생성
$(TARGET): $(SOURCE)
	$(CC) $(CFLAGS) -o $(TARGET) $(SOURCE)

# 실행
run: $(TARGET)
	./$(TARGET)

# 정리
clean:
	rm -f $(TARGET)

# Python 버전 실행
run-python:
	python3 python_to_c_example.py

.PHONY: all run clean run-python
