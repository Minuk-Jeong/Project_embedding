from collections.abc import Sequence
from typing import TypeAlias, Union, overload

import drjit


from builtins import (
    bool as Bool,
    float as Float,
    float as Float16,
    float as Float32,
    float as Float64,
    int as Int,
    int as Int16,
    int as Int32,
    int as Int64,
    int as UInt,
    int as UInt16,
    int as UInt32,
    int as UInt64
)

_Array0bCp: TypeAlias = Union['Array0b', bool]

class Array0b(drjit.ArrayBase[Array0b, _Array0bCp, bool, bool, bool, Array0b, Array0b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array0i8Cp: TypeAlias = Union['Array0i8', int]

class Array0i8(drjit.ArrayBase[Array0i8, _Array0i8Cp, int, int, int, Array0i8, Array0b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array0u8Cp: TypeAlias = Union['Array0u8', int]

class Array0u8(drjit.ArrayBase[Array0u8, _Array0u8Cp, int, int, int, Array0u8, Array0b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array0iCp: TypeAlias = Union['Array0i', int, '_Array0bCp']

class Array0i(drjit.ArrayBase[Array0i, _Array0iCp, int, int, int, Array0i, Array0b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array0uCp: TypeAlias = Union['Array0u', int, '_Array0iCp']

class Array0u(drjit.ArrayBase[Array0u, _Array0uCp, int, int, int, Array0u, Array0b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array0i64Cp: TypeAlias = Union['Array0i64', int, '_Array0uCp']

class Array0i64(drjit.ArrayBase[Array0i64, _Array0i64Cp, int, int, int, Array0i64, Array0b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array0u64Cp: TypeAlias = Union['Array0u64', int, '_Array0i64Cp']

class Array0u64(drjit.ArrayBase[Array0u64, _Array0u64Cp, int, int, int, Array0u64, Array0b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array0f16Cp: TypeAlias = Union['Array0f16', float, '_Array0u64Cp']

class Array0f16(drjit.ArrayBase[Array0f16, _Array0f16Cp, float, float, float, Array0f16, Array0b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array0fCp: TypeAlias = Union['Array0f', float, '_Array0f16Cp']

class Array0f(drjit.ArrayBase[Array0f, _Array0fCp, float, float, float, Array0f, Array0b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array0f64Cp: TypeAlias = Union['Array0f64', float, '_Array0fCp']

class Array0f64(drjit.ArrayBase[Array0f64, _Array0f64Cp, float, float, float, Array0f64, Array0b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array1bCp: TypeAlias = Union['Array1b', bool]

class Array1b(drjit.ArrayBase[Array1b, _Array1bCp, bool, bool, bool, Array1b, Array1b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array1i8Cp: TypeAlias = Union['Array1i8', int]

class Array1i8(drjit.ArrayBase[Array1i8, _Array1i8Cp, int, int, int, Array1i8, Array1b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array1u8Cp: TypeAlias = Union['Array1u8', int]

class Array1u8(drjit.ArrayBase[Array1u8, _Array1u8Cp, int, int, int, Array1u8, Array1b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array1iCp: TypeAlias = Union['Array1i', int, '_Array1bCp']

class Array1i(drjit.ArrayBase[Array1i, _Array1iCp, int, int, int, Array1i, Array1b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array1uCp: TypeAlias = Union['Array1u', int, '_Array1iCp']

class Array1u(drjit.ArrayBase[Array1u, _Array1uCp, int, int, int, Array1u, Array1b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array1i64Cp: TypeAlias = Union['Array1i64', int, '_Array1uCp']

class Array1i64(drjit.ArrayBase[Array1i64, _Array1i64Cp, int, int, int, Array1i64, Array1b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array1u64Cp: TypeAlias = Union['Array1u64', int, '_Array1i64Cp']

class Array1u64(drjit.ArrayBase[Array1u64, _Array1u64Cp, int, int, int, Array1u64, Array1b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array1f16Cp: TypeAlias = Union['Array1f16', float, '_Array1u64Cp']

class Array1f16(drjit.ArrayBase[Array1f16, _Array1f16Cp, float, float, float, Array1f16, Array1b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array1fCp: TypeAlias = Union['Array1f', float, '_Array1f16Cp']

class Array1f(drjit.ArrayBase[Array1f, _Array1fCp, float, float, float, Array1f, Array1b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array1f64Cp: TypeAlias = Union['Array1f64', float, '_Array1fCp']

class Array1f64(drjit.ArrayBase[Array1f64, _Array1f64Cp, float, float, float, Array1f64, Array1b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array2bCp: TypeAlias = Union['Array2b', bool]

class Array2b(drjit.ArrayBase[Array2b, _Array2bCp, bool, bool, bool, Array2b, Array2b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array2i8Cp: TypeAlias = Union['Array2i8', int]

class Array2i8(drjit.ArrayBase[Array2i8, _Array2i8Cp, int, int, int, Array2i8, Array2b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array2u8Cp: TypeAlias = Union['Array2u8', int]

class Array2u8(drjit.ArrayBase[Array2u8, _Array2u8Cp, int, int, int, Array2u8, Array2b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array2iCp: TypeAlias = Union['Array2i', int, '_Array2bCp']

class Array2i(drjit.ArrayBase[Array2i, _Array2iCp, int, int, int, Array2i, Array2b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array2uCp: TypeAlias = Union['Array2u', int, '_Array2iCp']

class Array2u(drjit.ArrayBase[Array2u, _Array2uCp, int, int, int, Array2u, Array2b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array2i64Cp: TypeAlias = Union['Array2i64', int, '_Array2uCp']

class Array2i64(drjit.ArrayBase[Array2i64, _Array2i64Cp, int, int, int, Array2i64, Array2b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array2u64Cp: TypeAlias = Union['Array2u64', int, '_Array2i64Cp']

class Array2u64(drjit.ArrayBase[Array2u64, _Array2u64Cp, int, int, int, Array2u64, Array2b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array2f16Cp: TypeAlias = Union['Array2f16', float, '_Array2u64Cp']

class Array2f16(drjit.ArrayBase[Array2f16, _Array2f16Cp, float, float, float, Array2f16, Array2b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array2fCp: TypeAlias = Union['Array2f', float, '_Array2f16Cp']

class Array2f(drjit.ArrayBase[Array2f, _Array2fCp, float, float, float, Array2f, Array2b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array2f64Cp: TypeAlias = Union['Array2f64', float, '_Array2fCp']

class Array2f64(drjit.ArrayBase[Array2f64, _Array2f64Cp, float, float, float, Array2f64, Array2b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array3bCp: TypeAlias = Union['Array3b', bool]

class Array3b(drjit.ArrayBase[Array3b, _Array3bCp, bool, bool, bool, Array3b, Array3b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array3i8Cp: TypeAlias = Union['Array3i8', int]

class Array3i8(drjit.ArrayBase[Array3i8, _Array3i8Cp, int, int, int, Array3i8, Array3b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array3u8Cp: TypeAlias = Union['Array3u8', int]

class Array3u8(drjit.ArrayBase[Array3u8, _Array3u8Cp, int, int, int, Array3u8, Array3b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array3iCp: TypeAlias = Union['Array3i', int, '_Array3bCp']

class Array3i(drjit.ArrayBase[Array3i, _Array3iCp, int, int, int, Array3i, Array3b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array3uCp: TypeAlias = Union['Array3u', int, '_Array3iCp']

class Array3u(drjit.ArrayBase[Array3u, _Array3uCp, int, int, int, Array3u, Array3b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array3i64Cp: TypeAlias = Union['Array3i64', int, '_Array3uCp']

class Array3i64(drjit.ArrayBase[Array3i64, _Array3i64Cp, int, int, int, Array3i64, Array3b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array3u64Cp: TypeAlias = Union['Array3u64', int, '_Array3i64Cp']

class Array3u64(drjit.ArrayBase[Array3u64, _Array3u64Cp, int, int, int, Array3u64, Array3b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array3f16Cp: TypeAlias = Union['Array3f16', float, '_Array3u64Cp']

class Array3f16(drjit.ArrayBase[Array3f16, _Array3f16Cp, float, float, float, Array3f16, Array3b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array3fCp: TypeAlias = Union['Array3f', float, '_Array3f16Cp']

class Array3f(drjit.ArrayBase[Array3f, _Array3fCp, float, float, float, Array3f, Array3b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array3f64Cp: TypeAlias = Union['Array3f64', float, '_Array3fCp']

class Array3f64(drjit.ArrayBase[Array3f64, _Array3f64Cp, float, float, float, Array3f64, Array3b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array4bCp: TypeAlias = Union['Array4b', bool]

class Array4b(drjit.ArrayBase[Array4b, _Array4bCp, bool, bool, bool, Array4b, Array4b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array4i8Cp: TypeAlias = Union['Array4i8', int]

class Array4i8(drjit.ArrayBase[Array4i8, _Array4i8Cp, int, int, int, Array4i8, Array4b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array4u8Cp: TypeAlias = Union['Array4u8', int]

class Array4u8(drjit.ArrayBase[Array4u8, _Array4u8Cp, int, int, int, Array4u8, Array4b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array4iCp: TypeAlias = Union['Array4i', int, '_Array4bCp']

class Array4i(drjit.ArrayBase[Array4i, _Array4iCp, int, int, int, Array4i, Array4b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array4uCp: TypeAlias = Union['Array4u', int, '_Array4iCp']

class Array4u(drjit.ArrayBase[Array4u, _Array4uCp, int, int, int, Array4u, Array4b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array4i64Cp: TypeAlias = Union['Array4i64', int, '_Array4uCp']

class Array4i64(drjit.ArrayBase[Array4i64, _Array4i64Cp, int, int, int, Array4i64, Array4b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array4u64Cp: TypeAlias = Union['Array4u64', int, '_Array4i64Cp']

class Array4u64(drjit.ArrayBase[Array4u64, _Array4u64Cp, int, int, int, Array4u64, Array4b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array4f16Cp: TypeAlias = Union['Array4f16', float, '_Array4u64Cp']

class Array4f16(drjit.ArrayBase[Array4f16, _Array4f16Cp, float, float, float, Array4f16, Array4b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array4fCp: TypeAlias = Union['Array4f', float, '_Array4f16Cp']

class Array4f(drjit.ArrayBase[Array4f, _Array4fCp, float, float, float, Array4f, Array4b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array4f64Cp: TypeAlias = Union['Array4f64', float, '_Array4fCp']

class Array4f64(drjit.ArrayBase[Array4f64, _Array4f64Cp, float, float, float, Array4f64, Array4b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_ArrayXbCp: TypeAlias = Union['ArrayXb', bool]

class ArrayXb(drjit.ArrayBase[ArrayXb, _ArrayXbCp, bool, bool, bool, ArrayXb, ArrayXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_ArrayXi8Cp: TypeAlias = Union['ArrayXi8', int]

class ArrayXi8(drjit.ArrayBase[ArrayXi8, _ArrayXi8Cp, int, int, int, ArrayXi8, ArrayXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_ArrayXu8Cp: TypeAlias = Union['ArrayXu8', int]

class ArrayXu8(drjit.ArrayBase[ArrayXu8, _ArrayXu8Cp, int, int, int, ArrayXu8, ArrayXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_ArrayXiCp: TypeAlias = Union['ArrayXi', int, '_ArrayXbCp']

class ArrayXi(drjit.ArrayBase[ArrayXi, _ArrayXiCp, int, int, int, ArrayXi, ArrayXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_ArrayXuCp: TypeAlias = Union['ArrayXu', int, '_ArrayXiCp']

class ArrayXu(drjit.ArrayBase[ArrayXu, _ArrayXuCp, int, int, int, ArrayXu, ArrayXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_ArrayXi64Cp: TypeAlias = Union['ArrayXi64', int, '_ArrayXuCp']

class ArrayXi64(drjit.ArrayBase[ArrayXi64, _ArrayXi64Cp, int, int, int, ArrayXi64, ArrayXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_ArrayXu64Cp: TypeAlias = Union['ArrayXu64', int, '_ArrayXi64Cp']

class ArrayXu64(drjit.ArrayBase[ArrayXu64, _ArrayXu64Cp, int, int, int, ArrayXu64, ArrayXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_ArrayXf16Cp: TypeAlias = Union['ArrayXf16', float, '_ArrayXu64Cp']

class ArrayXf16(drjit.ArrayBase[ArrayXf16, _ArrayXf16Cp, float, float, float, ArrayXf16, ArrayXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_ArrayXfCp: TypeAlias = Union['ArrayXf', float, '_ArrayXf16Cp']

class ArrayXf(drjit.ArrayBase[ArrayXf, _ArrayXfCp, float, float, float, ArrayXf, ArrayXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_ArrayXf64Cp: TypeAlias = Union['ArrayXf64', float, '_ArrayXfCp']

class ArrayXf64(drjit.ArrayBase[ArrayXf64, _ArrayXf64Cp, float, float, float, ArrayXf64, ArrayXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array22bCp: TypeAlias = Union['Array22b', '_Array2bCp']

class Array22b(drjit.ArrayBase[Array22b, _Array22bCp, Array2b, _Array2bCp, Array2b, Array22b, Array22b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array22f16Cp: TypeAlias = Union['Array22f16', '_Array2f16Cp']

class Array22f16(drjit.ArrayBase[Array22f16, _Array22f16Cp, Array2f16, _Array2f16Cp, Array2f16, Array22f16, Array22b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array22fCp: TypeAlias = Union['Array22f', '_Array2fCp', '_Array22f16Cp']

class Array22f(drjit.ArrayBase[Array22f, _Array22fCp, Array2f, _Array2fCp, Array2f, Array22f, Array22b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array22f64Cp: TypeAlias = Union['Array22f64', '_Array2f64Cp', '_Array22fCp']

class Array22f64(drjit.ArrayBase[Array22f64, _Array22f64Cp, Array2f64, _Array2f64Cp, Array2f64, Array22f64, Array22b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Matrix2f16Cp: TypeAlias = Union['Matrix2f16', '_Array2f16Cp']

class Matrix2f16(drjit.ArrayBase[Matrix2f16, _Matrix2f16Cp, Array2f16, _Array2f16Cp, Array2f16, Array22f16, Array22b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Matrix2fCp: TypeAlias = Union['Matrix2f', '_Array2fCp', '_Matrix2f16Cp']

class Matrix2f(drjit.ArrayBase[Matrix2f, _Matrix2fCp, Array2f, _Array2fCp, Array2f, Array22f, Array22b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Matrix2f64Cp: TypeAlias = Union['Matrix2f64', '_Array2f64Cp', '_Matrix2fCp']

class Matrix2f64(drjit.ArrayBase[Matrix2f64, _Matrix2f64Cp, Array2f64, _Array2f64Cp, Array2f64, Array22f64, Array22b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array33bCp: TypeAlias = Union['Array33b', '_Array3bCp']

class Array33b(drjit.ArrayBase[Array33b, _Array33bCp, Array3b, _Array3bCp, Array3b, Array33b, Array33b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array33f16Cp: TypeAlias = Union['Array33f16', '_Array3f16Cp']

class Array33f16(drjit.ArrayBase[Array33f16, _Array33f16Cp, Array3f16, _Array3f16Cp, Array3f16, Array33f16, Array33b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array33fCp: TypeAlias = Union['Array33f', '_Array3fCp', '_Array33f16Cp']

class Array33f(drjit.ArrayBase[Array33f, _Array33fCp, Array3f, _Array3fCp, Array3f, Array33f, Array33b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array33f64Cp: TypeAlias = Union['Array33f64', '_Array3f64Cp', '_Array33fCp']

class Array33f64(drjit.ArrayBase[Array33f64, _Array33f64Cp, Array3f64, _Array3f64Cp, Array3f64, Array33f64, Array33b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Matrix3f16Cp: TypeAlias = Union['Matrix3f16', '_Array3f16Cp']

class Matrix3f16(drjit.ArrayBase[Matrix3f16, _Matrix3f16Cp, Array3f16, _Array3f16Cp, Array3f16, Array33f16, Array33b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Matrix3fCp: TypeAlias = Union['Matrix3f', '_Array3fCp', '_Matrix3f16Cp']

class Matrix3f(drjit.ArrayBase[Matrix3f, _Matrix3fCp, Array3f, _Array3fCp, Array3f, Array33f, Array33b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Matrix3f64Cp: TypeAlias = Union['Matrix3f64', '_Array3f64Cp', '_Matrix3fCp']

class Matrix3f64(drjit.ArrayBase[Matrix3f64, _Matrix3f64Cp, Array3f64, _Array3f64Cp, Array3f64, Array33f64, Array33b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array44bCp: TypeAlias = Union['Array44b', '_Array4bCp']

class Array44b(drjit.ArrayBase[Array44b, _Array44bCp, Array4b, _Array4bCp, Array4b, Array44b, Array44b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array44f16Cp: TypeAlias = Union['Array44f16', '_Array4f16Cp']

class Array44f16(drjit.ArrayBase[Array44f16, _Array44f16Cp, Array4f16, _Array4f16Cp, Array4f16, Array44f16, Array44b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array44fCp: TypeAlias = Union['Array44f', '_Array4fCp', '_Array44f16Cp']

class Array44f(drjit.ArrayBase[Array44f, _Array44fCp, Array4f, _Array4fCp, Array4f, Array44f, Array44b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array44f64Cp: TypeAlias = Union['Array44f64', '_Array4f64Cp', '_Array44fCp']

class Array44f64(drjit.ArrayBase[Array44f64, _Array44f64Cp, Array4f64, _Array4f64Cp, Array4f64, Array44f64, Array44b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Matrix4f16Cp: TypeAlias = Union['Matrix4f16', '_Array4f16Cp']

class Matrix4f16(drjit.ArrayBase[Matrix4f16, _Matrix4f16Cp, Array4f16, _Array4f16Cp, Array4f16, Array44f16, Array44b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Matrix4fCp: TypeAlias = Union['Matrix4f', '_Array4fCp', '_Matrix4f16Cp']

class Matrix4f(drjit.ArrayBase[Matrix4f, _Matrix4fCp, Array4f, _Array4fCp, Array4f, Array44f, Array44b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Matrix4f64Cp: TypeAlias = Union['Matrix4f64', '_Array4f64Cp', '_Matrix4fCp']

class Matrix4f64(drjit.ArrayBase[Matrix4f64, _Matrix4f64Cp, Array4f64, _Array4f64Cp, Array4f64, Array44f64, Array44b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array41bCp: TypeAlias = Union['Array41b', '_Array1bCp']

class Array41b(drjit.ArrayBase[Array41b, _Array41bCp, Array1b, _Array1bCp, Array1b, Array41b, Array41b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array41f16Cp: TypeAlias = Union['Array41f16', '_Array1f16Cp']

class Array41f16(drjit.ArrayBase[Array41f16, _Array41f16Cp, Array1f16, _Array1f16Cp, Array1f16, Array41f16, Array41b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array41fCp: TypeAlias = Union['Array41f', '_Array1fCp', '_Array41f16Cp']

class Array41f(drjit.ArrayBase[Array41f, _Array41fCp, Array1f, _Array1fCp, Array1f, Array41f, Array41b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array41f64Cp: TypeAlias = Union['Array41f64', '_Array1f64Cp', '_Array41fCp']

class Array41f64(drjit.ArrayBase[Array41f64, _Array41f64Cp, Array1f64, _Array1f64Cp, Array1f64, Array41f64, Array41b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array441bCp: TypeAlias = Union['Array441b', '_Array41bCp']

class Array441b(drjit.ArrayBase[Array441b, _Array441bCp, Array41b, _Array41bCp, Array41b, Array441b, Array441b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array441f16Cp: TypeAlias = Union['Array441f16', '_Array41f16Cp']

class Array441f16(drjit.ArrayBase[Array441f16, _Array441f16Cp, Array41f16, _Array41f16Cp, Array41f16, Array441f16, Array441b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array441fCp: TypeAlias = Union['Array441f', '_Array41fCp', '_Array441f16Cp']

class Array441f(drjit.ArrayBase[Array441f, _Array441fCp, Array41f, _Array41fCp, Array41f, Array441f, Array441b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array441f64Cp: TypeAlias = Union['Array441f64', '_Array41f64Cp', '_Array441fCp']

class Array441f64(drjit.ArrayBase[Array441f64, _Array441f64Cp, Array41f64, _Array41f64Cp, Array41f64, Array441f64, Array441b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Matrix41f16Cp: TypeAlias = Union['Matrix41f16', '_Array41f16Cp']

class Matrix41f16(drjit.ArrayBase[Matrix41f16, _Matrix41f16Cp, Array41f16, _Array41f16Cp, Array41f16, Array441f16, Array441b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Matrix41fCp: TypeAlias = Union['Matrix41f', '_Array41fCp', '_Matrix41f16Cp']

class Matrix41f(drjit.ArrayBase[Matrix41f, _Matrix41fCp, Array41f, _Array41fCp, Array41f, Array441f, Array441b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Matrix41f64Cp: TypeAlias = Union['Matrix41f64', '_Array41f64Cp', '_Matrix41fCp']

class Matrix41f64(drjit.ArrayBase[Matrix41f64, _Matrix41f64Cp, Array41f64, _Array41f64Cp, Array41f64, Array441f64, Array441b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array43bCp: TypeAlias = Union['Array43b', '_Array3bCp']

class Array43b(drjit.ArrayBase[Array43b, _Array43bCp, Array3b, _Array3bCp, Array3b, Array43b, Array43b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array43f16Cp: TypeAlias = Union['Array43f16', '_Array3f16Cp']

class Array43f16(drjit.ArrayBase[Array43f16, _Array43f16Cp, Array3f16, _Array3f16Cp, Array3f16, Array43f16, Array43b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array43fCp: TypeAlias = Union['Array43f', '_Array3fCp', '_Array43f16Cp']

class Array43f(drjit.ArrayBase[Array43f, _Array43fCp, Array3f, _Array3fCp, Array3f, Array43f, Array43b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array43f64Cp: TypeAlias = Union['Array43f64', '_Array3f64Cp', '_Array43fCp']

class Array43f64(drjit.ArrayBase[Array43f64, _Array43f64Cp, Array3f64, _Array3f64Cp, Array3f64, Array43f64, Array43b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array443bCp: TypeAlias = Union['Array443b', '_Array43bCp']

class Array443b(drjit.ArrayBase[Array443b, _Array443bCp, Array43b, _Array43bCp, Array43b, Array443b, Array443b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array443f16Cp: TypeAlias = Union['Array443f16', '_Array43f16Cp']

class Array443f16(drjit.ArrayBase[Array443f16, _Array443f16Cp, Array43f16, _Array43f16Cp, Array43f16, Array443f16, Array443b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array443fCp: TypeAlias = Union['Array443f', '_Array43fCp', '_Array443f16Cp']

class Array443f(drjit.ArrayBase[Array443f, _Array443fCp, Array43f, _Array43fCp, Array43f, Array443f, Array443b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array443f64Cp: TypeAlias = Union['Array443f64', '_Array43f64Cp', '_Array443fCp']

class Array443f64(drjit.ArrayBase[Array443f64, _Array443f64Cp, Array43f64, _Array43f64Cp, Array43f64, Array443f64, Array443b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Matrix43f16Cp: TypeAlias = Union['Matrix43f16', '_Array43f16Cp']

class Matrix43f16(drjit.ArrayBase[Matrix43f16, _Matrix43f16Cp, Array43f16, _Array43f16Cp, Array43f16, Array443f16, Array443b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Matrix43fCp: TypeAlias = Union['Matrix43f', '_Array43fCp', '_Matrix43f16Cp']

class Matrix43f(drjit.ArrayBase[Matrix43f, _Matrix43fCp, Array43f, _Array43fCp, Array43f, Array443f, Array443b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Matrix43f64Cp: TypeAlias = Union['Matrix43f64', '_Array43f64Cp', '_Matrix43fCp']

class Matrix43f64(drjit.ArrayBase[Matrix43f64, _Matrix43f64Cp, Array43f64, _Array43f64Cp, Array43f64, Array443f64, Array443b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array34bCp: TypeAlias = Union['Array34b', '_Array4bCp']

class Array34b(drjit.ArrayBase[Array34b, _Array34bCp, Array4b, _Array4bCp, Array4b, Array34b, Array34b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array34f16Cp: TypeAlias = Union['Array34f16', '_Array4f16Cp']

class Array34f16(drjit.ArrayBase[Array34f16, _Array34f16Cp, Array4f16, _Array4f16Cp, Array4f16, Array34f16, Array34b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array34fCp: TypeAlias = Union['Array34f', '_Array4fCp', '_Array34f16Cp']

class Array34f(drjit.ArrayBase[Array34f, _Array34fCp, Array4f, _Array4fCp, Array4f, Array34f, Array34b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array34f64Cp: TypeAlias = Union['Array34f64', '_Array4f64Cp', '_Array34fCp']

class Array34f64(drjit.ArrayBase[Array34f64, _Array34f64Cp, Array4f64, _Array4f64Cp, Array4f64, Array34f64, Array34b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array334bCp: TypeAlias = Union['Array334b', '_Array34bCp']

class Array334b(drjit.ArrayBase[Array334b, _Array334bCp, Array34b, _Array34bCp, Array34b, Array334b, Array334b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array334f16Cp: TypeAlias = Union['Array334f16', '_Array34f16Cp']

class Array334f16(drjit.ArrayBase[Array334f16, _Array334f16Cp, Array34f16, _Array34f16Cp, Array34f16, Array334f16, Array334b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array334fCp: TypeAlias = Union['Array334f', '_Array34fCp', '_Array334f16Cp']

class Array334f(drjit.ArrayBase[Array334f, _Array334fCp, Array34f, _Array34fCp, Array34f, Array334f, Array334b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array334f64Cp: TypeAlias = Union['Array334f64', '_Array34f64Cp', '_Array334fCp']

class Array334f64(drjit.ArrayBase[Array334f64, _Array334f64Cp, Array34f64, _Array34f64Cp, Array34f64, Array334f64, Array334b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Matrix34f16Cp: TypeAlias = Union['Matrix34f16', '_Array34f16Cp']

class Matrix34f16(drjit.ArrayBase[Matrix34f16, _Matrix34f16Cp, Array34f16, _Array34f16Cp, Array34f16, Array334f16, Array334b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Matrix34fCp: TypeAlias = Union['Matrix34f', '_Array34fCp', '_Matrix34f16Cp']

class Matrix34f(drjit.ArrayBase[Matrix34f, _Matrix34fCp, Array34f, _Array34fCp, Array34f, Array334f, Array334b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Matrix34f64Cp: TypeAlias = Union['Matrix34f64', '_Array34f64Cp', '_Matrix34fCp']

class Matrix34f64(drjit.ArrayBase[Matrix34f64, _Matrix34f64Cp, Array34f64, _Array34f64Cp, Array34f64, Array334f64, Array334b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array444bCp: TypeAlias = Union['Array444b', '_Array44bCp']

class Array444b(drjit.ArrayBase[Array444b, _Array444bCp, Array44b, _Array44bCp, Array44b, Array444b, Array444b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array444f16Cp: TypeAlias = Union['Array444f16', '_Array44f16Cp']

class Array444f16(drjit.ArrayBase[Array444f16, _Array444f16Cp, Array44f16, _Array44f16Cp, Array44f16, Array444f16, Array444b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array444fCp: TypeAlias = Union['Array444f', '_Array44fCp', '_Array444f16Cp']

class Array444f(drjit.ArrayBase[Array444f, _Array444fCp, Array44f, _Array44fCp, Array44f, Array444f, Array444b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Array444f64Cp: TypeAlias = Union['Array444f64', '_Array44f64Cp', '_Array444fCp']

class Array444f64(drjit.ArrayBase[Array444f64, _Array444f64Cp, Array44f64, _Array44f64Cp, Array44f64, Array444f64, Array444b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Matrix44f16Cp: TypeAlias = Union['Matrix44f16', '_Array44f16Cp']

class Matrix44f16(drjit.ArrayBase[Matrix44f16, _Matrix44f16Cp, Array44f16, _Array44f16Cp, Array44f16, Array444f16, Array444b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Matrix44fCp: TypeAlias = Union['Matrix44f', '_Array44fCp', '_Matrix44f16Cp']

class Matrix44f(drjit.ArrayBase[Matrix44f, _Matrix44fCp, Array44f, _Array44fCp, Array44f, Array444f, Array444b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Matrix44f64Cp: TypeAlias = Union['Matrix44f64', '_Array44f64Cp', '_Matrix44fCp']

class Matrix44f64(drjit.ArrayBase[Matrix44f64, _Matrix44f64Cp, Array44f64, _Array44f64Cp, Array44f64, Array444f64, Array444b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Complex2fCp: TypeAlias = Union['Complex2f', float]

class Complex2f(drjit.ArrayBase[Complex2f, _Complex2fCp, float, float, float, Array2f, Array2b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Complex2f64Cp: TypeAlias = Union['Complex2f64', float, '_Complex2fCp']

class Complex2f64(drjit.ArrayBase[Complex2f64, _Complex2f64Cp, float, float, float, Array2f64, Array2b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Quaternion4f16Cp: TypeAlias = Union['Quaternion4f16', float]

class Quaternion4f16(drjit.ArrayBase[Quaternion4f16, _Quaternion4f16Cp, float, float, float, Array4f16, Array4b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Quaternion4fCp: TypeAlias = Union['Quaternion4f', float, '_Quaternion4f16Cp']

class Quaternion4f(drjit.ArrayBase[Quaternion4f, _Quaternion4fCp, float, float, float, Array4f, Array4b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_Quaternion4f64Cp: TypeAlias = Union['Quaternion4f64', float, '_Quaternion4fCp']

class Quaternion4f64(drjit.ArrayBase[Quaternion4f64, _Quaternion4f64Cp, float, float, float, Array4f64, Array4b]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_TensorXbCp: TypeAlias = Union['TensorXb', bool]

class TensorXb(drjit.ArrayBase[TensorXb, _TensorXbCp, TensorXb, _TensorXbCp, TensorXb, ArrayXb, TensorXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_TensorXi8Cp: TypeAlias = Union['TensorXi8', int]

class TensorXi8(drjit.ArrayBase[TensorXi8, _TensorXi8Cp, TensorXi8, _TensorXi8Cp, TensorXi8, ArrayXi8, TensorXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_TensorXiCp: TypeAlias = Union['TensorXi', int, '_TensorXbCp']

class TensorXi(drjit.ArrayBase[TensorXi, _TensorXiCp, TensorXi, _TensorXiCp, TensorXi, ArrayXi, TensorXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_TensorXi64Cp: TypeAlias = Union['TensorXi64', int]

class TensorXi64(drjit.ArrayBase[TensorXi64, _TensorXi64Cp, TensorXi64, _TensorXi64Cp, TensorXi64, ArrayXi64, TensorXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_TensorXu8Cp: TypeAlias = Union['TensorXu8', int]

class TensorXu8(drjit.ArrayBase[TensorXu8, _TensorXu8Cp, TensorXu8, _TensorXu8Cp, TensorXu8, ArrayXu8, TensorXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_TensorXuCp: TypeAlias = Union['TensorXu', int, '_TensorXiCp']

class TensorXu(drjit.ArrayBase[TensorXu, _TensorXuCp, TensorXu, _TensorXuCp, TensorXu, ArrayXu, TensorXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_TensorXu64Cp: TypeAlias = Union['TensorXu64', int, '_TensorXi64Cp']

class TensorXu64(drjit.ArrayBase[TensorXu64, _TensorXu64Cp, TensorXu64, _TensorXu64Cp, TensorXu64, ArrayXu64, TensorXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_TensorXf16Cp: TypeAlias = Union['TensorXf16', float, '_TensorXu64Cp']

class TensorXf16(drjit.ArrayBase[TensorXf16, _TensorXf16Cp, TensorXf16, _TensorXf16Cp, TensorXf16, ArrayXf16, TensorXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_TensorXfCp: TypeAlias = Union['TensorXf', float, '_TensorXf16Cp']

class TensorXf(drjit.ArrayBase[TensorXf, _TensorXfCp, TensorXf, _TensorXfCp, TensorXf, ArrayXf, TensorXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

_TensorXf64Cp: TypeAlias = Union['TensorXf64', float, '_TensorXfCp']

class TensorXf64(drjit.ArrayBase[TensorXf64, _TensorXf64Cp, TensorXf64, _TensorXf64Cp, TensorXf64, ArrayXf64, TensorXb]):
    def __getitem__(self, key, /):
        """Return self[key]."""

    def __setitem__(self, key, value, /):
        """Set self[key] to value."""

    def __delitem__(self, key, /):
        """Delete self[key]."""

class PCG32:
    r"""
    Implementation of PCG32, a member of the PCG family of random number
    generators proposed by Melissa O'Neill.

    PCG32 is a stateful pseudorandom number generator that combines a linear
    congruential generator (LCG) with a permutation function. It provides high
    statistical quality with a remarkably fast and compact implementation.
    Details on the PCG family of pseudorandom number generators can be found
    `here <https://www.pcg-random.org/index.html>`__.

    To create random tensors of different sizes in Python, prefer the
    higher-level :py:func:`dr.rng() <drjit.rng>` interface, which internally
    uses the :py:class:`Philox4x32` generator. The properties of PCG32 makes it
    most suitable for Monte Carlo applications requiring long sequences of
    random variates.

    Key properties of the PCG variant implemented here include:

    * **Compact**: 128 bits total state (64-bit state + 64-bit increment)

    * **Output**: 32-bit output with a period of 2^64 per stream

    * **Streams**: Multiple independent streams via the increment parameter
      (with caveats, see below)

    * **Low-cost sample generation**: a single 64 bit integer multiply-add plus
      a bit permutation applied to the output.

    * **Extra features**: provides fast multi-step advance/rewind functionality.

    **Caveats**: PCG32 produces random high-quality variates within each random
    number stream. For a given initial state, PCG32 can also produce multiple
    output streams by specifying a different sequence increment (``initseq``) to the
    constructor. However, the level of statistical independence *across streams*
    is generally insufficient when doing so. To obtain a series of high-quality
    independent parallel streams, it is recommended to use another method (e.g.,
    the Tiny Encryption Algorithm) to seed the `state` and `inc` parameters. This
    ensures independence both within and across streams.

    In Python, the :py:class:`PCG32` class is implemented as a :ref:`PyTree
    <pytrees>`, which means that it is compatible with symbolic function calls,
    loops, etc.

    .. note::

       Please watch out for the following pitfall when using the PCG32 class in
       long-running Dr.Jit calculations (e.g., steps of a gradient-based optimizer).
       Consuming random variates (e.g., through :py:func:`next_float`) changes
       the internal RNG state. If this state is never explicitly evaluated,
       the computation graph describing the state transformation keeps growing
       without bound, causing kernel compilation of increasingly large programs
       to eventually become a bottleneck. To evaluate the RNG, simply run

       .. code-block:: python

          rng: PCG32 = ....
          dr.eval(rng)

       For computation involving very large arrays, storing the RNG state (16
       bytes per entry) can be prohibitive. In this case, it is better to keep
       the RNG in symbolic form and re-seed it at every optimization iteration.

       In cases where a sampler is repeatedly used in a symbolic loop, it is
       more efficient to use the PCG32 API directly to seed once and reuse the
       random number generator throughout the loop.

       The :py:func:`drjit.rng <rng>` API avoids these pitfalls by eagerly
       evaluating the RNG state.

    Comparison with \ref Philox4x32:

    * :py:class:`PCG32 <drjit.auto.PCG32>`: State-based, better for sequential generation,
      low per-sample cost.

    * :py:class:`Philox4x32 <drjit.auto.Philox4x32>`: Counter-based, better for
      parallel generation, higher per-sample cost.
    """

    @overload
    def __init__(self, size: int = 1, initstate: int = UInt64(0x853c49e6748fea9b), initseq: int = UInt64(0xda3e39cb94b95bdb)) -> None:
        """
        Initialize a random number generator that generates ``size`` variates in parallel.

        The ``initstate`` and ``initseq`` inputs determine the initial state and increment
        of the linear congruential generator. Their defaults values are based on the
        original implementation.

        The implementation of this routine internally calls py:func:`seed`, with one
        small twist. When multiple random numbers are being generated in parallel, the
        constructor adds an offset equal to :py:func:`drjit.arange(UInt64, size)
        <drjit.arange>` to both ``initstate`` and ``initseq`` to de-correlate the
        generated sequences.
        """

    @overload
    def __init__(self, arg: PCG32) -> None:
        """Copy-construct a new PCG32 instance from an existing instance."""

    def seed(self, initstate: int = UInt64(0x853c49e6748fea9b), initseq: int = UInt64(0xda3e39cb94b95bdb)) -> None:
        """
        Seed the random number generator with the given initial state and sequence ID.

        The ``initstate`` and ``initseq`` inputs determine the initial state and increment
        of the linear congruential generator. Their values are the defaults from the
        original implementation.
        """

    @overload
    def next_uint32(self) -> int:
        """
        Generate a uniformly distributed unsigned 32-bit random number

        Two overloads of this function exist: the masked variant does not advance
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def next_uint32(self, arg: bool, /) -> int: ...

    @overload
    def prev_uint32(self) -> int:
        """
        Generate the previous uniformly distributed unsigned 32-bit random number
        by stepping the PCG32 state backwards.

        Two overloads of this function exist: the masked variant does not
        regress the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def prev_uint32(self, arg: bool, /) -> int: ...

    def next_uint32_bounded(self, bound: int, mask: bool = Bool(True)) -> int:
        r"""
        Generate a uniformly distributed 32-bit integer number on the
        interval :math:`[0, \texttt{bound})`.

        To ensure an unbiased result, the implementation relies on an iterative
        scheme that typically finishes after 1-2 iterations.
        """

    @overload
    def next_uint64(self) -> int:
        """
        Generate a uniformly distributed unsigned 64-bit random number

        Internally, the function calls :py:func:`next_uint32` twice.

        Two overloads of this function exist: the masked variant does not advance
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def next_uint64(self, arg: bool, /) -> int: ...

    @overload
    def prev_uint64(self) -> int:
        """
        Generate the previous uniformly distributed unsigned 64-bit random number
        by stepping the PCG32 state backwards.

        Internally, the function calls :py:func:`prev_uint32` twice.

        Two overloads of this function exist: the masked variant does not regress
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def prev_uint64(self, arg: bool, /) -> int: ...

    def next_uint64_bounded(self, bound: int, mask: bool = Bool(True)) -> int:
        r"""
        Generate a uniformly distributed 64-bit integer number on the
        interval :math:`[0, \texttt{bound})`.

        To ensure an unbiased result, the implementation relies on an iterative
        scheme that typically finishes after 1-2 iterations.
        """

    def next_float(self, dtype: type, mask: object = True) -> object:
        """
        Generate a uniformly distributed precision floating point number on the
        interval :math:`[0, 1)`.

        The function analyzes the provided target ``dtype`` and either invokes
        :py:func:`next_float16`, :py:func:`next_float32` or :py:func:`next_float64`
        depending on the
        requested precision.

        A mask can be optionally provided. Masked entries do not advance the PRNG state.
        """

    def prev_float(self, dtype: type, mask: object = True) -> object:
        """
        Generate the previous uniformly distributed precision floating point number
        on the half-open interval :math:`[0, 1)` by stepping the PCG32 state backwards.

        The function analyzes the provided target ``dtype`` and either invokes
        :py:func:`prev_float16`, :py:func:`prev_float32` or :py:func:`prev_float64`
        depending on the
        requested precision.

        A mask can be optionally provided. Masked entries do not regress the PRNG state.
        """

    @overload
    def next_float16(self) -> float:
        """
        Generate a uniformly distributed half precision floating point number on the
        interval :math:`[0, 1)`.

        Two overloads of this function exist: the masked variant does not advance
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def next_float16(self, arg: bool, /) -> float: ...

    @overload
    def prev_float16(self) -> float:
        """
        Generate the previous uniformly distributed half precision floating point number
        on the half-open interval :math:`[0, 1)` by stepping the PCG32 state backwards.

        Two overloads of this function exist: the masked variant does not regress
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def prev_float16(self, arg: bool, /) -> float: ...

    @overload
    def next_float32(self) -> float:
        """
        Generate a uniformly distributed single precision floating point number on the
        interval :math:`[0, 1)`.

        Two overloads of this function exist: the masked variant does not advance
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def next_float32(self, arg: bool, /) -> float: ...

    @overload
    def prev_float32(self) -> float:
        """
        Generate the previous uniformly distributed single precision floating point number
        on the half-open interval :math:`[0, 1)` by stepping the PCG32 state backwards.

        Two overloads of this function exist: the masked variant does not regress
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def prev_float32(self, arg: bool, /) -> float: ...

    @overload
    def next_float64(self) -> float:
        """
        Generate a uniformly distributed double precision floating point number on the
        interval :math:`[0, 1)`.

        Two overloads of this function exist: the masked variant does not advance
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def next_float64(self, arg: bool, /) -> float: ...

    @overload
    def prev_float64(self) -> float:
        """
        Generate the previous uniformly distributed double precision floating point number
        on the half-open interval :math:`[0, 1)` by stepping the PCG32 state backwards.

        Two overloads of this function exist: the masked variant does not regress
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def prev_float64(self, arg: bool, /) -> float: ...

    def next_float_normal(self, dtype: type, mask: object = True) -> object:
        """
        Generate a (standard) normally distributed precision floating point number.

        The function analyzes the provided target ``dtype`` and either invokes
        :py:func:`next_float16_normal`, :py:func:`next_float32_normal` or
        :py:func:`next_float64_normal` depending on the requested precision.

        A mask can be optionally provided. Masked entries do not advance the PRNG state.
        """

    def prev_float_normal(self, dtype: type, mask: object = True) -> object:
        """
        Generate the previous (standard) normally distributed precision floating point number
        by stepping the PCG32 state backwards.

        The function analyzes the provided target ``dtype`` and either invokes
        :py:func:`prev_float16_normal`, :py:func:`prev_float32_normal` or
        :py:func:`prev_float64_normal` depending on the requested precision.

        A mask can be optionally provided. Masked entries do not regress the PRNG state.
        """

    @overload
    def next_float16_normal(self) -> float:
        """
        Generate a (standard) normally distributed half precision floating point number.

        Two overloads of this function exist: the masked variant does not advance
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def next_float16_normal(self, arg: bool, /) -> float: ...

    @overload
    def prev_float16_normal(self) -> float:
        """
        Generate the previous (standard) normally distributed half precision floating
        point number by stepping the PCG32 state backwards.

        Two overloads of this function exist: the masked variant does not regress
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def prev_float16_normal(self, arg: bool, /) -> float: ...

    @overload
    def next_float32_normal(self) -> float:
        """
        Generate a (standard) normally distributed single precision floating point number.

        Two overloads of this function exist: the masked variant does not advance
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def next_float32_normal(self, arg: bool, /) -> float: ...

    @overload
    def prev_float32_normal(self) -> float:
        """
        Generate the previous (standard) normally distributed single precision floating
        point number by stepping the PCG32 state backwards.

        Two overloads of this function exist: the masked variant does not regress
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def prev_float32_normal(self, arg: bool, /) -> float: ...

    @overload
    def next_float64_normal(self) -> float:
        """
        Generate a (standard) normally distributed double precision floating point number.

        Two overloads of this function exist: the masked variant does not advance
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def next_float64_normal(self, arg: bool, /) -> float: ...

    @overload
    def prev_float64_normal(self) -> float:
        """
        Generate the previous (standard) normally distributed double precision floating
        point number by stepping the PCG32 state backwards.

        Two overloads of this function exist: the masked variant does not regress
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def prev_float64_normal(self, arg: bool, /) -> float: ...

    def __add__(self, arg: int, /) -> PCG32:
        """
        Advance the pseudorandom number generator.

        This function implements a multi-step advance function that is equivalent to
        (but more efficient than) calling the random number generator ``arg`` times
        in sequence.

        This is useful to advance a newly constructed PRNG to a certain known state.
        """

    def __iadd__(self, arg: int, /) -> PCG32:
        """In-place addition operator based on :py:func:`__add__`."""

    @overload
    def __sub__(self, arg: int, /) -> PCG32:
        """
        Rewind the pseudorandom number generator.

        This function implements the opposite of ``__add__`` to step a PRNG backwards.
        It can also compute the *difference* (as counted by the number of internal
        ``next_uint32`` steps) between two :py:class:`PCG32` instances. This assumes
        that the two instances were consistently seeded.
        """

    @overload
    def __sub__(self, arg: PCG32, /) -> int: ...

    def __isub__(self, arg: Int64, /) -> PCG32: # type: ignore
        """In-place subtraction operator based on :py:func:`__sub__`."""

    @property
    def state(self) -> int:
        """
        Sequence state of the PCG32 PRNG (an unsigned 64-bit integer or integer array). Please see the original paper for details on this field.
        """

    @state.setter
    def state(self, arg: int, /) -> None: ...

    @property
    def inc(self) -> int:
        """
        Sequence increment of the PCG32 PRNG (an unsigned 64-bit integer or integer array). Please see the original paper for details on this field.
        """

    @inc.setter
    def inc(self, arg: int, /) -> None: ...

    DRJIT_STRUCT: dict = {'state' : int, 'inc' : int}

class Philox4x32:
    """
    Philox4x32 counter-based PRNG

    This class implements the Philox 4x32 counter-based pseudo-random number
    generator based on the paper `Parallel Random Numbers: As Easy as 1, 2, 3
    <https://www.thesalmons.org/john/random123/papers/random123sc11.pdf>`__ by
    Salmon et al. [2011]. It uses strength-reduced cryptographic
    primitives to realize a complex transition function that turns a seed and
    set of counter values onto 4 pseudorandom outputs. Incrementing any of the
    counters or choosing a different seed produces statistically independent
    samples.

    The implementation here uses a reduced number of bits (32) for the
    arithmetic and sets the default number of rounds to 7. However, even with
    these simplifications it passes the `Test01
    <https://en.wikipedia.org/wiki/TestU01>`__ stringent ``BigCrush`` tests (a
    battery of statistical tests for non-uniformity and correlations). Please
    see the paper `Random number generators for massively parallel simulations
    on GPU <https://arxiv.org/abs/1204.6193>`__ by Manssen et al. [2012] for
    details.

    Functions like :py:func:`next_uint32x4()` or :py:func:`next_float32x4()`
    advance the PRNG state by incrementing the counter ``ctr[3]``.

    Key properties include:

    * Counter-based design: generation from counter + key

    * 192-bit bit state: 4x32-bit counters, 64-bit key

    * Trivial jump-ahead capability through counter manipulation

    The :py:class:`Philox4x32` class is implemented as a :ref:`PyTree <pytrees>`,
    making it compatible with symbolic function calls, loops, etc.

    .. note::

       :py:class:`Philox4x32` naturally produces 4 samples at a time, which may
       be awkward for applications that need individual random values.

    .. note::

       For a comparison of use cases between :py:class:`Philox4x32` and
       :py:class:`PCG32`, see the :py:class:`PCG32` class documentation. In
       brief: use :py:class:`PCG32` for sequential generation with lowest cost
       per sample; use :py:class:`Philox4x32` for parallel generation where
       independent streams are critical.

    .. note::

       Please watch out for the following pitfall when using the Philox4x32 class in
       long-running Dr.Jit calculations (e.g., steps of a gradient-based optimizer).
       Consuming random variates (e.g., through :py:func:`next_float_4x32`) changes
       the internal RNG counter value. If this state is never explicitly evaluated,
       the computation graph describing this cahnge keeps growing
       causing kernel compilation of increasingly large programs
       to eventually become a bottleneck.
       The :py:func:`drjit.rng <rng>` API avoids this pitfall by eagerly
       evaluating the RNG counter when needed.

       In cases where a sampler is repeatedly used in a symbolic loop, it is
       more efficient to use the PCG32 PRNG with its lower per-sample cost. You
       can seed this method once and reuse the random number generator
       throughout the loop.
    """

    @overload
    def __init__(self, seed: int, counter_0: int, counter_1: int = 0, counter_2: int = 0, iterations: int = 7) -> None:
        """
        Initialize a Philox4x32 random number generator.

        The function takes a ``seed`` and three of four ``counter`` component.
        The last component is zero-initialized and incremented by calls to the
        ``sample_*`` methods.

        Args:
            seed: The 64-bit seed value used as the key for the mapping
            ctr_0: The first 32-bit counter value (least significant)
            ctr_1: The second 32-bit counter value (default: 0)
            ctr_2: The third 32-bit counter value (default: 0)
            iterations: Number of rounds to apply (default: 7, range: 4-10)

        For parallel stream generation, simply use different counter values - each
        combination of counter values produces an independent random stream.
        """

    @overload
    def __init__(self, arg: Philox4x32) -> None:
        """Copy constructor"""

    def next_uint32x4(self, mask: bool = True) -> Array4u:
        """
        Generate 4 random 32-bit unsigned integers.

        Advances the internal counter and applies the Philox mapping to
        produce 4 independent 32-bit random values.

        Args:
            mask: Optional mask to control which lanes are updated

        Returns:
            Array of 4 random 32-bit unsigned integers
        """

    def next_uint64x2(self, mask: bool = True) -> Array2u64:
        """
        Generate 2 random 64-bit unsigned integers.

        Advances the internal counter and applies the Philox mapping to
        produce 4 independent 64-bit random values.

        Args:
            mask: Optional mask to control which lanes are updated

        Returns:
            Array of 2 random 64-bit unsigned integers
        """

    def next_float16x4(self, mask: bool = True) -> Array4f16:
        """
        Generate 4 random half-precision floats in :math:`[0, 1)`.

        Generates 4 random 32-bit unsigned integers and converts them to half
        precision floats that are uniformly distributed on the half-open interval
        :math:`[0, 1)`.

        Args:
            mask: Optional mask to control which lanes are updated

        Returns:
            Array of 4 random floats on the half-open interval :math:`[0, 1)`
        """

    def next_float32x4(self, mask: bool = True) -> Array4f:
        """
        Generate 4 random single-precision floats in :math:`[0, 1)`.

        Generates 4 random 32-bit unsigned integers and converts them to single
        precision floats that are uniformly distributed on the half-open interval
        :math:`[0, 1)`.

        Args:
            mask: Optional mask to control which lanes are updated

        Returns:
            Array of 4 random floats on the half-open interval :math:`[0, 1)`
        """

    def next_float64x2(self, mask: bool = True) -> Array2f64:
        """
        Generate 2 random double-precision floats in :math:`[0, 1)`.

        Generates 2 random 64-bit unsigned integers and converts them to
        floats uniformly distributed on the half-open interval :math:`[0, 1)`.

        Args:
            mask: Optional mask to control which lanes are updated

        Returns:
            Array of 2 random floats on the half-open interval :math:`[0, 1)`
        """

    def next_float16x4_normal(self, mask: bool = True) -> Array4f16:
        """
        Generate 4 normally distributed single-precision floats

        Advances the internal counter and applies the Philox mapping to produce 4
        single precision floats following a standard normal distribution.

        Args:
            mask: Optional mask to control which lanes are updated

        Returns:
            Array of 4 random floats from a standard normal distribution
        """

    def next_float32x4_normal(self, mask: bool = True) -> Array4f:
        """
        Generate 4 normally distributed single-precision floats

        Advances the internal counter and applies the Philox mapping to produce 4
        single precision floats following a standard normal distribution.

        Args:
            mask: Optional mask to control which lanes are updated

        Returns:
            Array of 4 random floats from a standard normal distribution
        """

    def next_float64x2_normal(self, mask: bool = True) -> Array2f64:
        """
        Generate 2 normally distributed double-precision floats

        Advances the internal counter and applies the Philox mapping to
        produce 2 double precision floats following a standard normal distribution.

        Args:
            mask: Optional mask to control which lanes are updated

        Returns:
            Array of 2 random floats from a standard normal distribution
        """

    @property
    def seed(self) -> Array2u: ...

    @seed.setter
    def seed(self, arg: Array2u, /) -> None: ...

    @property
    def counter(self) -> Array4u: ...

    @counter.setter
    def counter(self, arg: Array4u, /) -> None: ...

    @property
    def iterations(self) -> int: ...

    @iterations.setter
    def iterations(self, arg: int, /) -> None: ...

class Texture1f16:
    @overload
    def __init__(self, shape: Sequence[int], channels: int, use_accel: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Create a new texture with the specified size and channel count

        On CUDA, this is a slow operation that synchronizes the GPU pipeline, so
        texture objects should be reused/updated via :py:func:`set_value()` and
        :py:func:`set_tensor()` as much as possible.

        When ``use_accel`` is set to ``False`` on CUDA mode, the texture will not
        use hardware acceleration (allocation and evaluation). In other modes
        this argument has no effect.

        The ``filter_mode`` parameter defines the interpolation method to be used
        in all evaluation routines. By default, the texture is linearly
        interpolated. Besides nearest/linear filtering, the implementation also
        provides a clamped cubic B-spline interpolation scheme in case a
        higher-order interpolation is needed. In CUDA mode, this is done using a
        series of linear lookups to optimally use the hardware (hence, linear
        filtering must be enabled to use this feature).

        When evaluating the texture outside of its boundaries, the ``wrap_mode``
        defines the wrapping method. The default behavior is ``drjit.WrapMode.Clamp``,
        which indefinitely extends the colors on the boundary along each dimension.
        """

    @overload
    def __init__(self, tensor: TensorXf16, use_accel: bool = True, migrate: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Construct a new texture from a given tensor.

        This constructor allocates texture memory with the shape information
        deduced from ``tensor``. It subsequently invokes :py:func:`set_tensor(tensor)`
        to fill the texture memory with the provided tensor.

        When both ``migrate`` and ``use_accel`` are set to ``True`` in CUDA mode, the texture
        exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage. Note that the texture is still differentiable even when migrated.
        """

    def set_value(self, value: ArrayXf16, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided linearized 1D array.

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def set_tensor(self, tensor: TensorXf16, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided tensor.

        This method updates the values of all texels. Changing the texture
        resolution or its number of channels is also supported. However, on CUDA,
        such operations have a significantly larger overhead (the GPU pipeline
        needs to be synchronized for new texture objects to be created).

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def update_inplace(self, migrate: bool = False) -> None:
        """
        Update the texture after applying an indirect update to its tensor
        representation (obtained with py:func:`tensor()`).

        A tensor representation of this texture object can be retrived with
        py:func:`tensor()`. That representation can be modified, but in order to apply
        it succesfuly to the texture, this method must also be called. In short,
        this method will use the tensor representation to update the texture's
        internal state.

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.)
        """

    def value(self) -> ArrayXf16:
        """Return the texture data as an array object"""

    def tensor(self) -> TensorXf16:
        """Return the texture data as a tensor object"""

    def filter_mode(self) -> drjit.FilterMode:
        """Return the filter mode"""

    def wrap_mode(self) -> drjit.WrapMode:
        """Return the wrap mode"""

    def use_accel(self) -> bool:
        """Return whether texture uses the GPU for storage and evaluation"""

    def migrated(self) -> bool:
        """
        Return whether textures with :py:func:`use_accel()` set to ``True`` only store
        the data as a hardware-accelerated CUDA texture.

        If ``False`` then a copy of the array data will additionally be retained .
        """

    @property
    def shape(self) -> tuple:
        """Return the texture shape"""

    @overload
    def eval(self, pos: Array1f, active: bool | None = Bool(True)) -> list[float]:
        """Evaluate the linear interpolant represented by this texture."""

    @overload
    def eval(self, pos: Array1f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval(self, pos: Array1f64, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_fetch(self, pos: Array1f, active: bool | None = Bool(True)) -> list[list[float]]:
        """
        Fetch the texels that would be referenced in a texture lookup with
        linear interpolation without actually performing this interpolation.
        """

    @overload
    def eval_fetch(self, pos: Array1f16, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_fetch(self, pos: Array1f64, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_cubic(self, pos: Array1f, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]:
        """
        Evaluate a clamped cubic B-Spline interpolant represented by this
        texture

        Instead of interpolating the texture via B-Spline basis functions, the
        implementation transforms this calculation into an equivalent weighted
        sum of several linear interpolant evaluations. In CUDA mode, this can
        then be accelerated by hardware texture units, which runs faster than
        a naive implementation. More information can be found in:

            GPU Gems 2, Chapter 20, "Fast Third-Order Texture Filtering"
            by Christian Sigg.

        When the underlying grid data and the query position are differentiable,
        this transformation cannot be used as it is not linear with respect to position
        (thus the default AD graph gives incorrect results). The implementation
        calls :py:func:`eval_cubic_helper()` function to replace the AD graph with a
        direct evaluation of the B-Spline basis functions in that case.
        """

    @overload
    def eval_cubic(self, pos: Array1f16, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic(self, pos: Array1f64, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic_grad(self, pos: Array1f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_grad(self, pos: Array1f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_grad(self, pos: Array1f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array1f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient and hessian matrix of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_hessian(self, pos: Array1f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array1f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_helper(self, pos: Array1f, active: bool | None = Bool(True)) -> list[float]:
        """
        Helper function to evaluate a clamped cubic B-Spline interpolant

        This is an implementation detail and should only be called by the
        :py:func:`eval_cubic()` function to construct an AD graph. When only the cubic
        evaluation result is desired, the :py:func:`eval_cubic()` function is faster
        than this simple implementation
        """

    @overload
    def eval_cubic_helper(self, pos: Array1f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_cubic_helper(self, pos: Array1f64, active: bool | None = Bool(True)) -> list[float]: ...

    IsTexture: bool = True

class Texture2f16:
    @overload
    def __init__(self, shape: Sequence[int], channels: int, use_accel: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Create a new texture with the specified size and channel count

        On CUDA, this is a slow operation that synchronizes the GPU pipeline, so
        texture objects should be reused/updated via :py:func:`set_value()` and
        :py:func:`set_tensor()` as much as possible.

        When ``use_accel`` is set to ``False`` on CUDA mode, the texture will not
        use hardware acceleration (allocation and evaluation). In other modes
        this argument has no effect.

        The ``filter_mode`` parameter defines the interpolation method to be used
        in all evaluation routines. By default, the texture is linearly
        interpolated. Besides nearest/linear filtering, the implementation also
        provides a clamped cubic B-spline interpolation scheme in case a
        higher-order interpolation is needed. In CUDA mode, this is done using a
        series of linear lookups to optimally use the hardware (hence, linear
        filtering must be enabled to use this feature).

        When evaluating the texture outside of its boundaries, the ``wrap_mode``
        defines the wrapping method. The default behavior is ``drjit.WrapMode.Clamp``,
        which indefinitely extends the colors on the boundary along each dimension.
        """

    @overload
    def __init__(self, tensor: TensorXf16, use_accel: bool = True, migrate: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Construct a new texture from a given tensor.

        This constructor allocates texture memory with the shape information
        deduced from ``tensor``. It subsequently invokes :py:func:`set_tensor(tensor)`
        to fill the texture memory with the provided tensor.

        When both ``migrate`` and ``use_accel`` are set to ``True`` in CUDA mode, the texture
        exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage. Note that the texture is still differentiable even when migrated.
        """

    def set_value(self, value: ArrayXf16, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided linearized 1D array.

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def set_tensor(self, tensor: TensorXf16, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided tensor.

        This method updates the values of all texels. Changing the texture
        resolution or its number of channels is also supported. However, on CUDA,
        such operations have a significantly larger overhead (the GPU pipeline
        needs to be synchronized for new texture objects to be created).

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def update_inplace(self, migrate: bool = False) -> None:
        """
        Update the texture after applying an indirect update to its tensor
        representation (obtained with py:func:`tensor()`).

        A tensor representation of this texture object can be retrived with
        py:func:`tensor()`. That representation can be modified, but in order to apply
        it succesfuly to the texture, this method must also be called. In short,
        this method will use the tensor representation to update the texture's
        internal state.

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.)
        """

    def value(self) -> ArrayXf16:
        """Return the texture data as an array object"""

    def tensor(self) -> TensorXf16:
        """Return the texture data as a tensor object"""

    def filter_mode(self) -> drjit.FilterMode:
        """Return the filter mode"""

    def wrap_mode(self) -> drjit.WrapMode:
        """Return the wrap mode"""

    def use_accel(self) -> bool:
        """Return whether texture uses the GPU for storage and evaluation"""

    def migrated(self) -> bool:
        """
        Return whether textures with :py:func:`use_accel()` set to ``True`` only store
        the data as a hardware-accelerated CUDA texture.

        If ``False`` then a copy of the array data will additionally be retained .
        """

    @property
    def shape(self) -> tuple:
        """Return the texture shape"""

    @overload
    def eval(self, pos: Array2f, active: bool | None = Bool(True)) -> list[float]:
        """Evaluate the linear interpolant represented by this texture."""

    @overload
    def eval(self, pos: Array2f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval(self, pos: Array2f64, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_fetch(self, pos: Array2f, active: bool | None = Bool(True)) -> list[list[float]]:
        """
        Fetch the texels that would be referenced in a texture lookup with
        linear interpolation without actually performing this interpolation.
        """

    @overload
    def eval_fetch(self, pos: Array2f16, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_fetch(self, pos: Array2f64, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_cubic(self, pos: Array2f, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]:
        """
        Evaluate a clamped cubic B-Spline interpolant represented by this
        texture

        Instead of interpolating the texture via B-Spline basis functions, the
        implementation transforms this calculation into an equivalent weighted
        sum of several linear interpolant evaluations. In CUDA mode, this can
        then be accelerated by hardware texture units, which runs faster than
        a naive implementation. More information can be found in:

            GPU Gems 2, Chapter 20, "Fast Third-Order Texture Filtering"
            by Christian Sigg.

        When the underlying grid data and the query position are differentiable,
        this transformation cannot be used as it is not linear with respect to position
        (thus the default AD graph gives incorrect results). The implementation
        calls :py:func:`eval_cubic_helper()` function to replace the AD graph with a
        direct evaluation of the B-Spline basis functions in that case.
        """

    @overload
    def eval_cubic(self, pos: Array2f16, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic(self, pos: Array2f64, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic_grad(self, pos: Array2f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_grad(self, pos: Array2f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_grad(self, pos: Array2f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array2f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient and hessian matrix of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_hessian(self, pos: Array2f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array2f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_helper(self, pos: Array2f, active: bool | None = Bool(True)) -> list[float]:
        """
        Helper function to evaluate a clamped cubic B-Spline interpolant

        This is an implementation detail and should only be called by the
        :py:func:`eval_cubic()` function to construct an AD graph. When only the cubic
        evaluation result is desired, the :py:func:`eval_cubic()` function is faster
        than this simple implementation
        """

    @overload
    def eval_cubic_helper(self, pos: Array2f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_cubic_helper(self, pos: Array2f64, active: bool | None = Bool(True)) -> list[float]: ...

    IsTexture: bool = True

class Texture3f16:
    @overload
    def __init__(self, shape: Sequence[int], channels: int, use_accel: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Create a new texture with the specified size and channel count

        On CUDA, this is a slow operation that synchronizes the GPU pipeline, so
        texture objects should be reused/updated via :py:func:`set_value()` and
        :py:func:`set_tensor()` as much as possible.

        When ``use_accel`` is set to ``False`` on CUDA mode, the texture will not
        use hardware acceleration (allocation and evaluation). In other modes
        this argument has no effect.

        The ``filter_mode`` parameter defines the interpolation method to be used
        in all evaluation routines. By default, the texture is linearly
        interpolated. Besides nearest/linear filtering, the implementation also
        provides a clamped cubic B-spline interpolation scheme in case a
        higher-order interpolation is needed. In CUDA mode, this is done using a
        series of linear lookups to optimally use the hardware (hence, linear
        filtering must be enabled to use this feature).

        When evaluating the texture outside of its boundaries, the ``wrap_mode``
        defines the wrapping method. The default behavior is ``drjit.WrapMode.Clamp``,
        which indefinitely extends the colors on the boundary along each dimension.
        """

    @overload
    def __init__(self, tensor: TensorXf16, use_accel: bool = True, migrate: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Construct a new texture from a given tensor.

        This constructor allocates texture memory with the shape information
        deduced from ``tensor``. It subsequently invokes :py:func:`set_tensor(tensor)`
        to fill the texture memory with the provided tensor.

        When both ``migrate`` and ``use_accel`` are set to ``True`` in CUDA mode, the texture
        exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage. Note that the texture is still differentiable even when migrated.
        """

    def set_value(self, value: ArrayXf16, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided linearized 1D array.

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def set_tensor(self, tensor: TensorXf16, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided tensor.

        This method updates the values of all texels. Changing the texture
        resolution or its number of channels is also supported. However, on CUDA,
        such operations have a significantly larger overhead (the GPU pipeline
        needs to be synchronized for new texture objects to be created).

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def update_inplace(self, migrate: bool = False) -> None:
        """
        Update the texture after applying an indirect update to its tensor
        representation (obtained with py:func:`tensor()`).

        A tensor representation of this texture object can be retrived with
        py:func:`tensor()`. That representation can be modified, but in order to apply
        it succesfuly to the texture, this method must also be called. In short,
        this method will use the tensor representation to update the texture's
        internal state.

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.)
        """

    def value(self) -> ArrayXf16:
        """Return the texture data as an array object"""

    def tensor(self) -> TensorXf16:
        """Return the texture data as a tensor object"""

    def filter_mode(self) -> drjit.FilterMode:
        """Return the filter mode"""

    def wrap_mode(self) -> drjit.WrapMode:
        """Return the wrap mode"""

    def use_accel(self) -> bool:
        """Return whether texture uses the GPU for storage and evaluation"""

    def migrated(self) -> bool:
        """
        Return whether textures with :py:func:`use_accel()` set to ``True`` only store
        the data as a hardware-accelerated CUDA texture.

        If ``False`` then a copy of the array data will additionally be retained .
        """

    @property
    def shape(self) -> tuple:
        """Return the texture shape"""

    @overload
    def eval(self, pos: Array3f, active: bool | None = Bool(True)) -> list[float]:
        """Evaluate the linear interpolant represented by this texture."""

    @overload
    def eval(self, pos: Array3f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval(self, pos: Array3f64, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_fetch(self, pos: Array3f, active: bool | None = Bool(True)) -> list[list[float]]:
        """
        Fetch the texels that would be referenced in a texture lookup with
        linear interpolation without actually performing this interpolation.
        """

    @overload
    def eval_fetch(self, pos: Array3f16, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_fetch(self, pos: Array3f64, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_cubic(self, pos: Array3f, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]:
        """
        Evaluate a clamped cubic B-Spline interpolant represented by this
        texture

        Instead of interpolating the texture via B-Spline basis functions, the
        implementation transforms this calculation into an equivalent weighted
        sum of several linear interpolant evaluations. In CUDA mode, this can
        then be accelerated by hardware texture units, which runs faster than
        a naive implementation. More information can be found in:

            GPU Gems 2, Chapter 20, "Fast Third-Order Texture Filtering"
            by Christian Sigg.

        When the underlying grid data and the query position are differentiable,
        this transformation cannot be used as it is not linear with respect to position
        (thus the default AD graph gives incorrect results). The implementation
        calls :py:func:`eval_cubic_helper()` function to replace the AD graph with a
        direct evaluation of the B-Spline basis functions in that case.
        """

    @overload
    def eval_cubic(self, pos: Array3f16, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic(self, pos: Array3f64, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic_grad(self, pos: Array3f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_grad(self, pos: Array3f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_grad(self, pos: Array3f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array3f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient and hessian matrix of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_hessian(self, pos: Array3f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array3f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_helper(self, pos: Array3f, active: bool | None = Bool(True)) -> list[float]:
        """
        Helper function to evaluate a clamped cubic B-Spline interpolant

        This is an implementation detail and should only be called by the
        :py:func:`eval_cubic()` function to construct an AD graph. When only the cubic
        evaluation result is desired, the :py:func:`eval_cubic()` function is faster
        than this simple implementation
        """

    @overload
    def eval_cubic_helper(self, pos: Array3f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_cubic_helper(self, pos: Array3f64, active: bool | None = Bool(True)) -> list[float]: ...

    IsTexture: bool = True

class Texture1f:
    @overload
    def __init__(self, shape: Sequence[int], channels: int, use_accel: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Create a new texture with the specified size and channel count

        On CUDA, this is a slow operation that synchronizes the GPU pipeline, so
        texture objects should be reused/updated via :py:func:`set_value()` and
        :py:func:`set_tensor()` as much as possible.

        When ``use_accel`` is set to ``False`` on CUDA mode, the texture will not
        use hardware acceleration (allocation and evaluation). In other modes
        this argument has no effect.

        The ``filter_mode`` parameter defines the interpolation method to be used
        in all evaluation routines. By default, the texture is linearly
        interpolated. Besides nearest/linear filtering, the implementation also
        provides a clamped cubic B-spline interpolation scheme in case a
        higher-order interpolation is needed. In CUDA mode, this is done using a
        series of linear lookups to optimally use the hardware (hence, linear
        filtering must be enabled to use this feature).

        When evaluating the texture outside of its boundaries, the ``wrap_mode``
        defines the wrapping method. The default behavior is ``drjit.WrapMode.Clamp``,
        which indefinitely extends the colors on the boundary along each dimension.
        """

    @overload
    def __init__(self, tensor: TensorXf, use_accel: bool = True, migrate: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Construct a new texture from a given tensor.

        This constructor allocates texture memory with the shape information
        deduced from ``tensor``. It subsequently invokes :py:func:`set_tensor(tensor)`
        to fill the texture memory with the provided tensor.

        When both ``migrate`` and ``use_accel`` are set to ``True`` in CUDA mode, the texture
        exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage. Note that the texture is still differentiable even when migrated.
        """

    def set_value(self, value: ArrayXf, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided linearized 1D array.

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def set_tensor(self, tensor: TensorXf, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided tensor.

        This method updates the values of all texels. Changing the texture
        resolution or its number of channels is also supported. However, on CUDA,
        such operations have a significantly larger overhead (the GPU pipeline
        needs to be synchronized for new texture objects to be created).

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def update_inplace(self, migrate: bool = False) -> None:
        """
        Update the texture after applying an indirect update to its tensor
        representation (obtained with py:func:`tensor()`).

        A tensor representation of this texture object can be retrived with
        py:func:`tensor()`. That representation can be modified, but in order to apply
        it succesfuly to the texture, this method must also be called. In short,
        this method will use the tensor representation to update the texture's
        internal state.

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.)
        """

    def value(self) -> ArrayXf:
        """Return the texture data as an array object"""

    def tensor(self) -> TensorXf:
        """Return the texture data as a tensor object"""

    def filter_mode(self) -> drjit.FilterMode:
        """Return the filter mode"""

    def wrap_mode(self) -> drjit.WrapMode:
        """Return the wrap mode"""

    def use_accel(self) -> bool:
        """Return whether texture uses the GPU for storage and evaluation"""

    def migrated(self) -> bool:
        """
        Return whether textures with :py:func:`use_accel()` set to ``True`` only store
        the data as a hardware-accelerated CUDA texture.

        If ``False`` then a copy of the array data will additionally be retained .
        """

    @property
    def shape(self) -> tuple:
        """Return the texture shape"""

    @overload
    def eval(self, pos: Array1f, active: bool | None = Bool(True)) -> list[float]:
        """Evaluate the linear interpolant represented by this texture."""

    @overload
    def eval(self, pos: Array1f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval(self, pos: Array1f64, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_fetch(self, pos: Array1f, active: bool | None = Bool(True)) -> list[list[float]]:
        """
        Fetch the texels that would be referenced in a texture lookup with
        linear interpolation without actually performing this interpolation.
        """

    @overload
    def eval_fetch(self, pos: Array1f16, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_fetch(self, pos: Array1f64, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_cubic(self, pos: Array1f, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]:
        """
        Evaluate a clamped cubic B-Spline interpolant represented by this
        texture

        Instead of interpolating the texture via B-Spline basis functions, the
        implementation transforms this calculation into an equivalent weighted
        sum of several linear interpolant evaluations. In CUDA mode, this can
        then be accelerated by hardware texture units, which runs faster than
        a naive implementation. More information can be found in:

            GPU Gems 2, Chapter 20, "Fast Third-Order Texture Filtering"
            by Christian Sigg.

        When the underlying grid data and the query position are differentiable,
        this transformation cannot be used as it is not linear with respect to position
        (thus the default AD graph gives incorrect results). The implementation
        calls :py:func:`eval_cubic_helper()` function to replace the AD graph with a
        direct evaluation of the B-Spline basis functions in that case.
        """

    @overload
    def eval_cubic(self, pos: Array1f16, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic(self, pos: Array1f64, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic_grad(self, pos: Array1f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_grad(self, pos: Array1f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_grad(self, pos: Array1f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array1f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient and hessian matrix of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_hessian(self, pos: Array1f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array1f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_helper(self, pos: Array1f, active: bool | None = Bool(True)) -> list[float]:
        """
        Helper function to evaluate a clamped cubic B-Spline interpolant

        This is an implementation detail and should only be called by the
        :py:func:`eval_cubic()` function to construct an AD graph. When only the cubic
        evaluation result is desired, the :py:func:`eval_cubic()` function is faster
        than this simple implementation
        """

    @overload
    def eval_cubic_helper(self, pos: Array1f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_cubic_helper(self, pos: Array1f64, active: bool | None = Bool(True)) -> list[float]: ...

    IsTexture: bool = True

class Texture2f:
    @overload
    def __init__(self, shape: Sequence[int], channels: int, use_accel: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Create a new texture with the specified size and channel count

        On CUDA, this is a slow operation that synchronizes the GPU pipeline, so
        texture objects should be reused/updated via :py:func:`set_value()` and
        :py:func:`set_tensor()` as much as possible.

        When ``use_accel`` is set to ``False`` on CUDA mode, the texture will not
        use hardware acceleration (allocation and evaluation). In other modes
        this argument has no effect.

        The ``filter_mode`` parameter defines the interpolation method to be used
        in all evaluation routines. By default, the texture is linearly
        interpolated. Besides nearest/linear filtering, the implementation also
        provides a clamped cubic B-spline interpolation scheme in case a
        higher-order interpolation is needed. In CUDA mode, this is done using a
        series of linear lookups to optimally use the hardware (hence, linear
        filtering must be enabled to use this feature).

        When evaluating the texture outside of its boundaries, the ``wrap_mode``
        defines the wrapping method. The default behavior is ``drjit.WrapMode.Clamp``,
        which indefinitely extends the colors on the boundary along each dimension.
        """

    @overload
    def __init__(self, tensor: TensorXf, use_accel: bool = True, migrate: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Construct a new texture from a given tensor.

        This constructor allocates texture memory with the shape information
        deduced from ``tensor``. It subsequently invokes :py:func:`set_tensor(tensor)`
        to fill the texture memory with the provided tensor.

        When both ``migrate`` and ``use_accel`` are set to ``True`` in CUDA mode, the texture
        exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage. Note that the texture is still differentiable even when migrated.
        """

    def set_value(self, value: ArrayXf, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided linearized 1D array.

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def set_tensor(self, tensor: TensorXf, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided tensor.

        This method updates the values of all texels. Changing the texture
        resolution or its number of channels is also supported. However, on CUDA,
        such operations have a significantly larger overhead (the GPU pipeline
        needs to be synchronized for new texture objects to be created).

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def update_inplace(self, migrate: bool = False) -> None:
        """
        Update the texture after applying an indirect update to its tensor
        representation (obtained with py:func:`tensor()`).

        A tensor representation of this texture object can be retrived with
        py:func:`tensor()`. That representation can be modified, but in order to apply
        it succesfuly to the texture, this method must also be called. In short,
        this method will use the tensor representation to update the texture's
        internal state.

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.)
        """

    def value(self) -> ArrayXf:
        """Return the texture data as an array object"""

    def tensor(self) -> TensorXf:
        """Return the texture data as a tensor object"""

    def filter_mode(self) -> drjit.FilterMode:
        """Return the filter mode"""

    def wrap_mode(self) -> drjit.WrapMode:
        """Return the wrap mode"""

    def use_accel(self) -> bool:
        """Return whether texture uses the GPU for storage and evaluation"""

    def migrated(self) -> bool:
        """
        Return whether textures with :py:func:`use_accel()` set to ``True`` only store
        the data as a hardware-accelerated CUDA texture.

        If ``False`` then a copy of the array data will additionally be retained .
        """

    @property
    def shape(self) -> tuple:
        """Return the texture shape"""

    @overload
    def eval(self, pos: Array2f, active: bool | None = Bool(True)) -> list[float]:
        """Evaluate the linear interpolant represented by this texture."""

    @overload
    def eval(self, pos: Array2f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval(self, pos: Array2f64, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_fetch(self, pos: Array2f, active: bool | None = Bool(True)) -> list[list[float]]:
        """
        Fetch the texels that would be referenced in a texture lookup with
        linear interpolation without actually performing this interpolation.
        """

    @overload
    def eval_fetch(self, pos: Array2f16, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_fetch(self, pos: Array2f64, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_cubic(self, pos: Array2f, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]:
        """
        Evaluate a clamped cubic B-Spline interpolant represented by this
        texture

        Instead of interpolating the texture via B-Spline basis functions, the
        implementation transforms this calculation into an equivalent weighted
        sum of several linear interpolant evaluations. In CUDA mode, this can
        then be accelerated by hardware texture units, which runs faster than
        a naive implementation. More information can be found in:

            GPU Gems 2, Chapter 20, "Fast Third-Order Texture Filtering"
            by Christian Sigg.

        When the underlying grid data and the query position are differentiable,
        this transformation cannot be used as it is not linear with respect to position
        (thus the default AD graph gives incorrect results). The implementation
        calls :py:func:`eval_cubic_helper()` function to replace the AD graph with a
        direct evaluation of the B-Spline basis functions in that case.
        """

    @overload
    def eval_cubic(self, pos: Array2f16, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic(self, pos: Array2f64, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic_grad(self, pos: Array2f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_grad(self, pos: Array2f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_grad(self, pos: Array2f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array2f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient and hessian matrix of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_hessian(self, pos: Array2f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array2f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_helper(self, pos: Array2f, active: bool | None = Bool(True)) -> list[float]:
        """
        Helper function to evaluate a clamped cubic B-Spline interpolant

        This is an implementation detail and should only be called by the
        :py:func:`eval_cubic()` function to construct an AD graph. When only the cubic
        evaluation result is desired, the :py:func:`eval_cubic()` function is faster
        than this simple implementation
        """

    @overload
    def eval_cubic_helper(self, pos: Array2f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_cubic_helper(self, pos: Array2f64, active: bool | None = Bool(True)) -> list[float]: ...

    IsTexture: bool = True

class Texture3f:
    @overload
    def __init__(self, shape: Sequence[int], channels: int, use_accel: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Create a new texture with the specified size and channel count

        On CUDA, this is a slow operation that synchronizes the GPU pipeline, so
        texture objects should be reused/updated via :py:func:`set_value()` and
        :py:func:`set_tensor()` as much as possible.

        When ``use_accel`` is set to ``False`` on CUDA mode, the texture will not
        use hardware acceleration (allocation and evaluation). In other modes
        this argument has no effect.

        The ``filter_mode`` parameter defines the interpolation method to be used
        in all evaluation routines. By default, the texture is linearly
        interpolated. Besides nearest/linear filtering, the implementation also
        provides a clamped cubic B-spline interpolation scheme in case a
        higher-order interpolation is needed. In CUDA mode, this is done using a
        series of linear lookups to optimally use the hardware (hence, linear
        filtering must be enabled to use this feature).

        When evaluating the texture outside of its boundaries, the ``wrap_mode``
        defines the wrapping method. The default behavior is ``drjit.WrapMode.Clamp``,
        which indefinitely extends the colors on the boundary along each dimension.
        """

    @overload
    def __init__(self, tensor: TensorXf, use_accel: bool = True, migrate: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Construct a new texture from a given tensor.

        This constructor allocates texture memory with the shape information
        deduced from ``tensor``. It subsequently invokes :py:func:`set_tensor(tensor)`
        to fill the texture memory with the provided tensor.

        When both ``migrate`` and ``use_accel`` are set to ``True`` in CUDA mode, the texture
        exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage. Note that the texture is still differentiable even when migrated.
        """

    def set_value(self, value: ArrayXf, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided linearized 1D array.

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def set_tensor(self, tensor: TensorXf, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided tensor.

        This method updates the values of all texels. Changing the texture
        resolution or its number of channels is also supported. However, on CUDA,
        such operations have a significantly larger overhead (the GPU pipeline
        needs to be synchronized for new texture objects to be created).

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def update_inplace(self, migrate: bool = False) -> None:
        """
        Update the texture after applying an indirect update to its tensor
        representation (obtained with py:func:`tensor()`).

        A tensor representation of this texture object can be retrived with
        py:func:`tensor()`. That representation can be modified, but in order to apply
        it succesfuly to the texture, this method must also be called. In short,
        this method will use the tensor representation to update the texture's
        internal state.

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.)
        """

    def value(self) -> ArrayXf:
        """Return the texture data as an array object"""

    def tensor(self) -> TensorXf:
        """Return the texture data as a tensor object"""

    def filter_mode(self) -> drjit.FilterMode:
        """Return the filter mode"""

    def wrap_mode(self) -> drjit.WrapMode:
        """Return the wrap mode"""

    def use_accel(self) -> bool:
        """Return whether texture uses the GPU for storage and evaluation"""

    def migrated(self) -> bool:
        """
        Return whether textures with :py:func:`use_accel()` set to ``True`` only store
        the data as a hardware-accelerated CUDA texture.

        If ``False`` then a copy of the array data will additionally be retained .
        """

    @property
    def shape(self) -> tuple:
        """Return the texture shape"""

    @overload
    def eval(self, pos: Array3f, active: bool | None = Bool(True)) -> list[float]:
        """Evaluate the linear interpolant represented by this texture."""

    @overload
    def eval(self, pos: Array3f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval(self, pos: Array3f64, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_fetch(self, pos: Array3f, active: bool | None = Bool(True)) -> list[list[float]]:
        """
        Fetch the texels that would be referenced in a texture lookup with
        linear interpolation without actually performing this interpolation.
        """

    @overload
    def eval_fetch(self, pos: Array3f16, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_fetch(self, pos: Array3f64, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_cubic(self, pos: Array3f, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]:
        """
        Evaluate a clamped cubic B-Spline interpolant represented by this
        texture

        Instead of interpolating the texture via B-Spline basis functions, the
        implementation transforms this calculation into an equivalent weighted
        sum of several linear interpolant evaluations. In CUDA mode, this can
        then be accelerated by hardware texture units, which runs faster than
        a naive implementation. More information can be found in:

            GPU Gems 2, Chapter 20, "Fast Third-Order Texture Filtering"
            by Christian Sigg.

        When the underlying grid data and the query position are differentiable,
        this transformation cannot be used as it is not linear with respect to position
        (thus the default AD graph gives incorrect results). The implementation
        calls :py:func:`eval_cubic_helper()` function to replace the AD graph with a
        direct evaluation of the B-Spline basis functions in that case.
        """

    @overload
    def eval_cubic(self, pos: Array3f16, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic(self, pos: Array3f64, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic_grad(self, pos: Array3f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_grad(self, pos: Array3f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_grad(self, pos: Array3f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array3f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient and hessian matrix of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_hessian(self, pos: Array3f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array3f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_helper(self, pos: Array3f, active: bool | None = Bool(True)) -> list[float]:
        """
        Helper function to evaluate a clamped cubic B-Spline interpolant

        This is an implementation detail and should only be called by the
        :py:func:`eval_cubic()` function to construct an AD graph. When only the cubic
        evaluation result is desired, the :py:func:`eval_cubic()` function is faster
        than this simple implementation
        """

    @overload
    def eval_cubic_helper(self, pos: Array3f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_cubic_helper(self, pos: Array3f64, active: bool | None = Bool(True)) -> list[float]: ...

    IsTexture: bool = True

class Texture1f64:
    @overload
    def __init__(self, shape: Sequence[int], channels: int, use_accel: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Create a new texture with the specified size and channel count

        On CUDA, this is a slow operation that synchronizes the GPU pipeline, so
        texture objects should be reused/updated via :py:func:`set_value()` and
        :py:func:`set_tensor()` as much as possible.

        When ``use_accel`` is set to ``False`` on CUDA mode, the texture will not
        use hardware acceleration (allocation and evaluation). In other modes
        this argument has no effect.

        The ``filter_mode`` parameter defines the interpolation method to be used
        in all evaluation routines. By default, the texture is linearly
        interpolated. Besides nearest/linear filtering, the implementation also
        provides a clamped cubic B-spline interpolation scheme in case a
        higher-order interpolation is needed. In CUDA mode, this is done using a
        series of linear lookups to optimally use the hardware (hence, linear
        filtering must be enabled to use this feature).

        When evaluating the texture outside of its boundaries, the ``wrap_mode``
        defines the wrapping method. The default behavior is ``drjit.WrapMode.Clamp``,
        which indefinitely extends the colors on the boundary along each dimension.
        """

    @overload
    def __init__(self, tensor: TensorXf64, use_accel: bool = True, migrate: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Construct a new texture from a given tensor.

        This constructor allocates texture memory with the shape information
        deduced from ``tensor``. It subsequently invokes :py:func:`set_tensor(tensor)`
        to fill the texture memory with the provided tensor.

        When both ``migrate`` and ``use_accel`` are set to ``True`` in CUDA mode, the texture
        exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage. Note that the texture is still differentiable even when migrated.
        """

    def set_value(self, value: ArrayXf64, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided linearized 1D array.

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def set_tensor(self, tensor: TensorXf64, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided tensor.

        This method updates the values of all texels. Changing the texture
        resolution or its number of channels is also supported. However, on CUDA,
        such operations have a significantly larger overhead (the GPU pipeline
        needs to be synchronized for new texture objects to be created).

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def update_inplace(self, migrate: bool = False) -> None:
        """
        Update the texture after applying an indirect update to its tensor
        representation (obtained with py:func:`tensor()`).

        A tensor representation of this texture object can be retrived with
        py:func:`tensor()`. That representation can be modified, but in order to apply
        it succesfuly to the texture, this method must also be called. In short,
        this method will use the tensor representation to update the texture's
        internal state.

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.)
        """

    def value(self) -> ArrayXf64:
        """Return the texture data as an array object"""

    def tensor(self) -> TensorXf64:
        """Return the texture data as a tensor object"""

    def filter_mode(self) -> drjit.FilterMode:
        """Return the filter mode"""

    def wrap_mode(self) -> drjit.WrapMode:
        """Return the wrap mode"""

    def use_accel(self) -> bool:
        """Return whether texture uses the GPU for storage and evaluation"""

    def migrated(self) -> bool:
        """
        Return whether textures with :py:func:`use_accel()` set to ``True`` only store
        the data as a hardware-accelerated CUDA texture.

        If ``False`` then a copy of the array data will additionally be retained .
        """

    @property
    def shape(self) -> tuple:
        """Return the texture shape"""

    @overload
    def eval(self, pos: Array1f, active: bool | None = Bool(True)) -> list[float]:
        """Evaluate the linear interpolant represented by this texture."""

    @overload
    def eval(self, pos: Array1f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval(self, pos: Array1f64, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_fetch(self, pos: Array1f, active: bool | None = Bool(True)) -> list[list[float]]:
        """
        Fetch the texels that would be referenced in a texture lookup with
        linear interpolation without actually performing this interpolation.
        """

    @overload
    def eval_fetch(self, pos: Array1f16, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_fetch(self, pos: Array1f64, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_cubic(self, pos: Array1f, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]:
        """
        Evaluate a clamped cubic B-Spline interpolant represented by this
        texture

        Instead of interpolating the texture via B-Spline basis functions, the
        implementation transforms this calculation into an equivalent weighted
        sum of several linear interpolant evaluations. In CUDA mode, this can
        then be accelerated by hardware texture units, which runs faster than
        a naive implementation. More information can be found in:

            GPU Gems 2, Chapter 20, "Fast Third-Order Texture Filtering"
            by Christian Sigg.

        When the underlying grid data and the query position are differentiable,
        this transformation cannot be used as it is not linear with respect to position
        (thus the default AD graph gives incorrect results). The implementation
        calls :py:func:`eval_cubic_helper()` function to replace the AD graph with a
        direct evaluation of the B-Spline basis functions in that case.
        """

    @overload
    def eval_cubic(self, pos: Array1f16, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic(self, pos: Array1f64, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic_grad(self, pos: Array1f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_grad(self, pos: Array1f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_grad(self, pos: Array1f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array1f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient and hessian matrix of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_hessian(self, pos: Array1f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array1f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_helper(self, pos: Array1f, active: bool | None = Bool(True)) -> list[float]:
        """
        Helper function to evaluate a clamped cubic B-Spline interpolant

        This is an implementation detail and should only be called by the
        :py:func:`eval_cubic()` function to construct an AD graph. When only the cubic
        evaluation result is desired, the :py:func:`eval_cubic()` function is faster
        than this simple implementation
        """

    @overload
    def eval_cubic_helper(self, pos: Array1f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_cubic_helper(self, pos: Array1f64, active: bool | None = Bool(True)) -> list[float]: ...

    IsTexture: bool = True

class Texture2f64:
    @overload
    def __init__(self, shape: Sequence[int], channels: int, use_accel: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Create a new texture with the specified size and channel count

        On CUDA, this is a slow operation that synchronizes the GPU pipeline, so
        texture objects should be reused/updated via :py:func:`set_value()` and
        :py:func:`set_tensor()` as much as possible.

        When ``use_accel`` is set to ``False`` on CUDA mode, the texture will not
        use hardware acceleration (allocation and evaluation). In other modes
        this argument has no effect.

        The ``filter_mode`` parameter defines the interpolation method to be used
        in all evaluation routines. By default, the texture is linearly
        interpolated. Besides nearest/linear filtering, the implementation also
        provides a clamped cubic B-spline interpolation scheme in case a
        higher-order interpolation is needed. In CUDA mode, this is done using a
        series of linear lookups to optimally use the hardware (hence, linear
        filtering must be enabled to use this feature).

        When evaluating the texture outside of its boundaries, the ``wrap_mode``
        defines the wrapping method. The default behavior is ``drjit.WrapMode.Clamp``,
        which indefinitely extends the colors on the boundary along each dimension.
        """

    @overload
    def __init__(self, tensor: TensorXf64, use_accel: bool = True, migrate: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Construct a new texture from a given tensor.

        This constructor allocates texture memory with the shape information
        deduced from ``tensor``. It subsequently invokes :py:func:`set_tensor(tensor)`
        to fill the texture memory with the provided tensor.

        When both ``migrate`` and ``use_accel`` are set to ``True`` in CUDA mode, the texture
        exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage. Note that the texture is still differentiable even when migrated.
        """

    def set_value(self, value: ArrayXf64, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided linearized 1D array.

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def set_tensor(self, tensor: TensorXf64, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided tensor.

        This method updates the values of all texels. Changing the texture
        resolution or its number of channels is also supported. However, on CUDA,
        such operations have a significantly larger overhead (the GPU pipeline
        needs to be synchronized for new texture objects to be created).

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def update_inplace(self, migrate: bool = False) -> None:
        """
        Update the texture after applying an indirect update to its tensor
        representation (obtained with py:func:`tensor()`).

        A tensor representation of this texture object can be retrived with
        py:func:`tensor()`. That representation can be modified, but in order to apply
        it succesfuly to the texture, this method must also be called. In short,
        this method will use the tensor representation to update the texture's
        internal state.

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.)
        """

    def value(self) -> ArrayXf64:
        """Return the texture data as an array object"""

    def tensor(self) -> TensorXf64:
        """Return the texture data as a tensor object"""

    def filter_mode(self) -> drjit.FilterMode:
        """Return the filter mode"""

    def wrap_mode(self) -> drjit.WrapMode:
        """Return the wrap mode"""

    def use_accel(self) -> bool:
        """Return whether texture uses the GPU for storage and evaluation"""

    def migrated(self) -> bool:
        """
        Return whether textures with :py:func:`use_accel()` set to ``True`` only store
        the data as a hardware-accelerated CUDA texture.

        If ``False`` then a copy of the array data will additionally be retained .
        """

    @property
    def shape(self) -> tuple:
        """Return the texture shape"""

    @overload
    def eval(self, pos: Array2f, active: bool | None = Bool(True)) -> list[float]:
        """Evaluate the linear interpolant represented by this texture."""

    @overload
    def eval(self, pos: Array2f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval(self, pos: Array2f64, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_fetch(self, pos: Array2f, active: bool | None = Bool(True)) -> list[list[float]]:
        """
        Fetch the texels that would be referenced in a texture lookup with
        linear interpolation without actually performing this interpolation.
        """

    @overload
    def eval_fetch(self, pos: Array2f16, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_fetch(self, pos: Array2f64, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_cubic(self, pos: Array2f, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]:
        """
        Evaluate a clamped cubic B-Spline interpolant represented by this
        texture

        Instead of interpolating the texture via B-Spline basis functions, the
        implementation transforms this calculation into an equivalent weighted
        sum of several linear interpolant evaluations. In CUDA mode, this can
        then be accelerated by hardware texture units, which runs faster than
        a naive implementation. More information can be found in:

            GPU Gems 2, Chapter 20, "Fast Third-Order Texture Filtering"
            by Christian Sigg.

        When the underlying grid data and the query position are differentiable,
        this transformation cannot be used as it is not linear with respect to position
        (thus the default AD graph gives incorrect results). The implementation
        calls :py:func:`eval_cubic_helper()` function to replace the AD graph with a
        direct evaluation of the B-Spline basis functions in that case.
        """

    @overload
    def eval_cubic(self, pos: Array2f16, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic(self, pos: Array2f64, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic_grad(self, pos: Array2f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_grad(self, pos: Array2f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_grad(self, pos: Array2f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array2f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient and hessian matrix of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_hessian(self, pos: Array2f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array2f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_helper(self, pos: Array2f, active: bool | None = Bool(True)) -> list[float]:
        """
        Helper function to evaluate a clamped cubic B-Spline interpolant

        This is an implementation detail and should only be called by the
        :py:func:`eval_cubic()` function to construct an AD graph. When only the cubic
        evaluation result is desired, the :py:func:`eval_cubic()` function is faster
        than this simple implementation
        """

    @overload
    def eval_cubic_helper(self, pos: Array2f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_cubic_helper(self, pos: Array2f64, active: bool | None = Bool(True)) -> list[float]: ...

    IsTexture: bool = True

class Texture3f64:
    @overload
    def __init__(self, shape: Sequence[int], channels: int, use_accel: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Create a new texture with the specified size and channel count

        On CUDA, this is a slow operation that synchronizes the GPU pipeline, so
        texture objects should be reused/updated via :py:func:`set_value()` and
        :py:func:`set_tensor()` as much as possible.

        When ``use_accel`` is set to ``False`` on CUDA mode, the texture will not
        use hardware acceleration (allocation and evaluation). In other modes
        this argument has no effect.

        The ``filter_mode`` parameter defines the interpolation method to be used
        in all evaluation routines. By default, the texture is linearly
        interpolated. Besides nearest/linear filtering, the implementation also
        provides a clamped cubic B-spline interpolation scheme in case a
        higher-order interpolation is needed. In CUDA mode, this is done using a
        series of linear lookups to optimally use the hardware (hence, linear
        filtering must be enabled to use this feature).

        When evaluating the texture outside of its boundaries, the ``wrap_mode``
        defines the wrapping method. The default behavior is ``drjit.WrapMode.Clamp``,
        which indefinitely extends the colors on the boundary along each dimension.
        """

    @overload
    def __init__(self, tensor: TensorXf64, use_accel: bool = True, migrate: bool = True, filter_mode: drjit.FilterMode = drjit.FilterMode.Linear, wrap_mode: drjit.WrapMode = drjit.WrapMode.Clamp) -> None:
        """
        Construct a new texture from a given tensor.

        This constructor allocates texture memory with the shape information
        deduced from ``tensor``. It subsequently invokes :py:func:`set_tensor(tensor)`
        to fill the texture memory with the provided tensor.

        When both ``migrate`` and ``use_accel`` are set to ``True`` in CUDA mode, the texture
        exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage. Note that the texture is still differentiable even when migrated.
        """

    def set_value(self, value: ArrayXf64, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided linearized 1D array.

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def set_tensor(self, tensor: TensorXf64, migrate: bool = False) -> None:
        """
        Override the texture contents with the provided tensor.

        This method updates the values of all texels. Changing the texture
        resolution or its number of channels is also supported. However, on CUDA,
        such operations have a significantly larger overhead (the GPU pipeline
        needs to be synchronized for new texture objects to be created).

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.Note that the texture is still differentiable even when migrated.
        """

    def update_inplace(self, migrate: bool = False) -> None:
        """
        Update the texture after applying an indirect update to its tensor
        representation (obtained with py:func:`tensor()`).

        A tensor representation of this texture object can be retrived with
        py:func:`tensor()`. That representation can be modified, but in order to apply
        it succesfuly to the texture, this method must also be called. In short,
        this method will use the tensor representation to update the texture's
        internal state.

        In CUDA mode, when both the argument ``migrate`` and :py:func:`use_accel()` are ``True``,
        the texture exclusively stores a copy of the input data as a CUDA texture to avoid
        redundant storage.)
        """

    def value(self) -> ArrayXf64:
        """Return the texture data as an array object"""

    def tensor(self) -> TensorXf64:
        """Return the texture data as a tensor object"""

    def filter_mode(self) -> drjit.FilterMode:
        """Return the filter mode"""

    def wrap_mode(self) -> drjit.WrapMode:
        """Return the wrap mode"""

    def use_accel(self) -> bool:
        """Return whether texture uses the GPU for storage and evaluation"""

    def migrated(self) -> bool:
        """
        Return whether textures with :py:func:`use_accel()` set to ``True`` only store
        the data as a hardware-accelerated CUDA texture.

        If ``False`` then a copy of the array data will additionally be retained .
        """

    @property
    def shape(self) -> tuple:
        """Return the texture shape"""

    @overload
    def eval(self, pos: Array3f, active: bool | None = Bool(True)) -> list[float]:
        """Evaluate the linear interpolant represented by this texture."""

    @overload
    def eval(self, pos: Array3f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval(self, pos: Array3f64, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_fetch(self, pos: Array3f, active: bool | None = Bool(True)) -> list[list[float]]:
        """
        Fetch the texels that would be referenced in a texture lookup with
        linear interpolation without actually performing this interpolation.
        """

    @overload
    def eval_fetch(self, pos: Array3f16, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_fetch(self, pos: Array3f64, active: bool | None = Bool(True)) -> list[list[float]]: ...

    @overload
    def eval_cubic(self, pos: Array3f, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]:
        """
        Evaluate a clamped cubic B-Spline interpolant represented by this
        texture

        Instead of interpolating the texture via B-Spline basis functions, the
        implementation transforms this calculation into an equivalent weighted
        sum of several linear interpolant evaluations. In CUDA mode, this can
        then be accelerated by hardware texture units, which runs faster than
        a naive implementation. More information can be found in:

            GPU Gems 2, Chapter 20, "Fast Third-Order Texture Filtering"
            by Christian Sigg.

        When the underlying grid data and the query position are differentiable,
        this transformation cannot be used as it is not linear with respect to position
        (thus the default AD graph gives incorrect results). The implementation
        calls :py:func:`eval_cubic_helper()` function to replace the AD graph with a
        direct evaluation of the B-Spline basis functions in that case.
        """

    @overload
    def eval_cubic(self, pos: Array3f16, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic(self, pos: Array3f64, active: bool | None = Bool(True), force_nonaccel: bool = False) -> list[float]: ...

    @overload
    def eval_cubic_grad(self, pos: Array3f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_grad(self, pos: Array3f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_grad(self, pos: Array3f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array3f, active: bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient and hessian matrix of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_hessian(self, pos: Array3f16, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array3f64, active: bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_helper(self, pos: Array3f, active: bool | None = Bool(True)) -> list[float]:
        """
        Helper function to evaluate a clamped cubic B-Spline interpolant

        This is an implementation detail and should only be called by the
        :py:func:`eval_cubic()` function to construct an AD graph. When only the cubic
        evaluation result is desired, the :py:func:`eval_cubic()` function is faster
        than this simple implementation
        """

    @overload
    def eval_cubic_helper(self, pos: Array3f16, active: bool | None = Bool(True)) -> list[float]: ...

    @overload
    def eval_cubic_helper(self, pos: Array3f64, active: bool | None = Bool(True)) -> list[float]: ...

    IsTexture: bool = True
