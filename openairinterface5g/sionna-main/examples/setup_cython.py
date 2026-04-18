"""
Cython 확장 모듈을 빌드하기 위한 setup.py
"""

from setuptools import setup, Extension
from Cython.Build import cythonize
import numpy

# Cython 확장 모듈 정의
extensions = [
    Extension(
        "cython_example",
        ["cython_example.pyx"],
        include_dirs=[numpy.get_include()],
        extra_compile_args=['-O3'],  # 최적화 옵션
    )
]

setup(
    name='cython_example',
    ext_modules=cythonize(extensions, compiler_directives={
        'language_level': "3",  # Python 3 사용
        'boundscheck': False,   # 경계 검사 비활성화
        'wraparound': False,    # 음수 인덱스 비활성화
    }),
    zip_safe=False,
)
