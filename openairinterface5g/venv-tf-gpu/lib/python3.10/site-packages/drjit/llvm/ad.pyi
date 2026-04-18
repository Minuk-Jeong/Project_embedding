from collections.abc import Sequence
from typing import TypeAlias, Union, overload

import drjit
import drjit.llvm
from drjit.llvm import Event as Event
import drjit.scalar


_BoolCp: TypeAlias = Union['Bool', bool, 'drjit.llvm._BoolCp']

class Bool(drjit.ArrayBase[Bool, _BoolCp, bool, bool, Bool, Bool, Bool]):
    pass

_Int8Cp: TypeAlias = Union['Int8', int, 'drjit.llvm._Int8Cp']

class Int8(drjit.ArrayBase[Int8, _Int8Cp, int, int, Int8, Int8, Bool]):
    pass

_UInt8Cp: TypeAlias = Union['UInt8', int, 'drjit.llvm._UInt8Cp']

class UInt8(drjit.ArrayBase[UInt8, _UInt8Cp, int, int, UInt8, UInt8, Bool]):
    pass

_IntCp: TypeAlias = Union['Int', int, 'drjit.llvm._IntCp', '_BoolCp']

class Int(drjit.ArrayBase[Int, _IntCp, int, int, Int, Int, Bool]):
    pass

_UIntCp: TypeAlias = Union['UInt', int, 'drjit.llvm._UIntCp', '_IntCp']

class UInt(drjit.ArrayBase[UInt, _UIntCp, int, int, UInt, UInt, Bool]):
    pass

_Int64Cp: TypeAlias = Union['Int64', int, 'drjit.llvm._Int64Cp', '_UIntCp']

class Int64(drjit.ArrayBase[Int64, _Int64Cp, int, int, Int64, Int64, Bool]):
    pass

_UInt64Cp: TypeAlias = Union['UInt64', int, 'drjit.llvm._UInt64Cp', '_Int64Cp']

class UInt64(drjit.ArrayBase[UInt64, _UInt64Cp, int, int, UInt64, UInt64, Bool]):
    pass

_Float16Cp: TypeAlias = Union['Float16', float, 'drjit.llvm._Float16Cp', '_UInt64Cp']

class Float16(drjit.ArrayBase[Float16, _Float16Cp, float, float, Float16, Float16, Bool]):
    pass

_FloatCp: TypeAlias = Union['Float', float, 'drjit.llvm._FloatCp', '_Float16Cp']

class Float(drjit.ArrayBase[Float, _FloatCp, float, float, Float, Float, Bool]):
    pass

_Float64Cp: TypeAlias = Union['Float64', float, 'drjit.llvm._Float64Cp', '_FloatCp']

class Float64(drjit.ArrayBase[Float64, _Float64Cp, float, float, Float64, Float64, Bool]):
    pass

_Array0bCp: TypeAlias = Union['Array0b', '_BoolCp', 'drjit.scalar._Array0bCp', 'drjit.llvm._Array0bCp']

class Array0b(drjit.ArrayBase[Array0b, _Array0bCp, Bool, _BoolCp, Bool, Array0b, Array0b]):
    xx: Array2b
    xy: Array2b
    xz: Array2b
    xw: Array2b
    yx: Array2b
    yy: Array2b
    yz: Array2b
    yw: Array2b
    zx: Array2b
    zy: Array2b
    zz: Array2b
    zw: Array2b
    wx: Array2b
    wy: Array2b
    wz: Array2b
    ww: Array2b
    xxx: Array3b
    xxy: Array3b
    xxz: Array3b
    xxw: Array3b
    xyx: Array3b
    xyy: Array3b
    xyz: Array3b
    xyw: Array3b
    xzx: Array3b
    xzy: Array3b
    xzz: Array3b
    xzw: Array3b
    xwx: Array3b
    xwy: Array3b
    xwz: Array3b
    xww: Array3b
    yxx: Array3b
    yxy: Array3b
    yxz: Array3b
    yxw: Array3b
    yyx: Array3b
    yyy: Array3b
    yyz: Array3b
    yyw: Array3b
    yzx: Array3b
    yzy: Array3b
    yzz: Array3b
    yzw: Array3b
    ywx: Array3b
    ywy: Array3b
    ywz: Array3b
    yww: Array3b
    zxx: Array3b
    zxy: Array3b
    zxz: Array3b
    zxw: Array3b
    zyx: Array3b
    zyy: Array3b
    zyz: Array3b
    zyw: Array3b
    zzx: Array3b
    zzy: Array3b
    zzz: Array3b
    zzw: Array3b
    zwx: Array3b
    zwy: Array3b
    zwz: Array3b
    zww: Array3b
    wxx: Array3b
    wxy: Array3b
    wxz: Array3b
    wxw: Array3b
    wyx: Array3b
    wyy: Array3b
    wyz: Array3b
    wyw: Array3b
    wzx: Array3b
    wzy: Array3b
    wzz: Array3b
    wzw: Array3b
    wwx: Array3b
    wwy: Array3b
    wwz: Array3b
    www: Array3b
    xxxx: Array4b
    xxxy: Array4b
    xxxz: Array4b
    xxxw: Array4b
    xxyx: Array4b
    xxyy: Array4b
    xxyz: Array4b
    xxyw: Array4b
    xxzx: Array4b
    xxzy: Array4b
    xxzz: Array4b
    xxzw: Array4b
    xxwx: Array4b
    xxwy: Array4b
    xxwz: Array4b
    xxww: Array4b
    xyxx: Array4b
    xyxy: Array4b
    xyxz: Array4b
    xyxw: Array4b
    xyyx: Array4b
    xyyy: Array4b
    xyyz: Array4b
    xyyw: Array4b
    xyzx: Array4b
    xyzy: Array4b
    xyzz: Array4b
    xyzw: Array4b
    xywx: Array4b
    xywy: Array4b
    xywz: Array4b
    xyww: Array4b
    xzxx: Array4b
    xzxy: Array4b
    xzxz: Array4b
    xzxw: Array4b
    xzyx: Array4b
    xzyy: Array4b
    xzyz: Array4b
    xzyw: Array4b
    xzzx: Array4b
    xzzy: Array4b
    xzzz: Array4b
    xzzw: Array4b
    xzwx: Array4b
    xzwy: Array4b
    xzwz: Array4b
    xzww: Array4b
    xwxx: Array4b
    xwxy: Array4b
    xwxz: Array4b
    xwxw: Array4b
    xwyx: Array4b
    xwyy: Array4b
    xwyz: Array4b
    xwyw: Array4b
    xwzx: Array4b
    xwzy: Array4b
    xwzz: Array4b
    xwzw: Array4b
    xwwx: Array4b
    xwwy: Array4b
    xwwz: Array4b
    xwww: Array4b
    yxxx: Array4b
    yxxy: Array4b
    yxxz: Array4b
    yxxw: Array4b
    yxyx: Array4b
    yxyy: Array4b
    yxyz: Array4b
    yxyw: Array4b
    yxzx: Array4b
    yxzy: Array4b
    yxzz: Array4b
    yxzw: Array4b
    yxwx: Array4b
    yxwy: Array4b
    yxwz: Array4b
    yxww: Array4b
    yyxx: Array4b
    yyxy: Array4b
    yyxz: Array4b
    yyxw: Array4b
    yyyx: Array4b
    yyyy: Array4b
    yyyz: Array4b
    yyyw: Array4b
    yyzx: Array4b
    yyzy: Array4b
    yyzz: Array4b
    yyzw: Array4b
    yywx: Array4b
    yywy: Array4b
    yywz: Array4b
    yyww: Array4b
    yzxx: Array4b
    yzxy: Array4b
    yzxz: Array4b
    yzxw: Array4b
    yzyx: Array4b
    yzyy: Array4b
    yzyz: Array4b
    yzyw: Array4b
    yzzx: Array4b
    yzzy: Array4b
    yzzz: Array4b
    yzzw: Array4b
    yzwx: Array4b
    yzwy: Array4b
    yzwz: Array4b
    yzww: Array4b
    ywxx: Array4b
    ywxy: Array4b
    ywxz: Array4b
    ywxw: Array4b
    ywyx: Array4b
    ywyy: Array4b
    ywyz: Array4b
    ywyw: Array4b
    ywzx: Array4b
    ywzy: Array4b
    ywzz: Array4b
    ywzw: Array4b
    ywwx: Array4b
    ywwy: Array4b
    ywwz: Array4b
    ywww: Array4b
    zxxx: Array4b
    zxxy: Array4b
    zxxz: Array4b
    zxxw: Array4b
    zxyx: Array4b
    zxyy: Array4b
    zxyz: Array4b
    zxyw: Array4b
    zxzx: Array4b
    zxzy: Array4b
    zxzz: Array4b
    zxzw: Array4b
    zxwx: Array4b
    zxwy: Array4b
    zxwz: Array4b
    zxww: Array4b
    zyxx: Array4b
    zyxy: Array4b
    zyxz: Array4b
    zyxw: Array4b
    zyyx: Array4b
    zyyy: Array4b
    zyyz: Array4b
    zyyw: Array4b
    zyzx: Array4b
    zyzy: Array4b
    zyzz: Array4b
    zyzw: Array4b
    zywx: Array4b
    zywy: Array4b
    zywz: Array4b
    zyww: Array4b
    zzxx: Array4b
    zzxy: Array4b
    zzxz: Array4b
    zzxw: Array4b
    zzyx: Array4b
    zzyy: Array4b
    zzyz: Array4b
    zzyw: Array4b
    zzzx: Array4b
    zzzy: Array4b
    zzzz: Array4b
    zzzw: Array4b
    zzwx: Array4b
    zzwy: Array4b
    zzwz: Array4b
    zzww: Array4b
    zwxx: Array4b
    zwxy: Array4b
    zwxz: Array4b
    zwxw: Array4b
    zwyx: Array4b
    zwyy: Array4b
    zwyz: Array4b
    zwyw: Array4b
    zwzx: Array4b
    zwzy: Array4b
    zwzz: Array4b
    zwzw: Array4b
    zwwx: Array4b
    zwwy: Array4b
    zwwz: Array4b
    zwww: Array4b
    wxxx: Array4b
    wxxy: Array4b
    wxxz: Array4b
    wxxw: Array4b
    wxyx: Array4b
    wxyy: Array4b
    wxyz: Array4b
    wxyw: Array4b
    wxzx: Array4b
    wxzy: Array4b
    wxzz: Array4b
    wxzw: Array4b
    wxwx: Array4b
    wxwy: Array4b
    wxwz: Array4b
    wxww: Array4b
    wyxx: Array4b
    wyxy: Array4b
    wyxz: Array4b
    wyxw: Array4b
    wyyx: Array4b
    wyyy: Array4b
    wyyz: Array4b
    wyyw: Array4b
    wyzx: Array4b
    wyzy: Array4b
    wyzz: Array4b
    wyzw: Array4b
    wywx: Array4b
    wywy: Array4b
    wywz: Array4b
    wyww: Array4b
    wzxx: Array4b
    wzxy: Array4b
    wzxz: Array4b
    wzxw: Array4b
    wzyx: Array4b
    wzyy: Array4b
    wzyz: Array4b
    wzyw: Array4b
    wzzx: Array4b
    wzzy: Array4b
    wzzz: Array4b
    wzzw: Array4b
    wzwx: Array4b
    wzwy: Array4b
    wzwz: Array4b
    wzww: Array4b
    wwxx: Array4b
    wwxy: Array4b
    wwxz: Array4b
    wwxw: Array4b
    wwyx: Array4b
    wwyy: Array4b
    wwyz: Array4b
    wwyw: Array4b
    wwzx: Array4b
    wwzy: Array4b
    wwzz: Array4b
    wwzw: Array4b
    wwwx: Array4b
    wwwy: Array4b
    wwwz: Array4b
    wwww: Array4b

_Array0i8Cp: TypeAlias = Union['Array0i8', '_Int8Cp', 'drjit.scalar._Array0i8Cp', 'drjit.llvm._Array0i8Cp']

class Array0i8(drjit.ArrayBase[Array0i8, _Array0i8Cp, Int8, _Int8Cp, Int8, Array0i8, Array0b]):
    xx: Array2i8
    xy: Array2i8
    xz: Array2i8
    xw: Array2i8
    yx: Array2i8
    yy: Array2i8
    yz: Array2i8
    yw: Array2i8
    zx: Array2i8
    zy: Array2i8
    zz: Array2i8
    zw: Array2i8
    wx: Array2i8
    wy: Array2i8
    wz: Array2i8
    ww: Array2i8
    xxx: Array3i8
    xxy: Array3i8
    xxz: Array3i8
    xxw: Array3i8
    xyx: Array3i8
    xyy: Array3i8
    xyz: Array3i8
    xyw: Array3i8
    xzx: Array3i8
    xzy: Array3i8
    xzz: Array3i8
    xzw: Array3i8
    xwx: Array3i8
    xwy: Array3i8
    xwz: Array3i8
    xww: Array3i8
    yxx: Array3i8
    yxy: Array3i8
    yxz: Array3i8
    yxw: Array3i8
    yyx: Array3i8
    yyy: Array3i8
    yyz: Array3i8
    yyw: Array3i8
    yzx: Array3i8
    yzy: Array3i8
    yzz: Array3i8
    yzw: Array3i8
    ywx: Array3i8
    ywy: Array3i8
    ywz: Array3i8
    yww: Array3i8
    zxx: Array3i8
    zxy: Array3i8
    zxz: Array3i8
    zxw: Array3i8
    zyx: Array3i8
    zyy: Array3i8
    zyz: Array3i8
    zyw: Array3i8
    zzx: Array3i8
    zzy: Array3i8
    zzz: Array3i8
    zzw: Array3i8
    zwx: Array3i8
    zwy: Array3i8
    zwz: Array3i8
    zww: Array3i8
    wxx: Array3i8
    wxy: Array3i8
    wxz: Array3i8
    wxw: Array3i8
    wyx: Array3i8
    wyy: Array3i8
    wyz: Array3i8
    wyw: Array3i8
    wzx: Array3i8
    wzy: Array3i8
    wzz: Array3i8
    wzw: Array3i8
    wwx: Array3i8
    wwy: Array3i8
    wwz: Array3i8
    www: Array3i8
    xxxx: Array4i8
    xxxy: Array4i8
    xxxz: Array4i8
    xxxw: Array4i8
    xxyx: Array4i8
    xxyy: Array4i8
    xxyz: Array4i8
    xxyw: Array4i8
    xxzx: Array4i8
    xxzy: Array4i8
    xxzz: Array4i8
    xxzw: Array4i8
    xxwx: Array4i8
    xxwy: Array4i8
    xxwz: Array4i8
    xxww: Array4i8
    xyxx: Array4i8
    xyxy: Array4i8
    xyxz: Array4i8
    xyxw: Array4i8
    xyyx: Array4i8
    xyyy: Array4i8
    xyyz: Array4i8
    xyyw: Array4i8
    xyzx: Array4i8
    xyzy: Array4i8
    xyzz: Array4i8
    xyzw: Array4i8
    xywx: Array4i8
    xywy: Array4i8
    xywz: Array4i8
    xyww: Array4i8
    xzxx: Array4i8
    xzxy: Array4i8
    xzxz: Array4i8
    xzxw: Array4i8
    xzyx: Array4i8
    xzyy: Array4i8
    xzyz: Array4i8
    xzyw: Array4i8
    xzzx: Array4i8
    xzzy: Array4i8
    xzzz: Array4i8
    xzzw: Array4i8
    xzwx: Array4i8
    xzwy: Array4i8
    xzwz: Array4i8
    xzww: Array4i8
    xwxx: Array4i8
    xwxy: Array4i8
    xwxz: Array4i8
    xwxw: Array4i8
    xwyx: Array4i8
    xwyy: Array4i8
    xwyz: Array4i8
    xwyw: Array4i8
    xwzx: Array4i8
    xwzy: Array4i8
    xwzz: Array4i8
    xwzw: Array4i8
    xwwx: Array4i8
    xwwy: Array4i8
    xwwz: Array4i8
    xwww: Array4i8
    yxxx: Array4i8
    yxxy: Array4i8
    yxxz: Array4i8
    yxxw: Array4i8
    yxyx: Array4i8
    yxyy: Array4i8
    yxyz: Array4i8
    yxyw: Array4i8
    yxzx: Array4i8
    yxzy: Array4i8
    yxzz: Array4i8
    yxzw: Array4i8
    yxwx: Array4i8
    yxwy: Array4i8
    yxwz: Array4i8
    yxww: Array4i8
    yyxx: Array4i8
    yyxy: Array4i8
    yyxz: Array4i8
    yyxw: Array4i8
    yyyx: Array4i8
    yyyy: Array4i8
    yyyz: Array4i8
    yyyw: Array4i8
    yyzx: Array4i8
    yyzy: Array4i8
    yyzz: Array4i8
    yyzw: Array4i8
    yywx: Array4i8
    yywy: Array4i8
    yywz: Array4i8
    yyww: Array4i8
    yzxx: Array4i8
    yzxy: Array4i8
    yzxz: Array4i8
    yzxw: Array4i8
    yzyx: Array4i8
    yzyy: Array4i8
    yzyz: Array4i8
    yzyw: Array4i8
    yzzx: Array4i8
    yzzy: Array4i8
    yzzz: Array4i8
    yzzw: Array4i8
    yzwx: Array4i8
    yzwy: Array4i8
    yzwz: Array4i8
    yzww: Array4i8
    ywxx: Array4i8
    ywxy: Array4i8
    ywxz: Array4i8
    ywxw: Array4i8
    ywyx: Array4i8
    ywyy: Array4i8
    ywyz: Array4i8
    ywyw: Array4i8
    ywzx: Array4i8
    ywzy: Array4i8
    ywzz: Array4i8
    ywzw: Array4i8
    ywwx: Array4i8
    ywwy: Array4i8
    ywwz: Array4i8
    ywww: Array4i8
    zxxx: Array4i8
    zxxy: Array4i8
    zxxz: Array4i8
    zxxw: Array4i8
    zxyx: Array4i8
    zxyy: Array4i8
    zxyz: Array4i8
    zxyw: Array4i8
    zxzx: Array4i8
    zxzy: Array4i8
    zxzz: Array4i8
    zxzw: Array4i8
    zxwx: Array4i8
    zxwy: Array4i8
    zxwz: Array4i8
    zxww: Array4i8
    zyxx: Array4i8
    zyxy: Array4i8
    zyxz: Array4i8
    zyxw: Array4i8
    zyyx: Array4i8
    zyyy: Array4i8
    zyyz: Array4i8
    zyyw: Array4i8
    zyzx: Array4i8
    zyzy: Array4i8
    zyzz: Array4i8
    zyzw: Array4i8
    zywx: Array4i8
    zywy: Array4i8
    zywz: Array4i8
    zyww: Array4i8
    zzxx: Array4i8
    zzxy: Array4i8
    zzxz: Array4i8
    zzxw: Array4i8
    zzyx: Array4i8
    zzyy: Array4i8
    zzyz: Array4i8
    zzyw: Array4i8
    zzzx: Array4i8
    zzzy: Array4i8
    zzzz: Array4i8
    zzzw: Array4i8
    zzwx: Array4i8
    zzwy: Array4i8
    zzwz: Array4i8
    zzww: Array4i8
    zwxx: Array4i8
    zwxy: Array4i8
    zwxz: Array4i8
    zwxw: Array4i8
    zwyx: Array4i8
    zwyy: Array4i8
    zwyz: Array4i8
    zwyw: Array4i8
    zwzx: Array4i8
    zwzy: Array4i8
    zwzz: Array4i8
    zwzw: Array4i8
    zwwx: Array4i8
    zwwy: Array4i8
    zwwz: Array4i8
    zwww: Array4i8
    wxxx: Array4i8
    wxxy: Array4i8
    wxxz: Array4i8
    wxxw: Array4i8
    wxyx: Array4i8
    wxyy: Array4i8
    wxyz: Array4i8
    wxyw: Array4i8
    wxzx: Array4i8
    wxzy: Array4i8
    wxzz: Array4i8
    wxzw: Array4i8
    wxwx: Array4i8
    wxwy: Array4i8
    wxwz: Array4i8
    wxww: Array4i8
    wyxx: Array4i8
    wyxy: Array4i8
    wyxz: Array4i8
    wyxw: Array4i8
    wyyx: Array4i8
    wyyy: Array4i8
    wyyz: Array4i8
    wyyw: Array4i8
    wyzx: Array4i8
    wyzy: Array4i8
    wyzz: Array4i8
    wyzw: Array4i8
    wywx: Array4i8
    wywy: Array4i8
    wywz: Array4i8
    wyww: Array4i8
    wzxx: Array4i8
    wzxy: Array4i8
    wzxz: Array4i8
    wzxw: Array4i8
    wzyx: Array4i8
    wzyy: Array4i8
    wzyz: Array4i8
    wzyw: Array4i8
    wzzx: Array4i8
    wzzy: Array4i8
    wzzz: Array4i8
    wzzw: Array4i8
    wzwx: Array4i8
    wzwy: Array4i8
    wzwz: Array4i8
    wzww: Array4i8
    wwxx: Array4i8
    wwxy: Array4i8
    wwxz: Array4i8
    wwxw: Array4i8
    wwyx: Array4i8
    wwyy: Array4i8
    wwyz: Array4i8
    wwyw: Array4i8
    wwzx: Array4i8
    wwzy: Array4i8
    wwzz: Array4i8
    wwzw: Array4i8
    wwwx: Array4i8
    wwwy: Array4i8
    wwwz: Array4i8
    wwww: Array4i8

_Array0u8Cp: TypeAlias = Union['Array0u8', '_UInt8Cp', 'drjit.scalar._Array0u8Cp', 'drjit.llvm._Array0u8Cp']

class Array0u8(drjit.ArrayBase[Array0u8, _Array0u8Cp, UInt8, _UInt8Cp, UInt8, Array0u8, Array0b]):
    xx: Array2u8
    xy: Array2u8
    xz: Array2u8
    xw: Array2u8
    yx: Array2u8
    yy: Array2u8
    yz: Array2u8
    yw: Array2u8
    zx: Array2u8
    zy: Array2u8
    zz: Array2u8
    zw: Array2u8
    wx: Array2u8
    wy: Array2u8
    wz: Array2u8
    ww: Array2u8
    xxx: Array3u8
    xxy: Array3u8
    xxz: Array3u8
    xxw: Array3u8
    xyx: Array3u8
    xyy: Array3u8
    xyz: Array3u8
    xyw: Array3u8
    xzx: Array3u8
    xzy: Array3u8
    xzz: Array3u8
    xzw: Array3u8
    xwx: Array3u8
    xwy: Array3u8
    xwz: Array3u8
    xww: Array3u8
    yxx: Array3u8
    yxy: Array3u8
    yxz: Array3u8
    yxw: Array3u8
    yyx: Array3u8
    yyy: Array3u8
    yyz: Array3u8
    yyw: Array3u8
    yzx: Array3u8
    yzy: Array3u8
    yzz: Array3u8
    yzw: Array3u8
    ywx: Array3u8
    ywy: Array3u8
    ywz: Array3u8
    yww: Array3u8
    zxx: Array3u8
    zxy: Array3u8
    zxz: Array3u8
    zxw: Array3u8
    zyx: Array3u8
    zyy: Array3u8
    zyz: Array3u8
    zyw: Array3u8
    zzx: Array3u8
    zzy: Array3u8
    zzz: Array3u8
    zzw: Array3u8
    zwx: Array3u8
    zwy: Array3u8
    zwz: Array3u8
    zww: Array3u8
    wxx: Array3u8
    wxy: Array3u8
    wxz: Array3u8
    wxw: Array3u8
    wyx: Array3u8
    wyy: Array3u8
    wyz: Array3u8
    wyw: Array3u8
    wzx: Array3u8
    wzy: Array3u8
    wzz: Array3u8
    wzw: Array3u8
    wwx: Array3u8
    wwy: Array3u8
    wwz: Array3u8
    www: Array3u8
    xxxx: Array4u8
    xxxy: Array4u8
    xxxz: Array4u8
    xxxw: Array4u8
    xxyx: Array4u8
    xxyy: Array4u8
    xxyz: Array4u8
    xxyw: Array4u8
    xxzx: Array4u8
    xxzy: Array4u8
    xxzz: Array4u8
    xxzw: Array4u8
    xxwx: Array4u8
    xxwy: Array4u8
    xxwz: Array4u8
    xxww: Array4u8
    xyxx: Array4u8
    xyxy: Array4u8
    xyxz: Array4u8
    xyxw: Array4u8
    xyyx: Array4u8
    xyyy: Array4u8
    xyyz: Array4u8
    xyyw: Array4u8
    xyzx: Array4u8
    xyzy: Array4u8
    xyzz: Array4u8
    xyzw: Array4u8
    xywx: Array4u8
    xywy: Array4u8
    xywz: Array4u8
    xyww: Array4u8
    xzxx: Array4u8
    xzxy: Array4u8
    xzxz: Array4u8
    xzxw: Array4u8
    xzyx: Array4u8
    xzyy: Array4u8
    xzyz: Array4u8
    xzyw: Array4u8
    xzzx: Array4u8
    xzzy: Array4u8
    xzzz: Array4u8
    xzzw: Array4u8
    xzwx: Array4u8
    xzwy: Array4u8
    xzwz: Array4u8
    xzww: Array4u8
    xwxx: Array4u8
    xwxy: Array4u8
    xwxz: Array4u8
    xwxw: Array4u8
    xwyx: Array4u8
    xwyy: Array4u8
    xwyz: Array4u8
    xwyw: Array4u8
    xwzx: Array4u8
    xwzy: Array4u8
    xwzz: Array4u8
    xwzw: Array4u8
    xwwx: Array4u8
    xwwy: Array4u8
    xwwz: Array4u8
    xwww: Array4u8
    yxxx: Array4u8
    yxxy: Array4u8
    yxxz: Array4u8
    yxxw: Array4u8
    yxyx: Array4u8
    yxyy: Array4u8
    yxyz: Array4u8
    yxyw: Array4u8
    yxzx: Array4u8
    yxzy: Array4u8
    yxzz: Array4u8
    yxzw: Array4u8
    yxwx: Array4u8
    yxwy: Array4u8
    yxwz: Array4u8
    yxww: Array4u8
    yyxx: Array4u8
    yyxy: Array4u8
    yyxz: Array4u8
    yyxw: Array4u8
    yyyx: Array4u8
    yyyy: Array4u8
    yyyz: Array4u8
    yyyw: Array4u8
    yyzx: Array4u8
    yyzy: Array4u8
    yyzz: Array4u8
    yyzw: Array4u8
    yywx: Array4u8
    yywy: Array4u8
    yywz: Array4u8
    yyww: Array4u8
    yzxx: Array4u8
    yzxy: Array4u8
    yzxz: Array4u8
    yzxw: Array4u8
    yzyx: Array4u8
    yzyy: Array4u8
    yzyz: Array4u8
    yzyw: Array4u8
    yzzx: Array4u8
    yzzy: Array4u8
    yzzz: Array4u8
    yzzw: Array4u8
    yzwx: Array4u8
    yzwy: Array4u8
    yzwz: Array4u8
    yzww: Array4u8
    ywxx: Array4u8
    ywxy: Array4u8
    ywxz: Array4u8
    ywxw: Array4u8
    ywyx: Array4u8
    ywyy: Array4u8
    ywyz: Array4u8
    ywyw: Array4u8
    ywzx: Array4u8
    ywzy: Array4u8
    ywzz: Array4u8
    ywzw: Array4u8
    ywwx: Array4u8
    ywwy: Array4u8
    ywwz: Array4u8
    ywww: Array4u8
    zxxx: Array4u8
    zxxy: Array4u8
    zxxz: Array4u8
    zxxw: Array4u8
    zxyx: Array4u8
    zxyy: Array4u8
    zxyz: Array4u8
    zxyw: Array4u8
    zxzx: Array4u8
    zxzy: Array4u8
    zxzz: Array4u8
    zxzw: Array4u8
    zxwx: Array4u8
    zxwy: Array4u8
    zxwz: Array4u8
    zxww: Array4u8
    zyxx: Array4u8
    zyxy: Array4u8
    zyxz: Array4u8
    zyxw: Array4u8
    zyyx: Array4u8
    zyyy: Array4u8
    zyyz: Array4u8
    zyyw: Array4u8
    zyzx: Array4u8
    zyzy: Array4u8
    zyzz: Array4u8
    zyzw: Array4u8
    zywx: Array4u8
    zywy: Array4u8
    zywz: Array4u8
    zyww: Array4u8
    zzxx: Array4u8
    zzxy: Array4u8
    zzxz: Array4u8
    zzxw: Array4u8
    zzyx: Array4u8
    zzyy: Array4u8
    zzyz: Array4u8
    zzyw: Array4u8
    zzzx: Array4u8
    zzzy: Array4u8
    zzzz: Array4u8
    zzzw: Array4u8
    zzwx: Array4u8
    zzwy: Array4u8
    zzwz: Array4u8
    zzww: Array4u8
    zwxx: Array4u8
    zwxy: Array4u8
    zwxz: Array4u8
    zwxw: Array4u8
    zwyx: Array4u8
    zwyy: Array4u8
    zwyz: Array4u8
    zwyw: Array4u8
    zwzx: Array4u8
    zwzy: Array4u8
    zwzz: Array4u8
    zwzw: Array4u8
    zwwx: Array4u8
    zwwy: Array4u8
    zwwz: Array4u8
    zwww: Array4u8
    wxxx: Array4u8
    wxxy: Array4u8
    wxxz: Array4u8
    wxxw: Array4u8
    wxyx: Array4u8
    wxyy: Array4u8
    wxyz: Array4u8
    wxyw: Array4u8
    wxzx: Array4u8
    wxzy: Array4u8
    wxzz: Array4u8
    wxzw: Array4u8
    wxwx: Array4u8
    wxwy: Array4u8
    wxwz: Array4u8
    wxww: Array4u8
    wyxx: Array4u8
    wyxy: Array4u8
    wyxz: Array4u8
    wyxw: Array4u8
    wyyx: Array4u8
    wyyy: Array4u8
    wyyz: Array4u8
    wyyw: Array4u8
    wyzx: Array4u8
    wyzy: Array4u8
    wyzz: Array4u8
    wyzw: Array4u8
    wywx: Array4u8
    wywy: Array4u8
    wywz: Array4u8
    wyww: Array4u8
    wzxx: Array4u8
    wzxy: Array4u8
    wzxz: Array4u8
    wzxw: Array4u8
    wzyx: Array4u8
    wzyy: Array4u8
    wzyz: Array4u8
    wzyw: Array4u8
    wzzx: Array4u8
    wzzy: Array4u8
    wzzz: Array4u8
    wzzw: Array4u8
    wzwx: Array4u8
    wzwy: Array4u8
    wzwz: Array4u8
    wzww: Array4u8
    wwxx: Array4u8
    wwxy: Array4u8
    wwxz: Array4u8
    wwxw: Array4u8
    wwyx: Array4u8
    wwyy: Array4u8
    wwyz: Array4u8
    wwyw: Array4u8
    wwzx: Array4u8
    wwzy: Array4u8
    wwzz: Array4u8
    wwzw: Array4u8
    wwwx: Array4u8
    wwwy: Array4u8
    wwwz: Array4u8
    wwww: Array4u8

_Array0iCp: TypeAlias = Union['Array0i', '_IntCp', 'drjit.scalar._Array0iCp', 'drjit.llvm._Array0iCp', '_Array0bCp']

class Array0i(drjit.ArrayBase[Array0i, _Array0iCp, Int, _IntCp, Int, Array0i, Array0b]):
    xx: Array2i
    xy: Array2i
    xz: Array2i
    xw: Array2i
    yx: Array2i
    yy: Array2i
    yz: Array2i
    yw: Array2i
    zx: Array2i
    zy: Array2i
    zz: Array2i
    zw: Array2i
    wx: Array2i
    wy: Array2i
    wz: Array2i
    ww: Array2i
    xxx: Array3i
    xxy: Array3i
    xxz: Array3i
    xxw: Array3i
    xyx: Array3i
    xyy: Array3i
    xyz: Array3i
    xyw: Array3i
    xzx: Array3i
    xzy: Array3i
    xzz: Array3i
    xzw: Array3i
    xwx: Array3i
    xwy: Array3i
    xwz: Array3i
    xww: Array3i
    yxx: Array3i
    yxy: Array3i
    yxz: Array3i
    yxw: Array3i
    yyx: Array3i
    yyy: Array3i
    yyz: Array3i
    yyw: Array3i
    yzx: Array3i
    yzy: Array3i
    yzz: Array3i
    yzw: Array3i
    ywx: Array3i
    ywy: Array3i
    ywz: Array3i
    yww: Array3i
    zxx: Array3i
    zxy: Array3i
    zxz: Array3i
    zxw: Array3i
    zyx: Array3i
    zyy: Array3i
    zyz: Array3i
    zyw: Array3i
    zzx: Array3i
    zzy: Array3i
    zzz: Array3i
    zzw: Array3i
    zwx: Array3i
    zwy: Array3i
    zwz: Array3i
    zww: Array3i
    wxx: Array3i
    wxy: Array3i
    wxz: Array3i
    wxw: Array3i
    wyx: Array3i
    wyy: Array3i
    wyz: Array3i
    wyw: Array3i
    wzx: Array3i
    wzy: Array3i
    wzz: Array3i
    wzw: Array3i
    wwx: Array3i
    wwy: Array3i
    wwz: Array3i
    www: Array3i
    xxxx: Array4i
    xxxy: Array4i
    xxxz: Array4i
    xxxw: Array4i
    xxyx: Array4i
    xxyy: Array4i
    xxyz: Array4i
    xxyw: Array4i
    xxzx: Array4i
    xxzy: Array4i
    xxzz: Array4i
    xxzw: Array4i
    xxwx: Array4i
    xxwy: Array4i
    xxwz: Array4i
    xxww: Array4i
    xyxx: Array4i
    xyxy: Array4i
    xyxz: Array4i
    xyxw: Array4i
    xyyx: Array4i
    xyyy: Array4i
    xyyz: Array4i
    xyyw: Array4i
    xyzx: Array4i
    xyzy: Array4i
    xyzz: Array4i
    xyzw: Array4i
    xywx: Array4i
    xywy: Array4i
    xywz: Array4i
    xyww: Array4i
    xzxx: Array4i
    xzxy: Array4i
    xzxz: Array4i
    xzxw: Array4i
    xzyx: Array4i
    xzyy: Array4i
    xzyz: Array4i
    xzyw: Array4i
    xzzx: Array4i
    xzzy: Array4i
    xzzz: Array4i
    xzzw: Array4i
    xzwx: Array4i
    xzwy: Array4i
    xzwz: Array4i
    xzww: Array4i
    xwxx: Array4i
    xwxy: Array4i
    xwxz: Array4i
    xwxw: Array4i
    xwyx: Array4i
    xwyy: Array4i
    xwyz: Array4i
    xwyw: Array4i
    xwzx: Array4i
    xwzy: Array4i
    xwzz: Array4i
    xwzw: Array4i
    xwwx: Array4i
    xwwy: Array4i
    xwwz: Array4i
    xwww: Array4i
    yxxx: Array4i
    yxxy: Array4i
    yxxz: Array4i
    yxxw: Array4i
    yxyx: Array4i
    yxyy: Array4i
    yxyz: Array4i
    yxyw: Array4i
    yxzx: Array4i
    yxzy: Array4i
    yxzz: Array4i
    yxzw: Array4i
    yxwx: Array4i
    yxwy: Array4i
    yxwz: Array4i
    yxww: Array4i
    yyxx: Array4i
    yyxy: Array4i
    yyxz: Array4i
    yyxw: Array4i
    yyyx: Array4i
    yyyy: Array4i
    yyyz: Array4i
    yyyw: Array4i
    yyzx: Array4i
    yyzy: Array4i
    yyzz: Array4i
    yyzw: Array4i
    yywx: Array4i
    yywy: Array4i
    yywz: Array4i
    yyww: Array4i
    yzxx: Array4i
    yzxy: Array4i
    yzxz: Array4i
    yzxw: Array4i
    yzyx: Array4i
    yzyy: Array4i
    yzyz: Array4i
    yzyw: Array4i
    yzzx: Array4i
    yzzy: Array4i
    yzzz: Array4i
    yzzw: Array4i
    yzwx: Array4i
    yzwy: Array4i
    yzwz: Array4i
    yzww: Array4i
    ywxx: Array4i
    ywxy: Array4i
    ywxz: Array4i
    ywxw: Array4i
    ywyx: Array4i
    ywyy: Array4i
    ywyz: Array4i
    ywyw: Array4i
    ywzx: Array4i
    ywzy: Array4i
    ywzz: Array4i
    ywzw: Array4i
    ywwx: Array4i
    ywwy: Array4i
    ywwz: Array4i
    ywww: Array4i
    zxxx: Array4i
    zxxy: Array4i
    zxxz: Array4i
    zxxw: Array4i
    zxyx: Array4i
    zxyy: Array4i
    zxyz: Array4i
    zxyw: Array4i
    zxzx: Array4i
    zxzy: Array4i
    zxzz: Array4i
    zxzw: Array4i
    zxwx: Array4i
    zxwy: Array4i
    zxwz: Array4i
    zxww: Array4i
    zyxx: Array4i
    zyxy: Array4i
    zyxz: Array4i
    zyxw: Array4i
    zyyx: Array4i
    zyyy: Array4i
    zyyz: Array4i
    zyyw: Array4i
    zyzx: Array4i
    zyzy: Array4i
    zyzz: Array4i
    zyzw: Array4i
    zywx: Array4i
    zywy: Array4i
    zywz: Array4i
    zyww: Array4i
    zzxx: Array4i
    zzxy: Array4i
    zzxz: Array4i
    zzxw: Array4i
    zzyx: Array4i
    zzyy: Array4i
    zzyz: Array4i
    zzyw: Array4i
    zzzx: Array4i
    zzzy: Array4i
    zzzz: Array4i
    zzzw: Array4i
    zzwx: Array4i
    zzwy: Array4i
    zzwz: Array4i
    zzww: Array4i
    zwxx: Array4i
    zwxy: Array4i
    zwxz: Array4i
    zwxw: Array4i
    zwyx: Array4i
    zwyy: Array4i
    zwyz: Array4i
    zwyw: Array4i
    zwzx: Array4i
    zwzy: Array4i
    zwzz: Array4i
    zwzw: Array4i
    zwwx: Array4i
    zwwy: Array4i
    zwwz: Array4i
    zwww: Array4i
    wxxx: Array4i
    wxxy: Array4i
    wxxz: Array4i
    wxxw: Array4i
    wxyx: Array4i
    wxyy: Array4i
    wxyz: Array4i
    wxyw: Array4i
    wxzx: Array4i
    wxzy: Array4i
    wxzz: Array4i
    wxzw: Array4i
    wxwx: Array4i
    wxwy: Array4i
    wxwz: Array4i
    wxww: Array4i
    wyxx: Array4i
    wyxy: Array4i
    wyxz: Array4i
    wyxw: Array4i
    wyyx: Array4i
    wyyy: Array4i
    wyyz: Array4i
    wyyw: Array4i
    wyzx: Array4i
    wyzy: Array4i
    wyzz: Array4i
    wyzw: Array4i
    wywx: Array4i
    wywy: Array4i
    wywz: Array4i
    wyww: Array4i
    wzxx: Array4i
    wzxy: Array4i
    wzxz: Array4i
    wzxw: Array4i
    wzyx: Array4i
    wzyy: Array4i
    wzyz: Array4i
    wzyw: Array4i
    wzzx: Array4i
    wzzy: Array4i
    wzzz: Array4i
    wzzw: Array4i
    wzwx: Array4i
    wzwy: Array4i
    wzwz: Array4i
    wzww: Array4i
    wwxx: Array4i
    wwxy: Array4i
    wwxz: Array4i
    wwxw: Array4i
    wwyx: Array4i
    wwyy: Array4i
    wwyz: Array4i
    wwyw: Array4i
    wwzx: Array4i
    wwzy: Array4i
    wwzz: Array4i
    wwzw: Array4i
    wwwx: Array4i
    wwwy: Array4i
    wwwz: Array4i
    wwww: Array4i

_Array0uCp: TypeAlias = Union['Array0u', '_UIntCp', 'drjit.scalar._Array0uCp', 'drjit.llvm._Array0uCp', '_Array0iCp']

class Array0u(drjit.ArrayBase[Array0u, _Array0uCp, UInt, _UIntCp, UInt, Array0u, Array0b]):
    xx: Array2u
    xy: Array2u
    xz: Array2u
    xw: Array2u
    yx: Array2u
    yy: Array2u
    yz: Array2u
    yw: Array2u
    zx: Array2u
    zy: Array2u
    zz: Array2u
    zw: Array2u
    wx: Array2u
    wy: Array2u
    wz: Array2u
    ww: Array2u
    xxx: Array3u
    xxy: Array3u
    xxz: Array3u
    xxw: Array3u
    xyx: Array3u
    xyy: Array3u
    xyz: Array3u
    xyw: Array3u
    xzx: Array3u
    xzy: Array3u
    xzz: Array3u
    xzw: Array3u
    xwx: Array3u
    xwy: Array3u
    xwz: Array3u
    xww: Array3u
    yxx: Array3u
    yxy: Array3u
    yxz: Array3u
    yxw: Array3u
    yyx: Array3u
    yyy: Array3u
    yyz: Array3u
    yyw: Array3u
    yzx: Array3u
    yzy: Array3u
    yzz: Array3u
    yzw: Array3u
    ywx: Array3u
    ywy: Array3u
    ywz: Array3u
    yww: Array3u
    zxx: Array3u
    zxy: Array3u
    zxz: Array3u
    zxw: Array3u
    zyx: Array3u
    zyy: Array3u
    zyz: Array3u
    zyw: Array3u
    zzx: Array3u
    zzy: Array3u
    zzz: Array3u
    zzw: Array3u
    zwx: Array3u
    zwy: Array3u
    zwz: Array3u
    zww: Array3u
    wxx: Array3u
    wxy: Array3u
    wxz: Array3u
    wxw: Array3u
    wyx: Array3u
    wyy: Array3u
    wyz: Array3u
    wyw: Array3u
    wzx: Array3u
    wzy: Array3u
    wzz: Array3u
    wzw: Array3u
    wwx: Array3u
    wwy: Array3u
    wwz: Array3u
    www: Array3u
    xxxx: Array4u
    xxxy: Array4u
    xxxz: Array4u
    xxxw: Array4u
    xxyx: Array4u
    xxyy: Array4u
    xxyz: Array4u
    xxyw: Array4u
    xxzx: Array4u
    xxzy: Array4u
    xxzz: Array4u
    xxzw: Array4u
    xxwx: Array4u
    xxwy: Array4u
    xxwz: Array4u
    xxww: Array4u
    xyxx: Array4u
    xyxy: Array4u
    xyxz: Array4u
    xyxw: Array4u
    xyyx: Array4u
    xyyy: Array4u
    xyyz: Array4u
    xyyw: Array4u
    xyzx: Array4u
    xyzy: Array4u
    xyzz: Array4u
    xyzw: Array4u
    xywx: Array4u
    xywy: Array4u
    xywz: Array4u
    xyww: Array4u
    xzxx: Array4u
    xzxy: Array4u
    xzxz: Array4u
    xzxw: Array4u
    xzyx: Array4u
    xzyy: Array4u
    xzyz: Array4u
    xzyw: Array4u
    xzzx: Array4u
    xzzy: Array4u
    xzzz: Array4u
    xzzw: Array4u
    xzwx: Array4u
    xzwy: Array4u
    xzwz: Array4u
    xzww: Array4u
    xwxx: Array4u
    xwxy: Array4u
    xwxz: Array4u
    xwxw: Array4u
    xwyx: Array4u
    xwyy: Array4u
    xwyz: Array4u
    xwyw: Array4u
    xwzx: Array4u
    xwzy: Array4u
    xwzz: Array4u
    xwzw: Array4u
    xwwx: Array4u
    xwwy: Array4u
    xwwz: Array4u
    xwww: Array4u
    yxxx: Array4u
    yxxy: Array4u
    yxxz: Array4u
    yxxw: Array4u
    yxyx: Array4u
    yxyy: Array4u
    yxyz: Array4u
    yxyw: Array4u
    yxzx: Array4u
    yxzy: Array4u
    yxzz: Array4u
    yxzw: Array4u
    yxwx: Array4u
    yxwy: Array4u
    yxwz: Array4u
    yxww: Array4u
    yyxx: Array4u
    yyxy: Array4u
    yyxz: Array4u
    yyxw: Array4u
    yyyx: Array4u
    yyyy: Array4u
    yyyz: Array4u
    yyyw: Array4u
    yyzx: Array4u
    yyzy: Array4u
    yyzz: Array4u
    yyzw: Array4u
    yywx: Array4u
    yywy: Array4u
    yywz: Array4u
    yyww: Array4u
    yzxx: Array4u
    yzxy: Array4u
    yzxz: Array4u
    yzxw: Array4u
    yzyx: Array4u
    yzyy: Array4u
    yzyz: Array4u
    yzyw: Array4u
    yzzx: Array4u
    yzzy: Array4u
    yzzz: Array4u
    yzzw: Array4u
    yzwx: Array4u
    yzwy: Array4u
    yzwz: Array4u
    yzww: Array4u
    ywxx: Array4u
    ywxy: Array4u
    ywxz: Array4u
    ywxw: Array4u
    ywyx: Array4u
    ywyy: Array4u
    ywyz: Array4u
    ywyw: Array4u
    ywzx: Array4u
    ywzy: Array4u
    ywzz: Array4u
    ywzw: Array4u
    ywwx: Array4u
    ywwy: Array4u
    ywwz: Array4u
    ywww: Array4u
    zxxx: Array4u
    zxxy: Array4u
    zxxz: Array4u
    zxxw: Array4u
    zxyx: Array4u
    zxyy: Array4u
    zxyz: Array4u
    zxyw: Array4u
    zxzx: Array4u
    zxzy: Array4u
    zxzz: Array4u
    zxzw: Array4u
    zxwx: Array4u
    zxwy: Array4u
    zxwz: Array4u
    zxww: Array4u
    zyxx: Array4u
    zyxy: Array4u
    zyxz: Array4u
    zyxw: Array4u
    zyyx: Array4u
    zyyy: Array4u
    zyyz: Array4u
    zyyw: Array4u
    zyzx: Array4u
    zyzy: Array4u
    zyzz: Array4u
    zyzw: Array4u
    zywx: Array4u
    zywy: Array4u
    zywz: Array4u
    zyww: Array4u
    zzxx: Array4u
    zzxy: Array4u
    zzxz: Array4u
    zzxw: Array4u
    zzyx: Array4u
    zzyy: Array4u
    zzyz: Array4u
    zzyw: Array4u
    zzzx: Array4u
    zzzy: Array4u
    zzzz: Array4u
    zzzw: Array4u
    zzwx: Array4u
    zzwy: Array4u
    zzwz: Array4u
    zzww: Array4u
    zwxx: Array4u
    zwxy: Array4u
    zwxz: Array4u
    zwxw: Array4u
    zwyx: Array4u
    zwyy: Array4u
    zwyz: Array4u
    zwyw: Array4u
    zwzx: Array4u
    zwzy: Array4u
    zwzz: Array4u
    zwzw: Array4u
    zwwx: Array4u
    zwwy: Array4u
    zwwz: Array4u
    zwww: Array4u
    wxxx: Array4u
    wxxy: Array4u
    wxxz: Array4u
    wxxw: Array4u
    wxyx: Array4u
    wxyy: Array4u
    wxyz: Array4u
    wxyw: Array4u
    wxzx: Array4u
    wxzy: Array4u
    wxzz: Array4u
    wxzw: Array4u
    wxwx: Array4u
    wxwy: Array4u
    wxwz: Array4u
    wxww: Array4u
    wyxx: Array4u
    wyxy: Array4u
    wyxz: Array4u
    wyxw: Array4u
    wyyx: Array4u
    wyyy: Array4u
    wyyz: Array4u
    wyyw: Array4u
    wyzx: Array4u
    wyzy: Array4u
    wyzz: Array4u
    wyzw: Array4u
    wywx: Array4u
    wywy: Array4u
    wywz: Array4u
    wyww: Array4u
    wzxx: Array4u
    wzxy: Array4u
    wzxz: Array4u
    wzxw: Array4u
    wzyx: Array4u
    wzyy: Array4u
    wzyz: Array4u
    wzyw: Array4u
    wzzx: Array4u
    wzzy: Array4u
    wzzz: Array4u
    wzzw: Array4u
    wzwx: Array4u
    wzwy: Array4u
    wzwz: Array4u
    wzww: Array4u
    wwxx: Array4u
    wwxy: Array4u
    wwxz: Array4u
    wwxw: Array4u
    wwyx: Array4u
    wwyy: Array4u
    wwyz: Array4u
    wwyw: Array4u
    wwzx: Array4u
    wwzy: Array4u
    wwzz: Array4u
    wwzw: Array4u
    wwwx: Array4u
    wwwy: Array4u
    wwwz: Array4u
    wwww: Array4u

_Array0i64Cp: TypeAlias = Union['Array0i64', '_Int64Cp', 'drjit.scalar._Array0i64Cp', 'drjit.llvm._Array0i64Cp', '_Array0uCp']

class Array0i64(drjit.ArrayBase[Array0i64, _Array0i64Cp, Int64, _Int64Cp, Int64, Array0i64, Array0b]):
    xx: Array2i64
    xy: Array2i64
    xz: Array2i64
    xw: Array2i64
    yx: Array2i64
    yy: Array2i64
    yz: Array2i64
    yw: Array2i64
    zx: Array2i64
    zy: Array2i64
    zz: Array2i64
    zw: Array2i64
    wx: Array2i64
    wy: Array2i64
    wz: Array2i64
    ww: Array2i64
    xxx: Array3i64
    xxy: Array3i64
    xxz: Array3i64
    xxw: Array3i64
    xyx: Array3i64
    xyy: Array3i64
    xyz: Array3i64
    xyw: Array3i64
    xzx: Array3i64
    xzy: Array3i64
    xzz: Array3i64
    xzw: Array3i64
    xwx: Array3i64
    xwy: Array3i64
    xwz: Array3i64
    xww: Array3i64
    yxx: Array3i64
    yxy: Array3i64
    yxz: Array3i64
    yxw: Array3i64
    yyx: Array3i64
    yyy: Array3i64
    yyz: Array3i64
    yyw: Array3i64
    yzx: Array3i64
    yzy: Array3i64
    yzz: Array3i64
    yzw: Array3i64
    ywx: Array3i64
    ywy: Array3i64
    ywz: Array3i64
    yww: Array3i64
    zxx: Array3i64
    zxy: Array3i64
    zxz: Array3i64
    zxw: Array3i64
    zyx: Array3i64
    zyy: Array3i64
    zyz: Array3i64
    zyw: Array3i64
    zzx: Array3i64
    zzy: Array3i64
    zzz: Array3i64
    zzw: Array3i64
    zwx: Array3i64
    zwy: Array3i64
    zwz: Array3i64
    zww: Array3i64
    wxx: Array3i64
    wxy: Array3i64
    wxz: Array3i64
    wxw: Array3i64
    wyx: Array3i64
    wyy: Array3i64
    wyz: Array3i64
    wyw: Array3i64
    wzx: Array3i64
    wzy: Array3i64
    wzz: Array3i64
    wzw: Array3i64
    wwx: Array3i64
    wwy: Array3i64
    wwz: Array3i64
    www: Array3i64
    xxxx: Array4i64
    xxxy: Array4i64
    xxxz: Array4i64
    xxxw: Array4i64
    xxyx: Array4i64
    xxyy: Array4i64
    xxyz: Array4i64
    xxyw: Array4i64
    xxzx: Array4i64
    xxzy: Array4i64
    xxzz: Array4i64
    xxzw: Array4i64
    xxwx: Array4i64
    xxwy: Array4i64
    xxwz: Array4i64
    xxww: Array4i64
    xyxx: Array4i64
    xyxy: Array4i64
    xyxz: Array4i64
    xyxw: Array4i64
    xyyx: Array4i64
    xyyy: Array4i64
    xyyz: Array4i64
    xyyw: Array4i64
    xyzx: Array4i64
    xyzy: Array4i64
    xyzz: Array4i64
    xyzw: Array4i64
    xywx: Array4i64
    xywy: Array4i64
    xywz: Array4i64
    xyww: Array4i64
    xzxx: Array4i64
    xzxy: Array4i64
    xzxz: Array4i64
    xzxw: Array4i64
    xzyx: Array4i64
    xzyy: Array4i64
    xzyz: Array4i64
    xzyw: Array4i64
    xzzx: Array4i64
    xzzy: Array4i64
    xzzz: Array4i64
    xzzw: Array4i64
    xzwx: Array4i64
    xzwy: Array4i64
    xzwz: Array4i64
    xzww: Array4i64
    xwxx: Array4i64
    xwxy: Array4i64
    xwxz: Array4i64
    xwxw: Array4i64
    xwyx: Array4i64
    xwyy: Array4i64
    xwyz: Array4i64
    xwyw: Array4i64
    xwzx: Array4i64
    xwzy: Array4i64
    xwzz: Array4i64
    xwzw: Array4i64
    xwwx: Array4i64
    xwwy: Array4i64
    xwwz: Array4i64
    xwww: Array4i64
    yxxx: Array4i64
    yxxy: Array4i64
    yxxz: Array4i64
    yxxw: Array4i64
    yxyx: Array4i64
    yxyy: Array4i64
    yxyz: Array4i64
    yxyw: Array4i64
    yxzx: Array4i64
    yxzy: Array4i64
    yxzz: Array4i64
    yxzw: Array4i64
    yxwx: Array4i64
    yxwy: Array4i64
    yxwz: Array4i64
    yxww: Array4i64
    yyxx: Array4i64
    yyxy: Array4i64
    yyxz: Array4i64
    yyxw: Array4i64
    yyyx: Array4i64
    yyyy: Array4i64
    yyyz: Array4i64
    yyyw: Array4i64
    yyzx: Array4i64
    yyzy: Array4i64
    yyzz: Array4i64
    yyzw: Array4i64
    yywx: Array4i64
    yywy: Array4i64
    yywz: Array4i64
    yyww: Array4i64
    yzxx: Array4i64
    yzxy: Array4i64
    yzxz: Array4i64
    yzxw: Array4i64
    yzyx: Array4i64
    yzyy: Array4i64
    yzyz: Array4i64
    yzyw: Array4i64
    yzzx: Array4i64
    yzzy: Array4i64
    yzzz: Array4i64
    yzzw: Array4i64
    yzwx: Array4i64
    yzwy: Array4i64
    yzwz: Array4i64
    yzww: Array4i64
    ywxx: Array4i64
    ywxy: Array4i64
    ywxz: Array4i64
    ywxw: Array4i64
    ywyx: Array4i64
    ywyy: Array4i64
    ywyz: Array4i64
    ywyw: Array4i64
    ywzx: Array4i64
    ywzy: Array4i64
    ywzz: Array4i64
    ywzw: Array4i64
    ywwx: Array4i64
    ywwy: Array4i64
    ywwz: Array4i64
    ywww: Array4i64
    zxxx: Array4i64
    zxxy: Array4i64
    zxxz: Array4i64
    zxxw: Array4i64
    zxyx: Array4i64
    zxyy: Array4i64
    zxyz: Array4i64
    zxyw: Array4i64
    zxzx: Array4i64
    zxzy: Array4i64
    zxzz: Array4i64
    zxzw: Array4i64
    zxwx: Array4i64
    zxwy: Array4i64
    zxwz: Array4i64
    zxww: Array4i64
    zyxx: Array4i64
    zyxy: Array4i64
    zyxz: Array4i64
    zyxw: Array4i64
    zyyx: Array4i64
    zyyy: Array4i64
    zyyz: Array4i64
    zyyw: Array4i64
    zyzx: Array4i64
    zyzy: Array4i64
    zyzz: Array4i64
    zyzw: Array4i64
    zywx: Array4i64
    zywy: Array4i64
    zywz: Array4i64
    zyww: Array4i64
    zzxx: Array4i64
    zzxy: Array4i64
    zzxz: Array4i64
    zzxw: Array4i64
    zzyx: Array4i64
    zzyy: Array4i64
    zzyz: Array4i64
    zzyw: Array4i64
    zzzx: Array4i64
    zzzy: Array4i64
    zzzz: Array4i64
    zzzw: Array4i64
    zzwx: Array4i64
    zzwy: Array4i64
    zzwz: Array4i64
    zzww: Array4i64
    zwxx: Array4i64
    zwxy: Array4i64
    zwxz: Array4i64
    zwxw: Array4i64
    zwyx: Array4i64
    zwyy: Array4i64
    zwyz: Array4i64
    zwyw: Array4i64
    zwzx: Array4i64
    zwzy: Array4i64
    zwzz: Array4i64
    zwzw: Array4i64
    zwwx: Array4i64
    zwwy: Array4i64
    zwwz: Array4i64
    zwww: Array4i64
    wxxx: Array4i64
    wxxy: Array4i64
    wxxz: Array4i64
    wxxw: Array4i64
    wxyx: Array4i64
    wxyy: Array4i64
    wxyz: Array4i64
    wxyw: Array4i64
    wxzx: Array4i64
    wxzy: Array4i64
    wxzz: Array4i64
    wxzw: Array4i64
    wxwx: Array4i64
    wxwy: Array4i64
    wxwz: Array4i64
    wxww: Array4i64
    wyxx: Array4i64
    wyxy: Array4i64
    wyxz: Array4i64
    wyxw: Array4i64
    wyyx: Array4i64
    wyyy: Array4i64
    wyyz: Array4i64
    wyyw: Array4i64
    wyzx: Array4i64
    wyzy: Array4i64
    wyzz: Array4i64
    wyzw: Array4i64
    wywx: Array4i64
    wywy: Array4i64
    wywz: Array4i64
    wyww: Array4i64
    wzxx: Array4i64
    wzxy: Array4i64
    wzxz: Array4i64
    wzxw: Array4i64
    wzyx: Array4i64
    wzyy: Array4i64
    wzyz: Array4i64
    wzyw: Array4i64
    wzzx: Array4i64
    wzzy: Array4i64
    wzzz: Array4i64
    wzzw: Array4i64
    wzwx: Array4i64
    wzwy: Array4i64
    wzwz: Array4i64
    wzww: Array4i64
    wwxx: Array4i64
    wwxy: Array4i64
    wwxz: Array4i64
    wwxw: Array4i64
    wwyx: Array4i64
    wwyy: Array4i64
    wwyz: Array4i64
    wwyw: Array4i64
    wwzx: Array4i64
    wwzy: Array4i64
    wwzz: Array4i64
    wwzw: Array4i64
    wwwx: Array4i64
    wwwy: Array4i64
    wwwz: Array4i64
    wwww: Array4i64

_Array0u64Cp: TypeAlias = Union['Array0u64', '_UInt64Cp', 'drjit.scalar._Array0u64Cp', 'drjit.llvm._Array0u64Cp', '_Array0i64Cp']

class Array0u64(drjit.ArrayBase[Array0u64, _Array0u64Cp, UInt64, _UInt64Cp, UInt64, Array0u64, Array0b]):
    xx: Array2u64
    xy: Array2u64
    xz: Array2u64
    xw: Array2u64
    yx: Array2u64
    yy: Array2u64
    yz: Array2u64
    yw: Array2u64
    zx: Array2u64
    zy: Array2u64
    zz: Array2u64
    zw: Array2u64
    wx: Array2u64
    wy: Array2u64
    wz: Array2u64
    ww: Array2u64
    xxx: Array3u64
    xxy: Array3u64
    xxz: Array3u64
    xxw: Array3u64
    xyx: Array3u64
    xyy: Array3u64
    xyz: Array3u64
    xyw: Array3u64
    xzx: Array3u64
    xzy: Array3u64
    xzz: Array3u64
    xzw: Array3u64
    xwx: Array3u64
    xwy: Array3u64
    xwz: Array3u64
    xww: Array3u64
    yxx: Array3u64
    yxy: Array3u64
    yxz: Array3u64
    yxw: Array3u64
    yyx: Array3u64
    yyy: Array3u64
    yyz: Array3u64
    yyw: Array3u64
    yzx: Array3u64
    yzy: Array3u64
    yzz: Array3u64
    yzw: Array3u64
    ywx: Array3u64
    ywy: Array3u64
    ywz: Array3u64
    yww: Array3u64
    zxx: Array3u64
    zxy: Array3u64
    zxz: Array3u64
    zxw: Array3u64
    zyx: Array3u64
    zyy: Array3u64
    zyz: Array3u64
    zyw: Array3u64
    zzx: Array3u64
    zzy: Array3u64
    zzz: Array3u64
    zzw: Array3u64
    zwx: Array3u64
    zwy: Array3u64
    zwz: Array3u64
    zww: Array3u64
    wxx: Array3u64
    wxy: Array3u64
    wxz: Array3u64
    wxw: Array3u64
    wyx: Array3u64
    wyy: Array3u64
    wyz: Array3u64
    wyw: Array3u64
    wzx: Array3u64
    wzy: Array3u64
    wzz: Array3u64
    wzw: Array3u64
    wwx: Array3u64
    wwy: Array3u64
    wwz: Array3u64
    www: Array3u64
    xxxx: Array4u64
    xxxy: Array4u64
    xxxz: Array4u64
    xxxw: Array4u64
    xxyx: Array4u64
    xxyy: Array4u64
    xxyz: Array4u64
    xxyw: Array4u64
    xxzx: Array4u64
    xxzy: Array4u64
    xxzz: Array4u64
    xxzw: Array4u64
    xxwx: Array4u64
    xxwy: Array4u64
    xxwz: Array4u64
    xxww: Array4u64
    xyxx: Array4u64
    xyxy: Array4u64
    xyxz: Array4u64
    xyxw: Array4u64
    xyyx: Array4u64
    xyyy: Array4u64
    xyyz: Array4u64
    xyyw: Array4u64
    xyzx: Array4u64
    xyzy: Array4u64
    xyzz: Array4u64
    xyzw: Array4u64
    xywx: Array4u64
    xywy: Array4u64
    xywz: Array4u64
    xyww: Array4u64
    xzxx: Array4u64
    xzxy: Array4u64
    xzxz: Array4u64
    xzxw: Array4u64
    xzyx: Array4u64
    xzyy: Array4u64
    xzyz: Array4u64
    xzyw: Array4u64
    xzzx: Array4u64
    xzzy: Array4u64
    xzzz: Array4u64
    xzzw: Array4u64
    xzwx: Array4u64
    xzwy: Array4u64
    xzwz: Array4u64
    xzww: Array4u64
    xwxx: Array4u64
    xwxy: Array4u64
    xwxz: Array4u64
    xwxw: Array4u64
    xwyx: Array4u64
    xwyy: Array4u64
    xwyz: Array4u64
    xwyw: Array4u64
    xwzx: Array4u64
    xwzy: Array4u64
    xwzz: Array4u64
    xwzw: Array4u64
    xwwx: Array4u64
    xwwy: Array4u64
    xwwz: Array4u64
    xwww: Array4u64
    yxxx: Array4u64
    yxxy: Array4u64
    yxxz: Array4u64
    yxxw: Array4u64
    yxyx: Array4u64
    yxyy: Array4u64
    yxyz: Array4u64
    yxyw: Array4u64
    yxzx: Array4u64
    yxzy: Array4u64
    yxzz: Array4u64
    yxzw: Array4u64
    yxwx: Array4u64
    yxwy: Array4u64
    yxwz: Array4u64
    yxww: Array4u64
    yyxx: Array4u64
    yyxy: Array4u64
    yyxz: Array4u64
    yyxw: Array4u64
    yyyx: Array4u64
    yyyy: Array4u64
    yyyz: Array4u64
    yyyw: Array4u64
    yyzx: Array4u64
    yyzy: Array4u64
    yyzz: Array4u64
    yyzw: Array4u64
    yywx: Array4u64
    yywy: Array4u64
    yywz: Array4u64
    yyww: Array4u64
    yzxx: Array4u64
    yzxy: Array4u64
    yzxz: Array4u64
    yzxw: Array4u64
    yzyx: Array4u64
    yzyy: Array4u64
    yzyz: Array4u64
    yzyw: Array4u64
    yzzx: Array4u64
    yzzy: Array4u64
    yzzz: Array4u64
    yzzw: Array4u64
    yzwx: Array4u64
    yzwy: Array4u64
    yzwz: Array4u64
    yzww: Array4u64
    ywxx: Array4u64
    ywxy: Array4u64
    ywxz: Array4u64
    ywxw: Array4u64
    ywyx: Array4u64
    ywyy: Array4u64
    ywyz: Array4u64
    ywyw: Array4u64
    ywzx: Array4u64
    ywzy: Array4u64
    ywzz: Array4u64
    ywzw: Array4u64
    ywwx: Array4u64
    ywwy: Array4u64
    ywwz: Array4u64
    ywww: Array4u64
    zxxx: Array4u64
    zxxy: Array4u64
    zxxz: Array4u64
    zxxw: Array4u64
    zxyx: Array4u64
    zxyy: Array4u64
    zxyz: Array4u64
    zxyw: Array4u64
    zxzx: Array4u64
    zxzy: Array4u64
    zxzz: Array4u64
    zxzw: Array4u64
    zxwx: Array4u64
    zxwy: Array4u64
    zxwz: Array4u64
    zxww: Array4u64
    zyxx: Array4u64
    zyxy: Array4u64
    zyxz: Array4u64
    zyxw: Array4u64
    zyyx: Array4u64
    zyyy: Array4u64
    zyyz: Array4u64
    zyyw: Array4u64
    zyzx: Array4u64
    zyzy: Array4u64
    zyzz: Array4u64
    zyzw: Array4u64
    zywx: Array4u64
    zywy: Array4u64
    zywz: Array4u64
    zyww: Array4u64
    zzxx: Array4u64
    zzxy: Array4u64
    zzxz: Array4u64
    zzxw: Array4u64
    zzyx: Array4u64
    zzyy: Array4u64
    zzyz: Array4u64
    zzyw: Array4u64
    zzzx: Array4u64
    zzzy: Array4u64
    zzzz: Array4u64
    zzzw: Array4u64
    zzwx: Array4u64
    zzwy: Array4u64
    zzwz: Array4u64
    zzww: Array4u64
    zwxx: Array4u64
    zwxy: Array4u64
    zwxz: Array4u64
    zwxw: Array4u64
    zwyx: Array4u64
    zwyy: Array4u64
    zwyz: Array4u64
    zwyw: Array4u64
    zwzx: Array4u64
    zwzy: Array4u64
    zwzz: Array4u64
    zwzw: Array4u64
    zwwx: Array4u64
    zwwy: Array4u64
    zwwz: Array4u64
    zwww: Array4u64
    wxxx: Array4u64
    wxxy: Array4u64
    wxxz: Array4u64
    wxxw: Array4u64
    wxyx: Array4u64
    wxyy: Array4u64
    wxyz: Array4u64
    wxyw: Array4u64
    wxzx: Array4u64
    wxzy: Array4u64
    wxzz: Array4u64
    wxzw: Array4u64
    wxwx: Array4u64
    wxwy: Array4u64
    wxwz: Array4u64
    wxww: Array4u64
    wyxx: Array4u64
    wyxy: Array4u64
    wyxz: Array4u64
    wyxw: Array4u64
    wyyx: Array4u64
    wyyy: Array4u64
    wyyz: Array4u64
    wyyw: Array4u64
    wyzx: Array4u64
    wyzy: Array4u64
    wyzz: Array4u64
    wyzw: Array4u64
    wywx: Array4u64
    wywy: Array4u64
    wywz: Array4u64
    wyww: Array4u64
    wzxx: Array4u64
    wzxy: Array4u64
    wzxz: Array4u64
    wzxw: Array4u64
    wzyx: Array4u64
    wzyy: Array4u64
    wzyz: Array4u64
    wzyw: Array4u64
    wzzx: Array4u64
    wzzy: Array4u64
    wzzz: Array4u64
    wzzw: Array4u64
    wzwx: Array4u64
    wzwy: Array4u64
    wzwz: Array4u64
    wzww: Array4u64
    wwxx: Array4u64
    wwxy: Array4u64
    wwxz: Array4u64
    wwxw: Array4u64
    wwyx: Array4u64
    wwyy: Array4u64
    wwyz: Array4u64
    wwyw: Array4u64
    wwzx: Array4u64
    wwzy: Array4u64
    wwzz: Array4u64
    wwzw: Array4u64
    wwwx: Array4u64
    wwwy: Array4u64
    wwwz: Array4u64
    wwww: Array4u64

_Array0f16Cp: TypeAlias = Union['Array0f16', '_Float16Cp', 'drjit.scalar._Array0f16Cp', 'drjit.llvm._Array0f16Cp', '_Array0u64Cp']

class Array0f16(drjit.ArrayBase[Array0f16, _Array0f16Cp, Float16, _Float16Cp, Float16, Array0f16, Array0b]):
    xx: Array2f16
    xy: Array2f16
    xz: Array2f16
    xw: Array2f16
    yx: Array2f16
    yy: Array2f16
    yz: Array2f16
    yw: Array2f16
    zx: Array2f16
    zy: Array2f16
    zz: Array2f16
    zw: Array2f16
    wx: Array2f16
    wy: Array2f16
    wz: Array2f16
    ww: Array2f16
    xxx: Array3f16
    xxy: Array3f16
    xxz: Array3f16
    xxw: Array3f16
    xyx: Array3f16
    xyy: Array3f16
    xyz: Array3f16
    xyw: Array3f16
    xzx: Array3f16
    xzy: Array3f16
    xzz: Array3f16
    xzw: Array3f16
    xwx: Array3f16
    xwy: Array3f16
    xwz: Array3f16
    xww: Array3f16
    yxx: Array3f16
    yxy: Array3f16
    yxz: Array3f16
    yxw: Array3f16
    yyx: Array3f16
    yyy: Array3f16
    yyz: Array3f16
    yyw: Array3f16
    yzx: Array3f16
    yzy: Array3f16
    yzz: Array3f16
    yzw: Array3f16
    ywx: Array3f16
    ywy: Array3f16
    ywz: Array3f16
    yww: Array3f16
    zxx: Array3f16
    zxy: Array3f16
    zxz: Array3f16
    zxw: Array3f16
    zyx: Array3f16
    zyy: Array3f16
    zyz: Array3f16
    zyw: Array3f16
    zzx: Array3f16
    zzy: Array3f16
    zzz: Array3f16
    zzw: Array3f16
    zwx: Array3f16
    zwy: Array3f16
    zwz: Array3f16
    zww: Array3f16
    wxx: Array3f16
    wxy: Array3f16
    wxz: Array3f16
    wxw: Array3f16
    wyx: Array3f16
    wyy: Array3f16
    wyz: Array3f16
    wyw: Array3f16
    wzx: Array3f16
    wzy: Array3f16
    wzz: Array3f16
    wzw: Array3f16
    wwx: Array3f16
    wwy: Array3f16
    wwz: Array3f16
    www: Array3f16
    xxxx: Array4f16
    xxxy: Array4f16
    xxxz: Array4f16
    xxxw: Array4f16
    xxyx: Array4f16
    xxyy: Array4f16
    xxyz: Array4f16
    xxyw: Array4f16
    xxzx: Array4f16
    xxzy: Array4f16
    xxzz: Array4f16
    xxzw: Array4f16
    xxwx: Array4f16
    xxwy: Array4f16
    xxwz: Array4f16
    xxww: Array4f16
    xyxx: Array4f16
    xyxy: Array4f16
    xyxz: Array4f16
    xyxw: Array4f16
    xyyx: Array4f16
    xyyy: Array4f16
    xyyz: Array4f16
    xyyw: Array4f16
    xyzx: Array4f16
    xyzy: Array4f16
    xyzz: Array4f16
    xyzw: Array4f16
    xywx: Array4f16
    xywy: Array4f16
    xywz: Array4f16
    xyww: Array4f16
    xzxx: Array4f16
    xzxy: Array4f16
    xzxz: Array4f16
    xzxw: Array4f16
    xzyx: Array4f16
    xzyy: Array4f16
    xzyz: Array4f16
    xzyw: Array4f16
    xzzx: Array4f16
    xzzy: Array4f16
    xzzz: Array4f16
    xzzw: Array4f16
    xzwx: Array4f16
    xzwy: Array4f16
    xzwz: Array4f16
    xzww: Array4f16
    xwxx: Array4f16
    xwxy: Array4f16
    xwxz: Array4f16
    xwxw: Array4f16
    xwyx: Array4f16
    xwyy: Array4f16
    xwyz: Array4f16
    xwyw: Array4f16
    xwzx: Array4f16
    xwzy: Array4f16
    xwzz: Array4f16
    xwzw: Array4f16
    xwwx: Array4f16
    xwwy: Array4f16
    xwwz: Array4f16
    xwww: Array4f16
    yxxx: Array4f16
    yxxy: Array4f16
    yxxz: Array4f16
    yxxw: Array4f16
    yxyx: Array4f16
    yxyy: Array4f16
    yxyz: Array4f16
    yxyw: Array4f16
    yxzx: Array4f16
    yxzy: Array4f16
    yxzz: Array4f16
    yxzw: Array4f16
    yxwx: Array4f16
    yxwy: Array4f16
    yxwz: Array4f16
    yxww: Array4f16
    yyxx: Array4f16
    yyxy: Array4f16
    yyxz: Array4f16
    yyxw: Array4f16
    yyyx: Array4f16
    yyyy: Array4f16
    yyyz: Array4f16
    yyyw: Array4f16
    yyzx: Array4f16
    yyzy: Array4f16
    yyzz: Array4f16
    yyzw: Array4f16
    yywx: Array4f16
    yywy: Array4f16
    yywz: Array4f16
    yyww: Array4f16
    yzxx: Array4f16
    yzxy: Array4f16
    yzxz: Array4f16
    yzxw: Array4f16
    yzyx: Array4f16
    yzyy: Array4f16
    yzyz: Array4f16
    yzyw: Array4f16
    yzzx: Array4f16
    yzzy: Array4f16
    yzzz: Array4f16
    yzzw: Array4f16
    yzwx: Array4f16
    yzwy: Array4f16
    yzwz: Array4f16
    yzww: Array4f16
    ywxx: Array4f16
    ywxy: Array4f16
    ywxz: Array4f16
    ywxw: Array4f16
    ywyx: Array4f16
    ywyy: Array4f16
    ywyz: Array4f16
    ywyw: Array4f16
    ywzx: Array4f16
    ywzy: Array4f16
    ywzz: Array4f16
    ywzw: Array4f16
    ywwx: Array4f16
    ywwy: Array4f16
    ywwz: Array4f16
    ywww: Array4f16
    zxxx: Array4f16
    zxxy: Array4f16
    zxxz: Array4f16
    zxxw: Array4f16
    zxyx: Array4f16
    zxyy: Array4f16
    zxyz: Array4f16
    zxyw: Array4f16
    zxzx: Array4f16
    zxzy: Array4f16
    zxzz: Array4f16
    zxzw: Array4f16
    zxwx: Array4f16
    zxwy: Array4f16
    zxwz: Array4f16
    zxww: Array4f16
    zyxx: Array4f16
    zyxy: Array4f16
    zyxz: Array4f16
    zyxw: Array4f16
    zyyx: Array4f16
    zyyy: Array4f16
    zyyz: Array4f16
    zyyw: Array4f16
    zyzx: Array4f16
    zyzy: Array4f16
    zyzz: Array4f16
    zyzw: Array4f16
    zywx: Array4f16
    zywy: Array4f16
    zywz: Array4f16
    zyww: Array4f16
    zzxx: Array4f16
    zzxy: Array4f16
    zzxz: Array4f16
    zzxw: Array4f16
    zzyx: Array4f16
    zzyy: Array4f16
    zzyz: Array4f16
    zzyw: Array4f16
    zzzx: Array4f16
    zzzy: Array4f16
    zzzz: Array4f16
    zzzw: Array4f16
    zzwx: Array4f16
    zzwy: Array4f16
    zzwz: Array4f16
    zzww: Array4f16
    zwxx: Array4f16
    zwxy: Array4f16
    zwxz: Array4f16
    zwxw: Array4f16
    zwyx: Array4f16
    zwyy: Array4f16
    zwyz: Array4f16
    zwyw: Array4f16
    zwzx: Array4f16
    zwzy: Array4f16
    zwzz: Array4f16
    zwzw: Array4f16
    zwwx: Array4f16
    zwwy: Array4f16
    zwwz: Array4f16
    zwww: Array4f16
    wxxx: Array4f16
    wxxy: Array4f16
    wxxz: Array4f16
    wxxw: Array4f16
    wxyx: Array4f16
    wxyy: Array4f16
    wxyz: Array4f16
    wxyw: Array4f16
    wxzx: Array4f16
    wxzy: Array4f16
    wxzz: Array4f16
    wxzw: Array4f16
    wxwx: Array4f16
    wxwy: Array4f16
    wxwz: Array4f16
    wxww: Array4f16
    wyxx: Array4f16
    wyxy: Array4f16
    wyxz: Array4f16
    wyxw: Array4f16
    wyyx: Array4f16
    wyyy: Array4f16
    wyyz: Array4f16
    wyyw: Array4f16
    wyzx: Array4f16
    wyzy: Array4f16
    wyzz: Array4f16
    wyzw: Array4f16
    wywx: Array4f16
    wywy: Array4f16
    wywz: Array4f16
    wyww: Array4f16
    wzxx: Array4f16
    wzxy: Array4f16
    wzxz: Array4f16
    wzxw: Array4f16
    wzyx: Array4f16
    wzyy: Array4f16
    wzyz: Array4f16
    wzyw: Array4f16
    wzzx: Array4f16
    wzzy: Array4f16
    wzzz: Array4f16
    wzzw: Array4f16
    wzwx: Array4f16
    wzwy: Array4f16
    wzwz: Array4f16
    wzww: Array4f16
    wwxx: Array4f16
    wwxy: Array4f16
    wwxz: Array4f16
    wwxw: Array4f16
    wwyx: Array4f16
    wwyy: Array4f16
    wwyz: Array4f16
    wwyw: Array4f16
    wwzx: Array4f16
    wwzy: Array4f16
    wwzz: Array4f16
    wwzw: Array4f16
    wwwx: Array4f16
    wwwy: Array4f16
    wwwz: Array4f16
    wwww: Array4f16

_Array0fCp: TypeAlias = Union['Array0f', '_FloatCp', 'drjit.scalar._Array0fCp', 'drjit.llvm._Array0fCp', '_Array0f16Cp']

class Array0f(drjit.ArrayBase[Array0f, _Array0fCp, Float, _FloatCp, Float, Array0f, Array0b]):
    xx: Array2f
    xy: Array2f
    xz: Array2f
    xw: Array2f
    yx: Array2f
    yy: Array2f
    yz: Array2f
    yw: Array2f
    zx: Array2f
    zy: Array2f
    zz: Array2f
    zw: Array2f
    wx: Array2f
    wy: Array2f
    wz: Array2f
    ww: Array2f
    xxx: Array3f
    xxy: Array3f
    xxz: Array3f
    xxw: Array3f
    xyx: Array3f
    xyy: Array3f
    xyz: Array3f
    xyw: Array3f
    xzx: Array3f
    xzy: Array3f
    xzz: Array3f
    xzw: Array3f
    xwx: Array3f
    xwy: Array3f
    xwz: Array3f
    xww: Array3f
    yxx: Array3f
    yxy: Array3f
    yxz: Array3f
    yxw: Array3f
    yyx: Array3f
    yyy: Array3f
    yyz: Array3f
    yyw: Array3f
    yzx: Array3f
    yzy: Array3f
    yzz: Array3f
    yzw: Array3f
    ywx: Array3f
    ywy: Array3f
    ywz: Array3f
    yww: Array3f
    zxx: Array3f
    zxy: Array3f
    zxz: Array3f
    zxw: Array3f
    zyx: Array3f
    zyy: Array3f
    zyz: Array3f
    zyw: Array3f
    zzx: Array3f
    zzy: Array3f
    zzz: Array3f
    zzw: Array3f
    zwx: Array3f
    zwy: Array3f
    zwz: Array3f
    zww: Array3f
    wxx: Array3f
    wxy: Array3f
    wxz: Array3f
    wxw: Array3f
    wyx: Array3f
    wyy: Array3f
    wyz: Array3f
    wyw: Array3f
    wzx: Array3f
    wzy: Array3f
    wzz: Array3f
    wzw: Array3f
    wwx: Array3f
    wwy: Array3f
    wwz: Array3f
    www: Array3f
    xxxx: Array4f
    xxxy: Array4f
    xxxz: Array4f
    xxxw: Array4f
    xxyx: Array4f
    xxyy: Array4f
    xxyz: Array4f
    xxyw: Array4f
    xxzx: Array4f
    xxzy: Array4f
    xxzz: Array4f
    xxzw: Array4f
    xxwx: Array4f
    xxwy: Array4f
    xxwz: Array4f
    xxww: Array4f
    xyxx: Array4f
    xyxy: Array4f
    xyxz: Array4f
    xyxw: Array4f
    xyyx: Array4f
    xyyy: Array4f
    xyyz: Array4f
    xyyw: Array4f
    xyzx: Array4f
    xyzy: Array4f
    xyzz: Array4f
    xyzw: Array4f
    xywx: Array4f
    xywy: Array4f
    xywz: Array4f
    xyww: Array4f
    xzxx: Array4f
    xzxy: Array4f
    xzxz: Array4f
    xzxw: Array4f
    xzyx: Array4f
    xzyy: Array4f
    xzyz: Array4f
    xzyw: Array4f
    xzzx: Array4f
    xzzy: Array4f
    xzzz: Array4f
    xzzw: Array4f
    xzwx: Array4f
    xzwy: Array4f
    xzwz: Array4f
    xzww: Array4f
    xwxx: Array4f
    xwxy: Array4f
    xwxz: Array4f
    xwxw: Array4f
    xwyx: Array4f
    xwyy: Array4f
    xwyz: Array4f
    xwyw: Array4f
    xwzx: Array4f
    xwzy: Array4f
    xwzz: Array4f
    xwzw: Array4f
    xwwx: Array4f
    xwwy: Array4f
    xwwz: Array4f
    xwww: Array4f
    yxxx: Array4f
    yxxy: Array4f
    yxxz: Array4f
    yxxw: Array4f
    yxyx: Array4f
    yxyy: Array4f
    yxyz: Array4f
    yxyw: Array4f
    yxzx: Array4f
    yxzy: Array4f
    yxzz: Array4f
    yxzw: Array4f
    yxwx: Array4f
    yxwy: Array4f
    yxwz: Array4f
    yxww: Array4f
    yyxx: Array4f
    yyxy: Array4f
    yyxz: Array4f
    yyxw: Array4f
    yyyx: Array4f
    yyyy: Array4f
    yyyz: Array4f
    yyyw: Array4f
    yyzx: Array4f
    yyzy: Array4f
    yyzz: Array4f
    yyzw: Array4f
    yywx: Array4f
    yywy: Array4f
    yywz: Array4f
    yyww: Array4f
    yzxx: Array4f
    yzxy: Array4f
    yzxz: Array4f
    yzxw: Array4f
    yzyx: Array4f
    yzyy: Array4f
    yzyz: Array4f
    yzyw: Array4f
    yzzx: Array4f
    yzzy: Array4f
    yzzz: Array4f
    yzzw: Array4f
    yzwx: Array4f
    yzwy: Array4f
    yzwz: Array4f
    yzww: Array4f
    ywxx: Array4f
    ywxy: Array4f
    ywxz: Array4f
    ywxw: Array4f
    ywyx: Array4f
    ywyy: Array4f
    ywyz: Array4f
    ywyw: Array4f
    ywzx: Array4f
    ywzy: Array4f
    ywzz: Array4f
    ywzw: Array4f
    ywwx: Array4f
    ywwy: Array4f
    ywwz: Array4f
    ywww: Array4f
    zxxx: Array4f
    zxxy: Array4f
    zxxz: Array4f
    zxxw: Array4f
    zxyx: Array4f
    zxyy: Array4f
    zxyz: Array4f
    zxyw: Array4f
    zxzx: Array4f
    zxzy: Array4f
    zxzz: Array4f
    zxzw: Array4f
    zxwx: Array4f
    zxwy: Array4f
    zxwz: Array4f
    zxww: Array4f
    zyxx: Array4f
    zyxy: Array4f
    zyxz: Array4f
    zyxw: Array4f
    zyyx: Array4f
    zyyy: Array4f
    zyyz: Array4f
    zyyw: Array4f
    zyzx: Array4f
    zyzy: Array4f
    zyzz: Array4f
    zyzw: Array4f
    zywx: Array4f
    zywy: Array4f
    zywz: Array4f
    zyww: Array4f
    zzxx: Array4f
    zzxy: Array4f
    zzxz: Array4f
    zzxw: Array4f
    zzyx: Array4f
    zzyy: Array4f
    zzyz: Array4f
    zzyw: Array4f
    zzzx: Array4f
    zzzy: Array4f
    zzzz: Array4f
    zzzw: Array4f
    zzwx: Array4f
    zzwy: Array4f
    zzwz: Array4f
    zzww: Array4f
    zwxx: Array4f
    zwxy: Array4f
    zwxz: Array4f
    zwxw: Array4f
    zwyx: Array4f
    zwyy: Array4f
    zwyz: Array4f
    zwyw: Array4f
    zwzx: Array4f
    zwzy: Array4f
    zwzz: Array4f
    zwzw: Array4f
    zwwx: Array4f
    zwwy: Array4f
    zwwz: Array4f
    zwww: Array4f
    wxxx: Array4f
    wxxy: Array4f
    wxxz: Array4f
    wxxw: Array4f
    wxyx: Array4f
    wxyy: Array4f
    wxyz: Array4f
    wxyw: Array4f
    wxzx: Array4f
    wxzy: Array4f
    wxzz: Array4f
    wxzw: Array4f
    wxwx: Array4f
    wxwy: Array4f
    wxwz: Array4f
    wxww: Array4f
    wyxx: Array4f
    wyxy: Array4f
    wyxz: Array4f
    wyxw: Array4f
    wyyx: Array4f
    wyyy: Array4f
    wyyz: Array4f
    wyyw: Array4f
    wyzx: Array4f
    wyzy: Array4f
    wyzz: Array4f
    wyzw: Array4f
    wywx: Array4f
    wywy: Array4f
    wywz: Array4f
    wyww: Array4f
    wzxx: Array4f
    wzxy: Array4f
    wzxz: Array4f
    wzxw: Array4f
    wzyx: Array4f
    wzyy: Array4f
    wzyz: Array4f
    wzyw: Array4f
    wzzx: Array4f
    wzzy: Array4f
    wzzz: Array4f
    wzzw: Array4f
    wzwx: Array4f
    wzwy: Array4f
    wzwz: Array4f
    wzww: Array4f
    wwxx: Array4f
    wwxy: Array4f
    wwxz: Array4f
    wwxw: Array4f
    wwyx: Array4f
    wwyy: Array4f
    wwyz: Array4f
    wwyw: Array4f
    wwzx: Array4f
    wwzy: Array4f
    wwzz: Array4f
    wwzw: Array4f
    wwwx: Array4f
    wwwy: Array4f
    wwwz: Array4f
    wwww: Array4f

_Array0f64Cp: TypeAlias = Union['Array0f64', '_Float64Cp', 'drjit.scalar._Array0f64Cp', 'drjit.llvm._Array0f64Cp', '_Array0fCp']

class Array0f64(drjit.ArrayBase[Array0f64, _Array0f64Cp, Float64, _Float64Cp, Float64, Array0f64, Array0b]):
    xx: Array2f64
    xy: Array2f64
    xz: Array2f64
    xw: Array2f64
    yx: Array2f64
    yy: Array2f64
    yz: Array2f64
    yw: Array2f64
    zx: Array2f64
    zy: Array2f64
    zz: Array2f64
    zw: Array2f64
    wx: Array2f64
    wy: Array2f64
    wz: Array2f64
    ww: Array2f64
    xxx: Array3f64
    xxy: Array3f64
    xxz: Array3f64
    xxw: Array3f64
    xyx: Array3f64
    xyy: Array3f64
    xyz: Array3f64
    xyw: Array3f64
    xzx: Array3f64
    xzy: Array3f64
    xzz: Array3f64
    xzw: Array3f64
    xwx: Array3f64
    xwy: Array3f64
    xwz: Array3f64
    xww: Array3f64
    yxx: Array3f64
    yxy: Array3f64
    yxz: Array3f64
    yxw: Array3f64
    yyx: Array3f64
    yyy: Array3f64
    yyz: Array3f64
    yyw: Array3f64
    yzx: Array3f64
    yzy: Array3f64
    yzz: Array3f64
    yzw: Array3f64
    ywx: Array3f64
    ywy: Array3f64
    ywz: Array3f64
    yww: Array3f64
    zxx: Array3f64
    zxy: Array3f64
    zxz: Array3f64
    zxw: Array3f64
    zyx: Array3f64
    zyy: Array3f64
    zyz: Array3f64
    zyw: Array3f64
    zzx: Array3f64
    zzy: Array3f64
    zzz: Array3f64
    zzw: Array3f64
    zwx: Array3f64
    zwy: Array3f64
    zwz: Array3f64
    zww: Array3f64
    wxx: Array3f64
    wxy: Array3f64
    wxz: Array3f64
    wxw: Array3f64
    wyx: Array3f64
    wyy: Array3f64
    wyz: Array3f64
    wyw: Array3f64
    wzx: Array3f64
    wzy: Array3f64
    wzz: Array3f64
    wzw: Array3f64
    wwx: Array3f64
    wwy: Array3f64
    wwz: Array3f64
    www: Array3f64
    xxxx: Array4f64
    xxxy: Array4f64
    xxxz: Array4f64
    xxxw: Array4f64
    xxyx: Array4f64
    xxyy: Array4f64
    xxyz: Array4f64
    xxyw: Array4f64
    xxzx: Array4f64
    xxzy: Array4f64
    xxzz: Array4f64
    xxzw: Array4f64
    xxwx: Array4f64
    xxwy: Array4f64
    xxwz: Array4f64
    xxww: Array4f64
    xyxx: Array4f64
    xyxy: Array4f64
    xyxz: Array4f64
    xyxw: Array4f64
    xyyx: Array4f64
    xyyy: Array4f64
    xyyz: Array4f64
    xyyw: Array4f64
    xyzx: Array4f64
    xyzy: Array4f64
    xyzz: Array4f64
    xyzw: Array4f64
    xywx: Array4f64
    xywy: Array4f64
    xywz: Array4f64
    xyww: Array4f64
    xzxx: Array4f64
    xzxy: Array4f64
    xzxz: Array4f64
    xzxw: Array4f64
    xzyx: Array4f64
    xzyy: Array4f64
    xzyz: Array4f64
    xzyw: Array4f64
    xzzx: Array4f64
    xzzy: Array4f64
    xzzz: Array4f64
    xzzw: Array4f64
    xzwx: Array4f64
    xzwy: Array4f64
    xzwz: Array4f64
    xzww: Array4f64
    xwxx: Array4f64
    xwxy: Array4f64
    xwxz: Array4f64
    xwxw: Array4f64
    xwyx: Array4f64
    xwyy: Array4f64
    xwyz: Array4f64
    xwyw: Array4f64
    xwzx: Array4f64
    xwzy: Array4f64
    xwzz: Array4f64
    xwzw: Array4f64
    xwwx: Array4f64
    xwwy: Array4f64
    xwwz: Array4f64
    xwww: Array4f64
    yxxx: Array4f64
    yxxy: Array4f64
    yxxz: Array4f64
    yxxw: Array4f64
    yxyx: Array4f64
    yxyy: Array4f64
    yxyz: Array4f64
    yxyw: Array4f64
    yxzx: Array4f64
    yxzy: Array4f64
    yxzz: Array4f64
    yxzw: Array4f64
    yxwx: Array4f64
    yxwy: Array4f64
    yxwz: Array4f64
    yxww: Array4f64
    yyxx: Array4f64
    yyxy: Array4f64
    yyxz: Array4f64
    yyxw: Array4f64
    yyyx: Array4f64
    yyyy: Array4f64
    yyyz: Array4f64
    yyyw: Array4f64
    yyzx: Array4f64
    yyzy: Array4f64
    yyzz: Array4f64
    yyzw: Array4f64
    yywx: Array4f64
    yywy: Array4f64
    yywz: Array4f64
    yyww: Array4f64
    yzxx: Array4f64
    yzxy: Array4f64
    yzxz: Array4f64
    yzxw: Array4f64
    yzyx: Array4f64
    yzyy: Array4f64
    yzyz: Array4f64
    yzyw: Array4f64
    yzzx: Array4f64
    yzzy: Array4f64
    yzzz: Array4f64
    yzzw: Array4f64
    yzwx: Array4f64
    yzwy: Array4f64
    yzwz: Array4f64
    yzww: Array4f64
    ywxx: Array4f64
    ywxy: Array4f64
    ywxz: Array4f64
    ywxw: Array4f64
    ywyx: Array4f64
    ywyy: Array4f64
    ywyz: Array4f64
    ywyw: Array4f64
    ywzx: Array4f64
    ywzy: Array4f64
    ywzz: Array4f64
    ywzw: Array4f64
    ywwx: Array4f64
    ywwy: Array4f64
    ywwz: Array4f64
    ywww: Array4f64
    zxxx: Array4f64
    zxxy: Array4f64
    zxxz: Array4f64
    zxxw: Array4f64
    zxyx: Array4f64
    zxyy: Array4f64
    zxyz: Array4f64
    zxyw: Array4f64
    zxzx: Array4f64
    zxzy: Array4f64
    zxzz: Array4f64
    zxzw: Array4f64
    zxwx: Array4f64
    zxwy: Array4f64
    zxwz: Array4f64
    zxww: Array4f64
    zyxx: Array4f64
    zyxy: Array4f64
    zyxz: Array4f64
    zyxw: Array4f64
    zyyx: Array4f64
    zyyy: Array4f64
    zyyz: Array4f64
    zyyw: Array4f64
    zyzx: Array4f64
    zyzy: Array4f64
    zyzz: Array4f64
    zyzw: Array4f64
    zywx: Array4f64
    zywy: Array4f64
    zywz: Array4f64
    zyww: Array4f64
    zzxx: Array4f64
    zzxy: Array4f64
    zzxz: Array4f64
    zzxw: Array4f64
    zzyx: Array4f64
    zzyy: Array4f64
    zzyz: Array4f64
    zzyw: Array4f64
    zzzx: Array4f64
    zzzy: Array4f64
    zzzz: Array4f64
    zzzw: Array4f64
    zzwx: Array4f64
    zzwy: Array4f64
    zzwz: Array4f64
    zzww: Array4f64
    zwxx: Array4f64
    zwxy: Array4f64
    zwxz: Array4f64
    zwxw: Array4f64
    zwyx: Array4f64
    zwyy: Array4f64
    zwyz: Array4f64
    zwyw: Array4f64
    zwzx: Array4f64
    zwzy: Array4f64
    zwzz: Array4f64
    zwzw: Array4f64
    zwwx: Array4f64
    zwwy: Array4f64
    zwwz: Array4f64
    zwww: Array4f64
    wxxx: Array4f64
    wxxy: Array4f64
    wxxz: Array4f64
    wxxw: Array4f64
    wxyx: Array4f64
    wxyy: Array4f64
    wxyz: Array4f64
    wxyw: Array4f64
    wxzx: Array4f64
    wxzy: Array4f64
    wxzz: Array4f64
    wxzw: Array4f64
    wxwx: Array4f64
    wxwy: Array4f64
    wxwz: Array4f64
    wxww: Array4f64
    wyxx: Array4f64
    wyxy: Array4f64
    wyxz: Array4f64
    wyxw: Array4f64
    wyyx: Array4f64
    wyyy: Array4f64
    wyyz: Array4f64
    wyyw: Array4f64
    wyzx: Array4f64
    wyzy: Array4f64
    wyzz: Array4f64
    wyzw: Array4f64
    wywx: Array4f64
    wywy: Array4f64
    wywz: Array4f64
    wyww: Array4f64
    wzxx: Array4f64
    wzxy: Array4f64
    wzxz: Array4f64
    wzxw: Array4f64
    wzyx: Array4f64
    wzyy: Array4f64
    wzyz: Array4f64
    wzyw: Array4f64
    wzzx: Array4f64
    wzzy: Array4f64
    wzzz: Array4f64
    wzzw: Array4f64
    wzwx: Array4f64
    wzwy: Array4f64
    wzwz: Array4f64
    wzww: Array4f64
    wwxx: Array4f64
    wwxy: Array4f64
    wwxz: Array4f64
    wwxw: Array4f64
    wwyx: Array4f64
    wwyy: Array4f64
    wwyz: Array4f64
    wwyw: Array4f64
    wwzx: Array4f64
    wwzy: Array4f64
    wwzz: Array4f64
    wwzw: Array4f64
    wwwx: Array4f64
    wwwy: Array4f64
    wwwz: Array4f64
    wwww: Array4f64

_Array1bCp: TypeAlias = Union['Array1b', '_BoolCp', 'drjit.scalar._Array1bCp', 'drjit.llvm._Array1bCp']

class Array1b(drjit.ArrayBase[Array1b, _Array1bCp, Bool, _BoolCp, Bool, Array1b, Array1b]):
    xx: Array2b
    xy: Array2b
    xz: Array2b
    xw: Array2b
    yx: Array2b
    yy: Array2b
    yz: Array2b
    yw: Array2b
    zx: Array2b
    zy: Array2b
    zz: Array2b
    zw: Array2b
    wx: Array2b
    wy: Array2b
    wz: Array2b
    ww: Array2b
    xxx: Array3b
    xxy: Array3b
    xxz: Array3b
    xxw: Array3b
    xyx: Array3b
    xyy: Array3b
    xyz: Array3b
    xyw: Array3b
    xzx: Array3b
    xzy: Array3b
    xzz: Array3b
    xzw: Array3b
    xwx: Array3b
    xwy: Array3b
    xwz: Array3b
    xww: Array3b
    yxx: Array3b
    yxy: Array3b
    yxz: Array3b
    yxw: Array3b
    yyx: Array3b
    yyy: Array3b
    yyz: Array3b
    yyw: Array3b
    yzx: Array3b
    yzy: Array3b
    yzz: Array3b
    yzw: Array3b
    ywx: Array3b
    ywy: Array3b
    ywz: Array3b
    yww: Array3b
    zxx: Array3b
    zxy: Array3b
    zxz: Array3b
    zxw: Array3b
    zyx: Array3b
    zyy: Array3b
    zyz: Array3b
    zyw: Array3b
    zzx: Array3b
    zzy: Array3b
    zzz: Array3b
    zzw: Array3b
    zwx: Array3b
    zwy: Array3b
    zwz: Array3b
    zww: Array3b
    wxx: Array3b
    wxy: Array3b
    wxz: Array3b
    wxw: Array3b
    wyx: Array3b
    wyy: Array3b
    wyz: Array3b
    wyw: Array3b
    wzx: Array3b
    wzy: Array3b
    wzz: Array3b
    wzw: Array3b
    wwx: Array3b
    wwy: Array3b
    wwz: Array3b
    www: Array3b
    xxxx: Array4b
    xxxy: Array4b
    xxxz: Array4b
    xxxw: Array4b
    xxyx: Array4b
    xxyy: Array4b
    xxyz: Array4b
    xxyw: Array4b
    xxzx: Array4b
    xxzy: Array4b
    xxzz: Array4b
    xxzw: Array4b
    xxwx: Array4b
    xxwy: Array4b
    xxwz: Array4b
    xxww: Array4b
    xyxx: Array4b
    xyxy: Array4b
    xyxz: Array4b
    xyxw: Array4b
    xyyx: Array4b
    xyyy: Array4b
    xyyz: Array4b
    xyyw: Array4b
    xyzx: Array4b
    xyzy: Array4b
    xyzz: Array4b
    xyzw: Array4b
    xywx: Array4b
    xywy: Array4b
    xywz: Array4b
    xyww: Array4b
    xzxx: Array4b
    xzxy: Array4b
    xzxz: Array4b
    xzxw: Array4b
    xzyx: Array4b
    xzyy: Array4b
    xzyz: Array4b
    xzyw: Array4b
    xzzx: Array4b
    xzzy: Array4b
    xzzz: Array4b
    xzzw: Array4b
    xzwx: Array4b
    xzwy: Array4b
    xzwz: Array4b
    xzww: Array4b
    xwxx: Array4b
    xwxy: Array4b
    xwxz: Array4b
    xwxw: Array4b
    xwyx: Array4b
    xwyy: Array4b
    xwyz: Array4b
    xwyw: Array4b
    xwzx: Array4b
    xwzy: Array4b
    xwzz: Array4b
    xwzw: Array4b
    xwwx: Array4b
    xwwy: Array4b
    xwwz: Array4b
    xwww: Array4b
    yxxx: Array4b
    yxxy: Array4b
    yxxz: Array4b
    yxxw: Array4b
    yxyx: Array4b
    yxyy: Array4b
    yxyz: Array4b
    yxyw: Array4b
    yxzx: Array4b
    yxzy: Array4b
    yxzz: Array4b
    yxzw: Array4b
    yxwx: Array4b
    yxwy: Array4b
    yxwz: Array4b
    yxww: Array4b
    yyxx: Array4b
    yyxy: Array4b
    yyxz: Array4b
    yyxw: Array4b
    yyyx: Array4b
    yyyy: Array4b
    yyyz: Array4b
    yyyw: Array4b
    yyzx: Array4b
    yyzy: Array4b
    yyzz: Array4b
    yyzw: Array4b
    yywx: Array4b
    yywy: Array4b
    yywz: Array4b
    yyww: Array4b
    yzxx: Array4b
    yzxy: Array4b
    yzxz: Array4b
    yzxw: Array4b
    yzyx: Array4b
    yzyy: Array4b
    yzyz: Array4b
    yzyw: Array4b
    yzzx: Array4b
    yzzy: Array4b
    yzzz: Array4b
    yzzw: Array4b
    yzwx: Array4b
    yzwy: Array4b
    yzwz: Array4b
    yzww: Array4b
    ywxx: Array4b
    ywxy: Array4b
    ywxz: Array4b
    ywxw: Array4b
    ywyx: Array4b
    ywyy: Array4b
    ywyz: Array4b
    ywyw: Array4b
    ywzx: Array4b
    ywzy: Array4b
    ywzz: Array4b
    ywzw: Array4b
    ywwx: Array4b
    ywwy: Array4b
    ywwz: Array4b
    ywww: Array4b
    zxxx: Array4b
    zxxy: Array4b
    zxxz: Array4b
    zxxw: Array4b
    zxyx: Array4b
    zxyy: Array4b
    zxyz: Array4b
    zxyw: Array4b
    zxzx: Array4b
    zxzy: Array4b
    zxzz: Array4b
    zxzw: Array4b
    zxwx: Array4b
    zxwy: Array4b
    zxwz: Array4b
    zxww: Array4b
    zyxx: Array4b
    zyxy: Array4b
    zyxz: Array4b
    zyxw: Array4b
    zyyx: Array4b
    zyyy: Array4b
    zyyz: Array4b
    zyyw: Array4b
    zyzx: Array4b
    zyzy: Array4b
    zyzz: Array4b
    zyzw: Array4b
    zywx: Array4b
    zywy: Array4b
    zywz: Array4b
    zyww: Array4b
    zzxx: Array4b
    zzxy: Array4b
    zzxz: Array4b
    zzxw: Array4b
    zzyx: Array4b
    zzyy: Array4b
    zzyz: Array4b
    zzyw: Array4b
    zzzx: Array4b
    zzzy: Array4b
    zzzz: Array4b
    zzzw: Array4b
    zzwx: Array4b
    zzwy: Array4b
    zzwz: Array4b
    zzww: Array4b
    zwxx: Array4b
    zwxy: Array4b
    zwxz: Array4b
    zwxw: Array4b
    zwyx: Array4b
    zwyy: Array4b
    zwyz: Array4b
    zwyw: Array4b
    zwzx: Array4b
    zwzy: Array4b
    zwzz: Array4b
    zwzw: Array4b
    zwwx: Array4b
    zwwy: Array4b
    zwwz: Array4b
    zwww: Array4b
    wxxx: Array4b
    wxxy: Array4b
    wxxz: Array4b
    wxxw: Array4b
    wxyx: Array4b
    wxyy: Array4b
    wxyz: Array4b
    wxyw: Array4b
    wxzx: Array4b
    wxzy: Array4b
    wxzz: Array4b
    wxzw: Array4b
    wxwx: Array4b
    wxwy: Array4b
    wxwz: Array4b
    wxww: Array4b
    wyxx: Array4b
    wyxy: Array4b
    wyxz: Array4b
    wyxw: Array4b
    wyyx: Array4b
    wyyy: Array4b
    wyyz: Array4b
    wyyw: Array4b
    wyzx: Array4b
    wyzy: Array4b
    wyzz: Array4b
    wyzw: Array4b
    wywx: Array4b
    wywy: Array4b
    wywz: Array4b
    wyww: Array4b
    wzxx: Array4b
    wzxy: Array4b
    wzxz: Array4b
    wzxw: Array4b
    wzyx: Array4b
    wzyy: Array4b
    wzyz: Array4b
    wzyw: Array4b
    wzzx: Array4b
    wzzy: Array4b
    wzzz: Array4b
    wzzw: Array4b
    wzwx: Array4b
    wzwy: Array4b
    wzwz: Array4b
    wzww: Array4b
    wwxx: Array4b
    wwxy: Array4b
    wwxz: Array4b
    wwxw: Array4b
    wwyx: Array4b
    wwyy: Array4b
    wwyz: Array4b
    wwyw: Array4b
    wwzx: Array4b
    wwzy: Array4b
    wwzz: Array4b
    wwzw: Array4b
    wwwx: Array4b
    wwwy: Array4b
    wwwz: Array4b
    wwww: Array4b

_Array1i8Cp: TypeAlias = Union['Array1i8', '_Int8Cp', 'drjit.scalar._Array1i8Cp', 'drjit.llvm._Array1i8Cp']

class Array1i8(drjit.ArrayBase[Array1i8, _Array1i8Cp, Int8, _Int8Cp, Int8, Array1i8, Array1b]):
    xx: Array2i8
    xy: Array2i8
    xz: Array2i8
    xw: Array2i8
    yx: Array2i8
    yy: Array2i8
    yz: Array2i8
    yw: Array2i8
    zx: Array2i8
    zy: Array2i8
    zz: Array2i8
    zw: Array2i8
    wx: Array2i8
    wy: Array2i8
    wz: Array2i8
    ww: Array2i8
    xxx: Array3i8
    xxy: Array3i8
    xxz: Array3i8
    xxw: Array3i8
    xyx: Array3i8
    xyy: Array3i8
    xyz: Array3i8
    xyw: Array3i8
    xzx: Array3i8
    xzy: Array3i8
    xzz: Array3i8
    xzw: Array3i8
    xwx: Array3i8
    xwy: Array3i8
    xwz: Array3i8
    xww: Array3i8
    yxx: Array3i8
    yxy: Array3i8
    yxz: Array3i8
    yxw: Array3i8
    yyx: Array3i8
    yyy: Array3i8
    yyz: Array3i8
    yyw: Array3i8
    yzx: Array3i8
    yzy: Array3i8
    yzz: Array3i8
    yzw: Array3i8
    ywx: Array3i8
    ywy: Array3i8
    ywz: Array3i8
    yww: Array3i8
    zxx: Array3i8
    zxy: Array3i8
    zxz: Array3i8
    zxw: Array3i8
    zyx: Array3i8
    zyy: Array3i8
    zyz: Array3i8
    zyw: Array3i8
    zzx: Array3i8
    zzy: Array3i8
    zzz: Array3i8
    zzw: Array3i8
    zwx: Array3i8
    zwy: Array3i8
    zwz: Array3i8
    zww: Array3i8
    wxx: Array3i8
    wxy: Array3i8
    wxz: Array3i8
    wxw: Array3i8
    wyx: Array3i8
    wyy: Array3i8
    wyz: Array3i8
    wyw: Array3i8
    wzx: Array3i8
    wzy: Array3i8
    wzz: Array3i8
    wzw: Array3i8
    wwx: Array3i8
    wwy: Array3i8
    wwz: Array3i8
    www: Array3i8
    xxxx: Array4i8
    xxxy: Array4i8
    xxxz: Array4i8
    xxxw: Array4i8
    xxyx: Array4i8
    xxyy: Array4i8
    xxyz: Array4i8
    xxyw: Array4i8
    xxzx: Array4i8
    xxzy: Array4i8
    xxzz: Array4i8
    xxzw: Array4i8
    xxwx: Array4i8
    xxwy: Array4i8
    xxwz: Array4i8
    xxww: Array4i8
    xyxx: Array4i8
    xyxy: Array4i8
    xyxz: Array4i8
    xyxw: Array4i8
    xyyx: Array4i8
    xyyy: Array4i8
    xyyz: Array4i8
    xyyw: Array4i8
    xyzx: Array4i8
    xyzy: Array4i8
    xyzz: Array4i8
    xyzw: Array4i8
    xywx: Array4i8
    xywy: Array4i8
    xywz: Array4i8
    xyww: Array4i8
    xzxx: Array4i8
    xzxy: Array4i8
    xzxz: Array4i8
    xzxw: Array4i8
    xzyx: Array4i8
    xzyy: Array4i8
    xzyz: Array4i8
    xzyw: Array4i8
    xzzx: Array4i8
    xzzy: Array4i8
    xzzz: Array4i8
    xzzw: Array4i8
    xzwx: Array4i8
    xzwy: Array4i8
    xzwz: Array4i8
    xzww: Array4i8
    xwxx: Array4i8
    xwxy: Array4i8
    xwxz: Array4i8
    xwxw: Array4i8
    xwyx: Array4i8
    xwyy: Array4i8
    xwyz: Array4i8
    xwyw: Array4i8
    xwzx: Array4i8
    xwzy: Array4i8
    xwzz: Array4i8
    xwzw: Array4i8
    xwwx: Array4i8
    xwwy: Array4i8
    xwwz: Array4i8
    xwww: Array4i8
    yxxx: Array4i8
    yxxy: Array4i8
    yxxz: Array4i8
    yxxw: Array4i8
    yxyx: Array4i8
    yxyy: Array4i8
    yxyz: Array4i8
    yxyw: Array4i8
    yxzx: Array4i8
    yxzy: Array4i8
    yxzz: Array4i8
    yxzw: Array4i8
    yxwx: Array4i8
    yxwy: Array4i8
    yxwz: Array4i8
    yxww: Array4i8
    yyxx: Array4i8
    yyxy: Array4i8
    yyxz: Array4i8
    yyxw: Array4i8
    yyyx: Array4i8
    yyyy: Array4i8
    yyyz: Array4i8
    yyyw: Array4i8
    yyzx: Array4i8
    yyzy: Array4i8
    yyzz: Array4i8
    yyzw: Array4i8
    yywx: Array4i8
    yywy: Array4i8
    yywz: Array4i8
    yyww: Array4i8
    yzxx: Array4i8
    yzxy: Array4i8
    yzxz: Array4i8
    yzxw: Array4i8
    yzyx: Array4i8
    yzyy: Array4i8
    yzyz: Array4i8
    yzyw: Array4i8
    yzzx: Array4i8
    yzzy: Array4i8
    yzzz: Array4i8
    yzzw: Array4i8
    yzwx: Array4i8
    yzwy: Array4i8
    yzwz: Array4i8
    yzww: Array4i8
    ywxx: Array4i8
    ywxy: Array4i8
    ywxz: Array4i8
    ywxw: Array4i8
    ywyx: Array4i8
    ywyy: Array4i8
    ywyz: Array4i8
    ywyw: Array4i8
    ywzx: Array4i8
    ywzy: Array4i8
    ywzz: Array4i8
    ywzw: Array4i8
    ywwx: Array4i8
    ywwy: Array4i8
    ywwz: Array4i8
    ywww: Array4i8
    zxxx: Array4i8
    zxxy: Array4i8
    zxxz: Array4i8
    zxxw: Array4i8
    zxyx: Array4i8
    zxyy: Array4i8
    zxyz: Array4i8
    zxyw: Array4i8
    zxzx: Array4i8
    zxzy: Array4i8
    zxzz: Array4i8
    zxzw: Array4i8
    zxwx: Array4i8
    zxwy: Array4i8
    zxwz: Array4i8
    zxww: Array4i8
    zyxx: Array4i8
    zyxy: Array4i8
    zyxz: Array4i8
    zyxw: Array4i8
    zyyx: Array4i8
    zyyy: Array4i8
    zyyz: Array4i8
    zyyw: Array4i8
    zyzx: Array4i8
    zyzy: Array4i8
    zyzz: Array4i8
    zyzw: Array4i8
    zywx: Array4i8
    zywy: Array4i8
    zywz: Array4i8
    zyww: Array4i8
    zzxx: Array4i8
    zzxy: Array4i8
    zzxz: Array4i8
    zzxw: Array4i8
    zzyx: Array4i8
    zzyy: Array4i8
    zzyz: Array4i8
    zzyw: Array4i8
    zzzx: Array4i8
    zzzy: Array4i8
    zzzz: Array4i8
    zzzw: Array4i8
    zzwx: Array4i8
    zzwy: Array4i8
    zzwz: Array4i8
    zzww: Array4i8
    zwxx: Array4i8
    zwxy: Array4i8
    zwxz: Array4i8
    zwxw: Array4i8
    zwyx: Array4i8
    zwyy: Array4i8
    zwyz: Array4i8
    zwyw: Array4i8
    zwzx: Array4i8
    zwzy: Array4i8
    zwzz: Array4i8
    zwzw: Array4i8
    zwwx: Array4i8
    zwwy: Array4i8
    zwwz: Array4i8
    zwww: Array4i8
    wxxx: Array4i8
    wxxy: Array4i8
    wxxz: Array4i8
    wxxw: Array4i8
    wxyx: Array4i8
    wxyy: Array4i8
    wxyz: Array4i8
    wxyw: Array4i8
    wxzx: Array4i8
    wxzy: Array4i8
    wxzz: Array4i8
    wxzw: Array4i8
    wxwx: Array4i8
    wxwy: Array4i8
    wxwz: Array4i8
    wxww: Array4i8
    wyxx: Array4i8
    wyxy: Array4i8
    wyxz: Array4i8
    wyxw: Array4i8
    wyyx: Array4i8
    wyyy: Array4i8
    wyyz: Array4i8
    wyyw: Array4i8
    wyzx: Array4i8
    wyzy: Array4i8
    wyzz: Array4i8
    wyzw: Array4i8
    wywx: Array4i8
    wywy: Array4i8
    wywz: Array4i8
    wyww: Array4i8
    wzxx: Array4i8
    wzxy: Array4i8
    wzxz: Array4i8
    wzxw: Array4i8
    wzyx: Array4i8
    wzyy: Array4i8
    wzyz: Array4i8
    wzyw: Array4i8
    wzzx: Array4i8
    wzzy: Array4i8
    wzzz: Array4i8
    wzzw: Array4i8
    wzwx: Array4i8
    wzwy: Array4i8
    wzwz: Array4i8
    wzww: Array4i8
    wwxx: Array4i8
    wwxy: Array4i8
    wwxz: Array4i8
    wwxw: Array4i8
    wwyx: Array4i8
    wwyy: Array4i8
    wwyz: Array4i8
    wwyw: Array4i8
    wwzx: Array4i8
    wwzy: Array4i8
    wwzz: Array4i8
    wwzw: Array4i8
    wwwx: Array4i8
    wwwy: Array4i8
    wwwz: Array4i8
    wwww: Array4i8

_Array1u8Cp: TypeAlias = Union['Array1u8', '_UInt8Cp', 'drjit.scalar._Array1u8Cp', 'drjit.llvm._Array1u8Cp']

class Array1u8(drjit.ArrayBase[Array1u8, _Array1u8Cp, UInt8, _UInt8Cp, UInt8, Array1u8, Array1b]):
    xx: Array2u8
    xy: Array2u8
    xz: Array2u8
    xw: Array2u8
    yx: Array2u8
    yy: Array2u8
    yz: Array2u8
    yw: Array2u8
    zx: Array2u8
    zy: Array2u8
    zz: Array2u8
    zw: Array2u8
    wx: Array2u8
    wy: Array2u8
    wz: Array2u8
    ww: Array2u8
    xxx: Array3u8
    xxy: Array3u8
    xxz: Array3u8
    xxw: Array3u8
    xyx: Array3u8
    xyy: Array3u8
    xyz: Array3u8
    xyw: Array3u8
    xzx: Array3u8
    xzy: Array3u8
    xzz: Array3u8
    xzw: Array3u8
    xwx: Array3u8
    xwy: Array3u8
    xwz: Array3u8
    xww: Array3u8
    yxx: Array3u8
    yxy: Array3u8
    yxz: Array3u8
    yxw: Array3u8
    yyx: Array3u8
    yyy: Array3u8
    yyz: Array3u8
    yyw: Array3u8
    yzx: Array3u8
    yzy: Array3u8
    yzz: Array3u8
    yzw: Array3u8
    ywx: Array3u8
    ywy: Array3u8
    ywz: Array3u8
    yww: Array3u8
    zxx: Array3u8
    zxy: Array3u8
    zxz: Array3u8
    zxw: Array3u8
    zyx: Array3u8
    zyy: Array3u8
    zyz: Array3u8
    zyw: Array3u8
    zzx: Array3u8
    zzy: Array3u8
    zzz: Array3u8
    zzw: Array3u8
    zwx: Array3u8
    zwy: Array3u8
    zwz: Array3u8
    zww: Array3u8
    wxx: Array3u8
    wxy: Array3u8
    wxz: Array3u8
    wxw: Array3u8
    wyx: Array3u8
    wyy: Array3u8
    wyz: Array3u8
    wyw: Array3u8
    wzx: Array3u8
    wzy: Array3u8
    wzz: Array3u8
    wzw: Array3u8
    wwx: Array3u8
    wwy: Array3u8
    wwz: Array3u8
    www: Array3u8
    xxxx: Array4u8
    xxxy: Array4u8
    xxxz: Array4u8
    xxxw: Array4u8
    xxyx: Array4u8
    xxyy: Array4u8
    xxyz: Array4u8
    xxyw: Array4u8
    xxzx: Array4u8
    xxzy: Array4u8
    xxzz: Array4u8
    xxzw: Array4u8
    xxwx: Array4u8
    xxwy: Array4u8
    xxwz: Array4u8
    xxww: Array4u8
    xyxx: Array4u8
    xyxy: Array4u8
    xyxz: Array4u8
    xyxw: Array4u8
    xyyx: Array4u8
    xyyy: Array4u8
    xyyz: Array4u8
    xyyw: Array4u8
    xyzx: Array4u8
    xyzy: Array4u8
    xyzz: Array4u8
    xyzw: Array4u8
    xywx: Array4u8
    xywy: Array4u8
    xywz: Array4u8
    xyww: Array4u8
    xzxx: Array4u8
    xzxy: Array4u8
    xzxz: Array4u8
    xzxw: Array4u8
    xzyx: Array4u8
    xzyy: Array4u8
    xzyz: Array4u8
    xzyw: Array4u8
    xzzx: Array4u8
    xzzy: Array4u8
    xzzz: Array4u8
    xzzw: Array4u8
    xzwx: Array4u8
    xzwy: Array4u8
    xzwz: Array4u8
    xzww: Array4u8
    xwxx: Array4u8
    xwxy: Array4u8
    xwxz: Array4u8
    xwxw: Array4u8
    xwyx: Array4u8
    xwyy: Array4u8
    xwyz: Array4u8
    xwyw: Array4u8
    xwzx: Array4u8
    xwzy: Array4u8
    xwzz: Array4u8
    xwzw: Array4u8
    xwwx: Array4u8
    xwwy: Array4u8
    xwwz: Array4u8
    xwww: Array4u8
    yxxx: Array4u8
    yxxy: Array4u8
    yxxz: Array4u8
    yxxw: Array4u8
    yxyx: Array4u8
    yxyy: Array4u8
    yxyz: Array4u8
    yxyw: Array4u8
    yxzx: Array4u8
    yxzy: Array4u8
    yxzz: Array4u8
    yxzw: Array4u8
    yxwx: Array4u8
    yxwy: Array4u8
    yxwz: Array4u8
    yxww: Array4u8
    yyxx: Array4u8
    yyxy: Array4u8
    yyxz: Array4u8
    yyxw: Array4u8
    yyyx: Array4u8
    yyyy: Array4u8
    yyyz: Array4u8
    yyyw: Array4u8
    yyzx: Array4u8
    yyzy: Array4u8
    yyzz: Array4u8
    yyzw: Array4u8
    yywx: Array4u8
    yywy: Array4u8
    yywz: Array4u8
    yyww: Array4u8
    yzxx: Array4u8
    yzxy: Array4u8
    yzxz: Array4u8
    yzxw: Array4u8
    yzyx: Array4u8
    yzyy: Array4u8
    yzyz: Array4u8
    yzyw: Array4u8
    yzzx: Array4u8
    yzzy: Array4u8
    yzzz: Array4u8
    yzzw: Array4u8
    yzwx: Array4u8
    yzwy: Array4u8
    yzwz: Array4u8
    yzww: Array4u8
    ywxx: Array4u8
    ywxy: Array4u8
    ywxz: Array4u8
    ywxw: Array4u8
    ywyx: Array4u8
    ywyy: Array4u8
    ywyz: Array4u8
    ywyw: Array4u8
    ywzx: Array4u8
    ywzy: Array4u8
    ywzz: Array4u8
    ywzw: Array4u8
    ywwx: Array4u8
    ywwy: Array4u8
    ywwz: Array4u8
    ywww: Array4u8
    zxxx: Array4u8
    zxxy: Array4u8
    zxxz: Array4u8
    zxxw: Array4u8
    zxyx: Array4u8
    zxyy: Array4u8
    zxyz: Array4u8
    zxyw: Array4u8
    zxzx: Array4u8
    zxzy: Array4u8
    zxzz: Array4u8
    zxzw: Array4u8
    zxwx: Array4u8
    zxwy: Array4u8
    zxwz: Array4u8
    zxww: Array4u8
    zyxx: Array4u8
    zyxy: Array4u8
    zyxz: Array4u8
    zyxw: Array4u8
    zyyx: Array4u8
    zyyy: Array4u8
    zyyz: Array4u8
    zyyw: Array4u8
    zyzx: Array4u8
    zyzy: Array4u8
    zyzz: Array4u8
    zyzw: Array4u8
    zywx: Array4u8
    zywy: Array4u8
    zywz: Array4u8
    zyww: Array4u8
    zzxx: Array4u8
    zzxy: Array4u8
    zzxz: Array4u8
    zzxw: Array4u8
    zzyx: Array4u8
    zzyy: Array4u8
    zzyz: Array4u8
    zzyw: Array4u8
    zzzx: Array4u8
    zzzy: Array4u8
    zzzz: Array4u8
    zzzw: Array4u8
    zzwx: Array4u8
    zzwy: Array4u8
    zzwz: Array4u8
    zzww: Array4u8
    zwxx: Array4u8
    zwxy: Array4u8
    zwxz: Array4u8
    zwxw: Array4u8
    zwyx: Array4u8
    zwyy: Array4u8
    zwyz: Array4u8
    zwyw: Array4u8
    zwzx: Array4u8
    zwzy: Array4u8
    zwzz: Array4u8
    zwzw: Array4u8
    zwwx: Array4u8
    zwwy: Array4u8
    zwwz: Array4u8
    zwww: Array4u8
    wxxx: Array4u8
    wxxy: Array4u8
    wxxz: Array4u8
    wxxw: Array4u8
    wxyx: Array4u8
    wxyy: Array4u8
    wxyz: Array4u8
    wxyw: Array4u8
    wxzx: Array4u8
    wxzy: Array4u8
    wxzz: Array4u8
    wxzw: Array4u8
    wxwx: Array4u8
    wxwy: Array4u8
    wxwz: Array4u8
    wxww: Array4u8
    wyxx: Array4u8
    wyxy: Array4u8
    wyxz: Array4u8
    wyxw: Array4u8
    wyyx: Array4u8
    wyyy: Array4u8
    wyyz: Array4u8
    wyyw: Array4u8
    wyzx: Array4u8
    wyzy: Array4u8
    wyzz: Array4u8
    wyzw: Array4u8
    wywx: Array4u8
    wywy: Array4u8
    wywz: Array4u8
    wyww: Array4u8
    wzxx: Array4u8
    wzxy: Array4u8
    wzxz: Array4u8
    wzxw: Array4u8
    wzyx: Array4u8
    wzyy: Array4u8
    wzyz: Array4u8
    wzyw: Array4u8
    wzzx: Array4u8
    wzzy: Array4u8
    wzzz: Array4u8
    wzzw: Array4u8
    wzwx: Array4u8
    wzwy: Array4u8
    wzwz: Array4u8
    wzww: Array4u8
    wwxx: Array4u8
    wwxy: Array4u8
    wwxz: Array4u8
    wwxw: Array4u8
    wwyx: Array4u8
    wwyy: Array4u8
    wwyz: Array4u8
    wwyw: Array4u8
    wwzx: Array4u8
    wwzy: Array4u8
    wwzz: Array4u8
    wwzw: Array4u8
    wwwx: Array4u8
    wwwy: Array4u8
    wwwz: Array4u8
    wwww: Array4u8

_Array1iCp: TypeAlias = Union['Array1i', '_IntCp', 'drjit.scalar._Array1iCp', 'drjit.llvm._Array1iCp', '_Array1bCp']

class Array1i(drjit.ArrayBase[Array1i, _Array1iCp, Int, _IntCp, Int, Array1i, Array1b]):
    xx: Array2i
    xy: Array2i
    xz: Array2i
    xw: Array2i
    yx: Array2i
    yy: Array2i
    yz: Array2i
    yw: Array2i
    zx: Array2i
    zy: Array2i
    zz: Array2i
    zw: Array2i
    wx: Array2i
    wy: Array2i
    wz: Array2i
    ww: Array2i
    xxx: Array3i
    xxy: Array3i
    xxz: Array3i
    xxw: Array3i
    xyx: Array3i
    xyy: Array3i
    xyz: Array3i
    xyw: Array3i
    xzx: Array3i
    xzy: Array3i
    xzz: Array3i
    xzw: Array3i
    xwx: Array3i
    xwy: Array3i
    xwz: Array3i
    xww: Array3i
    yxx: Array3i
    yxy: Array3i
    yxz: Array3i
    yxw: Array3i
    yyx: Array3i
    yyy: Array3i
    yyz: Array3i
    yyw: Array3i
    yzx: Array3i
    yzy: Array3i
    yzz: Array3i
    yzw: Array3i
    ywx: Array3i
    ywy: Array3i
    ywz: Array3i
    yww: Array3i
    zxx: Array3i
    zxy: Array3i
    zxz: Array3i
    zxw: Array3i
    zyx: Array3i
    zyy: Array3i
    zyz: Array3i
    zyw: Array3i
    zzx: Array3i
    zzy: Array3i
    zzz: Array3i
    zzw: Array3i
    zwx: Array3i
    zwy: Array3i
    zwz: Array3i
    zww: Array3i
    wxx: Array3i
    wxy: Array3i
    wxz: Array3i
    wxw: Array3i
    wyx: Array3i
    wyy: Array3i
    wyz: Array3i
    wyw: Array3i
    wzx: Array3i
    wzy: Array3i
    wzz: Array3i
    wzw: Array3i
    wwx: Array3i
    wwy: Array3i
    wwz: Array3i
    www: Array3i
    xxxx: Array4i
    xxxy: Array4i
    xxxz: Array4i
    xxxw: Array4i
    xxyx: Array4i
    xxyy: Array4i
    xxyz: Array4i
    xxyw: Array4i
    xxzx: Array4i
    xxzy: Array4i
    xxzz: Array4i
    xxzw: Array4i
    xxwx: Array4i
    xxwy: Array4i
    xxwz: Array4i
    xxww: Array4i
    xyxx: Array4i
    xyxy: Array4i
    xyxz: Array4i
    xyxw: Array4i
    xyyx: Array4i
    xyyy: Array4i
    xyyz: Array4i
    xyyw: Array4i
    xyzx: Array4i
    xyzy: Array4i
    xyzz: Array4i
    xyzw: Array4i
    xywx: Array4i
    xywy: Array4i
    xywz: Array4i
    xyww: Array4i
    xzxx: Array4i
    xzxy: Array4i
    xzxz: Array4i
    xzxw: Array4i
    xzyx: Array4i
    xzyy: Array4i
    xzyz: Array4i
    xzyw: Array4i
    xzzx: Array4i
    xzzy: Array4i
    xzzz: Array4i
    xzzw: Array4i
    xzwx: Array4i
    xzwy: Array4i
    xzwz: Array4i
    xzww: Array4i
    xwxx: Array4i
    xwxy: Array4i
    xwxz: Array4i
    xwxw: Array4i
    xwyx: Array4i
    xwyy: Array4i
    xwyz: Array4i
    xwyw: Array4i
    xwzx: Array4i
    xwzy: Array4i
    xwzz: Array4i
    xwzw: Array4i
    xwwx: Array4i
    xwwy: Array4i
    xwwz: Array4i
    xwww: Array4i
    yxxx: Array4i
    yxxy: Array4i
    yxxz: Array4i
    yxxw: Array4i
    yxyx: Array4i
    yxyy: Array4i
    yxyz: Array4i
    yxyw: Array4i
    yxzx: Array4i
    yxzy: Array4i
    yxzz: Array4i
    yxzw: Array4i
    yxwx: Array4i
    yxwy: Array4i
    yxwz: Array4i
    yxww: Array4i
    yyxx: Array4i
    yyxy: Array4i
    yyxz: Array4i
    yyxw: Array4i
    yyyx: Array4i
    yyyy: Array4i
    yyyz: Array4i
    yyyw: Array4i
    yyzx: Array4i
    yyzy: Array4i
    yyzz: Array4i
    yyzw: Array4i
    yywx: Array4i
    yywy: Array4i
    yywz: Array4i
    yyww: Array4i
    yzxx: Array4i
    yzxy: Array4i
    yzxz: Array4i
    yzxw: Array4i
    yzyx: Array4i
    yzyy: Array4i
    yzyz: Array4i
    yzyw: Array4i
    yzzx: Array4i
    yzzy: Array4i
    yzzz: Array4i
    yzzw: Array4i
    yzwx: Array4i
    yzwy: Array4i
    yzwz: Array4i
    yzww: Array4i
    ywxx: Array4i
    ywxy: Array4i
    ywxz: Array4i
    ywxw: Array4i
    ywyx: Array4i
    ywyy: Array4i
    ywyz: Array4i
    ywyw: Array4i
    ywzx: Array4i
    ywzy: Array4i
    ywzz: Array4i
    ywzw: Array4i
    ywwx: Array4i
    ywwy: Array4i
    ywwz: Array4i
    ywww: Array4i
    zxxx: Array4i
    zxxy: Array4i
    zxxz: Array4i
    zxxw: Array4i
    zxyx: Array4i
    zxyy: Array4i
    zxyz: Array4i
    zxyw: Array4i
    zxzx: Array4i
    zxzy: Array4i
    zxzz: Array4i
    zxzw: Array4i
    zxwx: Array4i
    zxwy: Array4i
    zxwz: Array4i
    zxww: Array4i
    zyxx: Array4i
    zyxy: Array4i
    zyxz: Array4i
    zyxw: Array4i
    zyyx: Array4i
    zyyy: Array4i
    zyyz: Array4i
    zyyw: Array4i
    zyzx: Array4i
    zyzy: Array4i
    zyzz: Array4i
    zyzw: Array4i
    zywx: Array4i
    zywy: Array4i
    zywz: Array4i
    zyww: Array4i
    zzxx: Array4i
    zzxy: Array4i
    zzxz: Array4i
    zzxw: Array4i
    zzyx: Array4i
    zzyy: Array4i
    zzyz: Array4i
    zzyw: Array4i
    zzzx: Array4i
    zzzy: Array4i
    zzzz: Array4i
    zzzw: Array4i
    zzwx: Array4i
    zzwy: Array4i
    zzwz: Array4i
    zzww: Array4i
    zwxx: Array4i
    zwxy: Array4i
    zwxz: Array4i
    zwxw: Array4i
    zwyx: Array4i
    zwyy: Array4i
    zwyz: Array4i
    zwyw: Array4i
    zwzx: Array4i
    zwzy: Array4i
    zwzz: Array4i
    zwzw: Array4i
    zwwx: Array4i
    zwwy: Array4i
    zwwz: Array4i
    zwww: Array4i
    wxxx: Array4i
    wxxy: Array4i
    wxxz: Array4i
    wxxw: Array4i
    wxyx: Array4i
    wxyy: Array4i
    wxyz: Array4i
    wxyw: Array4i
    wxzx: Array4i
    wxzy: Array4i
    wxzz: Array4i
    wxzw: Array4i
    wxwx: Array4i
    wxwy: Array4i
    wxwz: Array4i
    wxww: Array4i
    wyxx: Array4i
    wyxy: Array4i
    wyxz: Array4i
    wyxw: Array4i
    wyyx: Array4i
    wyyy: Array4i
    wyyz: Array4i
    wyyw: Array4i
    wyzx: Array4i
    wyzy: Array4i
    wyzz: Array4i
    wyzw: Array4i
    wywx: Array4i
    wywy: Array4i
    wywz: Array4i
    wyww: Array4i
    wzxx: Array4i
    wzxy: Array4i
    wzxz: Array4i
    wzxw: Array4i
    wzyx: Array4i
    wzyy: Array4i
    wzyz: Array4i
    wzyw: Array4i
    wzzx: Array4i
    wzzy: Array4i
    wzzz: Array4i
    wzzw: Array4i
    wzwx: Array4i
    wzwy: Array4i
    wzwz: Array4i
    wzww: Array4i
    wwxx: Array4i
    wwxy: Array4i
    wwxz: Array4i
    wwxw: Array4i
    wwyx: Array4i
    wwyy: Array4i
    wwyz: Array4i
    wwyw: Array4i
    wwzx: Array4i
    wwzy: Array4i
    wwzz: Array4i
    wwzw: Array4i
    wwwx: Array4i
    wwwy: Array4i
    wwwz: Array4i
    wwww: Array4i

_Array1uCp: TypeAlias = Union['Array1u', '_UIntCp', 'drjit.scalar._Array1uCp', 'drjit.llvm._Array1uCp', '_Array1iCp']

class Array1u(drjit.ArrayBase[Array1u, _Array1uCp, UInt, _UIntCp, UInt, Array1u, Array1b]):
    xx: Array2u
    xy: Array2u
    xz: Array2u
    xw: Array2u
    yx: Array2u
    yy: Array2u
    yz: Array2u
    yw: Array2u
    zx: Array2u
    zy: Array2u
    zz: Array2u
    zw: Array2u
    wx: Array2u
    wy: Array2u
    wz: Array2u
    ww: Array2u
    xxx: Array3u
    xxy: Array3u
    xxz: Array3u
    xxw: Array3u
    xyx: Array3u
    xyy: Array3u
    xyz: Array3u
    xyw: Array3u
    xzx: Array3u
    xzy: Array3u
    xzz: Array3u
    xzw: Array3u
    xwx: Array3u
    xwy: Array3u
    xwz: Array3u
    xww: Array3u
    yxx: Array3u
    yxy: Array3u
    yxz: Array3u
    yxw: Array3u
    yyx: Array3u
    yyy: Array3u
    yyz: Array3u
    yyw: Array3u
    yzx: Array3u
    yzy: Array3u
    yzz: Array3u
    yzw: Array3u
    ywx: Array3u
    ywy: Array3u
    ywz: Array3u
    yww: Array3u
    zxx: Array3u
    zxy: Array3u
    zxz: Array3u
    zxw: Array3u
    zyx: Array3u
    zyy: Array3u
    zyz: Array3u
    zyw: Array3u
    zzx: Array3u
    zzy: Array3u
    zzz: Array3u
    zzw: Array3u
    zwx: Array3u
    zwy: Array3u
    zwz: Array3u
    zww: Array3u
    wxx: Array3u
    wxy: Array3u
    wxz: Array3u
    wxw: Array3u
    wyx: Array3u
    wyy: Array3u
    wyz: Array3u
    wyw: Array3u
    wzx: Array3u
    wzy: Array3u
    wzz: Array3u
    wzw: Array3u
    wwx: Array3u
    wwy: Array3u
    wwz: Array3u
    www: Array3u
    xxxx: Array4u
    xxxy: Array4u
    xxxz: Array4u
    xxxw: Array4u
    xxyx: Array4u
    xxyy: Array4u
    xxyz: Array4u
    xxyw: Array4u
    xxzx: Array4u
    xxzy: Array4u
    xxzz: Array4u
    xxzw: Array4u
    xxwx: Array4u
    xxwy: Array4u
    xxwz: Array4u
    xxww: Array4u
    xyxx: Array4u
    xyxy: Array4u
    xyxz: Array4u
    xyxw: Array4u
    xyyx: Array4u
    xyyy: Array4u
    xyyz: Array4u
    xyyw: Array4u
    xyzx: Array4u
    xyzy: Array4u
    xyzz: Array4u
    xyzw: Array4u
    xywx: Array4u
    xywy: Array4u
    xywz: Array4u
    xyww: Array4u
    xzxx: Array4u
    xzxy: Array4u
    xzxz: Array4u
    xzxw: Array4u
    xzyx: Array4u
    xzyy: Array4u
    xzyz: Array4u
    xzyw: Array4u
    xzzx: Array4u
    xzzy: Array4u
    xzzz: Array4u
    xzzw: Array4u
    xzwx: Array4u
    xzwy: Array4u
    xzwz: Array4u
    xzww: Array4u
    xwxx: Array4u
    xwxy: Array4u
    xwxz: Array4u
    xwxw: Array4u
    xwyx: Array4u
    xwyy: Array4u
    xwyz: Array4u
    xwyw: Array4u
    xwzx: Array4u
    xwzy: Array4u
    xwzz: Array4u
    xwzw: Array4u
    xwwx: Array4u
    xwwy: Array4u
    xwwz: Array4u
    xwww: Array4u
    yxxx: Array4u
    yxxy: Array4u
    yxxz: Array4u
    yxxw: Array4u
    yxyx: Array4u
    yxyy: Array4u
    yxyz: Array4u
    yxyw: Array4u
    yxzx: Array4u
    yxzy: Array4u
    yxzz: Array4u
    yxzw: Array4u
    yxwx: Array4u
    yxwy: Array4u
    yxwz: Array4u
    yxww: Array4u
    yyxx: Array4u
    yyxy: Array4u
    yyxz: Array4u
    yyxw: Array4u
    yyyx: Array4u
    yyyy: Array4u
    yyyz: Array4u
    yyyw: Array4u
    yyzx: Array4u
    yyzy: Array4u
    yyzz: Array4u
    yyzw: Array4u
    yywx: Array4u
    yywy: Array4u
    yywz: Array4u
    yyww: Array4u
    yzxx: Array4u
    yzxy: Array4u
    yzxz: Array4u
    yzxw: Array4u
    yzyx: Array4u
    yzyy: Array4u
    yzyz: Array4u
    yzyw: Array4u
    yzzx: Array4u
    yzzy: Array4u
    yzzz: Array4u
    yzzw: Array4u
    yzwx: Array4u
    yzwy: Array4u
    yzwz: Array4u
    yzww: Array4u
    ywxx: Array4u
    ywxy: Array4u
    ywxz: Array4u
    ywxw: Array4u
    ywyx: Array4u
    ywyy: Array4u
    ywyz: Array4u
    ywyw: Array4u
    ywzx: Array4u
    ywzy: Array4u
    ywzz: Array4u
    ywzw: Array4u
    ywwx: Array4u
    ywwy: Array4u
    ywwz: Array4u
    ywww: Array4u
    zxxx: Array4u
    zxxy: Array4u
    zxxz: Array4u
    zxxw: Array4u
    zxyx: Array4u
    zxyy: Array4u
    zxyz: Array4u
    zxyw: Array4u
    zxzx: Array4u
    zxzy: Array4u
    zxzz: Array4u
    zxzw: Array4u
    zxwx: Array4u
    zxwy: Array4u
    zxwz: Array4u
    zxww: Array4u
    zyxx: Array4u
    zyxy: Array4u
    zyxz: Array4u
    zyxw: Array4u
    zyyx: Array4u
    zyyy: Array4u
    zyyz: Array4u
    zyyw: Array4u
    zyzx: Array4u
    zyzy: Array4u
    zyzz: Array4u
    zyzw: Array4u
    zywx: Array4u
    zywy: Array4u
    zywz: Array4u
    zyww: Array4u
    zzxx: Array4u
    zzxy: Array4u
    zzxz: Array4u
    zzxw: Array4u
    zzyx: Array4u
    zzyy: Array4u
    zzyz: Array4u
    zzyw: Array4u
    zzzx: Array4u
    zzzy: Array4u
    zzzz: Array4u
    zzzw: Array4u
    zzwx: Array4u
    zzwy: Array4u
    zzwz: Array4u
    zzww: Array4u
    zwxx: Array4u
    zwxy: Array4u
    zwxz: Array4u
    zwxw: Array4u
    zwyx: Array4u
    zwyy: Array4u
    zwyz: Array4u
    zwyw: Array4u
    zwzx: Array4u
    zwzy: Array4u
    zwzz: Array4u
    zwzw: Array4u
    zwwx: Array4u
    zwwy: Array4u
    zwwz: Array4u
    zwww: Array4u
    wxxx: Array4u
    wxxy: Array4u
    wxxz: Array4u
    wxxw: Array4u
    wxyx: Array4u
    wxyy: Array4u
    wxyz: Array4u
    wxyw: Array4u
    wxzx: Array4u
    wxzy: Array4u
    wxzz: Array4u
    wxzw: Array4u
    wxwx: Array4u
    wxwy: Array4u
    wxwz: Array4u
    wxww: Array4u
    wyxx: Array4u
    wyxy: Array4u
    wyxz: Array4u
    wyxw: Array4u
    wyyx: Array4u
    wyyy: Array4u
    wyyz: Array4u
    wyyw: Array4u
    wyzx: Array4u
    wyzy: Array4u
    wyzz: Array4u
    wyzw: Array4u
    wywx: Array4u
    wywy: Array4u
    wywz: Array4u
    wyww: Array4u
    wzxx: Array4u
    wzxy: Array4u
    wzxz: Array4u
    wzxw: Array4u
    wzyx: Array4u
    wzyy: Array4u
    wzyz: Array4u
    wzyw: Array4u
    wzzx: Array4u
    wzzy: Array4u
    wzzz: Array4u
    wzzw: Array4u
    wzwx: Array4u
    wzwy: Array4u
    wzwz: Array4u
    wzww: Array4u
    wwxx: Array4u
    wwxy: Array4u
    wwxz: Array4u
    wwxw: Array4u
    wwyx: Array4u
    wwyy: Array4u
    wwyz: Array4u
    wwyw: Array4u
    wwzx: Array4u
    wwzy: Array4u
    wwzz: Array4u
    wwzw: Array4u
    wwwx: Array4u
    wwwy: Array4u
    wwwz: Array4u
    wwww: Array4u

_Array1i64Cp: TypeAlias = Union['Array1i64', '_Int64Cp', 'drjit.scalar._Array1i64Cp', 'drjit.llvm._Array1i64Cp', '_Array1uCp']

class Array1i64(drjit.ArrayBase[Array1i64, _Array1i64Cp, Int64, _Int64Cp, Int64, Array1i64, Array1b]):
    xx: Array2i64
    xy: Array2i64
    xz: Array2i64
    xw: Array2i64
    yx: Array2i64
    yy: Array2i64
    yz: Array2i64
    yw: Array2i64
    zx: Array2i64
    zy: Array2i64
    zz: Array2i64
    zw: Array2i64
    wx: Array2i64
    wy: Array2i64
    wz: Array2i64
    ww: Array2i64
    xxx: Array3i64
    xxy: Array3i64
    xxz: Array3i64
    xxw: Array3i64
    xyx: Array3i64
    xyy: Array3i64
    xyz: Array3i64
    xyw: Array3i64
    xzx: Array3i64
    xzy: Array3i64
    xzz: Array3i64
    xzw: Array3i64
    xwx: Array3i64
    xwy: Array3i64
    xwz: Array3i64
    xww: Array3i64
    yxx: Array3i64
    yxy: Array3i64
    yxz: Array3i64
    yxw: Array3i64
    yyx: Array3i64
    yyy: Array3i64
    yyz: Array3i64
    yyw: Array3i64
    yzx: Array3i64
    yzy: Array3i64
    yzz: Array3i64
    yzw: Array3i64
    ywx: Array3i64
    ywy: Array3i64
    ywz: Array3i64
    yww: Array3i64
    zxx: Array3i64
    zxy: Array3i64
    zxz: Array3i64
    zxw: Array3i64
    zyx: Array3i64
    zyy: Array3i64
    zyz: Array3i64
    zyw: Array3i64
    zzx: Array3i64
    zzy: Array3i64
    zzz: Array3i64
    zzw: Array3i64
    zwx: Array3i64
    zwy: Array3i64
    zwz: Array3i64
    zww: Array3i64
    wxx: Array3i64
    wxy: Array3i64
    wxz: Array3i64
    wxw: Array3i64
    wyx: Array3i64
    wyy: Array3i64
    wyz: Array3i64
    wyw: Array3i64
    wzx: Array3i64
    wzy: Array3i64
    wzz: Array3i64
    wzw: Array3i64
    wwx: Array3i64
    wwy: Array3i64
    wwz: Array3i64
    www: Array3i64
    xxxx: Array4i64
    xxxy: Array4i64
    xxxz: Array4i64
    xxxw: Array4i64
    xxyx: Array4i64
    xxyy: Array4i64
    xxyz: Array4i64
    xxyw: Array4i64
    xxzx: Array4i64
    xxzy: Array4i64
    xxzz: Array4i64
    xxzw: Array4i64
    xxwx: Array4i64
    xxwy: Array4i64
    xxwz: Array4i64
    xxww: Array4i64
    xyxx: Array4i64
    xyxy: Array4i64
    xyxz: Array4i64
    xyxw: Array4i64
    xyyx: Array4i64
    xyyy: Array4i64
    xyyz: Array4i64
    xyyw: Array4i64
    xyzx: Array4i64
    xyzy: Array4i64
    xyzz: Array4i64
    xyzw: Array4i64
    xywx: Array4i64
    xywy: Array4i64
    xywz: Array4i64
    xyww: Array4i64
    xzxx: Array4i64
    xzxy: Array4i64
    xzxz: Array4i64
    xzxw: Array4i64
    xzyx: Array4i64
    xzyy: Array4i64
    xzyz: Array4i64
    xzyw: Array4i64
    xzzx: Array4i64
    xzzy: Array4i64
    xzzz: Array4i64
    xzzw: Array4i64
    xzwx: Array4i64
    xzwy: Array4i64
    xzwz: Array4i64
    xzww: Array4i64
    xwxx: Array4i64
    xwxy: Array4i64
    xwxz: Array4i64
    xwxw: Array4i64
    xwyx: Array4i64
    xwyy: Array4i64
    xwyz: Array4i64
    xwyw: Array4i64
    xwzx: Array4i64
    xwzy: Array4i64
    xwzz: Array4i64
    xwzw: Array4i64
    xwwx: Array4i64
    xwwy: Array4i64
    xwwz: Array4i64
    xwww: Array4i64
    yxxx: Array4i64
    yxxy: Array4i64
    yxxz: Array4i64
    yxxw: Array4i64
    yxyx: Array4i64
    yxyy: Array4i64
    yxyz: Array4i64
    yxyw: Array4i64
    yxzx: Array4i64
    yxzy: Array4i64
    yxzz: Array4i64
    yxzw: Array4i64
    yxwx: Array4i64
    yxwy: Array4i64
    yxwz: Array4i64
    yxww: Array4i64
    yyxx: Array4i64
    yyxy: Array4i64
    yyxz: Array4i64
    yyxw: Array4i64
    yyyx: Array4i64
    yyyy: Array4i64
    yyyz: Array4i64
    yyyw: Array4i64
    yyzx: Array4i64
    yyzy: Array4i64
    yyzz: Array4i64
    yyzw: Array4i64
    yywx: Array4i64
    yywy: Array4i64
    yywz: Array4i64
    yyww: Array4i64
    yzxx: Array4i64
    yzxy: Array4i64
    yzxz: Array4i64
    yzxw: Array4i64
    yzyx: Array4i64
    yzyy: Array4i64
    yzyz: Array4i64
    yzyw: Array4i64
    yzzx: Array4i64
    yzzy: Array4i64
    yzzz: Array4i64
    yzzw: Array4i64
    yzwx: Array4i64
    yzwy: Array4i64
    yzwz: Array4i64
    yzww: Array4i64
    ywxx: Array4i64
    ywxy: Array4i64
    ywxz: Array4i64
    ywxw: Array4i64
    ywyx: Array4i64
    ywyy: Array4i64
    ywyz: Array4i64
    ywyw: Array4i64
    ywzx: Array4i64
    ywzy: Array4i64
    ywzz: Array4i64
    ywzw: Array4i64
    ywwx: Array4i64
    ywwy: Array4i64
    ywwz: Array4i64
    ywww: Array4i64
    zxxx: Array4i64
    zxxy: Array4i64
    zxxz: Array4i64
    zxxw: Array4i64
    zxyx: Array4i64
    zxyy: Array4i64
    zxyz: Array4i64
    zxyw: Array4i64
    zxzx: Array4i64
    zxzy: Array4i64
    zxzz: Array4i64
    zxzw: Array4i64
    zxwx: Array4i64
    zxwy: Array4i64
    zxwz: Array4i64
    zxww: Array4i64
    zyxx: Array4i64
    zyxy: Array4i64
    zyxz: Array4i64
    zyxw: Array4i64
    zyyx: Array4i64
    zyyy: Array4i64
    zyyz: Array4i64
    zyyw: Array4i64
    zyzx: Array4i64
    zyzy: Array4i64
    zyzz: Array4i64
    zyzw: Array4i64
    zywx: Array4i64
    zywy: Array4i64
    zywz: Array4i64
    zyww: Array4i64
    zzxx: Array4i64
    zzxy: Array4i64
    zzxz: Array4i64
    zzxw: Array4i64
    zzyx: Array4i64
    zzyy: Array4i64
    zzyz: Array4i64
    zzyw: Array4i64
    zzzx: Array4i64
    zzzy: Array4i64
    zzzz: Array4i64
    zzzw: Array4i64
    zzwx: Array4i64
    zzwy: Array4i64
    zzwz: Array4i64
    zzww: Array4i64
    zwxx: Array4i64
    zwxy: Array4i64
    zwxz: Array4i64
    zwxw: Array4i64
    zwyx: Array4i64
    zwyy: Array4i64
    zwyz: Array4i64
    zwyw: Array4i64
    zwzx: Array4i64
    zwzy: Array4i64
    zwzz: Array4i64
    zwzw: Array4i64
    zwwx: Array4i64
    zwwy: Array4i64
    zwwz: Array4i64
    zwww: Array4i64
    wxxx: Array4i64
    wxxy: Array4i64
    wxxz: Array4i64
    wxxw: Array4i64
    wxyx: Array4i64
    wxyy: Array4i64
    wxyz: Array4i64
    wxyw: Array4i64
    wxzx: Array4i64
    wxzy: Array4i64
    wxzz: Array4i64
    wxzw: Array4i64
    wxwx: Array4i64
    wxwy: Array4i64
    wxwz: Array4i64
    wxww: Array4i64
    wyxx: Array4i64
    wyxy: Array4i64
    wyxz: Array4i64
    wyxw: Array4i64
    wyyx: Array4i64
    wyyy: Array4i64
    wyyz: Array4i64
    wyyw: Array4i64
    wyzx: Array4i64
    wyzy: Array4i64
    wyzz: Array4i64
    wyzw: Array4i64
    wywx: Array4i64
    wywy: Array4i64
    wywz: Array4i64
    wyww: Array4i64
    wzxx: Array4i64
    wzxy: Array4i64
    wzxz: Array4i64
    wzxw: Array4i64
    wzyx: Array4i64
    wzyy: Array4i64
    wzyz: Array4i64
    wzyw: Array4i64
    wzzx: Array4i64
    wzzy: Array4i64
    wzzz: Array4i64
    wzzw: Array4i64
    wzwx: Array4i64
    wzwy: Array4i64
    wzwz: Array4i64
    wzww: Array4i64
    wwxx: Array4i64
    wwxy: Array4i64
    wwxz: Array4i64
    wwxw: Array4i64
    wwyx: Array4i64
    wwyy: Array4i64
    wwyz: Array4i64
    wwyw: Array4i64
    wwzx: Array4i64
    wwzy: Array4i64
    wwzz: Array4i64
    wwzw: Array4i64
    wwwx: Array4i64
    wwwy: Array4i64
    wwwz: Array4i64
    wwww: Array4i64

_Array1u64Cp: TypeAlias = Union['Array1u64', '_UInt64Cp', 'drjit.scalar._Array1u64Cp', 'drjit.llvm._Array1u64Cp', '_Array1i64Cp']

class Array1u64(drjit.ArrayBase[Array1u64, _Array1u64Cp, UInt64, _UInt64Cp, UInt64, Array1u64, Array1b]):
    xx: Array2u64
    xy: Array2u64
    xz: Array2u64
    xw: Array2u64
    yx: Array2u64
    yy: Array2u64
    yz: Array2u64
    yw: Array2u64
    zx: Array2u64
    zy: Array2u64
    zz: Array2u64
    zw: Array2u64
    wx: Array2u64
    wy: Array2u64
    wz: Array2u64
    ww: Array2u64
    xxx: Array3u64
    xxy: Array3u64
    xxz: Array3u64
    xxw: Array3u64
    xyx: Array3u64
    xyy: Array3u64
    xyz: Array3u64
    xyw: Array3u64
    xzx: Array3u64
    xzy: Array3u64
    xzz: Array3u64
    xzw: Array3u64
    xwx: Array3u64
    xwy: Array3u64
    xwz: Array3u64
    xww: Array3u64
    yxx: Array3u64
    yxy: Array3u64
    yxz: Array3u64
    yxw: Array3u64
    yyx: Array3u64
    yyy: Array3u64
    yyz: Array3u64
    yyw: Array3u64
    yzx: Array3u64
    yzy: Array3u64
    yzz: Array3u64
    yzw: Array3u64
    ywx: Array3u64
    ywy: Array3u64
    ywz: Array3u64
    yww: Array3u64
    zxx: Array3u64
    zxy: Array3u64
    zxz: Array3u64
    zxw: Array3u64
    zyx: Array3u64
    zyy: Array3u64
    zyz: Array3u64
    zyw: Array3u64
    zzx: Array3u64
    zzy: Array3u64
    zzz: Array3u64
    zzw: Array3u64
    zwx: Array3u64
    zwy: Array3u64
    zwz: Array3u64
    zww: Array3u64
    wxx: Array3u64
    wxy: Array3u64
    wxz: Array3u64
    wxw: Array3u64
    wyx: Array3u64
    wyy: Array3u64
    wyz: Array3u64
    wyw: Array3u64
    wzx: Array3u64
    wzy: Array3u64
    wzz: Array3u64
    wzw: Array3u64
    wwx: Array3u64
    wwy: Array3u64
    wwz: Array3u64
    www: Array3u64
    xxxx: Array4u64
    xxxy: Array4u64
    xxxz: Array4u64
    xxxw: Array4u64
    xxyx: Array4u64
    xxyy: Array4u64
    xxyz: Array4u64
    xxyw: Array4u64
    xxzx: Array4u64
    xxzy: Array4u64
    xxzz: Array4u64
    xxzw: Array4u64
    xxwx: Array4u64
    xxwy: Array4u64
    xxwz: Array4u64
    xxww: Array4u64
    xyxx: Array4u64
    xyxy: Array4u64
    xyxz: Array4u64
    xyxw: Array4u64
    xyyx: Array4u64
    xyyy: Array4u64
    xyyz: Array4u64
    xyyw: Array4u64
    xyzx: Array4u64
    xyzy: Array4u64
    xyzz: Array4u64
    xyzw: Array4u64
    xywx: Array4u64
    xywy: Array4u64
    xywz: Array4u64
    xyww: Array4u64
    xzxx: Array4u64
    xzxy: Array4u64
    xzxz: Array4u64
    xzxw: Array4u64
    xzyx: Array4u64
    xzyy: Array4u64
    xzyz: Array4u64
    xzyw: Array4u64
    xzzx: Array4u64
    xzzy: Array4u64
    xzzz: Array4u64
    xzzw: Array4u64
    xzwx: Array4u64
    xzwy: Array4u64
    xzwz: Array4u64
    xzww: Array4u64
    xwxx: Array4u64
    xwxy: Array4u64
    xwxz: Array4u64
    xwxw: Array4u64
    xwyx: Array4u64
    xwyy: Array4u64
    xwyz: Array4u64
    xwyw: Array4u64
    xwzx: Array4u64
    xwzy: Array4u64
    xwzz: Array4u64
    xwzw: Array4u64
    xwwx: Array4u64
    xwwy: Array4u64
    xwwz: Array4u64
    xwww: Array4u64
    yxxx: Array4u64
    yxxy: Array4u64
    yxxz: Array4u64
    yxxw: Array4u64
    yxyx: Array4u64
    yxyy: Array4u64
    yxyz: Array4u64
    yxyw: Array4u64
    yxzx: Array4u64
    yxzy: Array4u64
    yxzz: Array4u64
    yxzw: Array4u64
    yxwx: Array4u64
    yxwy: Array4u64
    yxwz: Array4u64
    yxww: Array4u64
    yyxx: Array4u64
    yyxy: Array4u64
    yyxz: Array4u64
    yyxw: Array4u64
    yyyx: Array4u64
    yyyy: Array4u64
    yyyz: Array4u64
    yyyw: Array4u64
    yyzx: Array4u64
    yyzy: Array4u64
    yyzz: Array4u64
    yyzw: Array4u64
    yywx: Array4u64
    yywy: Array4u64
    yywz: Array4u64
    yyww: Array4u64
    yzxx: Array4u64
    yzxy: Array4u64
    yzxz: Array4u64
    yzxw: Array4u64
    yzyx: Array4u64
    yzyy: Array4u64
    yzyz: Array4u64
    yzyw: Array4u64
    yzzx: Array4u64
    yzzy: Array4u64
    yzzz: Array4u64
    yzzw: Array4u64
    yzwx: Array4u64
    yzwy: Array4u64
    yzwz: Array4u64
    yzww: Array4u64
    ywxx: Array4u64
    ywxy: Array4u64
    ywxz: Array4u64
    ywxw: Array4u64
    ywyx: Array4u64
    ywyy: Array4u64
    ywyz: Array4u64
    ywyw: Array4u64
    ywzx: Array4u64
    ywzy: Array4u64
    ywzz: Array4u64
    ywzw: Array4u64
    ywwx: Array4u64
    ywwy: Array4u64
    ywwz: Array4u64
    ywww: Array4u64
    zxxx: Array4u64
    zxxy: Array4u64
    zxxz: Array4u64
    zxxw: Array4u64
    zxyx: Array4u64
    zxyy: Array4u64
    zxyz: Array4u64
    zxyw: Array4u64
    zxzx: Array4u64
    zxzy: Array4u64
    zxzz: Array4u64
    zxzw: Array4u64
    zxwx: Array4u64
    zxwy: Array4u64
    zxwz: Array4u64
    zxww: Array4u64
    zyxx: Array4u64
    zyxy: Array4u64
    zyxz: Array4u64
    zyxw: Array4u64
    zyyx: Array4u64
    zyyy: Array4u64
    zyyz: Array4u64
    zyyw: Array4u64
    zyzx: Array4u64
    zyzy: Array4u64
    zyzz: Array4u64
    zyzw: Array4u64
    zywx: Array4u64
    zywy: Array4u64
    zywz: Array4u64
    zyww: Array4u64
    zzxx: Array4u64
    zzxy: Array4u64
    zzxz: Array4u64
    zzxw: Array4u64
    zzyx: Array4u64
    zzyy: Array4u64
    zzyz: Array4u64
    zzyw: Array4u64
    zzzx: Array4u64
    zzzy: Array4u64
    zzzz: Array4u64
    zzzw: Array4u64
    zzwx: Array4u64
    zzwy: Array4u64
    zzwz: Array4u64
    zzww: Array4u64
    zwxx: Array4u64
    zwxy: Array4u64
    zwxz: Array4u64
    zwxw: Array4u64
    zwyx: Array4u64
    zwyy: Array4u64
    zwyz: Array4u64
    zwyw: Array4u64
    zwzx: Array4u64
    zwzy: Array4u64
    zwzz: Array4u64
    zwzw: Array4u64
    zwwx: Array4u64
    zwwy: Array4u64
    zwwz: Array4u64
    zwww: Array4u64
    wxxx: Array4u64
    wxxy: Array4u64
    wxxz: Array4u64
    wxxw: Array4u64
    wxyx: Array4u64
    wxyy: Array4u64
    wxyz: Array4u64
    wxyw: Array4u64
    wxzx: Array4u64
    wxzy: Array4u64
    wxzz: Array4u64
    wxzw: Array4u64
    wxwx: Array4u64
    wxwy: Array4u64
    wxwz: Array4u64
    wxww: Array4u64
    wyxx: Array4u64
    wyxy: Array4u64
    wyxz: Array4u64
    wyxw: Array4u64
    wyyx: Array4u64
    wyyy: Array4u64
    wyyz: Array4u64
    wyyw: Array4u64
    wyzx: Array4u64
    wyzy: Array4u64
    wyzz: Array4u64
    wyzw: Array4u64
    wywx: Array4u64
    wywy: Array4u64
    wywz: Array4u64
    wyww: Array4u64
    wzxx: Array4u64
    wzxy: Array4u64
    wzxz: Array4u64
    wzxw: Array4u64
    wzyx: Array4u64
    wzyy: Array4u64
    wzyz: Array4u64
    wzyw: Array4u64
    wzzx: Array4u64
    wzzy: Array4u64
    wzzz: Array4u64
    wzzw: Array4u64
    wzwx: Array4u64
    wzwy: Array4u64
    wzwz: Array4u64
    wzww: Array4u64
    wwxx: Array4u64
    wwxy: Array4u64
    wwxz: Array4u64
    wwxw: Array4u64
    wwyx: Array4u64
    wwyy: Array4u64
    wwyz: Array4u64
    wwyw: Array4u64
    wwzx: Array4u64
    wwzy: Array4u64
    wwzz: Array4u64
    wwzw: Array4u64
    wwwx: Array4u64
    wwwy: Array4u64
    wwwz: Array4u64
    wwww: Array4u64

_Array1f16Cp: TypeAlias = Union['Array1f16', '_Float16Cp', 'drjit.scalar._Array1f16Cp', 'drjit.llvm._Array1f16Cp', '_Array1u64Cp']

class Array1f16(drjit.ArrayBase[Array1f16, _Array1f16Cp, Float16, _Float16Cp, Float16, Array1f16, Array1b]):
    xx: Array2f16
    xy: Array2f16
    xz: Array2f16
    xw: Array2f16
    yx: Array2f16
    yy: Array2f16
    yz: Array2f16
    yw: Array2f16
    zx: Array2f16
    zy: Array2f16
    zz: Array2f16
    zw: Array2f16
    wx: Array2f16
    wy: Array2f16
    wz: Array2f16
    ww: Array2f16
    xxx: Array3f16
    xxy: Array3f16
    xxz: Array3f16
    xxw: Array3f16
    xyx: Array3f16
    xyy: Array3f16
    xyz: Array3f16
    xyw: Array3f16
    xzx: Array3f16
    xzy: Array3f16
    xzz: Array3f16
    xzw: Array3f16
    xwx: Array3f16
    xwy: Array3f16
    xwz: Array3f16
    xww: Array3f16
    yxx: Array3f16
    yxy: Array3f16
    yxz: Array3f16
    yxw: Array3f16
    yyx: Array3f16
    yyy: Array3f16
    yyz: Array3f16
    yyw: Array3f16
    yzx: Array3f16
    yzy: Array3f16
    yzz: Array3f16
    yzw: Array3f16
    ywx: Array3f16
    ywy: Array3f16
    ywz: Array3f16
    yww: Array3f16
    zxx: Array3f16
    zxy: Array3f16
    zxz: Array3f16
    zxw: Array3f16
    zyx: Array3f16
    zyy: Array3f16
    zyz: Array3f16
    zyw: Array3f16
    zzx: Array3f16
    zzy: Array3f16
    zzz: Array3f16
    zzw: Array3f16
    zwx: Array3f16
    zwy: Array3f16
    zwz: Array3f16
    zww: Array3f16
    wxx: Array3f16
    wxy: Array3f16
    wxz: Array3f16
    wxw: Array3f16
    wyx: Array3f16
    wyy: Array3f16
    wyz: Array3f16
    wyw: Array3f16
    wzx: Array3f16
    wzy: Array3f16
    wzz: Array3f16
    wzw: Array3f16
    wwx: Array3f16
    wwy: Array3f16
    wwz: Array3f16
    www: Array3f16
    xxxx: Array4f16
    xxxy: Array4f16
    xxxz: Array4f16
    xxxw: Array4f16
    xxyx: Array4f16
    xxyy: Array4f16
    xxyz: Array4f16
    xxyw: Array4f16
    xxzx: Array4f16
    xxzy: Array4f16
    xxzz: Array4f16
    xxzw: Array4f16
    xxwx: Array4f16
    xxwy: Array4f16
    xxwz: Array4f16
    xxww: Array4f16
    xyxx: Array4f16
    xyxy: Array4f16
    xyxz: Array4f16
    xyxw: Array4f16
    xyyx: Array4f16
    xyyy: Array4f16
    xyyz: Array4f16
    xyyw: Array4f16
    xyzx: Array4f16
    xyzy: Array4f16
    xyzz: Array4f16
    xyzw: Array4f16
    xywx: Array4f16
    xywy: Array4f16
    xywz: Array4f16
    xyww: Array4f16
    xzxx: Array4f16
    xzxy: Array4f16
    xzxz: Array4f16
    xzxw: Array4f16
    xzyx: Array4f16
    xzyy: Array4f16
    xzyz: Array4f16
    xzyw: Array4f16
    xzzx: Array4f16
    xzzy: Array4f16
    xzzz: Array4f16
    xzzw: Array4f16
    xzwx: Array4f16
    xzwy: Array4f16
    xzwz: Array4f16
    xzww: Array4f16
    xwxx: Array4f16
    xwxy: Array4f16
    xwxz: Array4f16
    xwxw: Array4f16
    xwyx: Array4f16
    xwyy: Array4f16
    xwyz: Array4f16
    xwyw: Array4f16
    xwzx: Array4f16
    xwzy: Array4f16
    xwzz: Array4f16
    xwzw: Array4f16
    xwwx: Array4f16
    xwwy: Array4f16
    xwwz: Array4f16
    xwww: Array4f16
    yxxx: Array4f16
    yxxy: Array4f16
    yxxz: Array4f16
    yxxw: Array4f16
    yxyx: Array4f16
    yxyy: Array4f16
    yxyz: Array4f16
    yxyw: Array4f16
    yxzx: Array4f16
    yxzy: Array4f16
    yxzz: Array4f16
    yxzw: Array4f16
    yxwx: Array4f16
    yxwy: Array4f16
    yxwz: Array4f16
    yxww: Array4f16
    yyxx: Array4f16
    yyxy: Array4f16
    yyxz: Array4f16
    yyxw: Array4f16
    yyyx: Array4f16
    yyyy: Array4f16
    yyyz: Array4f16
    yyyw: Array4f16
    yyzx: Array4f16
    yyzy: Array4f16
    yyzz: Array4f16
    yyzw: Array4f16
    yywx: Array4f16
    yywy: Array4f16
    yywz: Array4f16
    yyww: Array4f16
    yzxx: Array4f16
    yzxy: Array4f16
    yzxz: Array4f16
    yzxw: Array4f16
    yzyx: Array4f16
    yzyy: Array4f16
    yzyz: Array4f16
    yzyw: Array4f16
    yzzx: Array4f16
    yzzy: Array4f16
    yzzz: Array4f16
    yzzw: Array4f16
    yzwx: Array4f16
    yzwy: Array4f16
    yzwz: Array4f16
    yzww: Array4f16
    ywxx: Array4f16
    ywxy: Array4f16
    ywxz: Array4f16
    ywxw: Array4f16
    ywyx: Array4f16
    ywyy: Array4f16
    ywyz: Array4f16
    ywyw: Array4f16
    ywzx: Array4f16
    ywzy: Array4f16
    ywzz: Array4f16
    ywzw: Array4f16
    ywwx: Array4f16
    ywwy: Array4f16
    ywwz: Array4f16
    ywww: Array4f16
    zxxx: Array4f16
    zxxy: Array4f16
    zxxz: Array4f16
    zxxw: Array4f16
    zxyx: Array4f16
    zxyy: Array4f16
    zxyz: Array4f16
    zxyw: Array4f16
    zxzx: Array4f16
    zxzy: Array4f16
    zxzz: Array4f16
    zxzw: Array4f16
    zxwx: Array4f16
    zxwy: Array4f16
    zxwz: Array4f16
    zxww: Array4f16
    zyxx: Array4f16
    zyxy: Array4f16
    zyxz: Array4f16
    zyxw: Array4f16
    zyyx: Array4f16
    zyyy: Array4f16
    zyyz: Array4f16
    zyyw: Array4f16
    zyzx: Array4f16
    zyzy: Array4f16
    zyzz: Array4f16
    zyzw: Array4f16
    zywx: Array4f16
    zywy: Array4f16
    zywz: Array4f16
    zyww: Array4f16
    zzxx: Array4f16
    zzxy: Array4f16
    zzxz: Array4f16
    zzxw: Array4f16
    zzyx: Array4f16
    zzyy: Array4f16
    zzyz: Array4f16
    zzyw: Array4f16
    zzzx: Array4f16
    zzzy: Array4f16
    zzzz: Array4f16
    zzzw: Array4f16
    zzwx: Array4f16
    zzwy: Array4f16
    zzwz: Array4f16
    zzww: Array4f16
    zwxx: Array4f16
    zwxy: Array4f16
    zwxz: Array4f16
    zwxw: Array4f16
    zwyx: Array4f16
    zwyy: Array4f16
    zwyz: Array4f16
    zwyw: Array4f16
    zwzx: Array4f16
    zwzy: Array4f16
    zwzz: Array4f16
    zwzw: Array4f16
    zwwx: Array4f16
    zwwy: Array4f16
    zwwz: Array4f16
    zwww: Array4f16
    wxxx: Array4f16
    wxxy: Array4f16
    wxxz: Array4f16
    wxxw: Array4f16
    wxyx: Array4f16
    wxyy: Array4f16
    wxyz: Array4f16
    wxyw: Array4f16
    wxzx: Array4f16
    wxzy: Array4f16
    wxzz: Array4f16
    wxzw: Array4f16
    wxwx: Array4f16
    wxwy: Array4f16
    wxwz: Array4f16
    wxww: Array4f16
    wyxx: Array4f16
    wyxy: Array4f16
    wyxz: Array4f16
    wyxw: Array4f16
    wyyx: Array4f16
    wyyy: Array4f16
    wyyz: Array4f16
    wyyw: Array4f16
    wyzx: Array4f16
    wyzy: Array4f16
    wyzz: Array4f16
    wyzw: Array4f16
    wywx: Array4f16
    wywy: Array4f16
    wywz: Array4f16
    wyww: Array4f16
    wzxx: Array4f16
    wzxy: Array4f16
    wzxz: Array4f16
    wzxw: Array4f16
    wzyx: Array4f16
    wzyy: Array4f16
    wzyz: Array4f16
    wzyw: Array4f16
    wzzx: Array4f16
    wzzy: Array4f16
    wzzz: Array4f16
    wzzw: Array4f16
    wzwx: Array4f16
    wzwy: Array4f16
    wzwz: Array4f16
    wzww: Array4f16
    wwxx: Array4f16
    wwxy: Array4f16
    wwxz: Array4f16
    wwxw: Array4f16
    wwyx: Array4f16
    wwyy: Array4f16
    wwyz: Array4f16
    wwyw: Array4f16
    wwzx: Array4f16
    wwzy: Array4f16
    wwzz: Array4f16
    wwzw: Array4f16
    wwwx: Array4f16
    wwwy: Array4f16
    wwwz: Array4f16
    wwww: Array4f16

_Array1fCp: TypeAlias = Union['Array1f', '_FloatCp', 'drjit.scalar._Array1fCp', 'drjit.llvm._Array1fCp', '_Array1f16Cp']

class Array1f(drjit.ArrayBase[Array1f, _Array1fCp, Float, _FloatCp, Float, Array1f, Array1b]):
    xx: Array2f
    xy: Array2f
    xz: Array2f
    xw: Array2f
    yx: Array2f
    yy: Array2f
    yz: Array2f
    yw: Array2f
    zx: Array2f
    zy: Array2f
    zz: Array2f
    zw: Array2f
    wx: Array2f
    wy: Array2f
    wz: Array2f
    ww: Array2f
    xxx: Array3f
    xxy: Array3f
    xxz: Array3f
    xxw: Array3f
    xyx: Array3f
    xyy: Array3f
    xyz: Array3f
    xyw: Array3f
    xzx: Array3f
    xzy: Array3f
    xzz: Array3f
    xzw: Array3f
    xwx: Array3f
    xwy: Array3f
    xwz: Array3f
    xww: Array3f
    yxx: Array3f
    yxy: Array3f
    yxz: Array3f
    yxw: Array3f
    yyx: Array3f
    yyy: Array3f
    yyz: Array3f
    yyw: Array3f
    yzx: Array3f
    yzy: Array3f
    yzz: Array3f
    yzw: Array3f
    ywx: Array3f
    ywy: Array3f
    ywz: Array3f
    yww: Array3f
    zxx: Array3f
    zxy: Array3f
    zxz: Array3f
    zxw: Array3f
    zyx: Array3f
    zyy: Array3f
    zyz: Array3f
    zyw: Array3f
    zzx: Array3f
    zzy: Array3f
    zzz: Array3f
    zzw: Array3f
    zwx: Array3f
    zwy: Array3f
    zwz: Array3f
    zww: Array3f
    wxx: Array3f
    wxy: Array3f
    wxz: Array3f
    wxw: Array3f
    wyx: Array3f
    wyy: Array3f
    wyz: Array3f
    wyw: Array3f
    wzx: Array3f
    wzy: Array3f
    wzz: Array3f
    wzw: Array3f
    wwx: Array3f
    wwy: Array3f
    wwz: Array3f
    www: Array3f
    xxxx: Array4f
    xxxy: Array4f
    xxxz: Array4f
    xxxw: Array4f
    xxyx: Array4f
    xxyy: Array4f
    xxyz: Array4f
    xxyw: Array4f
    xxzx: Array4f
    xxzy: Array4f
    xxzz: Array4f
    xxzw: Array4f
    xxwx: Array4f
    xxwy: Array4f
    xxwz: Array4f
    xxww: Array4f
    xyxx: Array4f
    xyxy: Array4f
    xyxz: Array4f
    xyxw: Array4f
    xyyx: Array4f
    xyyy: Array4f
    xyyz: Array4f
    xyyw: Array4f
    xyzx: Array4f
    xyzy: Array4f
    xyzz: Array4f
    xyzw: Array4f
    xywx: Array4f
    xywy: Array4f
    xywz: Array4f
    xyww: Array4f
    xzxx: Array4f
    xzxy: Array4f
    xzxz: Array4f
    xzxw: Array4f
    xzyx: Array4f
    xzyy: Array4f
    xzyz: Array4f
    xzyw: Array4f
    xzzx: Array4f
    xzzy: Array4f
    xzzz: Array4f
    xzzw: Array4f
    xzwx: Array4f
    xzwy: Array4f
    xzwz: Array4f
    xzww: Array4f
    xwxx: Array4f
    xwxy: Array4f
    xwxz: Array4f
    xwxw: Array4f
    xwyx: Array4f
    xwyy: Array4f
    xwyz: Array4f
    xwyw: Array4f
    xwzx: Array4f
    xwzy: Array4f
    xwzz: Array4f
    xwzw: Array4f
    xwwx: Array4f
    xwwy: Array4f
    xwwz: Array4f
    xwww: Array4f
    yxxx: Array4f
    yxxy: Array4f
    yxxz: Array4f
    yxxw: Array4f
    yxyx: Array4f
    yxyy: Array4f
    yxyz: Array4f
    yxyw: Array4f
    yxzx: Array4f
    yxzy: Array4f
    yxzz: Array4f
    yxzw: Array4f
    yxwx: Array4f
    yxwy: Array4f
    yxwz: Array4f
    yxww: Array4f
    yyxx: Array4f
    yyxy: Array4f
    yyxz: Array4f
    yyxw: Array4f
    yyyx: Array4f
    yyyy: Array4f
    yyyz: Array4f
    yyyw: Array4f
    yyzx: Array4f
    yyzy: Array4f
    yyzz: Array4f
    yyzw: Array4f
    yywx: Array4f
    yywy: Array4f
    yywz: Array4f
    yyww: Array4f
    yzxx: Array4f
    yzxy: Array4f
    yzxz: Array4f
    yzxw: Array4f
    yzyx: Array4f
    yzyy: Array4f
    yzyz: Array4f
    yzyw: Array4f
    yzzx: Array4f
    yzzy: Array4f
    yzzz: Array4f
    yzzw: Array4f
    yzwx: Array4f
    yzwy: Array4f
    yzwz: Array4f
    yzww: Array4f
    ywxx: Array4f
    ywxy: Array4f
    ywxz: Array4f
    ywxw: Array4f
    ywyx: Array4f
    ywyy: Array4f
    ywyz: Array4f
    ywyw: Array4f
    ywzx: Array4f
    ywzy: Array4f
    ywzz: Array4f
    ywzw: Array4f
    ywwx: Array4f
    ywwy: Array4f
    ywwz: Array4f
    ywww: Array4f
    zxxx: Array4f
    zxxy: Array4f
    zxxz: Array4f
    zxxw: Array4f
    zxyx: Array4f
    zxyy: Array4f
    zxyz: Array4f
    zxyw: Array4f
    zxzx: Array4f
    zxzy: Array4f
    zxzz: Array4f
    zxzw: Array4f
    zxwx: Array4f
    zxwy: Array4f
    zxwz: Array4f
    zxww: Array4f
    zyxx: Array4f
    zyxy: Array4f
    zyxz: Array4f
    zyxw: Array4f
    zyyx: Array4f
    zyyy: Array4f
    zyyz: Array4f
    zyyw: Array4f
    zyzx: Array4f
    zyzy: Array4f
    zyzz: Array4f
    zyzw: Array4f
    zywx: Array4f
    zywy: Array4f
    zywz: Array4f
    zyww: Array4f
    zzxx: Array4f
    zzxy: Array4f
    zzxz: Array4f
    zzxw: Array4f
    zzyx: Array4f
    zzyy: Array4f
    zzyz: Array4f
    zzyw: Array4f
    zzzx: Array4f
    zzzy: Array4f
    zzzz: Array4f
    zzzw: Array4f
    zzwx: Array4f
    zzwy: Array4f
    zzwz: Array4f
    zzww: Array4f
    zwxx: Array4f
    zwxy: Array4f
    zwxz: Array4f
    zwxw: Array4f
    zwyx: Array4f
    zwyy: Array4f
    zwyz: Array4f
    zwyw: Array4f
    zwzx: Array4f
    zwzy: Array4f
    zwzz: Array4f
    zwzw: Array4f
    zwwx: Array4f
    zwwy: Array4f
    zwwz: Array4f
    zwww: Array4f
    wxxx: Array4f
    wxxy: Array4f
    wxxz: Array4f
    wxxw: Array4f
    wxyx: Array4f
    wxyy: Array4f
    wxyz: Array4f
    wxyw: Array4f
    wxzx: Array4f
    wxzy: Array4f
    wxzz: Array4f
    wxzw: Array4f
    wxwx: Array4f
    wxwy: Array4f
    wxwz: Array4f
    wxww: Array4f
    wyxx: Array4f
    wyxy: Array4f
    wyxz: Array4f
    wyxw: Array4f
    wyyx: Array4f
    wyyy: Array4f
    wyyz: Array4f
    wyyw: Array4f
    wyzx: Array4f
    wyzy: Array4f
    wyzz: Array4f
    wyzw: Array4f
    wywx: Array4f
    wywy: Array4f
    wywz: Array4f
    wyww: Array4f
    wzxx: Array4f
    wzxy: Array4f
    wzxz: Array4f
    wzxw: Array4f
    wzyx: Array4f
    wzyy: Array4f
    wzyz: Array4f
    wzyw: Array4f
    wzzx: Array4f
    wzzy: Array4f
    wzzz: Array4f
    wzzw: Array4f
    wzwx: Array4f
    wzwy: Array4f
    wzwz: Array4f
    wzww: Array4f
    wwxx: Array4f
    wwxy: Array4f
    wwxz: Array4f
    wwxw: Array4f
    wwyx: Array4f
    wwyy: Array4f
    wwyz: Array4f
    wwyw: Array4f
    wwzx: Array4f
    wwzy: Array4f
    wwzz: Array4f
    wwzw: Array4f
    wwwx: Array4f
    wwwy: Array4f
    wwwz: Array4f
    wwww: Array4f

_Array1f64Cp: TypeAlias = Union['Array1f64', '_Float64Cp', 'drjit.scalar._Array1f64Cp', 'drjit.llvm._Array1f64Cp', '_Array1fCp']

class Array1f64(drjit.ArrayBase[Array1f64, _Array1f64Cp, Float64, _Float64Cp, Float64, Array1f64, Array1b]):
    xx: Array2f64
    xy: Array2f64
    xz: Array2f64
    xw: Array2f64
    yx: Array2f64
    yy: Array2f64
    yz: Array2f64
    yw: Array2f64
    zx: Array2f64
    zy: Array2f64
    zz: Array2f64
    zw: Array2f64
    wx: Array2f64
    wy: Array2f64
    wz: Array2f64
    ww: Array2f64
    xxx: Array3f64
    xxy: Array3f64
    xxz: Array3f64
    xxw: Array3f64
    xyx: Array3f64
    xyy: Array3f64
    xyz: Array3f64
    xyw: Array3f64
    xzx: Array3f64
    xzy: Array3f64
    xzz: Array3f64
    xzw: Array3f64
    xwx: Array3f64
    xwy: Array3f64
    xwz: Array3f64
    xww: Array3f64
    yxx: Array3f64
    yxy: Array3f64
    yxz: Array3f64
    yxw: Array3f64
    yyx: Array3f64
    yyy: Array3f64
    yyz: Array3f64
    yyw: Array3f64
    yzx: Array3f64
    yzy: Array3f64
    yzz: Array3f64
    yzw: Array3f64
    ywx: Array3f64
    ywy: Array3f64
    ywz: Array3f64
    yww: Array3f64
    zxx: Array3f64
    zxy: Array3f64
    zxz: Array3f64
    zxw: Array3f64
    zyx: Array3f64
    zyy: Array3f64
    zyz: Array3f64
    zyw: Array3f64
    zzx: Array3f64
    zzy: Array3f64
    zzz: Array3f64
    zzw: Array3f64
    zwx: Array3f64
    zwy: Array3f64
    zwz: Array3f64
    zww: Array3f64
    wxx: Array3f64
    wxy: Array3f64
    wxz: Array3f64
    wxw: Array3f64
    wyx: Array3f64
    wyy: Array3f64
    wyz: Array3f64
    wyw: Array3f64
    wzx: Array3f64
    wzy: Array3f64
    wzz: Array3f64
    wzw: Array3f64
    wwx: Array3f64
    wwy: Array3f64
    wwz: Array3f64
    www: Array3f64
    xxxx: Array4f64
    xxxy: Array4f64
    xxxz: Array4f64
    xxxw: Array4f64
    xxyx: Array4f64
    xxyy: Array4f64
    xxyz: Array4f64
    xxyw: Array4f64
    xxzx: Array4f64
    xxzy: Array4f64
    xxzz: Array4f64
    xxzw: Array4f64
    xxwx: Array4f64
    xxwy: Array4f64
    xxwz: Array4f64
    xxww: Array4f64
    xyxx: Array4f64
    xyxy: Array4f64
    xyxz: Array4f64
    xyxw: Array4f64
    xyyx: Array4f64
    xyyy: Array4f64
    xyyz: Array4f64
    xyyw: Array4f64
    xyzx: Array4f64
    xyzy: Array4f64
    xyzz: Array4f64
    xyzw: Array4f64
    xywx: Array4f64
    xywy: Array4f64
    xywz: Array4f64
    xyww: Array4f64
    xzxx: Array4f64
    xzxy: Array4f64
    xzxz: Array4f64
    xzxw: Array4f64
    xzyx: Array4f64
    xzyy: Array4f64
    xzyz: Array4f64
    xzyw: Array4f64
    xzzx: Array4f64
    xzzy: Array4f64
    xzzz: Array4f64
    xzzw: Array4f64
    xzwx: Array4f64
    xzwy: Array4f64
    xzwz: Array4f64
    xzww: Array4f64
    xwxx: Array4f64
    xwxy: Array4f64
    xwxz: Array4f64
    xwxw: Array4f64
    xwyx: Array4f64
    xwyy: Array4f64
    xwyz: Array4f64
    xwyw: Array4f64
    xwzx: Array4f64
    xwzy: Array4f64
    xwzz: Array4f64
    xwzw: Array4f64
    xwwx: Array4f64
    xwwy: Array4f64
    xwwz: Array4f64
    xwww: Array4f64
    yxxx: Array4f64
    yxxy: Array4f64
    yxxz: Array4f64
    yxxw: Array4f64
    yxyx: Array4f64
    yxyy: Array4f64
    yxyz: Array4f64
    yxyw: Array4f64
    yxzx: Array4f64
    yxzy: Array4f64
    yxzz: Array4f64
    yxzw: Array4f64
    yxwx: Array4f64
    yxwy: Array4f64
    yxwz: Array4f64
    yxww: Array4f64
    yyxx: Array4f64
    yyxy: Array4f64
    yyxz: Array4f64
    yyxw: Array4f64
    yyyx: Array4f64
    yyyy: Array4f64
    yyyz: Array4f64
    yyyw: Array4f64
    yyzx: Array4f64
    yyzy: Array4f64
    yyzz: Array4f64
    yyzw: Array4f64
    yywx: Array4f64
    yywy: Array4f64
    yywz: Array4f64
    yyww: Array4f64
    yzxx: Array4f64
    yzxy: Array4f64
    yzxz: Array4f64
    yzxw: Array4f64
    yzyx: Array4f64
    yzyy: Array4f64
    yzyz: Array4f64
    yzyw: Array4f64
    yzzx: Array4f64
    yzzy: Array4f64
    yzzz: Array4f64
    yzzw: Array4f64
    yzwx: Array4f64
    yzwy: Array4f64
    yzwz: Array4f64
    yzww: Array4f64
    ywxx: Array4f64
    ywxy: Array4f64
    ywxz: Array4f64
    ywxw: Array4f64
    ywyx: Array4f64
    ywyy: Array4f64
    ywyz: Array4f64
    ywyw: Array4f64
    ywzx: Array4f64
    ywzy: Array4f64
    ywzz: Array4f64
    ywzw: Array4f64
    ywwx: Array4f64
    ywwy: Array4f64
    ywwz: Array4f64
    ywww: Array4f64
    zxxx: Array4f64
    zxxy: Array4f64
    zxxz: Array4f64
    zxxw: Array4f64
    zxyx: Array4f64
    zxyy: Array4f64
    zxyz: Array4f64
    zxyw: Array4f64
    zxzx: Array4f64
    zxzy: Array4f64
    zxzz: Array4f64
    zxzw: Array4f64
    zxwx: Array4f64
    zxwy: Array4f64
    zxwz: Array4f64
    zxww: Array4f64
    zyxx: Array4f64
    zyxy: Array4f64
    zyxz: Array4f64
    zyxw: Array4f64
    zyyx: Array4f64
    zyyy: Array4f64
    zyyz: Array4f64
    zyyw: Array4f64
    zyzx: Array4f64
    zyzy: Array4f64
    zyzz: Array4f64
    zyzw: Array4f64
    zywx: Array4f64
    zywy: Array4f64
    zywz: Array4f64
    zyww: Array4f64
    zzxx: Array4f64
    zzxy: Array4f64
    zzxz: Array4f64
    zzxw: Array4f64
    zzyx: Array4f64
    zzyy: Array4f64
    zzyz: Array4f64
    zzyw: Array4f64
    zzzx: Array4f64
    zzzy: Array4f64
    zzzz: Array4f64
    zzzw: Array4f64
    zzwx: Array4f64
    zzwy: Array4f64
    zzwz: Array4f64
    zzww: Array4f64
    zwxx: Array4f64
    zwxy: Array4f64
    zwxz: Array4f64
    zwxw: Array4f64
    zwyx: Array4f64
    zwyy: Array4f64
    zwyz: Array4f64
    zwyw: Array4f64
    zwzx: Array4f64
    zwzy: Array4f64
    zwzz: Array4f64
    zwzw: Array4f64
    zwwx: Array4f64
    zwwy: Array4f64
    zwwz: Array4f64
    zwww: Array4f64
    wxxx: Array4f64
    wxxy: Array4f64
    wxxz: Array4f64
    wxxw: Array4f64
    wxyx: Array4f64
    wxyy: Array4f64
    wxyz: Array4f64
    wxyw: Array4f64
    wxzx: Array4f64
    wxzy: Array4f64
    wxzz: Array4f64
    wxzw: Array4f64
    wxwx: Array4f64
    wxwy: Array4f64
    wxwz: Array4f64
    wxww: Array4f64
    wyxx: Array4f64
    wyxy: Array4f64
    wyxz: Array4f64
    wyxw: Array4f64
    wyyx: Array4f64
    wyyy: Array4f64
    wyyz: Array4f64
    wyyw: Array4f64
    wyzx: Array4f64
    wyzy: Array4f64
    wyzz: Array4f64
    wyzw: Array4f64
    wywx: Array4f64
    wywy: Array4f64
    wywz: Array4f64
    wyww: Array4f64
    wzxx: Array4f64
    wzxy: Array4f64
    wzxz: Array4f64
    wzxw: Array4f64
    wzyx: Array4f64
    wzyy: Array4f64
    wzyz: Array4f64
    wzyw: Array4f64
    wzzx: Array4f64
    wzzy: Array4f64
    wzzz: Array4f64
    wzzw: Array4f64
    wzwx: Array4f64
    wzwy: Array4f64
    wzwz: Array4f64
    wzww: Array4f64
    wwxx: Array4f64
    wwxy: Array4f64
    wwxz: Array4f64
    wwxw: Array4f64
    wwyx: Array4f64
    wwyy: Array4f64
    wwyz: Array4f64
    wwyw: Array4f64
    wwzx: Array4f64
    wwzy: Array4f64
    wwzz: Array4f64
    wwzw: Array4f64
    wwwx: Array4f64
    wwwy: Array4f64
    wwwz: Array4f64
    wwww: Array4f64

_Array2bCp: TypeAlias = Union['Array2b', '_BoolCp', 'drjit.scalar._Array2bCp', 'drjit.llvm._Array2bCp']

class Array2b(drjit.ArrayBase[Array2b, _Array2bCp, Bool, _BoolCp, Bool, Array2b, Array2b]):
    xx: Array2b
    xy: Array2b
    xz: Array2b
    xw: Array2b
    yx: Array2b
    yy: Array2b
    yz: Array2b
    yw: Array2b
    zx: Array2b
    zy: Array2b
    zz: Array2b
    zw: Array2b
    wx: Array2b
    wy: Array2b
    wz: Array2b
    ww: Array2b
    xxx: Array3b
    xxy: Array3b
    xxz: Array3b
    xxw: Array3b
    xyx: Array3b
    xyy: Array3b
    xyz: Array3b
    xyw: Array3b
    xzx: Array3b
    xzy: Array3b
    xzz: Array3b
    xzw: Array3b
    xwx: Array3b
    xwy: Array3b
    xwz: Array3b
    xww: Array3b
    yxx: Array3b
    yxy: Array3b
    yxz: Array3b
    yxw: Array3b
    yyx: Array3b
    yyy: Array3b
    yyz: Array3b
    yyw: Array3b
    yzx: Array3b
    yzy: Array3b
    yzz: Array3b
    yzw: Array3b
    ywx: Array3b
    ywy: Array3b
    ywz: Array3b
    yww: Array3b
    zxx: Array3b
    zxy: Array3b
    zxz: Array3b
    zxw: Array3b
    zyx: Array3b
    zyy: Array3b
    zyz: Array3b
    zyw: Array3b
    zzx: Array3b
    zzy: Array3b
    zzz: Array3b
    zzw: Array3b
    zwx: Array3b
    zwy: Array3b
    zwz: Array3b
    zww: Array3b
    wxx: Array3b
    wxy: Array3b
    wxz: Array3b
    wxw: Array3b
    wyx: Array3b
    wyy: Array3b
    wyz: Array3b
    wyw: Array3b
    wzx: Array3b
    wzy: Array3b
    wzz: Array3b
    wzw: Array3b
    wwx: Array3b
    wwy: Array3b
    wwz: Array3b
    www: Array3b
    xxxx: Array4b
    xxxy: Array4b
    xxxz: Array4b
    xxxw: Array4b
    xxyx: Array4b
    xxyy: Array4b
    xxyz: Array4b
    xxyw: Array4b
    xxzx: Array4b
    xxzy: Array4b
    xxzz: Array4b
    xxzw: Array4b
    xxwx: Array4b
    xxwy: Array4b
    xxwz: Array4b
    xxww: Array4b
    xyxx: Array4b
    xyxy: Array4b
    xyxz: Array4b
    xyxw: Array4b
    xyyx: Array4b
    xyyy: Array4b
    xyyz: Array4b
    xyyw: Array4b
    xyzx: Array4b
    xyzy: Array4b
    xyzz: Array4b
    xyzw: Array4b
    xywx: Array4b
    xywy: Array4b
    xywz: Array4b
    xyww: Array4b
    xzxx: Array4b
    xzxy: Array4b
    xzxz: Array4b
    xzxw: Array4b
    xzyx: Array4b
    xzyy: Array4b
    xzyz: Array4b
    xzyw: Array4b
    xzzx: Array4b
    xzzy: Array4b
    xzzz: Array4b
    xzzw: Array4b
    xzwx: Array4b
    xzwy: Array4b
    xzwz: Array4b
    xzww: Array4b
    xwxx: Array4b
    xwxy: Array4b
    xwxz: Array4b
    xwxw: Array4b
    xwyx: Array4b
    xwyy: Array4b
    xwyz: Array4b
    xwyw: Array4b
    xwzx: Array4b
    xwzy: Array4b
    xwzz: Array4b
    xwzw: Array4b
    xwwx: Array4b
    xwwy: Array4b
    xwwz: Array4b
    xwww: Array4b
    yxxx: Array4b
    yxxy: Array4b
    yxxz: Array4b
    yxxw: Array4b
    yxyx: Array4b
    yxyy: Array4b
    yxyz: Array4b
    yxyw: Array4b
    yxzx: Array4b
    yxzy: Array4b
    yxzz: Array4b
    yxzw: Array4b
    yxwx: Array4b
    yxwy: Array4b
    yxwz: Array4b
    yxww: Array4b
    yyxx: Array4b
    yyxy: Array4b
    yyxz: Array4b
    yyxw: Array4b
    yyyx: Array4b
    yyyy: Array4b
    yyyz: Array4b
    yyyw: Array4b
    yyzx: Array4b
    yyzy: Array4b
    yyzz: Array4b
    yyzw: Array4b
    yywx: Array4b
    yywy: Array4b
    yywz: Array4b
    yyww: Array4b
    yzxx: Array4b
    yzxy: Array4b
    yzxz: Array4b
    yzxw: Array4b
    yzyx: Array4b
    yzyy: Array4b
    yzyz: Array4b
    yzyw: Array4b
    yzzx: Array4b
    yzzy: Array4b
    yzzz: Array4b
    yzzw: Array4b
    yzwx: Array4b
    yzwy: Array4b
    yzwz: Array4b
    yzww: Array4b
    ywxx: Array4b
    ywxy: Array4b
    ywxz: Array4b
    ywxw: Array4b
    ywyx: Array4b
    ywyy: Array4b
    ywyz: Array4b
    ywyw: Array4b
    ywzx: Array4b
    ywzy: Array4b
    ywzz: Array4b
    ywzw: Array4b
    ywwx: Array4b
    ywwy: Array4b
    ywwz: Array4b
    ywww: Array4b
    zxxx: Array4b
    zxxy: Array4b
    zxxz: Array4b
    zxxw: Array4b
    zxyx: Array4b
    zxyy: Array4b
    zxyz: Array4b
    zxyw: Array4b
    zxzx: Array4b
    zxzy: Array4b
    zxzz: Array4b
    zxzw: Array4b
    zxwx: Array4b
    zxwy: Array4b
    zxwz: Array4b
    zxww: Array4b
    zyxx: Array4b
    zyxy: Array4b
    zyxz: Array4b
    zyxw: Array4b
    zyyx: Array4b
    zyyy: Array4b
    zyyz: Array4b
    zyyw: Array4b
    zyzx: Array4b
    zyzy: Array4b
    zyzz: Array4b
    zyzw: Array4b
    zywx: Array4b
    zywy: Array4b
    zywz: Array4b
    zyww: Array4b
    zzxx: Array4b
    zzxy: Array4b
    zzxz: Array4b
    zzxw: Array4b
    zzyx: Array4b
    zzyy: Array4b
    zzyz: Array4b
    zzyw: Array4b
    zzzx: Array4b
    zzzy: Array4b
    zzzz: Array4b
    zzzw: Array4b
    zzwx: Array4b
    zzwy: Array4b
    zzwz: Array4b
    zzww: Array4b
    zwxx: Array4b
    zwxy: Array4b
    zwxz: Array4b
    zwxw: Array4b
    zwyx: Array4b
    zwyy: Array4b
    zwyz: Array4b
    zwyw: Array4b
    zwzx: Array4b
    zwzy: Array4b
    zwzz: Array4b
    zwzw: Array4b
    zwwx: Array4b
    zwwy: Array4b
    zwwz: Array4b
    zwww: Array4b
    wxxx: Array4b
    wxxy: Array4b
    wxxz: Array4b
    wxxw: Array4b
    wxyx: Array4b
    wxyy: Array4b
    wxyz: Array4b
    wxyw: Array4b
    wxzx: Array4b
    wxzy: Array4b
    wxzz: Array4b
    wxzw: Array4b
    wxwx: Array4b
    wxwy: Array4b
    wxwz: Array4b
    wxww: Array4b
    wyxx: Array4b
    wyxy: Array4b
    wyxz: Array4b
    wyxw: Array4b
    wyyx: Array4b
    wyyy: Array4b
    wyyz: Array4b
    wyyw: Array4b
    wyzx: Array4b
    wyzy: Array4b
    wyzz: Array4b
    wyzw: Array4b
    wywx: Array4b
    wywy: Array4b
    wywz: Array4b
    wyww: Array4b
    wzxx: Array4b
    wzxy: Array4b
    wzxz: Array4b
    wzxw: Array4b
    wzyx: Array4b
    wzyy: Array4b
    wzyz: Array4b
    wzyw: Array4b
    wzzx: Array4b
    wzzy: Array4b
    wzzz: Array4b
    wzzw: Array4b
    wzwx: Array4b
    wzwy: Array4b
    wzwz: Array4b
    wzww: Array4b
    wwxx: Array4b
    wwxy: Array4b
    wwxz: Array4b
    wwxw: Array4b
    wwyx: Array4b
    wwyy: Array4b
    wwyz: Array4b
    wwyw: Array4b
    wwzx: Array4b
    wwzy: Array4b
    wwzz: Array4b
    wwzw: Array4b
    wwwx: Array4b
    wwwy: Array4b
    wwwz: Array4b
    wwww: Array4b

_Array2i8Cp: TypeAlias = Union['Array2i8', '_Int8Cp', 'drjit.scalar._Array2i8Cp', 'drjit.llvm._Array2i8Cp']

class Array2i8(drjit.ArrayBase[Array2i8, _Array2i8Cp, Int8, _Int8Cp, Int8, Array2i8, Array2b]):
    xx: Array2i8
    xy: Array2i8
    xz: Array2i8
    xw: Array2i8
    yx: Array2i8
    yy: Array2i8
    yz: Array2i8
    yw: Array2i8
    zx: Array2i8
    zy: Array2i8
    zz: Array2i8
    zw: Array2i8
    wx: Array2i8
    wy: Array2i8
    wz: Array2i8
    ww: Array2i8
    xxx: Array3i8
    xxy: Array3i8
    xxz: Array3i8
    xxw: Array3i8
    xyx: Array3i8
    xyy: Array3i8
    xyz: Array3i8
    xyw: Array3i8
    xzx: Array3i8
    xzy: Array3i8
    xzz: Array3i8
    xzw: Array3i8
    xwx: Array3i8
    xwy: Array3i8
    xwz: Array3i8
    xww: Array3i8
    yxx: Array3i8
    yxy: Array3i8
    yxz: Array3i8
    yxw: Array3i8
    yyx: Array3i8
    yyy: Array3i8
    yyz: Array3i8
    yyw: Array3i8
    yzx: Array3i8
    yzy: Array3i8
    yzz: Array3i8
    yzw: Array3i8
    ywx: Array3i8
    ywy: Array3i8
    ywz: Array3i8
    yww: Array3i8
    zxx: Array3i8
    zxy: Array3i8
    zxz: Array3i8
    zxw: Array3i8
    zyx: Array3i8
    zyy: Array3i8
    zyz: Array3i8
    zyw: Array3i8
    zzx: Array3i8
    zzy: Array3i8
    zzz: Array3i8
    zzw: Array3i8
    zwx: Array3i8
    zwy: Array3i8
    zwz: Array3i8
    zww: Array3i8
    wxx: Array3i8
    wxy: Array3i8
    wxz: Array3i8
    wxw: Array3i8
    wyx: Array3i8
    wyy: Array3i8
    wyz: Array3i8
    wyw: Array3i8
    wzx: Array3i8
    wzy: Array3i8
    wzz: Array3i8
    wzw: Array3i8
    wwx: Array3i8
    wwy: Array3i8
    wwz: Array3i8
    www: Array3i8
    xxxx: Array4i8
    xxxy: Array4i8
    xxxz: Array4i8
    xxxw: Array4i8
    xxyx: Array4i8
    xxyy: Array4i8
    xxyz: Array4i8
    xxyw: Array4i8
    xxzx: Array4i8
    xxzy: Array4i8
    xxzz: Array4i8
    xxzw: Array4i8
    xxwx: Array4i8
    xxwy: Array4i8
    xxwz: Array4i8
    xxww: Array4i8
    xyxx: Array4i8
    xyxy: Array4i8
    xyxz: Array4i8
    xyxw: Array4i8
    xyyx: Array4i8
    xyyy: Array4i8
    xyyz: Array4i8
    xyyw: Array4i8
    xyzx: Array4i8
    xyzy: Array4i8
    xyzz: Array4i8
    xyzw: Array4i8
    xywx: Array4i8
    xywy: Array4i8
    xywz: Array4i8
    xyww: Array4i8
    xzxx: Array4i8
    xzxy: Array4i8
    xzxz: Array4i8
    xzxw: Array4i8
    xzyx: Array4i8
    xzyy: Array4i8
    xzyz: Array4i8
    xzyw: Array4i8
    xzzx: Array4i8
    xzzy: Array4i8
    xzzz: Array4i8
    xzzw: Array4i8
    xzwx: Array4i8
    xzwy: Array4i8
    xzwz: Array4i8
    xzww: Array4i8
    xwxx: Array4i8
    xwxy: Array4i8
    xwxz: Array4i8
    xwxw: Array4i8
    xwyx: Array4i8
    xwyy: Array4i8
    xwyz: Array4i8
    xwyw: Array4i8
    xwzx: Array4i8
    xwzy: Array4i8
    xwzz: Array4i8
    xwzw: Array4i8
    xwwx: Array4i8
    xwwy: Array4i8
    xwwz: Array4i8
    xwww: Array4i8
    yxxx: Array4i8
    yxxy: Array4i8
    yxxz: Array4i8
    yxxw: Array4i8
    yxyx: Array4i8
    yxyy: Array4i8
    yxyz: Array4i8
    yxyw: Array4i8
    yxzx: Array4i8
    yxzy: Array4i8
    yxzz: Array4i8
    yxzw: Array4i8
    yxwx: Array4i8
    yxwy: Array4i8
    yxwz: Array4i8
    yxww: Array4i8
    yyxx: Array4i8
    yyxy: Array4i8
    yyxz: Array4i8
    yyxw: Array4i8
    yyyx: Array4i8
    yyyy: Array4i8
    yyyz: Array4i8
    yyyw: Array4i8
    yyzx: Array4i8
    yyzy: Array4i8
    yyzz: Array4i8
    yyzw: Array4i8
    yywx: Array4i8
    yywy: Array4i8
    yywz: Array4i8
    yyww: Array4i8
    yzxx: Array4i8
    yzxy: Array4i8
    yzxz: Array4i8
    yzxw: Array4i8
    yzyx: Array4i8
    yzyy: Array4i8
    yzyz: Array4i8
    yzyw: Array4i8
    yzzx: Array4i8
    yzzy: Array4i8
    yzzz: Array4i8
    yzzw: Array4i8
    yzwx: Array4i8
    yzwy: Array4i8
    yzwz: Array4i8
    yzww: Array4i8
    ywxx: Array4i8
    ywxy: Array4i8
    ywxz: Array4i8
    ywxw: Array4i8
    ywyx: Array4i8
    ywyy: Array4i8
    ywyz: Array4i8
    ywyw: Array4i8
    ywzx: Array4i8
    ywzy: Array4i8
    ywzz: Array4i8
    ywzw: Array4i8
    ywwx: Array4i8
    ywwy: Array4i8
    ywwz: Array4i8
    ywww: Array4i8
    zxxx: Array4i8
    zxxy: Array4i8
    zxxz: Array4i8
    zxxw: Array4i8
    zxyx: Array4i8
    zxyy: Array4i8
    zxyz: Array4i8
    zxyw: Array4i8
    zxzx: Array4i8
    zxzy: Array4i8
    zxzz: Array4i8
    zxzw: Array4i8
    zxwx: Array4i8
    zxwy: Array4i8
    zxwz: Array4i8
    zxww: Array4i8
    zyxx: Array4i8
    zyxy: Array4i8
    zyxz: Array4i8
    zyxw: Array4i8
    zyyx: Array4i8
    zyyy: Array4i8
    zyyz: Array4i8
    zyyw: Array4i8
    zyzx: Array4i8
    zyzy: Array4i8
    zyzz: Array4i8
    zyzw: Array4i8
    zywx: Array4i8
    zywy: Array4i8
    zywz: Array4i8
    zyww: Array4i8
    zzxx: Array4i8
    zzxy: Array4i8
    zzxz: Array4i8
    zzxw: Array4i8
    zzyx: Array4i8
    zzyy: Array4i8
    zzyz: Array4i8
    zzyw: Array4i8
    zzzx: Array4i8
    zzzy: Array4i8
    zzzz: Array4i8
    zzzw: Array4i8
    zzwx: Array4i8
    zzwy: Array4i8
    zzwz: Array4i8
    zzww: Array4i8
    zwxx: Array4i8
    zwxy: Array4i8
    zwxz: Array4i8
    zwxw: Array4i8
    zwyx: Array4i8
    zwyy: Array4i8
    zwyz: Array4i8
    zwyw: Array4i8
    zwzx: Array4i8
    zwzy: Array4i8
    zwzz: Array4i8
    zwzw: Array4i8
    zwwx: Array4i8
    zwwy: Array4i8
    zwwz: Array4i8
    zwww: Array4i8
    wxxx: Array4i8
    wxxy: Array4i8
    wxxz: Array4i8
    wxxw: Array4i8
    wxyx: Array4i8
    wxyy: Array4i8
    wxyz: Array4i8
    wxyw: Array4i8
    wxzx: Array4i8
    wxzy: Array4i8
    wxzz: Array4i8
    wxzw: Array4i8
    wxwx: Array4i8
    wxwy: Array4i8
    wxwz: Array4i8
    wxww: Array4i8
    wyxx: Array4i8
    wyxy: Array4i8
    wyxz: Array4i8
    wyxw: Array4i8
    wyyx: Array4i8
    wyyy: Array4i8
    wyyz: Array4i8
    wyyw: Array4i8
    wyzx: Array4i8
    wyzy: Array4i8
    wyzz: Array4i8
    wyzw: Array4i8
    wywx: Array4i8
    wywy: Array4i8
    wywz: Array4i8
    wyww: Array4i8
    wzxx: Array4i8
    wzxy: Array4i8
    wzxz: Array4i8
    wzxw: Array4i8
    wzyx: Array4i8
    wzyy: Array4i8
    wzyz: Array4i8
    wzyw: Array4i8
    wzzx: Array4i8
    wzzy: Array4i8
    wzzz: Array4i8
    wzzw: Array4i8
    wzwx: Array4i8
    wzwy: Array4i8
    wzwz: Array4i8
    wzww: Array4i8
    wwxx: Array4i8
    wwxy: Array4i8
    wwxz: Array4i8
    wwxw: Array4i8
    wwyx: Array4i8
    wwyy: Array4i8
    wwyz: Array4i8
    wwyw: Array4i8
    wwzx: Array4i8
    wwzy: Array4i8
    wwzz: Array4i8
    wwzw: Array4i8
    wwwx: Array4i8
    wwwy: Array4i8
    wwwz: Array4i8
    wwww: Array4i8

_Array2u8Cp: TypeAlias = Union['Array2u8', '_UInt8Cp', 'drjit.scalar._Array2u8Cp', 'drjit.llvm._Array2u8Cp']

class Array2u8(drjit.ArrayBase[Array2u8, _Array2u8Cp, UInt8, _UInt8Cp, UInt8, Array2u8, Array2b]):
    xx: Array2u8
    xy: Array2u8
    xz: Array2u8
    xw: Array2u8
    yx: Array2u8
    yy: Array2u8
    yz: Array2u8
    yw: Array2u8
    zx: Array2u8
    zy: Array2u8
    zz: Array2u8
    zw: Array2u8
    wx: Array2u8
    wy: Array2u8
    wz: Array2u8
    ww: Array2u8
    xxx: Array3u8
    xxy: Array3u8
    xxz: Array3u8
    xxw: Array3u8
    xyx: Array3u8
    xyy: Array3u8
    xyz: Array3u8
    xyw: Array3u8
    xzx: Array3u8
    xzy: Array3u8
    xzz: Array3u8
    xzw: Array3u8
    xwx: Array3u8
    xwy: Array3u8
    xwz: Array3u8
    xww: Array3u8
    yxx: Array3u8
    yxy: Array3u8
    yxz: Array3u8
    yxw: Array3u8
    yyx: Array3u8
    yyy: Array3u8
    yyz: Array3u8
    yyw: Array3u8
    yzx: Array3u8
    yzy: Array3u8
    yzz: Array3u8
    yzw: Array3u8
    ywx: Array3u8
    ywy: Array3u8
    ywz: Array3u8
    yww: Array3u8
    zxx: Array3u8
    zxy: Array3u8
    zxz: Array3u8
    zxw: Array3u8
    zyx: Array3u8
    zyy: Array3u8
    zyz: Array3u8
    zyw: Array3u8
    zzx: Array3u8
    zzy: Array3u8
    zzz: Array3u8
    zzw: Array3u8
    zwx: Array3u8
    zwy: Array3u8
    zwz: Array3u8
    zww: Array3u8
    wxx: Array3u8
    wxy: Array3u8
    wxz: Array3u8
    wxw: Array3u8
    wyx: Array3u8
    wyy: Array3u8
    wyz: Array3u8
    wyw: Array3u8
    wzx: Array3u8
    wzy: Array3u8
    wzz: Array3u8
    wzw: Array3u8
    wwx: Array3u8
    wwy: Array3u8
    wwz: Array3u8
    www: Array3u8
    xxxx: Array4u8
    xxxy: Array4u8
    xxxz: Array4u8
    xxxw: Array4u8
    xxyx: Array4u8
    xxyy: Array4u8
    xxyz: Array4u8
    xxyw: Array4u8
    xxzx: Array4u8
    xxzy: Array4u8
    xxzz: Array4u8
    xxzw: Array4u8
    xxwx: Array4u8
    xxwy: Array4u8
    xxwz: Array4u8
    xxww: Array4u8
    xyxx: Array4u8
    xyxy: Array4u8
    xyxz: Array4u8
    xyxw: Array4u8
    xyyx: Array4u8
    xyyy: Array4u8
    xyyz: Array4u8
    xyyw: Array4u8
    xyzx: Array4u8
    xyzy: Array4u8
    xyzz: Array4u8
    xyzw: Array4u8
    xywx: Array4u8
    xywy: Array4u8
    xywz: Array4u8
    xyww: Array4u8
    xzxx: Array4u8
    xzxy: Array4u8
    xzxz: Array4u8
    xzxw: Array4u8
    xzyx: Array4u8
    xzyy: Array4u8
    xzyz: Array4u8
    xzyw: Array4u8
    xzzx: Array4u8
    xzzy: Array4u8
    xzzz: Array4u8
    xzzw: Array4u8
    xzwx: Array4u8
    xzwy: Array4u8
    xzwz: Array4u8
    xzww: Array4u8
    xwxx: Array4u8
    xwxy: Array4u8
    xwxz: Array4u8
    xwxw: Array4u8
    xwyx: Array4u8
    xwyy: Array4u8
    xwyz: Array4u8
    xwyw: Array4u8
    xwzx: Array4u8
    xwzy: Array4u8
    xwzz: Array4u8
    xwzw: Array4u8
    xwwx: Array4u8
    xwwy: Array4u8
    xwwz: Array4u8
    xwww: Array4u8
    yxxx: Array4u8
    yxxy: Array4u8
    yxxz: Array4u8
    yxxw: Array4u8
    yxyx: Array4u8
    yxyy: Array4u8
    yxyz: Array4u8
    yxyw: Array4u8
    yxzx: Array4u8
    yxzy: Array4u8
    yxzz: Array4u8
    yxzw: Array4u8
    yxwx: Array4u8
    yxwy: Array4u8
    yxwz: Array4u8
    yxww: Array4u8
    yyxx: Array4u8
    yyxy: Array4u8
    yyxz: Array4u8
    yyxw: Array4u8
    yyyx: Array4u8
    yyyy: Array4u8
    yyyz: Array4u8
    yyyw: Array4u8
    yyzx: Array4u8
    yyzy: Array4u8
    yyzz: Array4u8
    yyzw: Array4u8
    yywx: Array4u8
    yywy: Array4u8
    yywz: Array4u8
    yyww: Array4u8
    yzxx: Array4u8
    yzxy: Array4u8
    yzxz: Array4u8
    yzxw: Array4u8
    yzyx: Array4u8
    yzyy: Array4u8
    yzyz: Array4u8
    yzyw: Array4u8
    yzzx: Array4u8
    yzzy: Array4u8
    yzzz: Array4u8
    yzzw: Array4u8
    yzwx: Array4u8
    yzwy: Array4u8
    yzwz: Array4u8
    yzww: Array4u8
    ywxx: Array4u8
    ywxy: Array4u8
    ywxz: Array4u8
    ywxw: Array4u8
    ywyx: Array4u8
    ywyy: Array4u8
    ywyz: Array4u8
    ywyw: Array4u8
    ywzx: Array4u8
    ywzy: Array4u8
    ywzz: Array4u8
    ywzw: Array4u8
    ywwx: Array4u8
    ywwy: Array4u8
    ywwz: Array4u8
    ywww: Array4u8
    zxxx: Array4u8
    zxxy: Array4u8
    zxxz: Array4u8
    zxxw: Array4u8
    zxyx: Array4u8
    zxyy: Array4u8
    zxyz: Array4u8
    zxyw: Array4u8
    zxzx: Array4u8
    zxzy: Array4u8
    zxzz: Array4u8
    zxzw: Array4u8
    zxwx: Array4u8
    zxwy: Array4u8
    zxwz: Array4u8
    zxww: Array4u8
    zyxx: Array4u8
    zyxy: Array4u8
    zyxz: Array4u8
    zyxw: Array4u8
    zyyx: Array4u8
    zyyy: Array4u8
    zyyz: Array4u8
    zyyw: Array4u8
    zyzx: Array4u8
    zyzy: Array4u8
    zyzz: Array4u8
    zyzw: Array4u8
    zywx: Array4u8
    zywy: Array4u8
    zywz: Array4u8
    zyww: Array4u8
    zzxx: Array4u8
    zzxy: Array4u8
    zzxz: Array4u8
    zzxw: Array4u8
    zzyx: Array4u8
    zzyy: Array4u8
    zzyz: Array4u8
    zzyw: Array4u8
    zzzx: Array4u8
    zzzy: Array4u8
    zzzz: Array4u8
    zzzw: Array4u8
    zzwx: Array4u8
    zzwy: Array4u8
    zzwz: Array4u8
    zzww: Array4u8
    zwxx: Array4u8
    zwxy: Array4u8
    zwxz: Array4u8
    zwxw: Array4u8
    zwyx: Array4u8
    zwyy: Array4u8
    zwyz: Array4u8
    zwyw: Array4u8
    zwzx: Array4u8
    zwzy: Array4u8
    zwzz: Array4u8
    zwzw: Array4u8
    zwwx: Array4u8
    zwwy: Array4u8
    zwwz: Array4u8
    zwww: Array4u8
    wxxx: Array4u8
    wxxy: Array4u8
    wxxz: Array4u8
    wxxw: Array4u8
    wxyx: Array4u8
    wxyy: Array4u8
    wxyz: Array4u8
    wxyw: Array4u8
    wxzx: Array4u8
    wxzy: Array4u8
    wxzz: Array4u8
    wxzw: Array4u8
    wxwx: Array4u8
    wxwy: Array4u8
    wxwz: Array4u8
    wxww: Array4u8
    wyxx: Array4u8
    wyxy: Array4u8
    wyxz: Array4u8
    wyxw: Array4u8
    wyyx: Array4u8
    wyyy: Array4u8
    wyyz: Array4u8
    wyyw: Array4u8
    wyzx: Array4u8
    wyzy: Array4u8
    wyzz: Array4u8
    wyzw: Array4u8
    wywx: Array4u8
    wywy: Array4u8
    wywz: Array4u8
    wyww: Array4u8
    wzxx: Array4u8
    wzxy: Array4u8
    wzxz: Array4u8
    wzxw: Array4u8
    wzyx: Array4u8
    wzyy: Array4u8
    wzyz: Array4u8
    wzyw: Array4u8
    wzzx: Array4u8
    wzzy: Array4u8
    wzzz: Array4u8
    wzzw: Array4u8
    wzwx: Array4u8
    wzwy: Array4u8
    wzwz: Array4u8
    wzww: Array4u8
    wwxx: Array4u8
    wwxy: Array4u8
    wwxz: Array4u8
    wwxw: Array4u8
    wwyx: Array4u8
    wwyy: Array4u8
    wwyz: Array4u8
    wwyw: Array4u8
    wwzx: Array4u8
    wwzy: Array4u8
    wwzz: Array4u8
    wwzw: Array4u8
    wwwx: Array4u8
    wwwy: Array4u8
    wwwz: Array4u8
    wwww: Array4u8

_Array2iCp: TypeAlias = Union['Array2i', '_IntCp', 'drjit.scalar._Array2iCp', 'drjit.llvm._Array2iCp', '_Array2bCp']

class Array2i(drjit.ArrayBase[Array2i, _Array2iCp, Int, _IntCp, Int, Array2i, Array2b]):
    xx: Array2i
    xy: Array2i
    xz: Array2i
    xw: Array2i
    yx: Array2i
    yy: Array2i
    yz: Array2i
    yw: Array2i
    zx: Array2i
    zy: Array2i
    zz: Array2i
    zw: Array2i
    wx: Array2i
    wy: Array2i
    wz: Array2i
    ww: Array2i
    xxx: Array3i
    xxy: Array3i
    xxz: Array3i
    xxw: Array3i
    xyx: Array3i
    xyy: Array3i
    xyz: Array3i
    xyw: Array3i
    xzx: Array3i
    xzy: Array3i
    xzz: Array3i
    xzw: Array3i
    xwx: Array3i
    xwy: Array3i
    xwz: Array3i
    xww: Array3i
    yxx: Array3i
    yxy: Array3i
    yxz: Array3i
    yxw: Array3i
    yyx: Array3i
    yyy: Array3i
    yyz: Array3i
    yyw: Array3i
    yzx: Array3i
    yzy: Array3i
    yzz: Array3i
    yzw: Array3i
    ywx: Array3i
    ywy: Array3i
    ywz: Array3i
    yww: Array3i
    zxx: Array3i
    zxy: Array3i
    zxz: Array3i
    zxw: Array3i
    zyx: Array3i
    zyy: Array3i
    zyz: Array3i
    zyw: Array3i
    zzx: Array3i
    zzy: Array3i
    zzz: Array3i
    zzw: Array3i
    zwx: Array3i
    zwy: Array3i
    zwz: Array3i
    zww: Array3i
    wxx: Array3i
    wxy: Array3i
    wxz: Array3i
    wxw: Array3i
    wyx: Array3i
    wyy: Array3i
    wyz: Array3i
    wyw: Array3i
    wzx: Array3i
    wzy: Array3i
    wzz: Array3i
    wzw: Array3i
    wwx: Array3i
    wwy: Array3i
    wwz: Array3i
    www: Array3i
    xxxx: Array4i
    xxxy: Array4i
    xxxz: Array4i
    xxxw: Array4i
    xxyx: Array4i
    xxyy: Array4i
    xxyz: Array4i
    xxyw: Array4i
    xxzx: Array4i
    xxzy: Array4i
    xxzz: Array4i
    xxzw: Array4i
    xxwx: Array4i
    xxwy: Array4i
    xxwz: Array4i
    xxww: Array4i
    xyxx: Array4i
    xyxy: Array4i
    xyxz: Array4i
    xyxw: Array4i
    xyyx: Array4i
    xyyy: Array4i
    xyyz: Array4i
    xyyw: Array4i
    xyzx: Array4i
    xyzy: Array4i
    xyzz: Array4i
    xyzw: Array4i
    xywx: Array4i
    xywy: Array4i
    xywz: Array4i
    xyww: Array4i
    xzxx: Array4i
    xzxy: Array4i
    xzxz: Array4i
    xzxw: Array4i
    xzyx: Array4i
    xzyy: Array4i
    xzyz: Array4i
    xzyw: Array4i
    xzzx: Array4i
    xzzy: Array4i
    xzzz: Array4i
    xzzw: Array4i
    xzwx: Array4i
    xzwy: Array4i
    xzwz: Array4i
    xzww: Array4i
    xwxx: Array4i
    xwxy: Array4i
    xwxz: Array4i
    xwxw: Array4i
    xwyx: Array4i
    xwyy: Array4i
    xwyz: Array4i
    xwyw: Array4i
    xwzx: Array4i
    xwzy: Array4i
    xwzz: Array4i
    xwzw: Array4i
    xwwx: Array4i
    xwwy: Array4i
    xwwz: Array4i
    xwww: Array4i
    yxxx: Array4i
    yxxy: Array4i
    yxxz: Array4i
    yxxw: Array4i
    yxyx: Array4i
    yxyy: Array4i
    yxyz: Array4i
    yxyw: Array4i
    yxzx: Array4i
    yxzy: Array4i
    yxzz: Array4i
    yxzw: Array4i
    yxwx: Array4i
    yxwy: Array4i
    yxwz: Array4i
    yxww: Array4i
    yyxx: Array4i
    yyxy: Array4i
    yyxz: Array4i
    yyxw: Array4i
    yyyx: Array4i
    yyyy: Array4i
    yyyz: Array4i
    yyyw: Array4i
    yyzx: Array4i
    yyzy: Array4i
    yyzz: Array4i
    yyzw: Array4i
    yywx: Array4i
    yywy: Array4i
    yywz: Array4i
    yyww: Array4i
    yzxx: Array4i
    yzxy: Array4i
    yzxz: Array4i
    yzxw: Array4i
    yzyx: Array4i
    yzyy: Array4i
    yzyz: Array4i
    yzyw: Array4i
    yzzx: Array4i
    yzzy: Array4i
    yzzz: Array4i
    yzzw: Array4i
    yzwx: Array4i
    yzwy: Array4i
    yzwz: Array4i
    yzww: Array4i
    ywxx: Array4i
    ywxy: Array4i
    ywxz: Array4i
    ywxw: Array4i
    ywyx: Array4i
    ywyy: Array4i
    ywyz: Array4i
    ywyw: Array4i
    ywzx: Array4i
    ywzy: Array4i
    ywzz: Array4i
    ywzw: Array4i
    ywwx: Array4i
    ywwy: Array4i
    ywwz: Array4i
    ywww: Array4i
    zxxx: Array4i
    zxxy: Array4i
    zxxz: Array4i
    zxxw: Array4i
    zxyx: Array4i
    zxyy: Array4i
    zxyz: Array4i
    zxyw: Array4i
    zxzx: Array4i
    zxzy: Array4i
    zxzz: Array4i
    zxzw: Array4i
    zxwx: Array4i
    zxwy: Array4i
    zxwz: Array4i
    zxww: Array4i
    zyxx: Array4i
    zyxy: Array4i
    zyxz: Array4i
    zyxw: Array4i
    zyyx: Array4i
    zyyy: Array4i
    zyyz: Array4i
    zyyw: Array4i
    zyzx: Array4i
    zyzy: Array4i
    zyzz: Array4i
    zyzw: Array4i
    zywx: Array4i
    zywy: Array4i
    zywz: Array4i
    zyww: Array4i
    zzxx: Array4i
    zzxy: Array4i
    zzxz: Array4i
    zzxw: Array4i
    zzyx: Array4i
    zzyy: Array4i
    zzyz: Array4i
    zzyw: Array4i
    zzzx: Array4i
    zzzy: Array4i
    zzzz: Array4i
    zzzw: Array4i
    zzwx: Array4i
    zzwy: Array4i
    zzwz: Array4i
    zzww: Array4i
    zwxx: Array4i
    zwxy: Array4i
    zwxz: Array4i
    zwxw: Array4i
    zwyx: Array4i
    zwyy: Array4i
    zwyz: Array4i
    zwyw: Array4i
    zwzx: Array4i
    zwzy: Array4i
    zwzz: Array4i
    zwzw: Array4i
    zwwx: Array4i
    zwwy: Array4i
    zwwz: Array4i
    zwww: Array4i
    wxxx: Array4i
    wxxy: Array4i
    wxxz: Array4i
    wxxw: Array4i
    wxyx: Array4i
    wxyy: Array4i
    wxyz: Array4i
    wxyw: Array4i
    wxzx: Array4i
    wxzy: Array4i
    wxzz: Array4i
    wxzw: Array4i
    wxwx: Array4i
    wxwy: Array4i
    wxwz: Array4i
    wxww: Array4i
    wyxx: Array4i
    wyxy: Array4i
    wyxz: Array4i
    wyxw: Array4i
    wyyx: Array4i
    wyyy: Array4i
    wyyz: Array4i
    wyyw: Array4i
    wyzx: Array4i
    wyzy: Array4i
    wyzz: Array4i
    wyzw: Array4i
    wywx: Array4i
    wywy: Array4i
    wywz: Array4i
    wyww: Array4i
    wzxx: Array4i
    wzxy: Array4i
    wzxz: Array4i
    wzxw: Array4i
    wzyx: Array4i
    wzyy: Array4i
    wzyz: Array4i
    wzyw: Array4i
    wzzx: Array4i
    wzzy: Array4i
    wzzz: Array4i
    wzzw: Array4i
    wzwx: Array4i
    wzwy: Array4i
    wzwz: Array4i
    wzww: Array4i
    wwxx: Array4i
    wwxy: Array4i
    wwxz: Array4i
    wwxw: Array4i
    wwyx: Array4i
    wwyy: Array4i
    wwyz: Array4i
    wwyw: Array4i
    wwzx: Array4i
    wwzy: Array4i
    wwzz: Array4i
    wwzw: Array4i
    wwwx: Array4i
    wwwy: Array4i
    wwwz: Array4i
    wwww: Array4i

_Array2uCp: TypeAlias = Union['Array2u', '_UIntCp', 'drjit.scalar._Array2uCp', 'drjit.llvm._Array2uCp', '_Array2iCp']

class Array2u(drjit.ArrayBase[Array2u, _Array2uCp, UInt, _UIntCp, UInt, Array2u, Array2b]):
    xx: Array2u
    xy: Array2u
    xz: Array2u
    xw: Array2u
    yx: Array2u
    yy: Array2u
    yz: Array2u
    yw: Array2u
    zx: Array2u
    zy: Array2u
    zz: Array2u
    zw: Array2u
    wx: Array2u
    wy: Array2u
    wz: Array2u
    ww: Array2u
    xxx: Array3u
    xxy: Array3u
    xxz: Array3u
    xxw: Array3u
    xyx: Array3u
    xyy: Array3u
    xyz: Array3u
    xyw: Array3u
    xzx: Array3u
    xzy: Array3u
    xzz: Array3u
    xzw: Array3u
    xwx: Array3u
    xwy: Array3u
    xwz: Array3u
    xww: Array3u
    yxx: Array3u
    yxy: Array3u
    yxz: Array3u
    yxw: Array3u
    yyx: Array3u
    yyy: Array3u
    yyz: Array3u
    yyw: Array3u
    yzx: Array3u
    yzy: Array3u
    yzz: Array3u
    yzw: Array3u
    ywx: Array3u
    ywy: Array3u
    ywz: Array3u
    yww: Array3u
    zxx: Array3u
    zxy: Array3u
    zxz: Array3u
    zxw: Array3u
    zyx: Array3u
    zyy: Array3u
    zyz: Array3u
    zyw: Array3u
    zzx: Array3u
    zzy: Array3u
    zzz: Array3u
    zzw: Array3u
    zwx: Array3u
    zwy: Array3u
    zwz: Array3u
    zww: Array3u
    wxx: Array3u
    wxy: Array3u
    wxz: Array3u
    wxw: Array3u
    wyx: Array3u
    wyy: Array3u
    wyz: Array3u
    wyw: Array3u
    wzx: Array3u
    wzy: Array3u
    wzz: Array3u
    wzw: Array3u
    wwx: Array3u
    wwy: Array3u
    wwz: Array3u
    www: Array3u
    xxxx: Array4u
    xxxy: Array4u
    xxxz: Array4u
    xxxw: Array4u
    xxyx: Array4u
    xxyy: Array4u
    xxyz: Array4u
    xxyw: Array4u
    xxzx: Array4u
    xxzy: Array4u
    xxzz: Array4u
    xxzw: Array4u
    xxwx: Array4u
    xxwy: Array4u
    xxwz: Array4u
    xxww: Array4u
    xyxx: Array4u
    xyxy: Array4u
    xyxz: Array4u
    xyxw: Array4u
    xyyx: Array4u
    xyyy: Array4u
    xyyz: Array4u
    xyyw: Array4u
    xyzx: Array4u
    xyzy: Array4u
    xyzz: Array4u
    xyzw: Array4u
    xywx: Array4u
    xywy: Array4u
    xywz: Array4u
    xyww: Array4u
    xzxx: Array4u
    xzxy: Array4u
    xzxz: Array4u
    xzxw: Array4u
    xzyx: Array4u
    xzyy: Array4u
    xzyz: Array4u
    xzyw: Array4u
    xzzx: Array4u
    xzzy: Array4u
    xzzz: Array4u
    xzzw: Array4u
    xzwx: Array4u
    xzwy: Array4u
    xzwz: Array4u
    xzww: Array4u
    xwxx: Array4u
    xwxy: Array4u
    xwxz: Array4u
    xwxw: Array4u
    xwyx: Array4u
    xwyy: Array4u
    xwyz: Array4u
    xwyw: Array4u
    xwzx: Array4u
    xwzy: Array4u
    xwzz: Array4u
    xwzw: Array4u
    xwwx: Array4u
    xwwy: Array4u
    xwwz: Array4u
    xwww: Array4u
    yxxx: Array4u
    yxxy: Array4u
    yxxz: Array4u
    yxxw: Array4u
    yxyx: Array4u
    yxyy: Array4u
    yxyz: Array4u
    yxyw: Array4u
    yxzx: Array4u
    yxzy: Array4u
    yxzz: Array4u
    yxzw: Array4u
    yxwx: Array4u
    yxwy: Array4u
    yxwz: Array4u
    yxww: Array4u
    yyxx: Array4u
    yyxy: Array4u
    yyxz: Array4u
    yyxw: Array4u
    yyyx: Array4u
    yyyy: Array4u
    yyyz: Array4u
    yyyw: Array4u
    yyzx: Array4u
    yyzy: Array4u
    yyzz: Array4u
    yyzw: Array4u
    yywx: Array4u
    yywy: Array4u
    yywz: Array4u
    yyww: Array4u
    yzxx: Array4u
    yzxy: Array4u
    yzxz: Array4u
    yzxw: Array4u
    yzyx: Array4u
    yzyy: Array4u
    yzyz: Array4u
    yzyw: Array4u
    yzzx: Array4u
    yzzy: Array4u
    yzzz: Array4u
    yzzw: Array4u
    yzwx: Array4u
    yzwy: Array4u
    yzwz: Array4u
    yzww: Array4u
    ywxx: Array4u
    ywxy: Array4u
    ywxz: Array4u
    ywxw: Array4u
    ywyx: Array4u
    ywyy: Array4u
    ywyz: Array4u
    ywyw: Array4u
    ywzx: Array4u
    ywzy: Array4u
    ywzz: Array4u
    ywzw: Array4u
    ywwx: Array4u
    ywwy: Array4u
    ywwz: Array4u
    ywww: Array4u
    zxxx: Array4u
    zxxy: Array4u
    zxxz: Array4u
    zxxw: Array4u
    zxyx: Array4u
    zxyy: Array4u
    zxyz: Array4u
    zxyw: Array4u
    zxzx: Array4u
    zxzy: Array4u
    zxzz: Array4u
    zxzw: Array4u
    zxwx: Array4u
    zxwy: Array4u
    zxwz: Array4u
    zxww: Array4u
    zyxx: Array4u
    zyxy: Array4u
    zyxz: Array4u
    zyxw: Array4u
    zyyx: Array4u
    zyyy: Array4u
    zyyz: Array4u
    zyyw: Array4u
    zyzx: Array4u
    zyzy: Array4u
    zyzz: Array4u
    zyzw: Array4u
    zywx: Array4u
    zywy: Array4u
    zywz: Array4u
    zyww: Array4u
    zzxx: Array4u
    zzxy: Array4u
    zzxz: Array4u
    zzxw: Array4u
    zzyx: Array4u
    zzyy: Array4u
    zzyz: Array4u
    zzyw: Array4u
    zzzx: Array4u
    zzzy: Array4u
    zzzz: Array4u
    zzzw: Array4u
    zzwx: Array4u
    zzwy: Array4u
    zzwz: Array4u
    zzww: Array4u
    zwxx: Array4u
    zwxy: Array4u
    zwxz: Array4u
    zwxw: Array4u
    zwyx: Array4u
    zwyy: Array4u
    zwyz: Array4u
    zwyw: Array4u
    zwzx: Array4u
    zwzy: Array4u
    zwzz: Array4u
    zwzw: Array4u
    zwwx: Array4u
    zwwy: Array4u
    zwwz: Array4u
    zwww: Array4u
    wxxx: Array4u
    wxxy: Array4u
    wxxz: Array4u
    wxxw: Array4u
    wxyx: Array4u
    wxyy: Array4u
    wxyz: Array4u
    wxyw: Array4u
    wxzx: Array4u
    wxzy: Array4u
    wxzz: Array4u
    wxzw: Array4u
    wxwx: Array4u
    wxwy: Array4u
    wxwz: Array4u
    wxww: Array4u
    wyxx: Array4u
    wyxy: Array4u
    wyxz: Array4u
    wyxw: Array4u
    wyyx: Array4u
    wyyy: Array4u
    wyyz: Array4u
    wyyw: Array4u
    wyzx: Array4u
    wyzy: Array4u
    wyzz: Array4u
    wyzw: Array4u
    wywx: Array4u
    wywy: Array4u
    wywz: Array4u
    wyww: Array4u
    wzxx: Array4u
    wzxy: Array4u
    wzxz: Array4u
    wzxw: Array4u
    wzyx: Array4u
    wzyy: Array4u
    wzyz: Array4u
    wzyw: Array4u
    wzzx: Array4u
    wzzy: Array4u
    wzzz: Array4u
    wzzw: Array4u
    wzwx: Array4u
    wzwy: Array4u
    wzwz: Array4u
    wzww: Array4u
    wwxx: Array4u
    wwxy: Array4u
    wwxz: Array4u
    wwxw: Array4u
    wwyx: Array4u
    wwyy: Array4u
    wwyz: Array4u
    wwyw: Array4u
    wwzx: Array4u
    wwzy: Array4u
    wwzz: Array4u
    wwzw: Array4u
    wwwx: Array4u
    wwwy: Array4u
    wwwz: Array4u
    wwww: Array4u

_Array2i64Cp: TypeAlias = Union['Array2i64', '_Int64Cp', 'drjit.scalar._Array2i64Cp', 'drjit.llvm._Array2i64Cp', '_Array2uCp']

class Array2i64(drjit.ArrayBase[Array2i64, _Array2i64Cp, Int64, _Int64Cp, Int64, Array2i64, Array2b]):
    xx: Array2i64
    xy: Array2i64
    xz: Array2i64
    xw: Array2i64
    yx: Array2i64
    yy: Array2i64
    yz: Array2i64
    yw: Array2i64
    zx: Array2i64
    zy: Array2i64
    zz: Array2i64
    zw: Array2i64
    wx: Array2i64
    wy: Array2i64
    wz: Array2i64
    ww: Array2i64
    xxx: Array3i64
    xxy: Array3i64
    xxz: Array3i64
    xxw: Array3i64
    xyx: Array3i64
    xyy: Array3i64
    xyz: Array3i64
    xyw: Array3i64
    xzx: Array3i64
    xzy: Array3i64
    xzz: Array3i64
    xzw: Array3i64
    xwx: Array3i64
    xwy: Array3i64
    xwz: Array3i64
    xww: Array3i64
    yxx: Array3i64
    yxy: Array3i64
    yxz: Array3i64
    yxw: Array3i64
    yyx: Array3i64
    yyy: Array3i64
    yyz: Array3i64
    yyw: Array3i64
    yzx: Array3i64
    yzy: Array3i64
    yzz: Array3i64
    yzw: Array3i64
    ywx: Array3i64
    ywy: Array3i64
    ywz: Array3i64
    yww: Array3i64
    zxx: Array3i64
    zxy: Array3i64
    zxz: Array3i64
    zxw: Array3i64
    zyx: Array3i64
    zyy: Array3i64
    zyz: Array3i64
    zyw: Array3i64
    zzx: Array3i64
    zzy: Array3i64
    zzz: Array3i64
    zzw: Array3i64
    zwx: Array3i64
    zwy: Array3i64
    zwz: Array3i64
    zww: Array3i64
    wxx: Array3i64
    wxy: Array3i64
    wxz: Array3i64
    wxw: Array3i64
    wyx: Array3i64
    wyy: Array3i64
    wyz: Array3i64
    wyw: Array3i64
    wzx: Array3i64
    wzy: Array3i64
    wzz: Array3i64
    wzw: Array3i64
    wwx: Array3i64
    wwy: Array3i64
    wwz: Array3i64
    www: Array3i64
    xxxx: Array4i64
    xxxy: Array4i64
    xxxz: Array4i64
    xxxw: Array4i64
    xxyx: Array4i64
    xxyy: Array4i64
    xxyz: Array4i64
    xxyw: Array4i64
    xxzx: Array4i64
    xxzy: Array4i64
    xxzz: Array4i64
    xxzw: Array4i64
    xxwx: Array4i64
    xxwy: Array4i64
    xxwz: Array4i64
    xxww: Array4i64
    xyxx: Array4i64
    xyxy: Array4i64
    xyxz: Array4i64
    xyxw: Array4i64
    xyyx: Array4i64
    xyyy: Array4i64
    xyyz: Array4i64
    xyyw: Array4i64
    xyzx: Array4i64
    xyzy: Array4i64
    xyzz: Array4i64
    xyzw: Array4i64
    xywx: Array4i64
    xywy: Array4i64
    xywz: Array4i64
    xyww: Array4i64
    xzxx: Array4i64
    xzxy: Array4i64
    xzxz: Array4i64
    xzxw: Array4i64
    xzyx: Array4i64
    xzyy: Array4i64
    xzyz: Array4i64
    xzyw: Array4i64
    xzzx: Array4i64
    xzzy: Array4i64
    xzzz: Array4i64
    xzzw: Array4i64
    xzwx: Array4i64
    xzwy: Array4i64
    xzwz: Array4i64
    xzww: Array4i64
    xwxx: Array4i64
    xwxy: Array4i64
    xwxz: Array4i64
    xwxw: Array4i64
    xwyx: Array4i64
    xwyy: Array4i64
    xwyz: Array4i64
    xwyw: Array4i64
    xwzx: Array4i64
    xwzy: Array4i64
    xwzz: Array4i64
    xwzw: Array4i64
    xwwx: Array4i64
    xwwy: Array4i64
    xwwz: Array4i64
    xwww: Array4i64
    yxxx: Array4i64
    yxxy: Array4i64
    yxxz: Array4i64
    yxxw: Array4i64
    yxyx: Array4i64
    yxyy: Array4i64
    yxyz: Array4i64
    yxyw: Array4i64
    yxzx: Array4i64
    yxzy: Array4i64
    yxzz: Array4i64
    yxzw: Array4i64
    yxwx: Array4i64
    yxwy: Array4i64
    yxwz: Array4i64
    yxww: Array4i64
    yyxx: Array4i64
    yyxy: Array4i64
    yyxz: Array4i64
    yyxw: Array4i64
    yyyx: Array4i64
    yyyy: Array4i64
    yyyz: Array4i64
    yyyw: Array4i64
    yyzx: Array4i64
    yyzy: Array4i64
    yyzz: Array4i64
    yyzw: Array4i64
    yywx: Array4i64
    yywy: Array4i64
    yywz: Array4i64
    yyww: Array4i64
    yzxx: Array4i64
    yzxy: Array4i64
    yzxz: Array4i64
    yzxw: Array4i64
    yzyx: Array4i64
    yzyy: Array4i64
    yzyz: Array4i64
    yzyw: Array4i64
    yzzx: Array4i64
    yzzy: Array4i64
    yzzz: Array4i64
    yzzw: Array4i64
    yzwx: Array4i64
    yzwy: Array4i64
    yzwz: Array4i64
    yzww: Array4i64
    ywxx: Array4i64
    ywxy: Array4i64
    ywxz: Array4i64
    ywxw: Array4i64
    ywyx: Array4i64
    ywyy: Array4i64
    ywyz: Array4i64
    ywyw: Array4i64
    ywzx: Array4i64
    ywzy: Array4i64
    ywzz: Array4i64
    ywzw: Array4i64
    ywwx: Array4i64
    ywwy: Array4i64
    ywwz: Array4i64
    ywww: Array4i64
    zxxx: Array4i64
    zxxy: Array4i64
    zxxz: Array4i64
    zxxw: Array4i64
    zxyx: Array4i64
    zxyy: Array4i64
    zxyz: Array4i64
    zxyw: Array4i64
    zxzx: Array4i64
    zxzy: Array4i64
    zxzz: Array4i64
    zxzw: Array4i64
    zxwx: Array4i64
    zxwy: Array4i64
    zxwz: Array4i64
    zxww: Array4i64
    zyxx: Array4i64
    zyxy: Array4i64
    zyxz: Array4i64
    zyxw: Array4i64
    zyyx: Array4i64
    zyyy: Array4i64
    zyyz: Array4i64
    zyyw: Array4i64
    zyzx: Array4i64
    zyzy: Array4i64
    zyzz: Array4i64
    zyzw: Array4i64
    zywx: Array4i64
    zywy: Array4i64
    zywz: Array4i64
    zyww: Array4i64
    zzxx: Array4i64
    zzxy: Array4i64
    zzxz: Array4i64
    zzxw: Array4i64
    zzyx: Array4i64
    zzyy: Array4i64
    zzyz: Array4i64
    zzyw: Array4i64
    zzzx: Array4i64
    zzzy: Array4i64
    zzzz: Array4i64
    zzzw: Array4i64
    zzwx: Array4i64
    zzwy: Array4i64
    zzwz: Array4i64
    zzww: Array4i64
    zwxx: Array4i64
    zwxy: Array4i64
    zwxz: Array4i64
    zwxw: Array4i64
    zwyx: Array4i64
    zwyy: Array4i64
    zwyz: Array4i64
    zwyw: Array4i64
    zwzx: Array4i64
    zwzy: Array4i64
    zwzz: Array4i64
    zwzw: Array4i64
    zwwx: Array4i64
    zwwy: Array4i64
    zwwz: Array4i64
    zwww: Array4i64
    wxxx: Array4i64
    wxxy: Array4i64
    wxxz: Array4i64
    wxxw: Array4i64
    wxyx: Array4i64
    wxyy: Array4i64
    wxyz: Array4i64
    wxyw: Array4i64
    wxzx: Array4i64
    wxzy: Array4i64
    wxzz: Array4i64
    wxzw: Array4i64
    wxwx: Array4i64
    wxwy: Array4i64
    wxwz: Array4i64
    wxww: Array4i64
    wyxx: Array4i64
    wyxy: Array4i64
    wyxz: Array4i64
    wyxw: Array4i64
    wyyx: Array4i64
    wyyy: Array4i64
    wyyz: Array4i64
    wyyw: Array4i64
    wyzx: Array4i64
    wyzy: Array4i64
    wyzz: Array4i64
    wyzw: Array4i64
    wywx: Array4i64
    wywy: Array4i64
    wywz: Array4i64
    wyww: Array4i64
    wzxx: Array4i64
    wzxy: Array4i64
    wzxz: Array4i64
    wzxw: Array4i64
    wzyx: Array4i64
    wzyy: Array4i64
    wzyz: Array4i64
    wzyw: Array4i64
    wzzx: Array4i64
    wzzy: Array4i64
    wzzz: Array4i64
    wzzw: Array4i64
    wzwx: Array4i64
    wzwy: Array4i64
    wzwz: Array4i64
    wzww: Array4i64
    wwxx: Array4i64
    wwxy: Array4i64
    wwxz: Array4i64
    wwxw: Array4i64
    wwyx: Array4i64
    wwyy: Array4i64
    wwyz: Array4i64
    wwyw: Array4i64
    wwzx: Array4i64
    wwzy: Array4i64
    wwzz: Array4i64
    wwzw: Array4i64
    wwwx: Array4i64
    wwwy: Array4i64
    wwwz: Array4i64
    wwww: Array4i64

_Array2u64Cp: TypeAlias = Union['Array2u64', '_UInt64Cp', 'drjit.scalar._Array2u64Cp', 'drjit.llvm._Array2u64Cp', '_Array2i64Cp']

class Array2u64(drjit.ArrayBase[Array2u64, _Array2u64Cp, UInt64, _UInt64Cp, UInt64, Array2u64, Array2b]):
    xx: Array2u64
    xy: Array2u64
    xz: Array2u64
    xw: Array2u64
    yx: Array2u64
    yy: Array2u64
    yz: Array2u64
    yw: Array2u64
    zx: Array2u64
    zy: Array2u64
    zz: Array2u64
    zw: Array2u64
    wx: Array2u64
    wy: Array2u64
    wz: Array2u64
    ww: Array2u64
    xxx: Array3u64
    xxy: Array3u64
    xxz: Array3u64
    xxw: Array3u64
    xyx: Array3u64
    xyy: Array3u64
    xyz: Array3u64
    xyw: Array3u64
    xzx: Array3u64
    xzy: Array3u64
    xzz: Array3u64
    xzw: Array3u64
    xwx: Array3u64
    xwy: Array3u64
    xwz: Array3u64
    xww: Array3u64
    yxx: Array3u64
    yxy: Array3u64
    yxz: Array3u64
    yxw: Array3u64
    yyx: Array3u64
    yyy: Array3u64
    yyz: Array3u64
    yyw: Array3u64
    yzx: Array3u64
    yzy: Array3u64
    yzz: Array3u64
    yzw: Array3u64
    ywx: Array3u64
    ywy: Array3u64
    ywz: Array3u64
    yww: Array3u64
    zxx: Array3u64
    zxy: Array3u64
    zxz: Array3u64
    zxw: Array3u64
    zyx: Array3u64
    zyy: Array3u64
    zyz: Array3u64
    zyw: Array3u64
    zzx: Array3u64
    zzy: Array3u64
    zzz: Array3u64
    zzw: Array3u64
    zwx: Array3u64
    zwy: Array3u64
    zwz: Array3u64
    zww: Array3u64
    wxx: Array3u64
    wxy: Array3u64
    wxz: Array3u64
    wxw: Array3u64
    wyx: Array3u64
    wyy: Array3u64
    wyz: Array3u64
    wyw: Array3u64
    wzx: Array3u64
    wzy: Array3u64
    wzz: Array3u64
    wzw: Array3u64
    wwx: Array3u64
    wwy: Array3u64
    wwz: Array3u64
    www: Array3u64
    xxxx: Array4u64
    xxxy: Array4u64
    xxxz: Array4u64
    xxxw: Array4u64
    xxyx: Array4u64
    xxyy: Array4u64
    xxyz: Array4u64
    xxyw: Array4u64
    xxzx: Array4u64
    xxzy: Array4u64
    xxzz: Array4u64
    xxzw: Array4u64
    xxwx: Array4u64
    xxwy: Array4u64
    xxwz: Array4u64
    xxww: Array4u64
    xyxx: Array4u64
    xyxy: Array4u64
    xyxz: Array4u64
    xyxw: Array4u64
    xyyx: Array4u64
    xyyy: Array4u64
    xyyz: Array4u64
    xyyw: Array4u64
    xyzx: Array4u64
    xyzy: Array4u64
    xyzz: Array4u64
    xyzw: Array4u64
    xywx: Array4u64
    xywy: Array4u64
    xywz: Array4u64
    xyww: Array4u64
    xzxx: Array4u64
    xzxy: Array4u64
    xzxz: Array4u64
    xzxw: Array4u64
    xzyx: Array4u64
    xzyy: Array4u64
    xzyz: Array4u64
    xzyw: Array4u64
    xzzx: Array4u64
    xzzy: Array4u64
    xzzz: Array4u64
    xzzw: Array4u64
    xzwx: Array4u64
    xzwy: Array4u64
    xzwz: Array4u64
    xzww: Array4u64
    xwxx: Array4u64
    xwxy: Array4u64
    xwxz: Array4u64
    xwxw: Array4u64
    xwyx: Array4u64
    xwyy: Array4u64
    xwyz: Array4u64
    xwyw: Array4u64
    xwzx: Array4u64
    xwzy: Array4u64
    xwzz: Array4u64
    xwzw: Array4u64
    xwwx: Array4u64
    xwwy: Array4u64
    xwwz: Array4u64
    xwww: Array4u64
    yxxx: Array4u64
    yxxy: Array4u64
    yxxz: Array4u64
    yxxw: Array4u64
    yxyx: Array4u64
    yxyy: Array4u64
    yxyz: Array4u64
    yxyw: Array4u64
    yxzx: Array4u64
    yxzy: Array4u64
    yxzz: Array4u64
    yxzw: Array4u64
    yxwx: Array4u64
    yxwy: Array4u64
    yxwz: Array4u64
    yxww: Array4u64
    yyxx: Array4u64
    yyxy: Array4u64
    yyxz: Array4u64
    yyxw: Array4u64
    yyyx: Array4u64
    yyyy: Array4u64
    yyyz: Array4u64
    yyyw: Array4u64
    yyzx: Array4u64
    yyzy: Array4u64
    yyzz: Array4u64
    yyzw: Array4u64
    yywx: Array4u64
    yywy: Array4u64
    yywz: Array4u64
    yyww: Array4u64
    yzxx: Array4u64
    yzxy: Array4u64
    yzxz: Array4u64
    yzxw: Array4u64
    yzyx: Array4u64
    yzyy: Array4u64
    yzyz: Array4u64
    yzyw: Array4u64
    yzzx: Array4u64
    yzzy: Array4u64
    yzzz: Array4u64
    yzzw: Array4u64
    yzwx: Array4u64
    yzwy: Array4u64
    yzwz: Array4u64
    yzww: Array4u64
    ywxx: Array4u64
    ywxy: Array4u64
    ywxz: Array4u64
    ywxw: Array4u64
    ywyx: Array4u64
    ywyy: Array4u64
    ywyz: Array4u64
    ywyw: Array4u64
    ywzx: Array4u64
    ywzy: Array4u64
    ywzz: Array4u64
    ywzw: Array4u64
    ywwx: Array4u64
    ywwy: Array4u64
    ywwz: Array4u64
    ywww: Array4u64
    zxxx: Array4u64
    zxxy: Array4u64
    zxxz: Array4u64
    zxxw: Array4u64
    zxyx: Array4u64
    zxyy: Array4u64
    zxyz: Array4u64
    zxyw: Array4u64
    zxzx: Array4u64
    zxzy: Array4u64
    zxzz: Array4u64
    zxzw: Array4u64
    zxwx: Array4u64
    zxwy: Array4u64
    zxwz: Array4u64
    zxww: Array4u64
    zyxx: Array4u64
    zyxy: Array4u64
    zyxz: Array4u64
    zyxw: Array4u64
    zyyx: Array4u64
    zyyy: Array4u64
    zyyz: Array4u64
    zyyw: Array4u64
    zyzx: Array4u64
    zyzy: Array4u64
    zyzz: Array4u64
    zyzw: Array4u64
    zywx: Array4u64
    zywy: Array4u64
    zywz: Array4u64
    zyww: Array4u64
    zzxx: Array4u64
    zzxy: Array4u64
    zzxz: Array4u64
    zzxw: Array4u64
    zzyx: Array4u64
    zzyy: Array4u64
    zzyz: Array4u64
    zzyw: Array4u64
    zzzx: Array4u64
    zzzy: Array4u64
    zzzz: Array4u64
    zzzw: Array4u64
    zzwx: Array4u64
    zzwy: Array4u64
    zzwz: Array4u64
    zzww: Array4u64
    zwxx: Array4u64
    zwxy: Array4u64
    zwxz: Array4u64
    zwxw: Array4u64
    zwyx: Array4u64
    zwyy: Array4u64
    zwyz: Array4u64
    zwyw: Array4u64
    zwzx: Array4u64
    zwzy: Array4u64
    zwzz: Array4u64
    zwzw: Array4u64
    zwwx: Array4u64
    zwwy: Array4u64
    zwwz: Array4u64
    zwww: Array4u64
    wxxx: Array4u64
    wxxy: Array4u64
    wxxz: Array4u64
    wxxw: Array4u64
    wxyx: Array4u64
    wxyy: Array4u64
    wxyz: Array4u64
    wxyw: Array4u64
    wxzx: Array4u64
    wxzy: Array4u64
    wxzz: Array4u64
    wxzw: Array4u64
    wxwx: Array4u64
    wxwy: Array4u64
    wxwz: Array4u64
    wxww: Array4u64
    wyxx: Array4u64
    wyxy: Array4u64
    wyxz: Array4u64
    wyxw: Array4u64
    wyyx: Array4u64
    wyyy: Array4u64
    wyyz: Array4u64
    wyyw: Array4u64
    wyzx: Array4u64
    wyzy: Array4u64
    wyzz: Array4u64
    wyzw: Array4u64
    wywx: Array4u64
    wywy: Array4u64
    wywz: Array4u64
    wyww: Array4u64
    wzxx: Array4u64
    wzxy: Array4u64
    wzxz: Array4u64
    wzxw: Array4u64
    wzyx: Array4u64
    wzyy: Array4u64
    wzyz: Array4u64
    wzyw: Array4u64
    wzzx: Array4u64
    wzzy: Array4u64
    wzzz: Array4u64
    wzzw: Array4u64
    wzwx: Array4u64
    wzwy: Array4u64
    wzwz: Array4u64
    wzww: Array4u64
    wwxx: Array4u64
    wwxy: Array4u64
    wwxz: Array4u64
    wwxw: Array4u64
    wwyx: Array4u64
    wwyy: Array4u64
    wwyz: Array4u64
    wwyw: Array4u64
    wwzx: Array4u64
    wwzy: Array4u64
    wwzz: Array4u64
    wwzw: Array4u64
    wwwx: Array4u64
    wwwy: Array4u64
    wwwz: Array4u64
    wwww: Array4u64

_Array2f16Cp: TypeAlias = Union['Array2f16', '_Float16Cp', 'drjit.scalar._Array2f16Cp', 'drjit.llvm._Array2f16Cp', '_Array2u64Cp']

class Array2f16(drjit.ArrayBase[Array2f16, _Array2f16Cp, Float16, _Float16Cp, Float16, Array2f16, Array2b]):
    xx: Array2f16
    xy: Array2f16
    xz: Array2f16
    xw: Array2f16
    yx: Array2f16
    yy: Array2f16
    yz: Array2f16
    yw: Array2f16
    zx: Array2f16
    zy: Array2f16
    zz: Array2f16
    zw: Array2f16
    wx: Array2f16
    wy: Array2f16
    wz: Array2f16
    ww: Array2f16
    xxx: Array3f16
    xxy: Array3f16
    xxz: Array3f16
    xxw: Array3f16
    xyx: Array3f16
    xyy: Array3f16
    xyz: Array3f16
    xyw: Array3f16
    xzx: Array3f16
    xzy: Array3f16
    xzz: Array3f16
    xzw: Array3f16
    xwx: Array3f16
    xwy: Array3f16
    xwz: Array3f16
    xww: Array3f16
    yxx: Array3f16
    yxy: Array3f16
    yxz: Array3f16
    yxw: Array3f16
    yyx: Array3f16
    yyy: Array3f16
    yyz: Array3f16
    yyw: Array3f16
    yzx: Array3f16
    yzy: Array3f16
    yzz: Array3f16
    yzw: Array3f16
    ywx: Array3f16
    ywy: Array3f16
    ywz: Array3f16
    yww: Array3f16
    zxx: Array3f16
    zxy: Array3f16
    zxz: Array3f16
    zxw: Array3f16
    zyx: Array3f16
    zyy: Array3f16
    zyz: Array3f16
    zyw: Array3f16
    zzx: Array3f16
    zzy: Array3f16
    zzz: Array3f16
    zzw: Array3f16
    zwx: Array3f16
    zwy: Array3f16
    zwz: Array3f16
    zww: Array3f16
    wxx: Array3f16
    wxy: Array3f16
    wxz: Array3f16
    wxw: Array3f16
    wyx: Array3f16
    wyy: Array3f16
    wyz: Array3f16
    wyw: Array3f16
    wzx: Array3f16
    wzy: Array3f16
    wzz: Array3f16
    wzw: Array3f16
    wwx: Array3f16
    wwy: Array3f16
    wwz: Array3f16
    www: Array3f16
    xxxx: Array4f16
    xxxy: Array4f16
    xxxz: Array4f16
    xxxw: Array4f16
    xxyx: Array4f16
    xxyy: Array4f16
    xxyz: Array4f16
    xxyw: Array4f16
    xxzx: Array4f16
    xxzy: Array4f16
    xxzz: Array4f16
    xxzw: Array4f16
    xxwx: Array4f16
    xxwy: Array4f16
    xxwz: Array4f16
    xxww: Array4f16
    xyxx: Array4f16
    xyxy: Array4f16
    xyxz: Array4f16
    xyxw: Array4f16
    xyyx: Array4f16
    xyyy: Array4f16
    xyyz: Array4f16
    xyyw: Array4f16
    xyzx: Array4f16
    xyzy: Array4f16
    xyzz: Array4f16
    xyzw: Array4f16
    xywx: Array4f16
    xywy: Array4f16
    xywz: Array4f16
    xyww: Array4f16
    xzxx: Array4f16
    xzxy: Array4f16
    xzxz: Array4f16
    xzxw: Array4f16
    xzyx: Array4f16
    xzyy: Array4f16
    xzyz: Array4f16
    xzyw: Array4f16
    xzzx: Array4f16
    xzzy: Array4f16
    xzzz: Array4f16
    xzzw: Array4f16
    xzwx: Array4f16
    xzwy: Array4f16
    xzwz: Array4f16
    xzww: Array4f16
    xwxx: Array4f16
    xwxy: Array4f16
    xwxz: Array4f16
    xwxw: Array4f16
    xwyx: Array4f16
    xwyy: Array4f16
    xwyz: Array4f16
    xwyw: Array4f16
    xwzx: Array4f16
    xwzy: Array4f16
    xwzz: Array4f16
    xwzw: Array4f16
    xwwx: Array4f16
    xwwy: Array4f16
    xwwz: Array4f16
    xwww: Array4f16
    yxxx: Array4f16
    yxxy: Array4f16
    yxxz: Array4f16
    yxxw: Array4f16
    yxyx: Array4f16
    yxyy: Array4f16
    yxyz: Array4f16
    yxyw: Array4f16
    yxzx: Array4f16
    yxzy: Array4f16
    yxzz: Array4f16
    yxzw: Array4f16
    yxwx: Array4f16
    yxwy: Array4f16
    yxwz: Array4f16
    yxww: Array4f16
    yyxx: Array4f16
    yyxy: Array4f16
    yyxz: Array4f16
    yyxw: Array4f16
    yyyx: Array4f16
    yyyy: Array4f16
    yyyz: Array4f16
    yyyw: Array4f16
    yyzx: Array4f16
    yyzy: Array4f16
    yyzz: Array4f16
    yyzw: Array4f16
    yywx: Array4f16
    yywy: Array4f16
    yywz: Array4f16
    yyww: Array4f16
    yzxx: Array4f16
    yzxy: Array4f16
    yzxz: Array4f16
    yzxw: Array4f16
    yzyx: Array4f16
    yzyy: Array4f16
    yzyz: Array4f16
    yzyw: Array4f16
    yzzx: Array4f16
    yzzy: Array4f16
    yzzz: Array4f16
    yzzw: Array4f16
    yzwx: Array4f16
    yzwy: Array4f16
    yzwz: Array4f16
    yzww: Array4f16
    ywxx: Array4f16
    ywxy: Array4f16
    ywxz: Array4f16
    ywxw: Array4f16
    ywyx: Array4f16
    ywyy: Array4f16
    ywyz: Array4f16
    ywyw: Array4f16
    ywzx: Array4f16
    ywzy: Array4f16
    ywzz: Array4f16
    ywzw: Array4f16
    ywwx: Array4f16
    ywwy: Array4f16
    ywwz: Array4f16
    ywww: Array4f16
    zxxx: Array4f16
    zxxy: Array4f16
    zxxz: Array4f16
    zxxw: Array4f16
    zxyx: Array4f16
    zxyy: Array4f16
    zxyz: Array4f16
    zxyw: Array4f16
    zxzx: Array4f16
    zxzy: Array4f16
    zxzz: Array4f16
    zxzw: Array4f16
    zxwx: Array4f16
    zxwy: Array4f16
    zxwz: Array4f16
    zxww: Array4f16
    zyxx: Array4f16
    zyxy: Array4f16
    zyxz: Array4f16
    zyxw: Array4f16
    zyyx: Array4f16
    zyyy: Array4f16
    zyyz: Array4f16
    zyyw: Array4f16
    zyzx: Array4f16
    zyzy: Array4f16
    zyzz: Array4f16
    zyzw: Array4f16
    zywx: Array4f16
    zywy: Array4f16
    zywz: Array4f16
    zyww: Array4f16
    zzxx: Array4f16
    zzxy: Array4f16
    zzxz: Array4f16
    zzxw: Array4f16
    zzyx: Array4f16
    zzyy: Array4f16
    zzyz: Array4f16
    zzyw: Array4f16
    zzzx: Array4f16
    zzzy: Array4f16
    zzzz: Array4f16
    zzzw: Array4f16
    zzwx: Array4f16
    zzwy: Array4f16
    zzwz: Array4f16
    zzww: Array4f16
    zwxx: Array4f16
    zwxy: Array4f16
    zwxz: Array4f16
    zwxw: Array4f16
    zwyx: Array4f16
    zwyy: Array4f16
    zwyz: Array4f16
    zwyw: Array4f16
    zwzx: Array4f16
    zwzy: Array4f16
    zwzz: Array4f16
    zwzw: Array4f16
    zwwx: Array4f16
    zwwy: Array4f16
    zwwz: Array4f16
    zwww: Array4f16
    wxxx: Array4f16
    wxxy: Array4f16
    wxxz: Array4f16
    wxxw: Array4f16
    wxyx: Array4f16
    wxyy: Array4f16
    wxyz: Array4f16
    wxyw: Array4f16
    wxzx: Array4f16
    wxzy: Array4f16
    wxzz: Array4f16
    wxzw: Array4f16
    wxwx: Array4f16
    wxwy: Array4f16
    wxwz: Array4f16
    wxww: Array4f16
    wyxx: Array4f16
    wyxy: Array4f16
    wyxz: Array4f16
    wyxw: Array4f16
    wyyx: Array4f16
    wyyy: Array4f16
    wyyz: Array4f16
    wyyw: Array4f16
    wyzx: Array4f16
    wyzy: Array4f16
    wyzz: Array4f16
    wyzw: Array4f16
    wywx: Array4f16
    wywy: Array4f16
    wywz: Array4f16
    wyww: Array4f16
    wzxx: Array4f16
    wzxy: Array4f16
    wzxz: Array4f16
    wzxw: Array4f16
    wzyx: Array4f16
    wzyy: Array4f16
    wzyz: Array4f16
    wzyw: Array4f16
    wzzx: Array4f16
    wzzy: Array4f16
    wzzz: Array4f16
    wzzw: Array4f16
    wzwx: Array4f16
    wzwy: Array4f16
    wzwz: Array4f16
    wzww: Array4f16
    wwxx: Array4f16
    wwxy: Array4f16
    wwxz: Array4f16
    wwxw: Array4f16
    wwyx: Array4f16
    wwyy: Array4f16
    wwyz: Array4f16
    wwyw: Array4f16
    wwzx: Array4f16
    wwzy: Array4f16
    wwzz: Array4f16
    wwzw: Array4f16
    wwwx: Array4f16
    wwwy: Array4f16
    wwwz: Array4f16
    wwww: Array4f16

_Array2fCp: TypeAlias = Union['Array2f', '_FloatCp', 'drjit.scalar._Array2fCp', 'drjit.llvm._Array2fCp', '_Array2f16Cp']

class Array2f(drjit.ArrayBase[Array2f, _Array2fCp, Float, _FloatCp, Float, Array2f, Array2b]):
    xx: Array2f
    xy: Array2f
    xz: Array2f
    xw: Array2f
    yx: Array2f
    yy: Array2f
    yz: Array2f
    yw: Array2f
    zx: Array2f
    zy: Array2f
    zz: Array2f
    zw: Array2f
    wx: Array2f
    wy: Array2f
    wz: Array2f
    ww: Array2f
    xxx: Array3f
    xxy: Array3f
    xxz: Array3f
    xxw: Array3f
    xyx: Array3f
    xyy: Array3f
    xyz: Array3f
    xyw: Array3f
    xzx: Array3f
    xzy: Array3f
    xzz: Array3f
    xzw: Array3f
    xwx: Array3f
    xwy: Array3f
    xwz: Array3f
    xww: Array3f
    yxx: Array3f
    yxy: Array3f
    yxz: Array3f
    yxw: Array3f
    yyx: Array3f
    yyy: Array3f
    yyz: Array3f
    yyw: Array3f
    yzx: Array3f
    yzy: Array3f
    yzz: Array3f
    yzw: Array3f
    ywx: Array3f
    ywy: Array3f
    ywz: Array3f
    yww: Array3f
    zxx: Array3f
    zxy: Array3f
    zxz: Array3f
    zxw: Array3f
    zyx: Array3f
    zyy: Array3f
    zyz: Array3f
    zyw: Array3f
    zzx: Array3f
    zzy: Array3f
    zzz: Array3f
    zzw: Array3f
    zwx: Array3f
    zwy: Array3f
    zwz: Array3f
    zww: Array3f
    wxx: Array3f
    wxy: Array3f
    wxz: Array3f
    wxw: Array3f
    wyx: Array3f
    wyy: Array3f
    wyz: Array3f
    wyw: Array3f
    wzx: Array3f
    wzy: Array3f
    wzz: Array3f
    wzw: Array3f
    wwx: Array3f
    wwy: Array3f
    wwz: Array3f
    www: Array3f
    xxxx: Array4f
    xxxy: Array4f
    xxxz: Array4f
    xxxw: Array4f
    xxyx: Array4f
    xxyy: Array4f
    xxyz: Array4f
    xxyw: Array4f
    xxzx: Array4f
    xxzy: Array4f
    xxzz: Array4f
    xxzw: Array4f
    xxwx: Array4f
    xxwy: Array4f
    xxwz: Array4f
    xxww: Array4f
    xyxx: Array4f
    xyxy: Array4f
    xyxz: Array4f
    xyxw: Array4f
    xyyx: Array4f
    xyyy: Array4f
    xyyz: Array4f
    xyyw: Array4f
    xyzx: Array4f
    xyzy: Array4f
    xyzz: Array4f
    xyzw: Array4f
    xywx: Array4f
    xywy: Array4f
    xywz: Array4f
    xyww: Array4f
    xzxx: Array4f
    xzxy: Array4f
    xzxz: Array4f
    xzxw: Array4f
    xzyx: Array4f
    xzyy: Array4f
    xzyz: Array4f
    xzyw: Array4f
    xzzx: Array4f
    xzzy: Array4f
    xzzz: Array4f
    xzzw: Array4f
    xzwx: Array4f
    xzwy: Array4f
    xzwz: Array4f
    xzww: Array4f
    xwxx: Array4f
    xwxy: Array4f
    xwxz: Array4f
    xwxw: Array4f
    xwyx: Array4f
    xwyy: Array4f
    xwyz: Array4f
    xwyw: Array4f
    xwzx: Array4f
    xwzy: Array4f
    xwzz: Array4f
    xwzw: Array4f
    xwwx: Array4f
    xwwy: Array4f
    xwwz: Array4f
    xwww: Array4f
    yxxx: Array4f
    yxxy: Array4f
    yxxz: Array4f
    yxxw: Array4f
    yxyx: Array4f
    yxyy: Array4f
    yxyz: Array4f
    yxyw: Array4f
    yxzx: Array4f
    yxzy: Array4f
    yxzz: Array4f
    yxzw: Array4f
    yxwx: Array4f
    yxwy: Array4f
    yxwz: Array4f
    yxww: Array4f
    yyxx: Array4f
    yyxy: Array4f
    yyxz: Array4f
    yyxw: Array4f
    yyyx: Array4f
    yyyy: Array4f
    yyyz: Array4f
    yyyw: Array4f
    yyzx: Array4f
    yyzy: Array4f
    yyzz: Array4f
    yyzw: Array4f
    yywx: Array4f
    yywy: Array4f
    yywz: Array4f
    yyww: Array4f
    yzxx: Array4f
    yzxy: Array4f
    yzxz: Array4f
    yzxw: Array4f
    yzyx: Array4f
    yzyy: Array4f
    yzyz: Array4f
    yzyw: Array4f
    yzzx: Array4f
    yzzy: Array4f
    yzzz: Array4f
    yzzw: Array4f
    yzwx: Array4f
    yzwy: Array4f
    yzwz: Array4f
    yzww: Array4f
    ywxx: Array4f
    ywxy: Array4f
    ywxz: Array4f
    ywxw: Array4f
    ywyx: Array4f
    ywyy: Array4f
    ywyz: Array4f
    ywyw: Array4f
    ywzx: Array4f
    ywzy: Array4f
    ywzz: Array4f
    ywzw: Array4f
    ywwx: Array4f
    ywwy: Array4f
    ywwz: Array4f
    ywww: Array4f
    zxxx: Array4f
    zxxy: Array4f
    zxxz: Array4f
    zxxw: Array4f
    zxyx: Array4f
    zxyy: Array4f
    zxyz: Array4f
    zxyw: Array4f
    zxzx: Array4f
    zxzy: Array4f
    zxzz: Array4f
    zxzw: Array4f
    zxwx: Array4f
    zxwy: Array4f
    zxwz: Array4f
    zxww: Array4f
    zyxx: Array4f
    zyxy: Array4f
    zyxz: Array4f
    zyxw: Array4f
    zyyx: Array4f
    zyyy: Array4f
    zyyz: Array4f
    zyyw: Array4f
    zyzx: Array4f
    zyzy: Array4f
    zyzz: Array4f
    zyzw: Array4f
    zywx: Array4f
    zywy: Array4f
    zywz: Array4f
    zyww: Array4f
    zzxx: Array4f
    zzxy: Array4f
    zzxz: Array4f
    zzxw: Array4f
    zzyx: Array4f
    zzyy: Array4f
    zzyz: Array4f
    zzyw: Array4f
    zzzx: Array4f
    zzzy: Array4f
    zzzz: Array4f
    zzzw: Array4f
    zzwx: Array4f
    zzwy: Array4f
    zzwz: Array4f
    zzww: Array4f
    zwxx: Array4f
    zwxy: Array4f
    zwxz: Array4f
    zwxw: Array4f
    zwyx: Array4f
    zwyy: Array4f
    zwyz: Array4f
    zwyw: Array4f
    zwzx: Array4f
    zwzy: Array4f
    zwzz: Array4f
    zwzw: Array4f
    zwwx: Array4f
    zwwy: Array4f
    zwwz: Array4f
    zwww: Array4f
    wxxx: Array4f
    wxxy: Array4f
    wxxz: Array4f
    wxxw: Array4f
    wxyx: Array4f
    wxyy: Array4f
    wxyz: Array4f
    wxyw: Array4f
    wxzx: Array4f
    wxzy: Array4f
    wxzz: Array4f
    wxzw: Array4f
    wxwx: Array4f
    wxwy: Array4f
    wxwz: Array4f
    wxww: Array4f
    wyxx: Array4f
    wyxy: Array4f
    wyxz: Array4f
    wyxw: Array4f
    wyyx: Array4f
    wyyy: Array4f
    wyyz: Array4f
    wyyw: Array4f
    wyzx: Array4f
    wyzy: Array4f
    wyzz: Array4f
    wyzw: Array4f
    wywx: Array4f
    wywy: Array4f
    wywz: Array4f
    wyww: Array4f
    wzxx: Array4f
    wzxy: Array4f
    wzxz: Array4f
    wzxw: Array4f
    wzyx: Array4f
    wzyy: Array4f
    wzyz: Array4f
    wzyw: Array4f
    wzzx: Array4f
    wzzy: Array4f
    wzzz: Array4f
    wzzw: Array4f
    wzwx: Array4f
    wzwy: Array4f
    wzwz: Array4f
    wzww: Array4f
    wwxx: Array4f
    wwxy: Array4f
    wwxz: Array4f
    wwxw: Array4f
    wwyx: Array4f
    wwyy: Array4f
    wwyz: Array4f
    wwyw: Array4f
    wwzx: Array4f
    wwzy: Array4f
    wwzz: Array4f
    wwzw: Array4f
    wwwx: Array4f
    wwwy: Array4f
    wwwz: Array4f
    wwww: Array4f

_Array2f64Cp: TypeAlias = Union['Array2f64', '_Float64Cp', 'drjit.scalar._Array2f64Cp', 'drjit.llvm._Array2f64Cp', '_Array2fCp']

class Array2f64(drjit.ArrayBase[Array2f64, _Array2f64Cp, Float64, _Float64Cp, Float64, Array2f64, Array2b]):
    xx: Array2f64
    xy: Array2f64
    xz: Array2f64
    xw: Array2f64
    yx: Array2f64
    yy: Array2f64
    yz: Array2f64
    yw: Array2f64
    zx: Array2f64
    zy: Array2f64
    zz: Array2f64
    zw: Array2f64
    wx: Array2f64
    wy: Array2f64
    wz: Array2f64
    ww: Array2f64
    xxx: Array3f64
    xxy: Array3f64
    xxz: Array3f64
    xxw: Array3f64
    xyx: Array3f64
    xyy: Array3f64
    xyz: Array3f64
    xyw: Array3f64
    xzx: Array3f64
    xzy: Array3f64
    xzz: Array3f64
    xzw: Array3f64
    xwx: Array3f64
    xwy: Array3f64
    xwz: Array3f64
    xww: Array3f64
    yxx: Array3f64
    yxy: Array3f64
    yxz: Array3f64
    yxw: Array3f64
    yyx: Array3f64
    yyy: Array3f64
    yyz: Array3f64
    yyw: Array3f64
    yzx: Array3f64
    yzy: Array3f64
    yzz: Array3f64
    yzw: Array3f64
    ywx: Array3f64
    ywy: Array3f64
    ywz: Array3f64
    yww: Array3f64
    zxx: Array3f64
    zxy: Array3f64
    zxz: Array3f64
    zxw: Array3f64
    zyx: Array3f64
    zyy: Array3f64
    zyz: Array3f64
    zyw: Array3f64
    zzx: Array3f64
    zzy: Array3f64
    zzz: Array3f64
    zzw: Array3f64
    zwx: Array3f64
    zwy: Array3f64
    zwz: Array3f64
    zww: Array3f64
    wxx: Array3f64
    wxy: Array3f64
    wxz: Array3f64
    wxw: Array3f64
    wyx: Array3f64
    wyy: Array3f64
    wyz: Array3f64
    wyw: Array3f64
    wzx: Array3f64
    wzy: Array3f64
    wzz: Array3f64
    wzw: Array3f64
    wwx: Array3f64
    wwy: Array3f64
    wwz: Array3f64
    www: Array3f64
    xxxx: Array4f64
    xxxy: Array4f64
    xxxz: Array4f64
    xxxw: Array4f64
    xxyx: Array4f64
    xxyy: Array4f64
    xxyz: Array4f64
    xxyw: Array4f64
    xxzx: Array4f64
    xxzy: Array4f64
    xxzz: Array4f64
    xxzw: Array4f64
    xxwx: Array4f64
    xxwy: Array4f64
    xxwz: Array4f64
    xxww: Array4f64
    xyxx: Array4f64
    xyxy: Array4f64
    xyxz: Array4f64
    xyxw: Array4f64
    xyyx: Array4f64
    xyyy: Array4f64
    xyyz: Array4f64
    xyyw: Array4f64
    xyzx: Array4f64
    xyzy: Array4f64
    xyzz: Array4f64
    xyzw: Array4f64
    xywx: Array4f64
    xywy: Array4f64
    xywz: Array4f64
    xyww: Array4f64
    xzxx: Array4f64
    xzxy: Array4f64
    xzxz: Array4f64
    xzxw: Array4f64
    xzyx: Array4f64
    xzyy: Array4f64
    xzyz: Array4f64
    xzyw: Array4f64
    xzzx: Array4f64
    xzzy: Array4f64
    xzzz: Array4f64
    xzzw: Array4f64
    xzwx: Array4f64
    xzwy: Array4f64
    xzwz: Array4f64
    xzww: Array4f64
    xwxx: Array4f64
    xwxy: Array4f64
    xwxz: Array4f64
    xwxw: Array4f64
    xwyx: Array4f64
    xwyy: Array4f64
    xwyz: Array4f64
    xwyw: Array4f64
    xwzx: Array4f64
    xwzy: Array4f64
    xwzz: Array4f64
    xwzw: Array4f64
    xwwx: Array4f64
    xwwy: Array4f64
    xwwz: Array4f64
    xwww: Array4f64
    yxxx: Array4f64
    yxxy: Array4f64
    yxxz: Array4f64
    yxxw: Array4f64
    yxyx: Array4f64
    yxyy: Array4f64
    yxyz: Array4f64
    yxyw: Array4f64
    yxzx: Array4f64
    yxzy: Array4f64
    yxzz: Array4f64
    yxzw: Array4f64
    yxwx: Array4f64
    yxwy: Array4f64
    yxwz: Array4f64
    yxww: Array4f64
    yyxx: Array4f64
    yyxy: Array4f64
    yyxz: Array4f64
    yyxw: Array4f64
    yyyx: Array4f64
    yyyy: Array4f64
    yyyz: Array4f64
    yyyw: Array4f64
    yyzx: Array4f64
    yyzy: Array4f64
    yyzz: Array4f64
    yyzw: Array4f64
    yywx: Array4f64
    yywy: Array4f64
    yywz: Array4f64
    yyww: Array4f64
    yzxx: Array4f64
    yzxy: Array4f64
    yzxz: Array4f64
    yzxw: Array4f64
    yzyx: Array4f64
    yzyy: Array4f64
    yzyz: Array4f64
    yzyw: Array4f64
    yzzx: Array4f64
    yzzy: Array4f64
    yzzz: Array4f64
    yzzw: Array4f64
    yzwx: Array4f64
    yzwy: Array4f64
    yzwz: Array4f64
    yzww: Array4f64
    ywxx: Array4f64
    ywxy: Array4f64
    ywxz: Array4f64
    ywxw: Array4f64
    ywyx: Array4f64
    ywyy: Array4f64
    ywyz: Array4f64
    ywyw: Array4f64
    ywzx: Array4f64
    ywzy: Array4f64
    ywzz: Array4f64
    ywzw: Array4f64
    ywwx: Array4f64
    ywwy: Array4f64
    ywwz: Array4f64
    ywww: Array4f64
    zxxx: Array4f64
    zxxy: Array4f64
    zxxz: Array4f64
    zxxw: Array4f64
    zxyx: Array4f64
    zxyy: Array4f64
    zxyz: Array4f64
    zxyw: Array4f64
    zxzx: Array4f64
    zxzy: Array4f64
    zxzz: Array4f64
    zxzw: Array4f64
    zxwx: Array4f64
    zxwy: Array4f64
    zxwz: Array4f64
    zxww: Array4f64
    zyxx: Array4f64
    zyxy: Array4f64
    zyxz: Array4f64
    zyxw: Array4f64
    zyyx: Array4f64
    zyyy: Array4f64
    zyyz: Array4f64
    zyyw: Array4f64
    zyzx: Array4f64
    zyzy: Array4f64
    zyzz: Array4f64
    zyzw: Array4f64
    zywx: Array4f64
    zywy: Array4f64
    zywz: Array4f64
    zyww: Array4f64
    zzxx: Array4f64
    zzxy: Array4f64
    zzxz: Array4f64
    zzxw: Array4f64
    zzyx: Array4f64
    zzyy: Array4f64
    zzyz: Array4f64
    zzyw: Array4f64
    zzzx: Array4f64
    zzzy: Array4f64
    zzzz: Array4f64
    zzzw: Array4f64
    zzwx: Array4f64
    zzwy: Array4f64
    zzwz: Array4f64
    zzww: Array4f64
    zwxx: Array4f64
    zwxy: Array4f64
    zwxz: Array4f64
    zwxw: Array4f64
    zwyx: Array4f64
    zwyy: Array4f64
    zwyz: Array4f64
    zwyw: Array4f64
    zwzx: Array4f64
    zwzy: Array4f64
    zwzz: Array4f64
    zwzw: Array4f64
    zwwx: Array4f64
    zwwy: Array4f64
    zwwz: Array4f64
    zwww: Array4f64
    wxxx: Array4f64
    wxxy: Array4f64
    wxxz: Array4f64
    wxxw: Array4f64
    wxyx: Array4f64
    wxyy: Array4f64
    wxyz: Array4f64
    wxyw: Array4f64
    wxzx: Array4f64
    wxzy: Array4f64
    wxzz: Array4f64
    wxzw: Array4f64
    wxwx: Array4f64
    wxwy: Array4f64
    wxwz: Array4f64
    wxww: Array4f64
    wyxx: Array4f64
    wyxy: Array4f64
    wyxz: Array4f64
    wyxw: Array4f64
    wyyx: Array4f64
    wyyy: Array4f64
    wyyz: Array4f64
    wyyw: Array4f64
    wyzx: Array4f64
    wyzy: Array4f64
    wyzz: Array4f64
    wyzw: Array4f64
    wywx: Array4f64
    wywy: Array4f64
    wywz: Array4f64
    wyww: Array4f64
    wzxx: Array4f64
    wzxy: Array4f64
    wzxz: Array4f64
    wzxw: Array4f64
    wzyx: Array4f64
    wzyy: Array4f64
    wzyz: Array4f64
    wzyw: Array4f64
    wzzx: Array4f64
    wzzy: Array4f64
    wzzz: Array4f64
    wzzw: Array4f64
    wzwx: Array4f64
    wzwy: Array4f64
    wzwz: Array4f64
    wzww: Array4f64
    wwxx: Array4f64
    wwxy: Array4f64
    wwxz: Array4f64
    wwxw: Array4f64
    wwyx: Array4f64
    wwyy: Array4f64
    wwyz: Array4f64
    wwyw: Array4f64
    wwzx: Array4f64
    wwzy: Array4f64
    wwzz: Array4f64
    wwzw: Array4f64
    wwwx: Array4f64
    wwwy: Array4f64
    wwwz: Array4f64
    wwww: Array4f64

_Array3bCp: TypeAlias = Union['Array3b', '_BoolCp', 'drjit.scalar._Array3bCp', 'drjit.llvm._Array3bCp']

class Array3b(drjit.ArrayBase[Array3b, _Array3bCp, Bool, _BoolCp, Bool, Array3b, Array3b]):
    xx: Array2b
    xy: Array2b
    xz: Array2b
    xw: Array2b
    yx: Array2b
    yy: Array2b
    yz: Array2b
    yw: Array2b
    zx: Array2b
    zy: Array2b
    zz: Array2b
    zw: Array2b
    wx: Array2b
    wy: Array2b
    wz: Array2b
    ww: Array2b
    xxx: Array3b
    xxy: Array3b
    xxz: Array3b
    xxw: Array3b
    xyx: Array3b
    xyy: Array3b
    xyz: Array3b
    xyw: Array3b
    xzx: Array3b
    xzy: Array3b
    xzz: Array3b
    xzw: Array3b
    xwx: Array3b
    xwy: Array3b
    xwz: Array3b
    xww: Array3b
    yxx: Array3b
    yxy: Array3b
    yxz: Array3b
    yxw: Array3b
    yyx: Array3b
    yyy: Array3b
    yyz: Array3b
    yyw: Array3b
    yzx: Array3b
    yzy: Array3b
    yzz: Array3b
    yzw: Array3b
    ywx: Array3b
    ywy: Array3b
    ywz: Array3b
    yww: Array3b
    zxx: Array3b
    zxy: Array3b
    zxz: Array3b
    zxw: Array3b
    zyx: Array3b
    zyy: Array3b
    zyz: Array3b
    zyw: Array3b
    zzx: Array3b
    zzy: Array3b
    zzz: Array3b
    zzw: Array3b
    zwx: Array3b
    zwy: Array3b
    zwz: Array3b
    zww: Array3b
    wxx: Array3b
    wxy: Array3b
    wxz: Array3b
    wxw: Array3b
    wyx: Array3b
    wyy: Array3b
    wyz: Array3b
    wyw: Array3b
    wzx: Array3b
    wzy: Array3b
    wzz: Array3b
    wzw: Array3b
    wwx: Array3b
    wwy: Array3b
    wwz: Array3b
    www: Array3b
    xxxx: Array4b
    xxxy: Array4b
    xxxz: Array4b
    xxxw: Array4b
    xxyx: Array4b
    xxyy: Array4b
    xxyz: Array4b
    xxyw: Array4b
    xxzx: Array4b
    xxzy: Array4b
    xxzz: Array4b
    xxzw: Array4b
    xxwx: Array4b
    xxwy: Array4b
    xxwz: Array4b
    xxww: Array4b
    xyxx: Array4b
    xyxy: Array4b
    xyxz: Array4b
    xyxw: Array4b
    xyyx: Array4b
    xyyy: Array4b
    xyyz: Array4b
    xyyw: Array4b
    xyzx: Array4b
    xyzy: Array4b
    xyzz: Array4b
    xyzw: Array4b
    xywx: Array4b
    xywy: Array4b
    xywz: Array4b
    xyww: Array4b
    xzxx: Array4b
    xzxy: Array4b
    xzxz: Array4b
    xzxw: Array4b
    xzyx: Array4b
    xzyy: Array4b
    xzyz: Array4b
    xzyw: Array4b
    xzzx: Array4b
    xzzy: Array4b
    xzzz: Array4b
    xzzw: Array4b
    xzwx: Array4b
    xzwy: Array4b
    xzwz: Array4b
    xzww: Array4b
    xwxx: Array4b
    xwxy: Array4b
    xwxz: Array4b
    xwxw: Array4b
    xwyx: Array4b
    xwyy: Array4b
    xwyz: Array4b
    xwyw: Array4b
    xwzx: Array4b
    xwzy: Array4b
    xwzz: Array4b
    xwzw: Array4b
    xwwx: Array4b
    xwwy: Array4b
    xwwz: Array4b
    xwww: Array4b
    yxxx: Array4b
    yxxy: Array4b
    yxxz: Array4b
    yxxw: Array4b
    yxyx: Array4b
    yxyy: Array4b
    yxyz: Array4b
    yxyw: Array4b
    yxzx: Array4b
    yxzy: Array4b
    yxzz: Array4b
    yxzw: Array4b
    yxwx: Array4b
    yxwy: Array4b
    yxwz: Array4b
    yxww: Array4b
    yyxx: Array4b
    yyxy: Array4b
    yyxz: Array4b
    yyxw: Array4b
    yyyx: Array4b
    yyyy: Array4b
    yyyz: Array4b
    yyyw: Array4b
    yyzx: Array4b
    yyzy: Array4b
    yyzz: Array4b
    yyzw: Array4b
    yywx: Array4b
    yywy: Array4b
    yywz: Array4b
    yyww: Array4b
    yzxx: Array4b
    yzxy: Array4b
    yzxz: Array4b
    yzxw: Array4b
    yzyx: Array4b
    yzyy: Array4b
    yzyz: Array4b
    yzyw: Array4b
    yzzx: Array4b
    yzzy: Array4b
    yzzz: Array4b
    yzzw: Array4b
    yzwx: Array4b
    yzwy: Array4b
    yzwz: Array4b
    yzww: Array4b
    ywxx: Array4b
    ywxy: Array4b
    ywxz: Array4b
    ywxw: Array4b
    ywyx: Array4b
    ywyy: Array4b
    ywyz: Array4b
    ywyw: Array4b
    ywzx: Array4b
    ywzy: Array4b
    ywzz: Array4b
    ywzw: Array4b
    ywwx: Array4b
    ywwy: Array4b
    ywwz: Array4b
    ywww: Array4b
    zxxx: Array4b
    zxxy: Array4b
    zxxz: Array4b
    zxxw: Array4b
    zxyx: Array4b
    zxyy: Array4b
    zxyz: Array4b
    zxyw: Array4b
    zxzx: Array4b
    zxzy: Array4b
    zxzz: Array4b
    zxzw: Array4b
    zxwx: Array4b
    zxwy: Array4b
    zxwz: Array4b
    zxww: Array4b
    zyxx: Array4b
    zyxy: Array4b
    zyxz: Array4b
    zyxw: Array4b
    zyyx: Array4b
    zyyy: Array4b
    zyyz: Array4b
    zyyw: Array4b
    zyzx: Array4b
    zyzy: Array4b
    zyzz: Array4b
    zyzw: Array4b
    zywx: Array4b
    zywy: Array4b
    zywz: Array4b
    zyww: Array4b
    zzxx: Array4b
    zzxy: Array4b
    zzxz: Array4b
    zzxw: Array4b
    zzyx: Array4b
    zzyy: Array4b
    zzyz: Array4b
    zzyw: Array4b
    zzzx: Array4b
    zzzy: Array4b
    zzzz: Array4b
    zzzw: Array4b
    zzwx: Array4b
    zzwy: Array4b
    zzwz: Array4b
    zzww: Array4b
    zwxx: Array4b
    zwxy: Array4b
    zwxz: Array4b
    zwxw: Array4b
    zwyx: Array4b
    zwyy: Array4b
    zwyz: Array4b
    zwyw: Array4b
    zwzx: Array4b
    zwzy: Array4b
    zwzz: Array4b
    zwzw: Array4b
    zwwx: Array4b
    zwwy: Array4b
    zwwz: Array4b
    zwww: Array4b
    wxxx: Array4b
    wxxy: Array4b
    wxxz: Array4b
    wxxw: Array4b
    wxyx: Array4b
    wxyy: Array4b
    wxyz: Array4b
    wxyw: Array4b
    wxzx: Array4b
    wxzy: Array4b
    wxzz: Array4b
    wxzw: Array4b
    wxwx: Array4b
    wxwy: Array4b
    wxwz: Array4b
    wxww: Array4b
    wyxx: Array4b
    wyxy: Array4b
    wyxz: Array4b
    wyxw: Array4b
    wyyx: Array4b
    wyyy: Array4b
    wyyz: Array4b
    wyyw: Array4b
    wyzx: Array4b
    wyzy: Array4b
    wyzz: Array4b
    wyzw: Array4b
    wywx: Array4b
    wywy: Array4b
    wywz: Array4b
    wyww: Array4b
    wzxx: Array4b
    wzxy: Array4b
    wzxz: Array4b
    wzxw: Array4b
    wzyx: Array4b
    wzyy: Array4b
    wzyz: Array4b
    wzyw: Array4b
    wzzx: Array4b
    wzzy: Array4b
    wzzz: Array4b
    wzzw: Array4b
    wzwx: Array4b
    wzwy: Array4b
    wzwz: Array4b
    wzww: Array4b
    wwxx: Array4b
    wwxy: Array4b
    wwxz: Array4b
    wwxw: Array4b
    wwyx: Array4b
    wwyy: Array4b
    wwyz: Array4b
    wwyw: Array4b
    wwzx: Array4b
    wwzy: Array4b
    wwzz: Array4b
    wwzw: Array4b
    wwwx: Array4b
    wwwy: Array4b
    wwwz: Array4b
    wwww: Array4b

_Array3i8Cp: TypeAlias = Union['Array3i8', '_Int8Cp', 'drjit.scalar._Array3i8Cp', 'drjit.llvm._Array3i8Cp']

class Array3i8(drjit.ArrayBase[Array3i8, _Array3i8Cp, Int8, _Int8Cp, Int8, Array3i8, Array3b]):
    xx: Array2i8
    xy: Array2i8
    xz: Array2i8
    xw: Array2i8
    yx: Array2i8
    yy: Array2i8
    yz: Array2i8
    yw: Array2i8
    zx: Array2i8
    zy: Array2i8
    zz: Array2i8
    zw: Array2i8
    wx: Array2i8
    wy: Array2i8
    wz: Array2i8
    ww: Array2i8
    xxx: Array3i8
    xxy: Array3i8
    xxz: Array3i8
    xxw: Array3i8
    xyx: Array3i8
    xyy: Array3i8
    xyz: Array3i8
    xyw: Array3i8
    xzx: Array3i8
    xzy: Array3i8
    xzz: Array3i8
    xzw: Array3i8
    xwx: Array3i8
    xwy: Array3i8
    xwz: Array3i8
    xww: Array3i8
    yxx: Array3i8
    yxy: Array3i8
    yxz: Array3i8
    yxw: Array3i8
    yyx: Array3i8
    yyy: Array3i8
    yyz: Array3i8
    yyw: Array3i8
    yzx: Array3i8
    yzy: Array3i8
    yzz: Array3i8
    yzw: Array3i8
    ywx: Array3i8
    ywy: Array3i8
    ywz: Array3i8
    yww: Array3i8
    zxx: Array3i8
    zxy: Array3i8
    zxz: Array3i8
    zxw: Array3i8
    zyx: Array3i8
    zyy: Array3i8
    zyz: Array3i8
    zyw: Array3i8
    zzx: Array3i8
    zzy: Array3i8
    zzz: Array3i8
    zzw: Array3i8
    zwx: Array3i8
    zwy: Array3i8
    zwz: Array3i8
    zww: Array3i8
    wxx: Array3i8
    wxy: Array3i8
    wxz: Array3i8
    wxw: Array3i8
    wyx: Array3i8
    wyy: Array3i8
    wyz: Array3i8
    wyw: Array3i8
    wzx: Array3i8
    wzy: Array3i8
    wzz: Array3i8
    wzw: Array3i8
    wwx: Array3i8
    wwy: Array3i8
    wwz: Array3i8
    www: Array3i8
    xxxx: Array4i8
    xxxy: Array4i8
    xxxz: Array4i8
    xxxw: Array4i8
    xxyx: Array4i8
    xxyy: Array4i8
    xxyz: Array4i8
    xxyw: Array4i8
    xxzx: Array4i8
    xxzy: Array4i8
    xxzz: Array4i8
    xxzw: Array4i8
    xxwx: Array4i8
    xxwy: Array4i8
    xxwz: Array4i8
    xxww: Array4i8
    xyxx: Array4i8
    xyxy: Array4i8
    xyxz: Array4i8
    xyxw: Array4i8
    xyyx: Array4i8
    xyyy: Array4i8
    xyyz: Array4i8
    xyyw: Array4i8
    xyzx: Array4i8
    xyzy: Array4i8
    xyzz: Array4i8
    xyzw: Array4i8
    xywx: Array4i8
    xywy: Array4i8
    xywz: Array4i8
    xyww: Array4i8
    xzxx: Array4i8
    xzxy: Array4i8
    xzxz: Array4i8
    xzxw: Array4i8
    xzyx: Array4i8
    xzyy: Array4i8
    xzyz: Array4i8
    xzyw: Array4i8
    xzzx: Array4i8
    xzzy: Array4i8
    xzzz: Array4i8
    xzzw: Array4i8
    xzwx: Array4i8
    xzwy: Array4i8
    xzwz: Array4i8
    xzww: Array4i8
    xwxx: Array4i8
    xwxy: Array4i8
    xwxz: Array4i8
    xwxw: Array4i8
    xwyx: Array4i8
    xwyy: Array4i8
    xwyz: Array4i8
    xwyw: Array4i8
    xwzx: Array4i8
    xwzy: Array4i8
    xwzz: Array4i8
    xwzw: Array4i8
    xwwx: Array4i8
    xwwy: Array4i8
    xwwz: Array4i8
    xwww: Array4i8
    yxxx: Array4i8
    yxxy: Array4i8
    yxxz: Array4i8
    yxxw: Array4i8
    yxyx: Array4i8
    yxyy: Array4i8
    yxyz: Array4i8
    yxyw: Array4i8
    yxzx: Array4i8
    yxzy: Array4i8
    yxzz: Array4i8
    yxzw: Array4i8
    yxwx: Array4i8
    yxwy: Array4i8
    yxwz: Array4i8
    yxww: Array4i8
    yyxx: Array4i8
    yyxy: Array4i8
    yyxz: Array4i8
    yyxw: Array4i8
    yyyx: Array4i8
    yyyy: Array4i8
    yyyz: Array4i8
    yyyw: Array4i8
    yyzx: Array4i8
    yyzy: Array4i8
    yyzz: Array4i8
    yyzw: Array4i8
    yywx: Array4i8
    yywy: Array4i8
    yywz: Array4i8
    yyww: Array4i8
    yzxx: Array4i8
    yzxy: Array4i8
    yzxz: Array4i8
    yzxw: Array4i8
    yzyx: Array4i8
    yzyy: Array4i8
    yzyz: Array4i8
    yzyw: Array4i8
    yzzx: Array4i8
    yzzy: Array4i8
    yzzz: Array4i8
    yzzw: Array4i8
    yzwx: Array4i8
    yzwy: Array4i8
    yzwz: Array4i8
    yzww: Array4i8
    ywxx: Array4i8
    ywxy: Array4i8
    ywxz: Array4i8
    ywxw: Array4i8
    ywyx: Array4i8
    ywyy: Array4i8
    ywyz: Array4i8
    ywyw: Array4i8
    ywzx: Array4i8
    ywzy: Array4i8
    ywzz: Array4i8
    ywzw: Array4i8
    ywwx: Array4i8
    ywwy: Array4i8
    ywwz: Array4i8
    ywww: Array4i8
    zxxx: Array4i8
    zxxy: Array4i8
    zxxz: Array4i8
    zxxw: Array4i8
    zxyx: Array4i8
    zxyy: Array4i8
    zxyz: Array4i8
    zxyw: Array4i8
    zxzx: Array4i8
    zxzy: Array4i8
    zxzz: Array4i8
    zxzw: Array4i8
    zxwx: Array4i8
    zxwy: Array4i8
    zxwz: Array4i8
    zxww: Array4i8
    zyxx: Array4i8
    zyxy: Array4i8
    zyxz: Array4i8
    zyxw: Array4i8
    zyyx: Array4i8
    zyyy: Array4i8
    zyyz: Array4i8
    zyyw: Array4i8
    zyzx: Array4i8
    zyzy: Array4i8
    zyzz: Array4i8
    zyzw: Array4i8
    zywx: Array4i8
    zywy: Array4i8
    zywz: Array4i8
    zyww: Array4i8
    zzxx: Array4i8
    zzxy: Array4i8
    zzxz: Array4i8
    zzxw: Array4i8
    zzyx: Array4i8
    zzyy: Array4i8
    zzyz: Array4i8
    zzyw: Array4i8
    zzzx: Array4i8
    zzzy: Array4i8
    zzzz: Array4i8
    zzzw: Array4i8
    zzwx: Array4i8
    zzwy: Array4i8
    zzwz: Array4i8
    zzww: Array4i8
    zwxx: Array4i8
    zwxy: Array4i8
    zwxz: Array4i8
    zwxw: Array4i8
    zwyx: Array4i8
    zwyy: Array4i8
    zwyz: Array4i8
    zwyw: Array4i8
    zwzx: Array4i8
    zwzy: Array4i8
    zwzz: Array4i8
    zwzw: Array4i8
    zwwx: Array4i8
    zwwy: Array4i8
    zwwz: Array4i8
    zwww: Array4i8
    wxxx: Array4i8
    wxxy: Array4i8
    wxxz: Array4i8
    wxxw: Array4i8
    wxyx: Array4i8
    wxyy: Array4i8
    wxyz: Array4i8
    wxyw: Array4i8
    wxzx: Array4i8
    wxzy: Array4i8
    wxzz: Array4i8
    wxzw: Array4i8
    wxwx: Array4i8
    wxwy: Array4i8
    wxwz: Array4i8
    wxww: Array4i8
    wyxx: Array4i8
    wyxy: Array4i8
    wyxz: Array4i8
    wyxw: Array4i8
    wyyx: Array4i8
    wyyy: Array4i8
    wyyz: Array4i8
    wyyw: Array4i8
    wyzx: Array4i8
    wyzy: Array4i8
    wyzz: Array4i8
    wyzw: Array4i8
    wywx: Array4i8
    wywy: Array4i8
    wywz: Array4i8
    wyww: Array4i8
    wzxx: Array4i8
    wzxy: Array4i8
    wzxz: Array4i8
    wzxw: Array4i8
    wzyx: Array4i8
    wzyy: Array4i8
    wzyz: Array4i8
    wzyw: Array4i8
    wzzx: Array4i8
    wzzy: Array4i8
    wzzz: Array4i8
    wzzw: Array4i8
    wzwx: Array4i8
    wzwy: Array4i8
    wzwz: Array4i8
    wzww: Array4i8
    wwxx: Array4i8
    wwxy: Array4i8
    wwxz: Array4i8
    wwxw: Array4i8
    wwyx: Array4i8
    wwyy: Array4i8
    wwyz: Array4i8
    wwyw: Array4i8
    wwzx: Array4i8
    wwzy: Array4i8
    wwzz: Array4i8
    wwzw: Array4i8
    wwwx: Array4i8
    wwwy: Array4i8
    wwwz: Array4i8
    wwww: Array4i8

_Array3u8Cp: TypeAlias = Union['Array3u8', '_UInt8Cp', 'drjit.scalar._Array3u8Cp', 'drjit.llvm._Array3u8Cp']

class Array3u8(drjit.ArrayBase[Array3u8, _Array3u8Cp, UInt8, _UInt8Cp, UInt8, Array3u8, Array3b]):
    xx: Array2u8
    xy: Array2u8
    xz: Array2u8
    xw: Array2u8
    yx: Array2u8
    yy: Array2u8
    yz: Array2u8
    yw: Array2u8
    zx: Array2u8
    zy: Array2u8
    zz: Array2u8
    zw: Array2u8
    wx: Array2u8
    wy: Array2u8
    wz: Array2u8
    ww: Array2u8
    xxx: Array3u8
    xxy: Array3u8
    xxz: Array3u8
    xxw: Array3u8
    xyx: Array3u8
    xyy: Array3u8
    xyz: Array3u8
    xyw: Array3u8
    xzx: Array3u8
    xzy: Array3u8
    xzz: Array3u8
    xzw: Array3u8
    xwx: Array3u8
    xwy: Array3u8
    xwz: Array3u8
    xww: Array3u8
    yxx: Array3u8
    yxy: Array3u8
    yxz: Array3u8
    yxw: Array3u8
    yyx: Array3u8
    yyy: Array3u8
    yyz: Array3u8
    yyw: Array3u8
    yzx: Array3u8
    yzy: Array3u8
    yzz: Array3u8
    yzw: Array3u8
    ywx: Array3u8
    ywy: Array3u8
    ywz: Array3u8
    yww: Array3u8
    zxx: Array3u8
    zxy: Array3u8
    zxz: Array3u8
    zxw: Array3u8
    zyx: Array3u8
    zyy: Array3u8
    zyz: Array3u8
    zyw: Array3u8
    zzx: Array3u8
    zzy: Array3u8
    zzz: Array3u8
    zzw: Array3u8
    zwx: Array3u8
    zwy: Array3u8
    zwz: Array3u8
    zww: Array3u8
    wxx: Array3u8
    wxy: Array3u8
    wxz: Array3u8
    wxw: Array3u8
    wyx: Array3u8
    wyy: Array3u8
    wyz: Array3u8
    wyw: Array3u8
    wzx: Array3u8
    wzy: Array3u8
    wzz: Array3u8
    wzw: Array3u8
    wwx: Array3u8
    wwy: Array3u8
    wwz: Array3u8
    www: Array3u8
    xxxx: Array4u8
    xxxy: Array4u8
    xxxz: Array4u8
    xxxw: Array4u8
    xxyx: Array4u8
    xxyy: Array4u8
    xxyz: Array4u8
    xxyw: Array4u8
    xxzx: Array4u8
    xxzy: Array4u8
    xxzz: Array4u8
    xxzw: Array4u8
    xxwx: Array4u8
    xxwy: Array4u8
    xxwz: Array4u8
    xxww: Array4u8
    xyxx: Array4u8
    xyxy: Array4u8
    xyxz: Array4u8
    xyxw: Array4u8
    xyyx: Array4u8
    xyyy: Array4u8
    xyyz: Array4u8
    xyyw: Array4u8
    xyzx: Array4u8
    xyzy: Array4u8
    xyzz: Array4u8
    xyzw: Array4u8
    xywx: Array4u8
    xywy: Array4u8
    xywz: Array4u8
    xyww: Array4u8
    xzxx: Array4u8
    xzxy: Array4u8
    xzxz: Array4u8
    xzxw: Array4u8
    xzyx: Array4u8
    xzyy: Array4u8
    xzyz: Array4u8
    xzyw: Array4u8
    xzzx: Array4u8
    xzzy: Array4u8
    xzzz: Array4u8
    xzzw: Array4u8
    xzwx: Array4u8
    xzwy: Array4u8
    xzwz: Array4u8
    xzww: Array4u8
    xwxx: Array4u8
    xwxy: Array4u8
    xwxz: Array4u8
    xwxw: Array4u8
    xwyx: Array4u8
    xwyy: Array4u8
    xwyz: Array4u8
    xwyw: Array4u8
    xwzx: Array4u8
    xwzy: Array4u8
    xwzz: Array4u8
    xwzw: Array4u8
    xwwx: Array4u8
    xwwy: Array4u8
    xwwz: Array4u8
    xwww: Array4u8
    yxxx: Array4u8
    yxxy: Array4u8
    yxxz: Array4u8
    yxxw: Array4u8
    yxyx: Array4u8
    yxyy: Array4u8
    yxyz: Array4u8
    yxyw: Array4u8
    yxzx: Array4u8
    yxzy: Array4u8
    yxzz: Array4u8
    yxzw: Array4u8
    yxwx: Array4u8
    yxwy: Array4u8
    yxwz: Array4u8
    yxww: Array4u8
    yyxx: Array4u8
    yyxy: Array4u8
    yyxz: Array4u8
    yyxw: Array4u8
    yyyx: Array4u8
    yyyy: Array4u8
    yyyz: Array4u8
    yyyw: Array4u8
    yyzx: Array4u8
    yyzy: Array4u8
    yyzz: Array4u8
    yyzw: Array4u8
    yywx: Array4u8
    yywy: Array4u8
    yywz: Array4u8
    yyww: Array4u8
    yzxx: Array4u8
    yzxy: Array4u8
    yzxz: Array4u8
    yzxw: Array4u8
    yzyx: Array4u8
    yzyy: Array4u8
    yzyz: Array4u8
    yzyw: Array4u8
    yzzx: Array4u8
    yzzy: Array4u8
    yzzz: Array4u8
    yzzw: Array4u8
    yzwx: Array4u8
    yzwy: Array4u8
    yzwz: Array4u8
    yzww: Array4u8
    ywxx: Array4u8
    ywxy: Array4u8
    ywxz: Array4u8
    ywxw: Array4u8
    ywyx: Array4u8
    ywyy: Array4u8
    ywyz: Array4u8
    ywyw: Array4u8
    ywzx: Array4u8
    ywzy: Array4u8
    ywzz: Array4u8
    ywzw: Array4u8
    ywwx: Array4u8
    ywwy: Array4u8
    ywwz: Array4u8
    ywww: Array4u8
    zxxx: Array4u8
    zxxy: Array4u8
    zxxz: Array4u8
    zxxw: Array4u8
    zxyx: Array4u8
    zxyy: Array4u8
    zxyz: Array4u8
    zxyw: Array4u8
    zxzx: Array4u8
    zxzy: Array4u8
    zxzz: Array4u8
    zxzw: Array4u8
    zxwx: Array4u8
    zxwy: Array4u8
    zxwz: Array4u8
    zxww: Array4u8
    zyxx: Array4u8
    zyxy: Array4u8
    zyxz: Array4u8
    zyxw: Array4u8
    zyyx: Array4u8
    zyyy: Array4u8
    zyyz: Array4u8
    zyyw: Array4u8
    zyzx: Array4u8
    zyzy: Array4u8
    zyzz: Array4u8
    zyzw: Array4u8
    zywx: Array4u8
    zywy: Array4u8
    zywz: Array4u8
    zyww: Array4u8
    zzxx: Array4u8
    zzxy: Array4u8
    zzxz: Array4u8
    zzxw: Array4u8
    zzyx: Array4u8
    zzyy: Array4u8
    zzyz: Array4u8
    zzyw: Array4u8
    zzzx: Array4u8
    zzzy: Array4u8
    zzzz: Array4u8
    zzzw: Array4u8
    zzwx: Array4u8
    zzwy: Array4u8
    zzwz: Array4u8
    zzww: Array4u8
    zwxx: Array4u8
    zwxy: Array4u8
    zwxz: Array4u8
    zwxw: Array4u8
    zwyx: Array4u8
    zwyy: Array4u8
    zwyz: Array4u8
    zwyw: Array4u8
    zwzx: Array4u8
    zwzy: Array4u8
    zwzz: Array4u8
    zwzw: Array4u8
    zwwx: Array4u8
    zwwy: Array4u8
    zwwz: Array4u8
    zwww: Array4u8
    wxxx: Array4u8
    wxxy: Array4u8
    wxxz: Array4u8
    wxxw: Array4u8
    wxyx: Array4u8
    wxyy: Array4u8
    wxyz: Array4u8
    wxyw: Array4u8
    wxzx: Array4u8
    wxzy: Array4u8
    wxzz: Array4u8
    wxzw: Array4u8
    wxwx: Array4u8
    wxwy: Array4u8
    wxwz: Array4u8
    wxww: Array4u8
    wyxx: Array4u8
    wyxy: Array4u8
    wyxz: Array4u8
    wyxw: Array4u8
    wyyx: Array4u8
    wyyy: Array4u8
    wyyz: Array4u8
    wyyw: Array4u8
    wyzx: Array4u8
    wyzy: Array4u8
    wyzz: Array4u8
    wyzw: Array4u8
    wywx: Array4u8
    wywy: Array4u8
    wywz: Array4u8
    wyww: Array4u8
    wzxx: Array4u8
    wzxy: Array4u8
    wzxz: Array4u8
    wzxw: Array4u8
    wzyx: Array4u8
    wzyy: Array4u8
    wzyz: Array4u8
    wzyw: Array4u8
    wzzx: Array4u8
    wzzy: Array4u8
    wzzz: Array4u8
    wzzw: Array4u8
    wzwx: Array4u8
    wzwy: Array4u8
    wzwz: Array4u8
    wzww: Array4u8
    wwxx: Array4u8
    wwxy: Array4u8
    wwxz: Array4u8
    wwxw: Array4u8
    wwyx: Array4u8
    wwyy: Array4u8
    wwyz: Array4u8
    wwyw: Array4u8
    wwzx: Array4u8
    wwzy: Array4u8
    wwzz: Array4u8
    wwzw: Array4u8
    wwwx: Array4u8
    wwwy: Array4u8
    wwwz: Array4u8
    wwww: Array4u8

_Array3iCp: TypeAlias = Union['Array3i', '_IntCp', 'drjit.scalar._Array3iCp', 'drjit.llvm._Array3iCp', '_Array3bCp']

class Array3i(drjit.ArrayBase[Array3i, _Array3iCp, Int, _IntCp, Int, Array3i, Array3b]):
    xx: Array2i
    xy: Array2i
    xz: Array2i
    xw: Array2i
    yx: Array2i
    yy: Array2i
    yz: Array2i
    yw: Array2i
    zx: Array2i
    zy: Array2i
    zz: Array2i
    zw: Array2i
    wx: Array2i
    wy: Array2i
    wz: Array2i
    ww: Array2i
    xxx: Array3i
    xxy: Array3i
    xxz: Array3i
    xxw: Array3i
    xyx: Array3i
    xyy: Array3i
    xyz: Array3i
    xyw: Array3i
    xzx: Array3i
    xzy: Array3i
    xzz: Array3i
    xzw: Array3i
    xwx: Array3i
    xwy: Array3i
    xwz: Array3i
    xww: Array3i
    yxx: Array3i
    yxy: Array3i
    yxz: Array3i
    yxw: Array3i
    yyx: Array3i
    yyy: Array3i
    yyz: Array3i
    yyw: Array3i
    yzx: Array3i
    yzy: Array3i
    yzz: Array3i
    yzw: Array3i
    ywx: Array3i
    ywy: Array3i
    ywz: Array3i
    yww: Array3i
    zxx: Array3i
    zxy: Array3i
    zxz: Array3i
    zxw: Array3i
    zyx: Array3i
    zyy: Array3i
    zyz: Array3i
    zyw: Array3i
    zzx: Array3i
    zzy: Array3i
    zzz: Array3i
    zzw: Array3i
    zwx: Array3i
    zwy: Array3i
    zwz: Array3i
    zww: Array3i
    wxx: Array3i
    wxy: Array3i
    wxz: Array3i
    wxw: Array3i
    wyx: Array3i
    wyy: Array3i
    wyz: Array3i
    wyw: Array3i
    wzx: Array3i
    wzy: Array3i
    wzz: Array3i
    wzw: Array3i
    wwx: Array3i
    wwy: Array3i
    wwz: Array3i
    www: Array3i
    xxxx: Array4i
    xxxy: Array4i
    xxxz: Array4i
    xxxw: Array4i
    xxyx: Array4i
    xxyy: Array4i
    xxyz: Array4i
    xxyw: Array4i
    xxzx: Array4i
    xxzy: Array4i
    xxzz: Array4i
    xxzw: Array4i
    xxwx: Array4i
    xxwy: Array4i
    xxwz: Array4i
    xxww: Array4i
    xyxx: Array4i
    xyxy: Array4i
    xyxz: Array4i
    xyxw: Array4i
    xyyx: Array4i
    xyyy: Array4i
    xyyz: Array4i
    xyyw: Array4i
    xyzx: Array4i
    xyzy: Array4i
    xyzz: Array4i
    xyzw: Array4i
    xywx: Array4i
    xywy: Array4i
    xywz: Array4i
    xyww: Array4i
    xzxx: Array4i
    xzxy: Array4i
    xzxz: Array4i
    xzxw: Array4i
    xzyx: Array4i
    xzyy: Array4i
    xzyz: Array4i
    xzyw: Array4i
    xzzx: Array4i
    xzzy: Array4i
    xzzz: Array4i
    xzzw: Array4i
    xzwx: Array4i
    xzwy: Array4i
    xzwz: Array4i
    xzww: Array4i
    xwxx: Array4i
    xwxy: Array4i
    xwxz: Array4i
    xwxw: Array4i
    xwyx: Array4i
    xwyy: Array4i
    xwyz: Array4i
    xwyw: Array4i
    xwzx: Array4i
    xwzy: Array4i
    xwzz: Array4i
    xwzw: Array4i
    xwwx: Array4i
    xwwy: Array4i
    xwwz: Array4i
    xwww: Array4i
    yxxx: Array4i
    yxxy: Array4i
    yxxz: Array4i
    yxxw: Array4i
    yxyx: Array4i
    yxyy: Array4i
    yxyz: Array4i
    yxyw: Array4i
    yxzx: Array4i
    yxzy: Array4i
    yxzz: Array4i
    yxzw: Array4i
    yxwx: Array4i
    yxwy: Array4i
    yxwz: Array4i
    yxww: Array4i
    yyxx: Array4i
    yyxy: Array4i
    yyxz: Array4i
    yyxw: Array4i
    yyyx: Array4i
    yyyy: Array4i
    yyyz: Array4i
    yyyw: Array4i
    yyzx: Array4i
    yyzy: Array4i
    yyzz: Array4i
    yyzw: Array4i
    yywx: Array4i
    yywy: Array4i
    yywz: Array4i
    yyww: Array4i
    yzxx: Array4i
    yzxy: Array4i
    yzxz: Array4i
    yzxw: Array4i
    yzyx: Array4i
    yzyy: Array4i
    yzyz: Array4i
    yzyw: Array4i
    yzzx: Array4i
    yzzy: Array4i
    yzzz: Array4i
    yzzw: Array4i
    yzwx: Array4i
    yzwy: Array4i
    yzwz: Array4i
    yzww: Array4i
    ywxx: Array4i
    ywxy: Array4i
    ywxz: Array4i
    ywxw: Array4i
    ywyx: Array4i
    ywyy: Array4i
    ywyz: Array4i
    ywyw: Array4i
    ywzx: Array4i
    ywzy: Array4i
    ywzz: Array4i
    ywzw: Array4i
    ywwx: Array4i
    ywwy: Array4i
    ywwz: Array4i
    ywww: Array4i
    zxxx: Array4i
    zxxy: Array4i
    zxxz: Array4i
    zxxw: Array4i
    zxyx: Array4i
    zxyy: Array4i
    zxyz: Array4i
    zxyw: Array4i
    zxzx: Array4i
    zxzy: Array4i
    zxzz: Array4i
    zxzw: Array4i
    zxwx: Array4i
    zxwy: Array4i
    zxwz: Array4i
    zxww: Array4i
    zyxx: Array4i
    zyxy: Array4i
    zyxz: Array4i
    zyxw: Array4i
    zyyx: Array4i
    zyyy: Array4i
    zyyz: Array4i
    zyyw: Array4i
    zyzx: Array4i
    zyzy: Array4i
    zyzz: Array4i
    zyzw: Array4i
    zywx: Array4i
    zywy: Array4i
    zywz: Array4i
    zyww: Array4i
    zzxx: Array4i
    zzxy: Array4i
    zzxz: Array4i
    zzxw: Array4i
    zzyx: Array4i
    zzyy: Array4i
    zzyz: Array4i
    zzyw: Array4i
    zzzx: Array4i
    zzzy: Array4i
    zzzz: Array4i
    zzzw: Array4i
    zzwx: Array4i
    zzwy: Array4i
    zzwz: Array4i
    zzww: Array4i
    zwxx: Array4i
    zwxy: Array4i
    zwxz: Array4i
    zwxw: Array4i
    zwyx: Array4i
    zwyy: Array4i
    zwyz: Array4i
    zwyw: Array4i
    zwzx: Array4i
    zwzy: Array4i
    zwzz: Array4i
    zwzw: Array4i
    zwwx: Array4i
    zwwy: Array4i
    zwwz: Array4i
    zwww: Array4i
    wxxx: Array4i
    wxxy: Array4i
    wxxz: Array4i
    wxxw: Array4i
    wxyx: Array4i
    wxyy: Array4i
    wxyz: Array4i
    wxyw: Array4i
    wxzx: Array4i
    wxzy: Array4i
    wxzz: Array4i
    wxzw: Array4i
    wxwx: Array4i
    wxwy: Array4i
    wxwz: Array4i
    wxww: Array4i
    wyxx: Array4i
    wyxy: Array4i
    wyxz: Array4i
    wyxw: Array4i
    wyyx: Array4i
    wyyy: Array4i
    wyyz: Array4i
    wyyw: Array4i
    wyzx: Array4i
    wyzy: Array4i
    wyzz: Array4i
    wyzw: Array4i
    wywx: Array4i
    wywy: Array4i
    wywz: Array4i
    wyww: Array4i
    wzxx: Array4i
    wzxy: Array4i
    wzxz: Array4i
    wzxw: Array4i
    wzyx: Array4i
    wzyy: Array4i
    wzyz: Array4i
    wzyw: Array4i
    wzzx: Array4i
    wzzy: Array4i
    wzzz: Array4i
    wzzw: Array4i
    wzwx: Array4i
    wzwy: Array4i
    wzwz: Array4i
    wzww: Array4i
    wwxx: Array4i
    wwxy: Array4i
    wwxz: Array4i
    wwxw: Array4i
    wwyx: Array4i
    wwyy: Array4i
    wwyz: Array4i
    wwyw: Array4i
    wwzx: Array4i
    wwzy: Array4i
    wwzz: Array4i
    wwzw: Array4i
    wwwx: Array4i
    wwwy: Array4i
    wwwz: Array4i
    wwww: Array4i

_Array3uCp: TypeAlias = Union['Array3u', '_UIntCp', 'drjit.scalar._Array3uCp', 'drjit.llvm._Array3uCp', '_Array3iCp']

class Array3u(drjit.ArrayBase[Array3u, _Array3uCp, UInt, _UIntCp, UInt, Array3u, Array3b]):
    xx: Array2u
    xy: Array2u
    xz: Array2u
    xw: Array2u
    yx: Array2u
    yy: Array2u
    yz: Array2u
    yw: Array2u
    zx: Array2u
    zy: Array2u
    zz: Array2u
    zw: Array2u
    wx: Array2u
    wy: Array2u
    wz: Array2u
    ww: Array2u
    xxx: Array3u
    xxy: Array3u
    xxz: Array3u
    xxw: Array3u
    xyx: Array3u
    xyy: Array3u
    xyz: Array3u
    xyw: Array3u
    xzx: Array3u
    xzy: Array3u
    xzz: Array3u
    xzw: Array3u
    xwx: Array3u
    xwy: Array3u
    xwz: Array3u
    xww: Array3u
    yxx: Array3u
    yxy: Array3u
    yxz: Array3u
    yxw: Array3u
    yyx: Array3u
    yyy: Array3u
    yyz: Array3u
    yyw: Array3u
    yzx: Array3u
    yzy: Array3u
    yzz: Array3u
    yzw: Array3u
    ywx: Array3u
    ywy: Array3u
    ywz: Array3u
    yww: Array3u
    zxx: Array3u
    zxy: Array3u
    zxz: Array3u
    zxw: Array3u
    zyx: Array3u
    zyy: Array3u
    zyz: Array3u
    zyw: Array3u
    zzx: Array3u
    zzy: Array3u
    zzz: Array3u
    zzw: Array3u
    zwx: Array3u
    zwy: Array3u
    zwz: Array3u
    zww: Array3u
    wxx: Array3u
    wxy: Array3u
    wxz: Array3u
    wxw: Array3u
    wyx: Array3u
    wyy: Array3u
    wyz: Array3u
    wyw: Array3u
    wzx: Array3u
    wzy: Array3u
    wzz: Array3u
    wzw: Array3u
    wwx: Array3u
    wwy: Array3u
    wwz: Array3u
    www: Array3u
    xxxx: Array4u
    xxxy: Array4u
    xxxz: Array4u
    xxxw: Array4u
    xxyx: Array4u
    xxyy: Array4u
    xxyz: Array4u
    xxyw: Array4u
    xxzx: Array4u
    xxzy: Array4u
    xxzz: Array4u
    xxzw: Array4u
    xxwx: Array4u
    xxwy: Array4u
    xxwz: Array4u
    xxww: Array4u
    xyxx: Array4u
    xyxy: Array4u
    xyxz: Array4u
    xyxw: Array4u
    xyyx: Array4u
    xyyy: Array4u
    xyyz: Array4u
    xyyw: Array4u
    xyzx: Array4u
    xyzy: Array4u
    xyzz: Array4u
    xyzw: Array4u
    xywx: Array4u
    xywy: Array4u
    xywz: Array4u
    xyww: Array4u
    xzxx: Array4u
    xzxy: Array4u
    xzxz: Array4u
    xzxw: Array4u
    xzyx: Array4u
    xzyy: Array4u
    xzyz: Array4u
    xzyw: Array4u
    xzzx: Array4u
    xzzy: Array4u
    xzzz: Array4u
    xzzw: Array4u
    xzwx: Array4u
    xzwy: Array4u
    xzwz: Array4u
    xzww: Array4u
    xwxx: Array4u
    xwxy: Array4u
    xwxz: Array4u
    xwxw: Array4u
    xwyx: Array4u
    xwyy: Array4u
    xwyz: Array4u
    xwyw: Array4u
    xwzx: Array4u
    xwzy: Array4u
    xwzz: Array4u
    xwzw: Array4u
    xwwx: Array4u
    xwwy: Array4u
    xwwz: Array4u
    xwww: Array4u
    yxxx: Array4u
    yxxy: Array4u
    yxxz: Array4u
    yxxw: Array4u
    yxyx: Array4u
    yxyy: Array4u
    yxyz: Array4u
    yxyw: Array4u
    yxzx: Array4u
    yxzy: Array4u
    yxzz: Array4u
    yxzw: Array4u
    yxwx: Array4u
    yxwy: Array4u
    yxwz: Array4u
    yxww: Array4u
    yyxx: Array4u
    yyxy: Array4u
    yyxz: Array4u
    yyxw: Array4u
    yyyx: Array4u
    yyyy: Array4u
    yyyz: Array4u
    yyyw: Array4u
    yyzx: Array4u
    yyzy: Array4u
    yyzz: Array4u
    yyzw: Array4u
    yywx: Array4u
    yywy: Array4u
    yywz: Array4u
    yyww: Array4u
    yzxx: Array4u
    yzxy: Array4u
    yzxz: Array4u
    yzxw: Array4u
    yzyx: Array4u
    yzyy: Array4u
    yzyz: Array4u
    yzyw: Array4u
    yzzx: Array4u
    yzzy: Array4u
    yzzz: Array4u
    yzzw: Array4u
    yzwx: Array4u
    yzwy: Array4u
    yzwz: Array4u
    yzww: Array4u
    ywxx: Array4u
    ywxy: Array4u
    ywxz: Array4u
    ywxw: Array4u
    ywyx: Array4u
    ywyy: Array4u
    ywyz: Array4u
    ywyw: Array4u
    ywzx: Array4u
    ywzy: Array4u
    ywzz: Array4u
    ywzw: Array4u
    ywwx: Array4u
    ywwy: Array4u
    ywwz: Array4u
    ywww: Array4u
    zxxx: Array4u
    zxxy: Array4u
    zxxz: Array4u
    zxxw: Array4u
    zxyx: Array4u
    zxyy: Array4u
    zxyz: Array4u
    zxyw: Array4u
    zxzx: Array4u
    zxzy: Array4u
    zxzz: Array4u
    zxzw: Array4u
    zxwx: Array4u
    zxwy: Array4u
    zxwz: Array4u
    zxww: Array4u
    zyxx: Array4u
    zyxy: Array4u
    zyxz: Array4u
    zyxw: Array4u
    zyyx: Array4u
    zyyy: Array4u
    zyyz: Array4u
    zyyw: Array4u
    zyzx: Array4u
    zyzy: Array4u
    zyzz: Array4u
    zyzw: Array4u
    zywx: Array4u
    zywy: Array4u
    zywz: Array4u
    zyww: Array4u
    zzxx: Array4u
    zzxy: Array4u
    zzxz: Array4u
    zzxw: Array4u
    zzyx: Array4u
    zzyy: Array4u
    zzyz: Array4u
    zzyw: Array4u
    zzzx: Array4u
    zzzy: Array4u
    zzzz: Array4u
    zzzw: Array4u
    zzwx: Array4u
    zzwy: Array4u
    zzwz: Array4u
    zzww: Array4u
    zwxx: Array4u
    zwxy: Array4u
    zwxz: Array4u
    zwxw: Array4u
    zwyx: Array4u
    zwyy: Array4u
    zwyz: Array4u
    zwyw: Array4u
    zwzx: Array4u
    zwzy: Array4u
    zwzz: Array4u
    zwzw: Array4u
    zwwx: Array4u
    zwwy: Array4u
    zwwz: Array4u
    zwww: Array4u
    wxxx: Array4u
    wxxy: Array4u
    wxxz: Array4u
    wxxw: Array4u
    wxyx: Array4u
    wxyy: Array4u
    wxyz: Array4u
    wxyw: Array4u
    wxzx: Array4u
    wxzy: Array4u
    wxzz: Array4u
    wxzw: Array4u
    wxwx: Array4u
    wxwy: Array4u
    wxwz: Array4u
    wxww: Array4u
    wyxx: Array4u
    wyxy: Array4u
    wyxz: Array4u
    wyxw: Array4u
    wyyx: Array4u
    wyyy: Array4u
    wyyz: Array4u
    wyyw: Array4u
    wyzx: Array4u
    wyzy: Array4u
    wyzz: Array4u
    wyzw: Array4u
    wywx: Array4u
    wywy: Array4u
    wywz: Array4u
    wyww: Array4u
    wzxx: Array4u
    wzxy: Array4u
    wzxz: Array4u
    wzxw: Array4u
    wzyx: Array4u
    wzyy: Array4u
    wzyz: Array4u
    wzyw: Array4u
    wzzx: Array4u
    wzzy: Array4u
    wzzz: Array4u
    wzzw: Array4u
    wzwx: Array4u
    wzwy: Array4u
    wzwz: Array4u
    wzww: Array4u
    wwxx: Array4u
    wwxy: Array4u
    wwxz: Array4u
    wwxw: Array4u
    wwyx: Array4u
    wwyy: Array4u
    wwyz: Array4u
    wwyw: Array4u
    wwzx: Array4u
    wwzy: Array4u
    wwzz: Array4u
    wwzw: Array4u
    wwwx: Array4u
    wwwy: Array4u
    wwwz: Array4u
    wwww: Array4u

_Array3i64Cp: TypeAlias = Union['Array3i64', '_Int64Cp', 'drjit.scalar._Array3i64Cp', 'drjit.llvm._Array3i64Cp', '_Array3uCp']

class Array3i64(drjit.ArrayBase[Array3i64, _Array3i64Cp, Int64, _Int64Cp, Int64, Array3i64, Array3b]):
    xx: Array2i64
    xy: Array2i64
    xz: Array2i64
    xw: Array2i64
    yx: Array2i64
    yy: Array2i64
    yz: Array2i64
    yw: Array2i64
    zx: Array2i64
    zy: Array2i64
    zz: Array2i64
    zw: Array2i64
    wx: Array2i64
    wy: Array2i64
    wz: Array2i64
    ww: Array2i64
    xxx: Array3i64
    xxy: Array3i64
    xxz: Array3i64
    xxw: Array3i64
    xyx: Array3i64
    xyy: Array3i64
    xyz: Array3i64
    xyw: Array3i64
    xzx: Array3i64
    xzy: Array3i64
    xzz: Array3i64
    xzw: Array3i64
    xwx: Array3i64
    xwy: Array3i64
    xwz: Array3i64
    xww: Array3i64
    yxx: Array3i64
    yxy: Array3i64
    yxz: Array3i64
    yxw: Array3i64
    yyx: Array3i64
    yyy: Array3i64
    yyz: Array3i64
    yyw: Array3i64
    yzx: Array3i64
    yzy: Array3i64
    yzz: Array3i64
    yzw: Array3i64
    ywx: Array3i64
    ywy: Array3i64
    ywz: Array3i64
    yww: Array3i64
    zxx: Array3i64
    zxy: Array3i64
    zxz: Array3i64
    zxw: Array3i64
    zyx: Array3i64
    zyy: Array3i64
    zyz: Array3i64
    zyw: Array3i64
    zzx: Array3i64
    zzy: Array3i64
    zzz: Array3i64
    zzw: Array3i64
    zwx: Array3i64
    zwy: Array3i64
    zwz: Array3i64
    zww: Array3i64
    wxx: Array3i64
    wxy: Array3i64
    wxz: Array3i64
    wxw: Array3i64
    wyx: Array3i64
    wyy: Array3i64
    wyz: Array3i64
    wyw: Array3i64
    wzx: Array3i64
    wzy: Array3i64
    wzz: Array3i64
    wzw: Array3i64
    wwx: Array3i64
    wwy: Array3i64
    wwz: Array3i64
    www: Array3i64
    xxxx: Array4i64
    xxxy: Array4i64
    xxxz: Array4i64
    xxxw: Array4i64
    xxyx: Array4i64
    xxyy: Array4i64
    xxyz: Array4i64
    xxyw: Array4i64
    xxzx: Array4i64
    xxzy: Array4i64
    xxzz: Array4i64
    xxzw: Array4i64
    xxwx: Array4i64
    xxwy: Array4i64
    xxwz: Array4i64
    xxww: Array4i64
    xyxx: Array4i64
    xyxy: Array4i64
    xyxz: Array4i64
    xyxw: Array4i64
    xyyx: Array4i64
    xyyy: Array4i64
    xyyz: Array4i64
    xyyw: Array4i64
    xyzx: Array4i64
    xyzy: Array4i64
    xyzz: Array4i64
    xyzw: Array4i64
    xywx: Array4i64
    xywy: Array4i64
    xywz: Array4i64
    xyww: Array4i64
    xzxx: Array4i64
    xzxy: Array4i64
    xzxz: Array4i64
    xzxw: Array4i64
    xzyx: Array4i64
    xzyy: Array4i64
    xzyz: Array4i64
    xzyw: Array4i64
    xzzx: Array4i64
    xzzy: Array4i64
    xzzz: Array4i64
    xzzw: Array4i64
    xzwx: Array4i64
    xzwy: Array4i64
    xzwz: Array4i64
    xzww: Array4i64
    xwxx: Array4i64
    xwxy: Array4i64
    xwxz: Array4i64
    xwxw: Array4i64
    xwyx: Array4i64
    xwyy: Array4i64
    xwyz: Array4i64
    xwyw: Array4i64
    xwzx: Array4i64
    xwzy: Array4i64
    xwzz: Array4i64
    xwzw: Array4i64
    xwwx: Array4i64
    xwwy: Array4i64
    xwwz: Array4i64
    xwww: Array4i64
    yxxx: Array4i64
    yxxy: Array4i64
    yxxz: Array4i64
    yxxw: Array4i64
    yxyx: Array4i64
    yxyy: Array4i64
    yxyz: Array4i64
    yxyw: Array4i64
    yxzx: Array4i64
    yxzy: Array4i64
    yxzz: Array4i64
    yxzw: Array4i64
    yxwx: Array4i64
    yxwy: Array4i64
    yxwz: Array4i64
    yxww: Array4i64
    yyxx: Array4i64
    yyxy: Array4i64
    yyxz: Array4i64
    yyxw: Array4i64
    yyyx: Array4i64
    yyyy: Array4i64
    yyyz: Array4i64
    yyyw: Array4i64
    yyzx: Array4i64
    yyzy: Array4i64
    yyzz: Array4i64
    yyzw: Array4i64
    yywx: Array4i64
    yywy: Array4i64
    yywz: Array4i64
    yyww: Array4i64
    yzxx: Array4i64
    yzxy: Array4i64
    yzxz: Array4i64
    yzxw: Array4i64
    yzyx: Array4i64
    yzyy: Array4i64
    yzyz: Array4i64
    yzyw: Array4i64
    yzzx: Array4i64
    yzzy: Array4i64
    yzzz: Array4i64
    yzzw: Array4i64
    yzwx: Array4i64
    yzwy: Array4i64
    yzwz: Array4i64
    yzww: Array4i64
    ywxx: Array4i64
    ywxy: Array4i64
    ywxz: Array4i64
    ywxw: Array4i64
    ywyx: Array4i64
    ywyy: Array4i64
    ywyz: Array4i64
    ywyw: Array4i64
    ywzx: Array4i64
    ywzy: Array4i64
    ywzz: Array4i64
    ywzw: Array4i64
    ywwx: Array4i64
    ywwy: Array4i64
    ywwz: Array4i64
    ywww: Array4i64
    zxxx: Array4i64
    zxxy: Array4i64
    zxxz: Array4i64
    zxxw: Array4i64
    zxyx: Array4i64
    zxyy: Array4i64
    zxyz: Array4i64
    zxyw: Array4i64
    zxzx: Array4i64
    zxzy: Array4i64
    zxzz: Array4i64
    zxzw: Array4i64
    zxwx: Array4i64
    zxwy: Array4i64
    zxwz: Array4i64
    zxww: Array4i64
    zyxx: Array4i64
    zyxy: Array4i64
    zyxz: Array4i64
    zyxw: Array4i64
    zyyx: Array4i64
    zyyy: Array4i64
    zyyz: Array4i64
    zyyw: Array4i64
    zyzx: Array4i64
    zyzy: Array4i64
    zyzz: Array4i64
    zyzw: Array4i64
    zywx: Array4i64
    zywy: Array4i64
    zywz: Array4i64
    zyww: Array4i64
    zzxx: Array4i64
    zzxy: Array4i64
    zzxz: Array4i64
    zzxw: Array4i64
    zzyx: Array4i64
    zzyy: Array4i64
    zzyz: Array4i64
    zzyw: Array4i64
    zzzx: Array4i64
    zzzy: Array4i64
    zzzz: Array4i64
    zzzw: Array4i64
    zzwx: Array4i64
    zzwy: Array4i64
    zzwz: Array4i64
    zzww: Array4i64
    zwxx: Array4i64
    zwxy: Array4i64
    zwxz: Array4i64
    zwxw: Array4i64
    zwyx: Array4i64
    zwyy: Array4i64
    zwyz: Array4i64
    zwyw: Array4i64
    zwzx: Array4i64
    zwzy: Array4i64
    zwzz: Array4i64
    zwzw: Array4i64
    zwwx: Array4i64
    zwwy: Array4i64
    zwwz: Array4i64
    zwww: Array4i64
    wxxx: Array4i64
    wxxy: Array4i64
    wxxz: Array4i64
    wxxw: Array4i64
    wxyx: Array4i64
    wxyy: Array4i64
    wxyz: Array4i64
    wxyw: Array4i64
    wxzx: Array4i64
    wxzy: Array4i64
    wxzz: Array4i64
    wxzw: Array4i64
    wxwx: Array4i64
    wxwy: Array4i64
    wxwz: Array4i64
    wxww: Array4i64
    wyxx: Array4i64
    wyxy: Array4i64
    wyxz: Array4i64
    wyxw: Array4i64
    wyyx: Array4i64
    wyyy: Array4i64
    wyyz: Array4i64
    wyyw: Array4i64
    wyzx: Array4i64
    wyzy: Array4i64
    wyzz: Array4i64
    wyzw: Array4i64
    wywx: Array4i64
    wywy: Array4i64
    wywz: Array4i64
    wyww: Array4i64
    wzxx: Array4i64
    wzxy: Array4i64
    wzxz: Array4i64
    wzxw: Array4i64
    wzyx: Array4i64
    wzyy: Array4i64
    wzyz: Array4i64
    wzyw: Array4i64
    wzzx: Array4i64
    wzzy: Array4i64
    wzzz: Array4i64
    wzzw: Array4i64
    wzwx: Array4i64
    wzwy: Array4i64
    wzwz: Array4i64
    wzww: Array4i64
    wwxx: Array4i64
    wwxy: Array4i64
    wwxz: Array4i64
    wwxw: Array4i64
    wwyx: Array4i64
    wwyy: Array4i64
    wwyz: Array4i64
    wwyw: Array4i64
    wwzx: Array4i64
    wwzy: Array4i64
    wwzz: Array4i64
    wwzw: Array4i64
    wwwx: Array4i64
    wwwy: Array4i64
    wwwz: Array4i64
    wwww: Array4i64

_Array3u64Cp: TypeAlias = Union['Array3u64', '_UInt64Cp', 'drjit.scalar._Array3u64Cp', 'drjit.llvm._Array3u64Cp', '_Array3i64Cp']

class Array3u64(drjit.ArrayBase[Array3u64, _Array3u64Cp, UInt64, _UInt64Cp, UInt64, Array3u64, Array3b]):
    xx: Array2u64
    xy: Array2u64
    xz: Array2u64
    xw: Array2u64
    yx: Array2u64
    yy: Array2u64
    yz: Array2u64
    yw: Array2u64
    zx: Array2u64
    zy: Array2u64
    zz: Array2u64
    zw: Array2u64
    wx: Array2u64
    wy: Array2u64
    wz: Array2u64
    ww: Array2u64
    xxx: Array3u64
    xxy: Array3u64
    xxz: Array3u64
    xxw: Array3u64
    xyx: Array3u64
    xyy: Array3u64
    xyz: Array3u64
    xyw: Array3u64
    xzx: Array3u64
    xzy: Array3u64
    xzz: Array3u64
    xzw: Array3u64
    xwx: Array3u64
    xwy: Array3u64
    xwz: Array3u64
    xww: Array3u64
    yxx: Array3u64
    yxy: Array3u64
    yxz: Array3u64
    yxw: Array3u64
    yyx: Array3u64
    yyy: Array3u64
    yyz: Array3u64
    yyw: Array3u64
    yzx: Array3u64
    yzy: Array3u64
    yzz: Array3u64
    yzw: Array3u64
    ywx: Array3u64
    ywy: Array3u64
    ywz: Array3u64
    yww: Array3u64
    zxx: Array3u64
    zxy: Array3u64
    zxz: Array3u64
    zxw: Array3u64
    zyx: Array3u64
    zyy: Array3u64
    zyz: Array3u64
    zyw: Array3u64
    zzx: Array3u64
    zzy: Array3u64
    zzz: Array3u64
    zzw: Array3u64
    zwx: Array3u64
    zwy: Array3u64
    zwz: Array3u64
    zww: Array3u64
    wxx: Array3u64
    wxy: Array3u64
    wxz: Array3u64
    wxw: Array3u64
    wyx: Array3u64
    wyy: Array3u64
    wyz: Array3u64
    wyw: Array3u64
    wzx: Array3u64
    wzy: Array3u64
    wzz: Array3u64
    wzw: Array3u64
    wwx: Array3u64
    wwy: Array3u64
    wwz: Array3u64
    www: Array3u64
    xxxx: Array4u64
    xxxy: Array4u64
    xxxz: Array4u64
    xxxw: Array4u64
    xxyx: Array4u64
    xxyy: Array4u64
    xxyz: Array4u64
    xxyw: Array4u64
    xxzx: Array4u64
    xxzy: Array4u64
    xxzz: Array4u64
    xxzw: Array4u64
    xxwx: Array4u64
    xxwy: Array4u64
    xxwz: Array4u64
    xxww: Array4u64
    xyxx: Array4u64
    xyxy: Array4u64
    xyxz: Array4u64
    xyxw: Array4u64
    xyyx: Array4u64
    xyyy: Array4u64
    xyyz: Array4u64
    xyyw: Array4u64
    xyzx: Array4u64
    xyzy: Array4u64
    xyzz: Array4u64
    xyzw: Array4u64
    xywx: Array4u64
    xywy: Array4u64
    xywz: Array4u64
    xyww: Array4u64
    xzxx: Array4u64
    xzxy: Array4u64
    xzxz: Array4u64
    xzxw: Array4u64
    xzyx: Array4u64
    xzyy: Array4u64
    xzyz: Array4u64
    xzyw: Array4u64
    xzzx: Array4u64
    xzzy: Array4u64
    xzzz: Array4u64
    xzzw: Array4u64
    xzwx: Array4u64
    xzwy: Array4u64
    xzwz: Array4u64
    xzww: Array4u64
    xwxx: Array4u64
    xwxy: Array4u64
    xwxz: Array4u64
    xwxw: Array4u64
    xwyx: Array4u64
    xwyy: Array4u64
    xwyz: Array4u64
    xwyw: Array4u64
    xwzx: Array4u64
    xwzy: Array4u64
    xwzz: Array4u64
    xwzw: Array4u64
    xwwx: Array4u64
    xwwy: Array4u64
    xwwz: Array4u64
    xwww: Array4u64
    yxxx: Array4u64
    yxxy: Array4u64
    yxxz: Array4u64
    yxxw: Array4u64
    yxyx: Array4u64
    yxyy: Array4u64
    yxyz: Array4u64
    yxyw: Array4u64
    yxzx: Array4u64
    yxzy: Array4u64
    yxzz: Array4u64
    yxzw: Array4u64
    yxwx: Array4u64
    yxwy: Array4u64
    yxwz: Array4u64
    yxww: Array4u64
    yyxx: Array4u64
    yyxy: Array4u64
    yyxz: Array4u64
    yyxw: Array4u64
    yyyx: Array4u64
    yyyy: Array4u64
    yyyz: Array4u64
    yyyw: Array4u64
    yyzx: Array4u64
    yyzy: Array4u64
    yyzz: Array4u64
    yyzw: Array4u64
    yywx: Array4u64
    yywy: Array4u64
    yywz: Array4u64
    yyww: Array4u64
    yzxx: Array4u64
    yzxy: Array4u64
    yzxz: Array4u64
    yzxw: Array4u64
    yzyx: Array4u64
    yzyy: Array4u64
    yzyz: Array4u64
    yzyw: Array4u64
    yzzx: Array4u64
    yzzy: Array4u64
    yzzz: Array4u64
    yzzw: Array4u64
    yzwx: Array4u64
    yzwy: Array4u64
    yzwz: Array4u64
    yzww: Array4u64
    ywxx: Array4u64
    ywxy: Array4u64
    ywxz: Array4u64
    ywxw: Array4u64
    ywyx: Array4u64
    ywyy: Array4u64
    ywyz: Array4u64
    ywyw: Array4u64
    ywzx: Array4u64
    ywzy: Array4u64
    ywzz: Array4u64
    ywzw: Array4u64
    ywwx: Array4u64
    ywwy: Array4u64
    ywwz: Array4u64
    ywww: Array4u64
    zxxx: Array4u64
    zxxy: Array4u64
    zxxz: Array4u64
    zxxw: Array4u64
    zxyx: Array4u64
    zxyy: Array4u64
    zxyz: Array4u64
    zxyw: Array4u64
    zxzx: Array4u64
    zxzy: Array4u64
    zxzz: Array4u64
    zxzw: Array4u64
    zxwx: Array4u64
    zxwy: Array4u64
    zxwz: Array4u64
    zxww: Array4u64
    zyxx: Array4u64
    zyxy: Array4u64
    zyxz: Array4u64
    zyxw: Array4u64
    zyyx: Array4u64
    zyyy: Array4u64
    zyyz: Array4u64
    zyyw: Array4u64
    zyzx: Array4u64
    zyzy: Array4u64
    zyzz: Array4u64
    zyzw: Array4u64
    zywx: Array4u64
    zywy: Array4u64
    zywz: Array4u64
    zyww: Array4u64
    zzxx: Array4u64
    zzxy: Array4u64
    zzxz: Array4u64
    zzxw: Array4u64
    zzyx: Array4u64
    zzyy: Array4u64
    zzyz: Array4u64
    zzyw: Array4u64
    zzzx: Array4u64
    zzzy: Array4u64
    zzzz: Array4u64
    zzzw: Array4u64
    zzwx: Array4u64
    zzwy: Array4u64
    zzwz: Array4u64
    zzww: Array4u64
    zwxx: Array4u64
    zwxy: Array4u64
    zwxz: Array4u64
    zwxw: Array4u64
    zwyx: Array4u64
    zwyy: Array4u64
    zwyz: Array4u64
    zwyw: Array4u64
    zwzx: Array4u64
    zwzy: Array4u64
    zwzz: Array4u64
    zwzw: Array4u64
    zwwx: Array4u64
    zwwy: Array4u64
    zwwz: Array4u64
    zwww: Array4u64
    wxxx: Array4u64
    wxxy: Array4u64
    wxxz: Array4u64
    wxxw: Array4u64
    wxyx: Array4u64
    wxyy: Array4u64
    wxyz: Array4u64
    wxyw: Array4u64
    wxzx: Array4u64
    wxzy: Array4u64
    wxzz: Array4u64
    wxzw: Array4u64
    wxwx: Array4u64
    wxwy: Array4u64
    wxwz: Array4u64
    wxww: Array4u64
    wyxx: Array4u64
    wyxy: Array4u64
    wyxz: Array4u64
    wyxw: Array4u64
    wyyx: Array4u64
    wyyy: Array4u64
    wyyz: Array4u64
    wyyw: Array4u64
    wyzx: Array4u64
    wyzy: Array4u64
    wyzz: Array4u64
    wyzw: Array4u64
    wywx: Array4u64
    wywy: Array4u64
    wywz: Array4u64
    wyww: Array4u64
    wzxx: Array4u64
    wzxy: Array4u64
    wzxz: Array4u64
    wzxw: Array4u64
    wzyx: Array4u64
    wzyy: Array4u64
    wzyz: Array4u64
    wzyw: Array4u64
    wzzx: Array4u64
    wzzy: Array4u64
    wzzz: Array4u64
    wzzw: Array4u64
    wzwx: Array4u64
    wzwy: Array4u64
    wzwz: Array4u64
    wzww: Array4u64
    wwxx: Array4u64
    wwxy: Array4u64
    wwxz: Array4u64
    wwxw: Array4u64
    wwyx: Array4u64
    wwyy: Array4u64
    wwyz: Array4u64
    wwyw: Array4u64
    wwzx: Array4u64
    wwzy: Array4u64
    wwzz: Array4u64
    wwzw: Array4u64
    wwwx: Array4u64
    wwwy: Array4u64
    wwwz: Array4u64
    wwww: Array4u64

_Array3f16Cp: TypeAlias = Union['Array3f16', '_Float16Cp', 'drjit.scalar._Array3f16Cp', 'drjit.llvm._Array3f16Cp', '_Array3u64Cp']

class Array3f16(drjit.ArrayBase[Array3f16, _Array3f16Cp, Float16, _Float16Cp, Float16, Array3f16, Array3b]):
    xx: Array2f16
    xy: Array2f16
    xz: Array2f16
    xw: Array2f16
    yx: Array2f16
    yy: Array2f16
    yz: Array2f16
    yw: Array2f16
    zx: Array2f16
    zy: Array2f16
    zz: Array2f16
    zw: Array2f16
    wx: Array2f16
    wy: Array2f16
    wz: Array2f16
    ww: Array2f16
    xxx: Array3f16
    xxy: Array3f16
    xxz: Array3f16
    xxw: Array3f16
    xyx: Array3f16
    xyy: Array3f16
    xyz: Array3f16
    xyw: Array3f16
    xzx: Array3f16
    xzy: Array3f16
    xzz: Array3f16
    xzw: Array3f16
    xwx: Array3f16
    xwy: Array3f16
    xwz: Array3f16
    xww: Array3f16
    yxx: Array3f16
    yxy: Array3f16
    yxz: Array3f16
    yxw: Array3f16
    yyx: Array3f16
    yyy: Array3f16
    yyz: Array3f16
    yyw: Array3f16
    yzx: Array3f16
    yzy: Array3f16
    yzz: Array3f16
    yzw: Array3f16
    ywx: Array3f16
    ywy: Array3f16
    ywz: Array3f16
    yww: Array3f16
    zxx: Array3f16
    zxy: Array3f16
    zxz: Array3f16
    zxw: Array3f16
    zyx: Array3f16
    zyy: Array3f16
    zyz: Array3f16
    zyw: Array3f16
    zzx: Array3f16
    zzy: Array3f16
    zzz: Array3f16
    zzw: Array3f16
    zwx: Array3f16
    zwy: Array3f16
    zwz: Array3f16
    zww: Array3f16
    wxx: Array3f16
    wxy: Array3f16
    wxz: Array3f16
    wxw: Array3f16
    wyx: Array3f16
    wyy: Array3f16
    wyz: Array3f16
    wyw: Array3f16
    wzx: Array3f16
    wzy: Array3f16
    wzz: Array3f16
    wzw: Array3f16
    wwx: Array3f16
    wwy: Array3f16
    wwz: Array3f16
    www: Array3f16
    xxxx: Array4f16
    xxxy: Array4f16
    xxxz: Array4f16
    xxxw: Array4f16
    xxyx: Array4f16
    xxyy: Array4f16
    xxyz: Array4f16
    xxyw: Array4f16
    xxzx: Array4f16
    xxzy: Array4f16
    xxzz: Array4f16
    xxzw: Array4f16
    xxwx: Array4f16
    xxwy: Array4f16
    xxwz: Array4f16
    xxww: Array4f16
    xyxx: Array4f16
    xyxy: Array4f16
    xyxz: Array4f16
    xyxw: Array4f16
    xyyx: Array4f16
    xyyy: Array4f16
    xyyz: Array4f16
    xyyw: Array4f16
    xyzx: Array4f16
    xyzy: Array4f16
    xyzz: Array4f16
    xyzw: Array4f16
    xywx: Array4f16
    xywy: Array4f16
    xywz: Array4f16
    xyww: Array4f16
    xzxx: Array4f16
    xzxy: Array4f16
    xzxz: Array4f16
    xzxw: Array4f16
    xzyx: Array4f16
    xzyy: Array4f16
    xzyz: Array4f16
    xzyw: Array4f16
    xzzx: Array4f16
    xzzy: Array4f16
    xzzz: Array4f16
    xzzw: Array4f16
    xzwx: Array4f16
    xzwy: Array4f16
    xzwz: Array4f16
    xzww: Array4f16
    xwxx: Array4f16
    xwxy: Array4f16
    xwxz: Array4f16
    xwxw: Array4f16
    xwyx: Array4f16
    xwyy: Array4f16
    xwyz: Array4f16
    xwyw: Array4f16
    xwzx: Array4f16
    xwzy: Array4f16
    xwzz: Array4f16
    xwzw: Array4f16
    xwwx: Array4f16
    xwwy: Array4f16
    xwwz: Array4f16
    xwww: Array4f16
    yxxx: Array4f16
    yxxy: Array4f16
    yxxz: Array4f16
    yxxw: Array4f16
    yxyx: Array4f16
    yxyy: Array4f16
    yxyz: Array4f16
    yxyw: Array4f16
    yxzx: Array4f16
    yxzy: Array4f16
    yxzz: Array4f16
    yxzw: Array4f16
    yxwx: Array4f16
    yxwy: Array4f16
    yxwz: Array4f16
    yxww: Array4f16
    yyxx: Array4f16
    yyxy: Array4f16
    yyxz: Array4f16
    yyxw: Array4f16
    yyyx: Array4f16
    yyyy: Array4f16
    yyyz: Array4f16
    yyyw: Array4f16
    yyzx: Array4f16
    yyzy: Array4f16
    yyzz: Array4f16
    yyzw: Array4f16
    yywx: Array4f16
    yywy: Array4f16
    yywz: Array4f16
    yyww: Array4f16
    yzxx: Array4f16
    yzxy: Array4f16
    yzxz: Array4f16
    yzxw: Array4f16
    yzyx: Array4f16
    yzyy: Array4f16
    yzyz: Array4f16
    yzyw: Array4f16
    yzzx: Array4f16
    yzzy: Array4f16
    yzzz: Array4f16
    yzzw: Array4f16
    yzwx: Array4f16
    yzwy: Array4f16
    yzwz: Array4f16
    yzww: Array4f16
    ywxx: Array4f16
    ywxy: Array4f16
    ywxz: Array4f16
    ywxw: Array4f16
    ywyx: Array4f16
    ywyy: Array4f16
    ywyz: Array4f16
    ywyw: Array4f16
    ywzx: Array4f16
    ywzy: Array4f16
    ywzz: Array4f16
    ywzw: Array4f16
    ywwx: Array4f16
    ywwy: Array4f16
    ywwz: Array4f16
    ywww: Array4f16
    zxxx: Array4f16
    zxxy: Array4f16
    zxxz: Array4f16
    zxxw: Array4f16
    zxyx: Array4f16
    zxyy: Array4f16
    zxyz: Array4f16
    zxyw: Array4f16
    zxzx: Array4f16
    zxzy: Array4f16
    zxzz: Array4f16
    zxzw: Array4f16
    zxwx: Array4f16
    zxwy: Array4f16
    zxwz: Array4f16
    zxww: Array4f16
    zyxx: Array4f16
    zyxy: Array4f16
    zyxz: Array4f16
    zyxw: Array4f16
    zyyx: Array4f16
    zyyy: Array4f16
    zyyz: Array4f16
    zyyw: Array4f16
    zyzx: Array4f16
    zyzy: Array4f16
    zyzz: Array4f16
    zyzw: Array4f16
    zywx: Array4f16
    zywy: Array4f16
    zywz: Array4f16
    zyww: Array4f16
    zzxx: Array4f16
    zzxy: Array4f16
    zzxz: Array4f16
    zzxw: Array4f16
    zzyx: Array4f16
    zzyy: Array4f16
    zzyz: Array4f16
    zzyw: Array4f16
    zzzx: Array4f16
    zzzy: Array4f16
    zzzz: Array4f16
    zzzw: Array4f16
    zzwx: Array4f16
    zzwy: Array4f16
    zzwz: Array4f16
    zzww: Array4f16
    zwxx: Array4f16
    zwxy: Array4f16
    zwxz: Array4f16
    zwxw: Array4f16
    zwyx: Array4f16
    zwyy: Array4f16
    zwyz: Array4f16
    zwyw: Array4f16
    zwzx: Array4f16
    zwzy: Array4f16
    zwzz: Array4f16
    zwzw: Array4f16
    zwwx: Array4f16
    zwwy: Array4f16
    zwwz: Array4f16
    zwww: Array4f16
    wxxx: Array4f16
    wxxy: Array4f16
    wxxz: Array4f16
    wxxw: Array4f16
    wxyx: Array4f16
    wxyy: Array4f16
    wxyz: Array4f16
    wxyw: Array4f16
    wxzx: Array4f16
    wxzy: Array4f16
    wxzz: Array4f16
    wxzw: Array4f16
    wxwx: Array4f16
    wxwy: Array4f16
    wxwz: Array4f16
    wxww: Array4f16
    wyxx: Array4f16
    wyxy: Array4f16
    wyxz: Array4f16
    wyxw: Array4f16
    wyyx: Array4f16
    wyyy: Array4f16
    wyyz: Array4f16
    wyyw: Array4f16
    wyzx: Array4f16
    wyzy: Array4f16
    wyzz: Array4f16
    wyzw: Array4f16
    wywx: Array4f16
    wywy: Array4f16
    wywz: Array4f16
    wyww: Array4f16
    wzxx: Array4f16
    wzxy: Array4f16
    wzxz: Array4f16
    wzxw: Array4f16
    wzyx: Array4f16
    wzyy: Array4f16
    wzyz: Array4f16
    wzyw: Array4f16
    wzzx: Array4f16
    wzzy: Array4f16
    wzzz: Array4f16
    wzzw: Array4f16
    wzwx: Array4f16
    wzwy: Array4f16
    wzwz: Array4f16
    wzww: Array4f16
    wwxx: Array4f16
    wwxy: Array4f16
    wwxz: Array4f16
    wwxw: Array4f16
    wwyx: Array4f16
    wwyy: Array4f16
    wwyz: Array4f16
    wwyw: Array4f16
    wwzx: Array4f16
    wwzy: Array4f16
    wwzz: Array4f16
    wwzw: Array4f16
    wwwx: Array4f16
    wwwy: Array4f16
    wwwz: Array4f16
    wwww: Array4f16

_Array3fCp: TypeAlias = Union['Array3f', '_FloatCp', 'drjit.scalar._Array3fCp', 'drjit.llvm._Array3fCp', '_Array3f16Cp']

class Array3f(drjit.ArrayBase[Array3f, _Array3fCp, Float, _FloatCp, Float, Array3f, Array3b]):
    xx: Array2f
    xy: Array2f
    xz: Array2f
    xw: Array2f
    yx: Array2f
    yy: Array2f
    yz: Array2f
    yw: Array2f
    zx: Array2f
    zy: Array2f
    zz: Array2f
    zw: Array2f
    wx: Array2f
    wy: Array2f
    wz: Array2f
    ww: Array2f
    xxx: Array3f
    xxy: Array3f
    xxz: Array3f
    xxw: Array3f
    xyx: Array3f
    xyy: Array3f
    xyz: Array3f
    xyw: Array3f
    xzx: Array3f
    xzy: Array3f
    xzz: Array3f
    xzw: Array3f
    xwx: Array3f
    xwy: Array3f
    xwz: Array3f
    xww: Array3f
    yxx: Array3f
    yxy: Array3f
    yxz: Array3f
    yxw: Array3f
    yyx: Array3f
    yyy: Array3f
    yyz: Array3f
    yyw: Array3f
    yzx: Array3f
    yzy: Array3f
    yzz: Array3f
    yzw: Array3f
    ywx: Array3f
    ywy: Array3f
    ywz: Array3f
    yww: Array3f
    zxx: Array3f
    zxy: Array3f
    zxz: Array3f
    zxw: Array3f
    zyx: Array3f
    zyy: Array3f
    zyz: Array3f
    zyw: Array3f
    zzx: Array3f
    zzy: Array3f
    zzz: Array3f
    zzw: Array3f
    zwx: Array3f
    zwy: Array3f
    zwz: Array3f
    zww: Array3f
    wxx: Array3f
    wxy: Array3f
    wxz: Array3f
    wxw: Array3f
    wyx: Array3f
    wyy: Array3f
    wyz: Array3f
    wyw: Array3f
    wzx: Array3f
    wzy: Array3f
    wzz: Array3f
    wzw: Array3f
    wwx: Array3f
    wwy: Array3f
    wwz: Array3f
    www: Array3f
    xxxx: Array4f
    xxxy: Array4f
    xxxz: Array4f
    xxxw: Array4f
    xxyx: Array4f
    xxyy: Array4f
    xxyz: Array4f
    xxyw: Array4f
    xxzx: Array4f
    xxzy: Array4f
    xxzz: Array4f
    xxzw: Array4f
    xxwx: Array4f
    xxwy: Array4f
    xxwz: Array4f
    xxww: Array4f
    xyxx: Array4f
    xyxy: Array4f
    xyxz: Array4f
    xyxw: Array4f
    xyyx: Array4f
    xyyy: Array4f
    xyyz: Array4f
    xyyw: Array4f
    xyzx: Array4f
    xyzy: Array4f
    xyzz: Array4f
    xyzw: Array4f
    xywx: Array4f
    xywy: Array4f
    xywz: Array4f
    xyww: Array4f
    xzxx: Array4f
    xzxy: Array4f
    xzxz: Array4f
    xzxw: Array4f
    xzyx: Array4f
    xzyy: Array4f
    xzyz: Array4f
    xzyw: Array4f
    xzzx: Array4f
    xzzy: Array4f
    xzzz: Array4f
    xzzw: Array4f
    xzwx: Array4f
    xzwy: Array4f
    xzwz: Array4f
    xzww: Array4f
    xwxx: Array4f
    xwxy: Array4f
    xwxz: Array4f
    xwxw: Array4f
    xwyx: Array4f
    xwyy: Array4f
    xwyz: Array4f
    xwyw: Array4f
    xwzx: Array4f
    xwzy: Array4f
    xwzz: Array4f
    xwzw: Array4f
    xwwx: Array4f
    xwwy: Array4f
    xwwz: Array4f
    xwww: Array4f
    yxxx: Array4f
    yxxy: Array4f
    yxxz: Array4f
    yxxw: Array4f
    yxyx: Array4f
    yxyy: Array4f
    yxyz: Array4f
    yxyw: Array4f
    yxzx: Array4f
    yxzy: Array4f
    yxzz: Array4f
    yxzw: Array4f
    yxwx: Array4f
    yxwy: Array4f
    yxwz: Array4f
    yxww: Array4f
    yyxx: Array4f
    yyxy: Array4f
    yyxz: Array4f
    yyxw: Array4f
    yyyx: Array4f
    yyyy: Array4f
    yyyz: Array4f
    yyyw: Array4f
    yyzx: Array4f
    yyzy: Array4f
    yyzz: Array4f
    yyzw: Array4f
    yywx: Array4f
    yywy: Array4f
    yywz: Array4f
    yyww: Array4f
    yzxx: Array4f
    yzxy: Array4f
    yzxz: Array4f
    yzxw: Array4f
    yzyx: Array4f
    yzyy: Array4f
    yzyz: Array4f
    yzyw: Array4f
    yzzx: Array4f
    yzzy: Array4f
    yzzz: Array4f
    yzzw: Array4f
    yzwx: Array4f
    yzwy: Array4f
    yzwz: Array4f
    yzww: Array4f
    ywxx: Array4f
    ywxy: Array4f
    ywxz: Array4f
    ywxw: Array4f
    ywyx: Array4f
    ywyy: Array4f
    ywyz: Array4f
    ywyw: Array4f
    ywzx: Array4f
    ywzy: Array4f
    ywzz: Array4f
    ywzw: Array4f
    ywwx: Array4f
    ywwy: Array4f
    ywwz: Array4f
    ywww: Array4f
    zxxx: Array4f
    zxxy: Array4f
    zxxz: Array4f
    zxxw: Array4f
    zxyx: Array4f
    zxyy: Array4f
    zxyz: Array4f
    zxyw: Array4f
    zxzx: Array4f
    zxzy: Array4f
    zxzz: Array4f
    zxzw: Array4f
    zxwx: Array4f
    zxwy: Array4f
    zxwz: Array4f
    zxww: Array4f
    zyxx: Array4f
    zyxy: Array4f
    zyxz: Array4f
    zyxw: Array4f
    zyyx: Array4f
    zyyy: Array4f
    zyyz: Array4f
    zyyw: Array4f
    zyzx: Array4f
    zyzy: Array4f
    zyzz: Array4f
    zyzw: Array4f
    zywx: Array4f
    zywy: Array4f
    zywz: Array4f
    zyww: Array4f
    zzxx: Array4f
    zzxy: Array4f
    zzxz: Array4f
    zzxw: Array4f
    zzyx: Array4f
    zzyy: Array4f
    zzyz: Array4f
    zzyw: Array4f
    zzzx: Array4f
    zzzy: Array4f
    zzzz: Array4f
    zzzw: Array4f
    zzwx: Array4f
    zzwy: Array4f
    zzwz: Array4f
    zzww: Array4f
    zwxx: Array4f
    zwxy: Array4f
    zwxz: Array4f
    zwxw: Array4f
    zwyx: Array4f
    zwyy: Array4f
    zwyz: Array4f
    zwyw: Array4f
    zwzx: Array4f
    zwzy: Array4f
    zwzz: Array4f
    zwzw: Array4f
    zwwx: Array4f
    zwwy: Array4f
    zwwz: Array4f
    zwww: Array4f
    wxxx: Array4f
    wxxy: Array4f
    wxxz: Array4f
    wxxw: Array4f
    wxyx: Array4f
    wxyy: Array4f
    wxyz: Array4f
    wxyw: Array4f
    wxzx: Array4f
    wxzy: Array4f
    wxzz: Array4f
    wxzw: Array4f
    wxwx: Array4f
    wxwy: Array4f
    wxwz: Array4f
    wxww: Array4f
    wyxx: Array4f
    wyxy: Array4f
    wyxz: Array4f
    wyxw: Array4f
    wyyx: Array4f
    wyyy: Array4f
    wyyz: Array4f
    wyyw: Array4f
    wyzx: Array4f
    wyzy: Array4f
    wyzz: Array4f
    wyzw: Array4f
    wywx: Array4f
    wywy: Array4f
    wywz: Array4f
    wyww: Array4f
    wzxx: Array4f
    wzxy: Array4f
    wzxz: Array4f
    wzxw: Array4f
    wzyx: Array4f
    wzyy: Array4f
    wzyz: Array4f
    wzyw: Array4f
    wzzx: Array4f
    wzzy: Array4f
    wzzz: Array4f
    wzzw: Array4f
    wzwx: Array4f
    wzwy: Array4f
    wzwz: Array4f
    wzww: Array4f
    wwxx: Array4f
    wwxy: Array4f
    wwxz: Array4f
    wwxw: Array4f
    wwyx: Array4f
    wwyy: Array4f
    wwyz: Array4f
    wwyw: Array4f
    wwzx: Array4f
    wwzy: Array4f
    wwzz: Array4f
    wwzw: Array4f
    wwwx: Array4f
    wwwy: Array4f
    wwwz: Array4f
    wwww: Array4f

_Array3f64Cp: TypeAlias = Union['Array3f64', '_Float64Cp', 'drjit.scalar._Array3f64Cp', 'drjit.llvm._Array3f64Cp', '_Array3fCp']

class Array3f64(drjit.ArrayBase[Array3f64, _Array3f64Cp, Float64, _Float64Cp, Float64, Array3f64, Array3b]):
    xx: Array2f64
    xy: Array2f64
    xz: Array2f64
    xw: Array2f64
    yx: Array2f64
    yy: Array2f64
    yz: Array2f64
    yw: Array2f64
    zx: Array2f64
    zy: Array2f64
    zz: Array2f64
    zw: Array2f64
    wx: Array2f64
    wy: Array2f64
    wz: Array2f64
    ww: Array2f64
    xxx: Array3f64
    xxy: Array3f64
    xxz: Array3f64
    xxw: Array3f64
    xyx: Array3f64
    xyy: Array3f64
    xyz: Array3f64
    xyw: Array3f64
    xzx: Array3f64
    xzy: Array3f64
    xzz: Array3f64
    xzw: Array3f64
    xwx: Array3f64
    xwy: Array3f64
    xwz: Array3f64
    xww: Array3f64
    yxx: Array3f64
    yxy: Array3f64
    yxz: Array3f64
    yxw: Array3f64
    yyx: Array3f64
    yyy: Array3f64
    yyz: Array3f64
    yyw: Array3f64
    yzx: Array3f64
    yzy: Array3f64
    yzz: Array3f64
    yzw: Array3f64
    ywx: Array3f64
    ywy: Array3f64
    ywz: Array3f64
    yww: Array3f64
    zxx: Array3f64
    zxy: Array3f64
    zxz: Array3f64
    zxw: Array3f64
    zyx: Array3f64
    zyy: Array3f64
    zyz: Array3f64
    zyw: Array3f64
    zzx: Array3f64
    zzy: Array3f64
    zzz: Array3f64
    zzw: Array3f64
    zwx: Array3f64
    zwy: Array3f64
    zwz: Array3f64
    zww: Array3f64
    wxx: Array3f64
    wxy: Array3f64
    wxz: Array3f64
    wxw: Array3f64
    wyx: Array3f64
    wyy: Array3f64
    wyz: Array3f64
    wyw: Array3f64
    wzx: Array3f64
    wzy: Array3f64
    wzz: Array3f64
    wzw: Array3f64
    wwx: Array3f64
    wwy: Array3f64
    wwz: Array3f64
    www: Array3f64
    xxxx: Array4f64
    xxxy: Array4f64
    xxxz: Array4f64
    xxxw: Array4f64
    xxyx: Array4f64
    xxyy: Array4f64
    xxyz: Array4f64
    xxyw: Array4f64
    xxzx: Array4f64
    xxzy: Array4f64
    xxzz: Array4f64
    xxzw: Array4f64
    xxwx: Array4f64
    xxwy: Array4f64
    xxwz: Array4f64
    xxww: Array4f64
    xyxx: Array4f64
    xyxy: Array4f64
    xyxz: Array4f64
    xyxw: Array4f64
    xyyx: Array4f64
    xyyy: Array4f64
    xyyz: Array4f64
    xyyw: Array4f64
    xyzx: Array4f64
    xyzy: Array4f64
    xyzz: Array4f64
    xyzw: Array4f64
    xywx: Array4f64
    xywy: Array4f64
    xywz: Array4f64
    xyww: Array4f64
    xzxx: Array4f64
    xzxy: Array4f64
    xzxz: Array4f64
    xzxw: Array4f64
    xzyx: Array4f64
    xzyy: Array4f64
    xzyz: Array4f64
    xzyw: Array4f64
    xzzx: Array4f64
    xzzy: Array4f64
    xzzz: Array4f64
    xzzw: Array4f64
    xzwx: Array4f64
    xzwy: Array4f64
    xzwz: Array4f64
    xzww: Array4f64
    xwxx: Array4f64
    xwxy: Array4f64
    xwxz: Array4f64
    xwxw: Array4f64
    xwyx: Array4f64
    xwyy: Array4f64
    xwyz: Array4f64
    xwyw: Array4f64
    xwzx: Array4f64
    xwzy: Array4f64
    xwzz: Array4f64
    xwzw: Array4f64
    xwwx: Array4f64
    xwwy: Array4f64
    xwwz: Array4f64
    xwww: Array4f64
    yxxx: Array4f64
    yxxy: Array4f64
    yxxz: Array4f64
    yxxw: Array4f64
    yxyx: Array4f64
    yxyy: Array4f64
    yxyz: Array4f64
    yxyw: Array4f64
    yxzx: Array4f64
    yxzy: Array4f64
    yxzz: Array4f64
    yxzw: Array4f64
    yxwx: Array4f64
    yxwy: Array4f64
    yxwz: Array4f64
    yxww: Array4f64
    yyxx: Array4f64
    yyxy: Array4f64
    yyxz: Array4f64
    yyxw: Array4f64
    yyyx: Array4f64
    yyyy: Array4f64
    yyyz: Array4f64
    yyyw: Array4f64
    yyzx: Array4f64
    yyzy: Array4f64
    yyzz: Array4f64
    yyzw: Array4f64
    yywx: Array4f64
    yywy: Array4f64
    yywz: Array4f64
    yyww: Array4f64
    yzxx: Array4f64
    yzxy: Array4f64
    yzxz: Array4f64
    yzxw: Array4f64
    yzyx: Array4f64
    yzyy: Array4f64
    yzyz: Array4f64
    yzyw: Array4f64
    yzzx: Array4f64
    yzzy: Array4f64
    yzzz: Array4f64
    yzzw: Array4f64
    yzwx: Array4f64
    yzwy: Array4f64
    yzwz: Array4f64
    yzww: Array4f64
    ywxx: Array4f64
    ywxy: Array4f64
    ywxz: Array4f64
    ywxw: Array4f64
    ywyx: Array4f64
    ywyy: Array4f64
    ywyz: Array4f64
    ywyw: Array4f64
    ywzx: Array4f64
    ywzy: Array4f64
    ywzz: Array4f64
    ywzw: Array4f64
    ywwx: Array4f64
    ywwy: Array4f64
    ywwz: Array4f64
    ywww: Array4f64
    zxxx: Array4f64
    zxxy: Array4f64
    zxxz: Array4f64
    zxxw: Array4f64
    zxyx: Array4f64
    zxyy: Array4f64
    zxyz: Array4f64
    zxyw: Array4f64
    zxzx: Array4f64
    zxzy: Array4f64
    zxzz: Array4f64
    zxzw: Array4f64
    zxwx: Array4f64
    zxwy: Array4f64
    zxwz: Array4f64
    zxww: Array4f64
    zyxx: Array4f64
    zyxy: Array4f64
    zyxz: Array4f64
    zyxw: Array4f64
    zyyx: Array4f64
    zyyy: Array4f64
    zyyz: Array4f64
    zyyw: Array4f64
    zyzx: Array4f64
    zyzy: Array4f64
    zyzz: Array4f64
    zyzw: Array4f64
    zywx: Array4f64
    zywy: Array4f64
    zywz: Array4f64
    zyww: Array4f64
    zzxx: Array4f64
    zzxy: Array4f64
    zzxz: Array4f64
    zzxw: Array4f64
    zzyx: Array4f64
    zzyy: Array4f64
    zzyz: Array4f64
    zzyw: Array4f64
    zzzx: Array4f64
    zzzy: Array4f64
    zzzz: Array4f64
    zzzw: Array4f64
    zzwx: Array4f64
    zzwy: Array4f64
    zzwz: Array4f64
    zzww: Array4f64
    zwxx: Array4f64
    zwxy: Array4f64
    zwxz: Array4f64
    zwxw: Array4f64
    zwyx: Array4f64
    zwyy: Array4f64
    zwyz: Array4f64
    zwyw: Array4f64
    zwzx: Array4f64
    zwzy: Array4f64
    zwzz: Array4f64
    zwzw: Array4f64
    zwwx: Array4f64
    zwwy: Array4f64
    zwwz: Array4f64
    zwww: Array4f64
    wxxx: Array4f64
    wxxy: Array4f64
    wxxz: Array4f64
    wxxw: Array4f64
    wxyx: Array4f64
    wxyy: Array4f64
    wxyz: Array4f64
    wxyw: Array4f64
    wxzx: Array4f64
    wxzy: Array4f64
    wxzz: Array4f64
    wxzw: Array4f64
    wxwx: Array4f64
    wxwy: Array4f64
    wxwz: Array4f64
    wxww: Array4f64
    wyxx: Array4f64
    wyxy: Array4f64
    wyxz: Array4f64
    wyxw: Array4f64
    wyyx: Array4f64
    wyyy: Array4f64
    wyyz: Array4f64
    wyyw: Array4f64
    wyzx: Array4f64
    wyzy: Array4f64
    wyzz: Array4f64
    wyzw: Array4f64
    wywx: Array4f64
    wywy: Array4f64
    wywz: Array4f64
    wyww: Array4f64
    wzxx: Array4f64
    wzxy: Array4f64
    wzxz: Array4f64
    wzxw: Array4f64
    wzyx: Array4f64
    wzyy: Array4f64
    wzyz: Array4f64
    wzyw: Array4f64
    wzzx: Array4f64
    wzzy: Array4f64
    wzzz: Array4f64
    wzzw: Array4f64
    wzwx: Array4f64
    wzwy: Array4f64
    wzwz: Array4f64
    wzww: Array4f64
    wwxx: Array4f64
    wwxy: Array4f64
    wwxz: Array4f64
    wwxw: Array4f64
    wwyx: Array4f64
    wwyy: Array4f64
    wwyz: Array4f64
    wwyw: Array4f64
    wwzx: Array4f64
    wwzy: Array4f64
    wwzz: Array4f64
    wwzw: Array4f64
    wwwx: Array4f64
    wwwy: Array4f64
    wwwz: Array4f64
    wwww: Array4f64

_Array4bCp: TypeAlias = Union['Array4b', '_BoolCp', 'drjit.scalar._Array4bCp', 'drjit.llvm._Array4bCp']

class Array4b(drjit.ArrayBase[Array4b, _Array4bCp, Bool, _BoolCp, Bool, Array4b, Array4b]):
    xx: Array2b
    xy: Array2b
    xz: Array2b
    xw: Array2b
    yx: Array2b
    yy: Array2b
    yz: Array2b
    yw: Array2b
    zx: Array2b
    zy: Array2b
    zz: Array2b
    zw: Array2b
    wx: Array2b
    wy: Array2b
    wz: Array2b
    ww: Array2b
    xxx: Array3b
    xxy: Array3b
    xxz: Array3b
    xxw: Array3b
    xyx: Array3b
    xyy: Array3b
    xyz: Array3b
    xyw: Array3b
    xzx: Array3b
    xzy: Array3b
    xzz: Array3b
    xzw: Array3b
    xwx: Array3b
    xwy: Array3b
    xwz: Array3b
    xww: Array3b
    yxx: Array3b
    yxy: Array3b
    yxz: Array3b
    yxw: Array3b
    yyx: Array3b
    yyy: Array3b
    yyz: Array3b
    yyw: Array3b
    yzx: Array3b
    yzy: Array3b
    yzz: Array3b
    yzw: Array3b
    ywx: Array3b
    ywy: Array3b
    ywz: Array3b
    yww: Array3b
    zxx: Array3b
    zxy: Array3b
    zxz: Array3b
    zxw: Array3b
    zyx: Array3b
    zyy: Array3b
    zyz: Array3b
    zyw: Array3b
    zzx: Array3b
    zzy: Array3b
    zzz: Array3b
    zzw: Array3b
    zwx: Array3b
    zwy: Array3b
    zwz: Array3b
    zww: Array3b
    wxx: Array3b
    wxy: Array3b
    wxz: Array3b
    wxw: Array3b
    wyx: Array3b
    wyy: Array3b
    wyz: Array3b
    wyw: Array3b
    wzx: Array3b
    wzy: Array3b
    wzz: Array3b
    wzw: Array3b
    wwx: Array3b
    wwy: Array3b
    wwz: Array3b
    www: Array3b
    xxxx: Array4b
    xxxy: Array4b
    xxxz: Array4b
    xxxw: Array4b
    xxyx: Array4b
    xxyy: Array4b
    xxyz: Array4b
    xxyw: Array4b
    xxzx: Array4b
    xxzy: Array4b
    xxzz: Array4b
    xxzw: Array4b
    xxwx: Array4b
    xxwy: Array4b
    xxwz: Array4b
    xxww: Array4b
    xyxx: Array4b
    xyxy: Array4b
    xyxz: Array4b
    xyxw: Array4b
    xyyx: Array4b
    xyyy: Array4b
    xyyz: Array4b
    xyyw: Array4b
    xyzx: Array4b
    xyzy: Array4b
    xyzz: Array4b
    xyzw: Array4b
    xywx: Array4b
    xywy: Array4b
    xywz: Array4b
    xyww: Array4b
    xzxx: Array4b
    xzxy: Array4b
    xzxz: Array4b
    xzxw: Array4b
    xzyx: Array4b
    xzyy: Array4b
    xzyz: Array4b
    xzyw: Array4b
    xzzx: Array4b
    xzzy: Array4b
    xzzz: Array4b
    xzzw: Array4b
    xzwx: Array4b
    xzwy: Array4b
    xzwz: Array4b
    xzww: Array4b
    xwxx: Array4b
    xwxy: Array4b
    xwxz: Array4b
    xwxw: Array4b
    xwyx: Array4b
    xwyy: Array4b
    xwyz: Array4b
    xwyw: Array4b
    xwzx: Array4b
    xwzy: Array4b
    xwzz: Array4b
    xwzw: Array4b
    xwwx: Array4b
    xwwy: Array4b
    xwwz: Array4b
    xwww: Array4b
    yxxx: Array4b
    yxxy: Array4b
    yxxz: Array4b
    yxxw: Array4b
    yxyx: Array4b
    yxyy: Array4b
    yxyz: Array4b
    yxyw: Array4b
    yxzx: Array4b
    yxzy: Array4b
    yxzz: Array4b
    yxzw: Array4b
    yxwx: Array4b
    yxwy: Array4b
    yxwz: Array4b
    yxww: Array4b
    yyxx: Array4b
    yyxy: Array4b
    yyxz: Array4b
    yyxw: Array4b
    yyyx: Array4b
    yyyy: Array4b
    yyyz: Array4b
    yyyw: Array4b
    yyzx: Array4b
    yyzy: Array4b
    yyzz: Array4b
    yyzw: Array4b
    yywx: Array4b
    yywy: Array4b
    yywz: Array4b
    yyww: Array4b
    yzxx: Array4b
    yzxy: Array4b
    yzxz: Array4b
    yzxw: Array4b
    yzyx: Array4b
    yzyy: Array4b
    yzyz: Array4b
    yzyw: Array4b
    yzzx: Array4b
    yzzy: Array4b
    yzzz: Array4b
    yzzw: Array4b
    yzwx: Array4b
    yzwy: Array4b
    yzwz: Array4b
    yzww: Array4b
    ywxx: Array4b
    ywxy: Array4b
    ywxz: Array4b
    ywxw: Array4b
    ywyx: Array4b
    ywyy: Array4b
    ywyz: Array4b
    ywyw: Array4b
    ywzx: Array4b
    ywzy: Array4b
    ywzz: Array4b
    ywzw: Array4b
    ywwx: Array4b
    ywwy: Array4b
    ywwz: Array4b
    ywww: Array4b
    zxxx: Array4b
    zxxy: Array4b
    zxxz: Array4b
    zxxw: Array4b
    zxyx: Array4b
    zxyy: Array4b
    zxyz: Array4b
    zxyw: Array4b
    zxzx: Array4b
    zxzy: Array4b
    zxzz: Array4b
    zxzw: Array4b
    zxwx: Array4b
    zxwy: Array4b
    zxwz: Array4b
    zxww: Array4b
    zyxx: Array4b
    zyxy: Array4b
    zyxz: Array4b
    zyxw: Array4b
    zyyx: Array4b
    zyyy: Array4b
    zyyz: Array4b
    zyyw: Array4b
    zyzx: Array4b
    zyzy: Array4b
    zyzz: Array4b
    zyzw: Array4b
    zywx: Array4b
    zywy: Array4b
    zywz: Array4b
    zyww: Array4b
    zzxx: Array4b
    zzxy: Array4b
    zzxz: Array4b
    zzxw: Array4b
    zzyx: Array4b
    zzyy: Array4b
    zzyz: Array4b
    zzyw: Array4b
    zzzx: Array4b
    zzzy: Array4b
    zzzz: Array4b
    zzzw: Array4b
    zzwx: Array4b
    zzwy: Array4b
    zzwz: Array4b
    zzww: Array4b
    zwxx: Array4b
    zwxy: Array4b
    zwxz: Array4b
    zwxw: Array4b
    zwyx: Array4b
    zwyy: Array4b
    zwyz: Array4b
    zwyw: Array4b
    zwzx: Array4b
    zwzy: Array4b
    zwzz: Array4b
    zwzw: Array4b
    zwwx: Array4b
    zwwy: Array4b
    zwwz: Array4b
    zwww: Array4b
    wxxx: Array4b
    wxxy: Array4b
    wxxz: Array4b
    wxxw: Array4b
    wxyx: Array4b
    wxyy: Array4b
    wxyz: Array4b
    wxyw: Array4b
    wxzx: Array4b
    wxzy: Array4b
    wxzz: Array4b
    wxzw: Array4b
    wxwx: Array4b
    wxwy: Array4b
    wxwz: Array4b
    wxww: Array4b
    wyxx: Array4b
    wyxy: Array4b
    wyxz: Array4b
    wyxw: Array4b
    wyyx: Array4b
    wyyy: Array4b
    wyyz: Array4b
    wyyw: Array4b
    wyzx: Array4b
    wyzy: Array4b
    wyzz: Array4b
    wyzw: Array4b
    wywx: Array4b
    wywy: Array4b
    wywz: Array4b
    wyww: Array4b
    wzxx: Array4b
    wzxy: Array4b
    wzxz: Array4b
    wzxw: Array4b
    wzyx: Array4b
    wzyy: Array4b
    wzyz: Array4b
    wzyw: Array4b
    wzzx: Array4b
    wzzy: Array4b
    wzzz: Array4b
    wzzw: Array4b
    wzwx: Array4b
    wzwy: Array4b
    wzwz: Array4b
    wzww: Array4b
    wwxx: Array4b
    wwxy: Array4b
    wwxz: Array4b
    wwxw: Array4b
    wwyx: Array4b
    wwyy: Array4b
    wwyz: Array4b
    wwyw: Array4b
    wwzx: Array4b
    wwzy: Array4b
    wwzz: Array4b
    wwzw: Array4b
    wwwx: Array4b
    wwwy: Array4b
    wwwz: Array4b
    wwww: Array4b

_Array4i8Cp: TypeAlias = Union['Array4i8', '_Int8Cp', 'drjit.scalar._Array4i8Cp', 'drjit.llvm._Array4i8Cp']

class Array4i8(drjit.ArrayBase[Array4i8, _Array4i8Cp, Int8, _Int8Cp, Int8, Array4i8, Array4b]):
    xx: Array2i8
    xy: Array2i8
    xz: Array2i8
    xw: Array2i8
    yx: Array2i8
    yy: Array2i8
    yz: Array2i8
    yw: Array2i8
    zx: Array2i8
    zy: Array2i8
    zz: Array2i8
    zw: Array2i8
    wx: Array2i8
    wy: Array2i8
    wz: Array2i8
    ww: Array2i8
    xxx: Array3i8
    xxy: Array3i8
    xxz: Array3i8
    xxw: Array3i8
    xyx: Array3i8
    xyy: Array3i8
    xyz: Array3i8
    xyw: Array3i8
    xzx: Array3i8
    xzy: Array3i8
    xzz: Array3i8
    xzw: Array3i8
    xwx: Array3i8
    xwy: Array3i8
    xwz: Array3i8
    xww: Array3i8
    yxx: Array3i8
    yxy: Array3i8
    yxz: Array3i8
    yxw: Array3i8
    yyx: Array3i8
    yyy: Array3i8
    yyz: Array3i8
    yyw: Array3i8
    yzx: Array3i8
    yzy: Array3i8
    yzz: Array3i8
    yzw: Array3i8
    ywx: Array3i8
    ywy: Array3i8
    ywz: Array3i8
    yww: Array3i8
    zxx: Array3i8
    zxy: Array3i8
    zxz: Array3i8
    zxw: Array3i8
    zyx: Array3i8
    zyy: Array3i8
    zyz: Array3i8
    zyw: Array3i8
    zzx: Array3i8
    zzy: Array3i8
    zzz: Array3i8
    zzw: Array3i8
    zwx: Array3i8
    zwy: Array3i8
    zwz: Array3i8
    zww: Array3i8
    wxx: Array3i8
    wxy: Array3i8
    wxz: Array3i8
    wxw: Array3i8
    wyx: Array3i8
    wyy: Array3i8
    wyz: Array3i8
    wyw: Array3i8
    wzx: Array3i8
    wzy: Array3i8
    wzz: Array3i8
    wzw: Array3i8
    wwx: Array3i8
    wwy: Array3i8
    wwz: Array3i8
    www: Array3i8
    xxxx: Array4i8
    xxxy: Array4i8
    xxxz: Array4i8
    xxxw: Array4i8
    xxyx: Array4i8
    xxyy: Array4i8
    xxyz: Array4i8
    xxyw: Array4i8
    xxzx: Array4i8
    xxzy: Array4i8
    xxzz: Array4i8
    xxzw: Array4i8
    xxwx: Array4i8
    xxwy: Array4i8
    xxwz: Array4i8
    xxww: Array4i8
    xyxx: Array4i8
    xyxy: Array4i8
    xyxz: Array4i8
    xyxw: Array4i8
    xyyx: Array4i8
    xyyy: Array4i8
    xyyz: Array4i8
    xyyw: Array4i8
    xyzx: Array4i8
    xyzy: Array4i8
    xyzz: Array4i8
    xyzw: Array4i8
    xywx: Array4i8
    xywy: Array4i8
    xywz: Array4i8
    xyww: Array4i8
    xzxx: Array4i8
    xzxy: Array4i8
    xzxz: Array4i8
    xzxw: Array4i8
    xzyx: Array4i8
    xzyy: Array4i8
    xzyz: Array4i8
    xzyw: Array4i8
    xzzx: Array4i8
    xzzy: Array4i8
    xzzz: Array4i8
    xzzw: Array4i8
    xzwx: Array4i8
    xzwy: Array4i8
    xzwz: Array4i8
    xzww: Array4i8
    xwxx: Array4i8
    xwxy: Array4i8
    xwxz: Array4i8
    xwxw: Array4i8
    xwyx: Array4i8
    xwyy: Array4i8
    xwyz: Array4i8
    xwyw: Array4i8
    xwzx: Array4i8
    xwzy: Array4i8
    xwzz: Array4i8
    xwzw: Array4i8
    xwwx: Array4i8
    xwwy: Array4i8
    xwwz: Array4i8
    xwww: Array4i8
    yxxx: Array4i8
    yxxy: Array4i8
    yxxz: Array4i8
    yxxw: Array4i8
    yxyx: Array4i8
    yxyy: Array4i8
    yxyz: Array4i8
    yxyw: Array4i8
    yxzx: Array4i8
    yxzy: Array4i8
    yxzz: Array4i8
    yxzw: Array4i8
    yxwx: Array4i8
    yxwy: Array4i8
    yxwz: Array4i8
    yxww: Array4i8
    yyxx: Array4i8
    yyxy: Array4i8
    yyxz: Array4i8
    yyxw: Array4i8
    yyyx: Array4i8
    yyyy: Array4i8
    yyyz: Array4i8
    yyyw: Array4i8
    yyzx: Array4i8
    yyzy: Array4i8
    yyzz: Array4i8
    yyzw: Array4i8
    yywx: Array4i8
    yywy: Array4i8
    yywz: Array4i8
    yyww: Array4i8
    yzxx: Array4i8
    yzxy: Array4i8
    yzxz: Array4i8
    yzxw: Array4i8
    yzyx: Array4i8
    yzyy: Array4i8
    yzyz: Array4i8
    yzyw: Array4i8
    yzzx: Array4i8
    yzzy: Array4i8
    yzzz: Array4i8
    yzzw: Array4i8
    yzwx: Array4i8
    yzwy: Array4i8
    yzwz: Array4i8
    yzww: Array4i8
    ywxx: Array4i8
    ywxy: Array4i8
    ywxz: Array4i8
    ywxw: Array4i8
    ywyx: Array4i8
    ywyy: Array4i8
    ywyz: Array4i8
    ywyw: Array4i8
    ywzx: Array4i8
    ywzy: Array4i8
    ywzz: Array4i8
    ywzw: Array4i8
    ywwx: Array4i8
    ywwy: Array4i8
    ywwz: Array4i8
    ywww: Array4i8
    zxxx: Array4i8
    zxxy: Array4i8
    zxxz: Array4i8
    zxxw: Array4i8
    zxyx: Array4i8
    zxyy: Array4i8
    zxyz: Array4i8
    zxyw: Array4i8
    zxzx: Array4i8
    zxzy: Array4i8
    zxzz: Array4i8
    zxzw: Array4i8
    zxwx: Array4i8
    zxwy: Array4i8
    zxwz: Array4i8
    zxww: Array4i8
    zyxx: Array4i8
    zyxy: Array4i8
    zyxz: Array4i8
    zyxw: Array4i8
    zyyx: Array4i8
    zyyy: Array4i8
    zyyz: Array4i8
    zyyw: Array4i8
    zyzx: Array4i8
    zyzy: Array4i8
    zyzz: Array4i8
    zyzw: Array4i8
    zywx: Array4i8
    zywy: Array4i8
    zywz: Array4i8
    zyww: Array4i8
    zzxx: Array4i8
    zzxy: Array4i8
    zzxz: Array4i8
    zzxw: Array4i8
    zzyx: Array4i8
    zzyy: Array4i8
    zzyz: Array4i8
    zzyw: Array4i8
    zzzx: Array4i8
    zzzy: Array4i8
    zzzz: Array4i8
    zzzw: Array4i8
    zzwx: Array4i8
    zzwy: Array4i8
    zzwz: Array4i8
    zzww: Array4i8
    zwxx: Array4i8
    zwxy: Array4i8
    zwxz: Array4i8
    zwxw: Array4i8
    zwyx: Array4i8
    zwyy: Array4i8
    zwyz: Array4i8
    zwyw: Array4i8
    zwzx: Array4i8
    zwzy: Array4i8
    zwzz: Array4i8
    zwzw: Array4i8
    zwwx: Array4i8
    zwwy: Array4i8
    zwwz: Array4i8
    zwww: Array4i8
    wxxx: Array4i8
    wxxy: Array4i8
    wxxz: Array4i8
    wxxw: Array4i8
    wxyx: Array4i8
    wxyy: Array4i8
    wxyz: Array4i8
    wxyw: Array4i8
    wxzx: Array4i8
    wxzy: Array4i8
    wxzz: Array4i8
    wxzw: Array4i8
    wxwx: Array4i8
    wxwy: Array4i8
    wxwz: Array4i8
    wxww: Array4i8
    wyxx: Array4i8
    wyxy: Array4i8
    wyxz: Array4i8
    wyxw: Array4i8
    wyyx: Array4i8
    wyyy: Array4i8
    wyyz: Array4i8
    wyyw: Array4i8
    wyzx: Array4i8
    wyzy: Array4i8
    wyzz: Array4i8
    wyzw: Array4i8
    wywx: Array4i8
    wywy: Array4i8
    wywz: Array4i8
    wyww: Array4i8
    wzxx: Array4i8
    wzxy: Array4i8
    wzxz: Array4i8
    wzxw: Array4i8
    wzyx: Array4i8
    wzyy: Array4i8
    wzyz: Array4i8
    wzyw: Array4i8
    wzzx: Array4i8
    wzzy: Array4i8
    wzzz: Array4i8
    wzzw: Array4i8
    wzwx: Array4i8
    wzwy: Array4i8
    wzwz: Array4i8
    wzww: Array4i8
    wwxx: Array4i8
    wwxy: Array4i8
    wwxz: Array4i8
    wwxw: Array4i8
    wwyx: Array4i8
    wwyy: Array4i8
    wwyz: Array4i8
    wwyw: Array4i8
    wwzx: Array4i8
    wwzy: Array4i8
    wwzz: Array4i8
    wwzw: Array4i8
    wwwx: Array4i8
    wwwy: Array4i8
    wwwz: Array4i8
    wwww: Array4i8

_Array4u8Cp: TypeAlias = Union['Array4u8', '_UInt8Cp', 'drjit.scalar._Array4u8Cp', 'drjit.llvm._Array4u8Cp']

class Array4u8(drjit.ArrayBase[Array4u8, _Array4u8Cp, UInt8, _UInt8Cp, UInt8, Array4u8, Array4b]):
    xx: Array2u8
    xy: Array2u8
    xz: Array2u8
    xw: Array2u8
    yx: Array2u8
    yy: Array2u8
    yz: Array2u8
    yw: Array2u8
    zx: Array2u8
    zy: Array2u8
    zz: Array2u8
    zw: Array2u8
    wx: Array2u8
    wy: Array2u8
    wz: Array2u8
    ww: Array2u8
    xxx: Array3u8
    xxy: Array3u8
    xxz: Array3u8
    xxw: Array3u8
    xyx: Array3u8
    xyy: Array3u8
    xyz: Array3u8
    xyw: Array3u8
    xzx: Array3u8
    xzy: Array3u8
    xzz: Array3u8
    xzw: Array3u8
    xwx: Array3u8
    xwy: Array3u8
    xwz: Array3u8
    xww: Array3u8
    yxx: Array3u8
    yxy: Array3u8
    yxz: Array3u8
    yxw: Array3u8
    yyx: Array3u8
    yyy: Array3u8
    yyz: Array3u8
    yyw: Array3u8
    yzx: Array3u8
    yzy: Array3u8
    yzz: Array3u8
    yzw: Array3u8
    ywx: Array3u8
    ywy: Array3u8
    ywz: Array3u8
    yww: Array3u8
    zxx: Array3u8
    zxy: Array3u8
    zxz: Array3u8
    zxw: Array3u8
    zyx: Array3u8
    zyy: Array3u8
    zyz: Array3u8
    zyw: Array3u8
    zzx: Array3u8
    zzy: Array3u8
    zzz: Array3u8
    zzw: Array3u8
    zwx: Array3u8
    zwy: Array3u8
    zwz: Array3u8
    zww: Array3u8
    wxx: Array3u8
    wxy: Array3u8
    wxz: Array3u8
    wxw: Array3u8
    wyx: Array3u8
    wyy: Array3u8
    wyz: Array3u8
    wyw: Array3u8
    wzx: Array3u8
    wzy: Array3u8
    wzz: Array3u8
    wzw: Array3u8
    wwx: Array3u8
    wwy: Array3u8
    wwz: Array3u8
    www: Array3u8
    xxxx: Array4u8
    xxxy: Array4u8
    xxxz: Array4u8
    xxxw: Array4u8
    xxyx: Array4u8
    xxyy: Array4u8
    xxyz: Array4u8
    xxyw: Array4u8
    xxzx: Array4u8
    xxzy: Array4u8
    xxzz: Array4u8
    xxzw: Array4u8
    xxwx: Array4u8
    xxwy: Array4u8
    xxwz: Array4u8
    xxww: Array4u8
    xyxx: Array4u8
    xyxy: Array4u8
    xyxz: Array4u8
    xyxw: Array4u8
    xyyx: Array4u8
    xyyy: Array4u8
    xyyz: Array4u8
    xyyw: Array4u8
    xyzx: Array4u8
    xyzy: Array4u8
    xyzz: Array4u8
    xyzw: Array4u8
    xywx: Array4u8
    xywy: Array4u8
    xywz: Array4u8
    xyww: Array4u8
    xzxx: Array4u8
    xzxy: Array4u8
    xzxz: Array4u8
    xzxw: Array4u8
    xzyx: Array4u8
    xzyy: Array4u8
    xzyz: Array4u8
    xzyw: Array4u8
    xzzx: Array4u8
    xzzy: Array4u8
    xzzz: Array4u8
    xzzw: Array4u8
    xzwx: Array4u8
    xzwy: Array4u8
    xzwz: Array4u8
    xzww: Array4u8
    xwxx: Array4u8
    xwxy: Array4u8
    xwxz: Array4u8
    xwxw: Array4u8
    xwyx: Array4u8
    xwyy: Array4u8
    xwyz: Array4u8
    xwyw: Array4u8
    xwzx: Array4u8
    xwzy: Array4u8
    xwzz: Array4u8
    xwzw: Array4u8
    xwwx: Array4u8
    xwwy: Array4u8
    xwwz: Array4u8
    xwww: Array4u8
    yxxx: Array4u8
    yxxy: Array4u8
    yxxz: Array4u8
    yxxw: Array4u8
    yxyx: Array4u8
    yxyy: Array4u8
    yxyz: Array4u8
    yxyw: Array4u8
    yxzx: Array4u8
    yxzy: Array4u8
    yxzz: Array4u8
    yxzw: Array4u8
    yxwx: Array4u8
    yxwy: Array4u8
    yxwz: Array4u8
    yxww: Array4u8
    yyxx: Array4u8
    yyxy: Array4u8
    yyxz: Array4u8
    yyxw: Array4u8
    yyyx: Array4u8
    yyyy: Array4u8
    yyyz: Array4u8
    yyyw: Array4u8
    yyzx: Array4u8
    yyzy: Array4u8
    yyzz: Array4u8
    yyzw: Array4u8
    yywx: Array4u8
    yywy: Array4u8
    yywz: Array4u8
    yyww: Array4u8
    yzxx: Array4u8
    yzxy: Array4u8
    yzxz: Array4u8
    yzxw: Array4u8
    yzyx: Array4u8
    yzyy: Array4u8
    yzyz: Array4u8
    yzyw: Array4u8
    yzzx: Array4u8
    yzzy: Array4u8
    yzzz: Array4u8
    yzzw: Array4u8
    yzwx: Array4u8
    yzwy: Array4u8
    yzwz: Array4u8
    yzww: Array4u8
    ywxx: Array4u8
    ywxy: Array4u8
    ywxz: Array4u8
    ywxw: Array4u8
    ywyx: Array4u8
    ywyy: Array4u8
    ywyz: Array4u8
    ywyw: Array4u8
    ywzx: Array4u8
    ywzy: Array4u8
    ywzz: Array4u8
    ywzw: Array4u8
    ywwx: Array4u8
    ywwy: Array4u8
    ywwz: Array4u8
    ywww: Array4u8
    zxxx: Array4u8
    zxxy: Array4u8
    zxxz: Array4u8
    zxxw: Array4u8
    zxyx: Array4u8
    zxyy: Array4u8
    zxyz: Array4u8
    zxyw: Array4u8
    zxzx: Array4u8
    zxzy: Array4u8
    zxzz: Array4u8
    zxzw: Array4u8
    zxwx: Array4u8
    zxwy: Array4u8
    zxwz: Array4u8
    zxww: Array4u8
    zyxx: Array4u8
    zyxy: Array4u8
    zyxz: Array4u8
    zyxw: Array4u8
    zyyx: Array4u8
    zyyy: Array4u8
    zyyz: Array4u8
    zyyw: Array4u8
    zyzx: Array4u8
    zyzy: Array4u8
    zyzz: Array4u8
    zyzw: Array4u8
    zywx: Array4u8
    zywy: Array4u8
    zywz: Array4u8
    zyww: Array4u8
    zzxx: Array4u8
    zzxy: Array4u8
    zzxz: Array4u8
    zzxw: Array4u8
    zzyx: Array4u8
    zzyy: Array4u8
    zzyz: Array4u8
    zzyw: Array4u8
    zzzx: Array4u8
    zzzy: Array4u8
    zzzz: Array4u8
    zzzw: Array4u8
    zzwx: Array4u8
    zzwy: Array4u8
    zzwz: Array4u8
    zzww: Array4u8
    zwxx: Array4u8
    zwxy: Array4u8
    zwxz: Array4u8
    zwxw: Array4u8
    zwyx: Array4u8
    zwyy: Array4u8
    zwyz: Array4u8
    zwyw: Array4u8
    zwzx: Array4u8
    zwzy: Array4u8
    zwzz: Array4u8
    zwzw: Array4u8
    zwwx: Array4u8
    zwwy: Array4u8
    zwwz: Array4u8
    zwww: Array4u8
    wxxx: Array4u8
    wxxy: Array4u8
    wxxz: Array4u8
    wxxw: Array4u8
    wxyx: Array4u8
    wxyy: Array4u8
    wxyz: Array4u8
    wxyw: Array4u8
    wxzx: Array4u8
    wxzy: Array4u8
    wxzz: Array4u8
    wxzw: Array4u8
    wxwx: Array4u8
    wxwy: Array4u8
    wxwz: Array4u8
    wxww: Array4u8
    wyxx: Array4u8
    wyxy: Array4u8
    wyxz: Array4u8
    wyxw: Array4u8
    wyyx: Array4u8
    wyyy: Array4u8
    wyyz: Array4u8
    wyyw: Array4u8
    wyzx: Array4u8
    wyzy: Array4u8
    wyzz: Array4u8
    wyzw: Array4u8
    wywx: Array4u8
    wywy: Array4u8
    wywz: Array4u8
    wyww: Array4u8
    wzxx: Array4u8
    wzxy: Array4u8
    wzxz: Array4u8
    wzxw: Array4u8
    wzyx: Array4u8
    wzyy: Array4u8
    wzyz: Array4u8
    wzyw: Array4u8
    wzzx: Array4u8
    wzzy: Array4u8
    wzzz: Array4u8
    wzzw: Array4u8
    wzwx: Array4u8
    wzwy: Array4u8
    wzwz: Array4u8
    wzww: Array4u8
    wwxx: Array4u8
    wwxy: Array4u8
    wwxz: Array4u8
    wwxw: Array4u8
    wwyx: Array4u8
    wwyy: Array4u8
    wwyz: Array4u8
    wwyw: Array4u8
    wwzx: Array4u8
    wwzy: Array4u8
    wwzz: Array4u8
    wwzw: Array4u8
    wwwx: Array4u8
    wwwy: Array4u8
    wwwz: Array4u8
    wwww: Array4u8

_Array4iCp: TypeAlias = Union['Array4i', '_IntCp', 'drjit.scalar._Array4iCp', 'drjit.llvm._Array4iCp', '_Array4bCp']

class Array4i(drjit.ArrayBase[Array4i, _Array4iCp, Int, _IntCp, Int, Array4i, Array4b]):
    xx: Array2i
    xy: Array2i
    xz: Array2i
    xw: Array2i
    yx: Array2i
    yy: Array2i
    yz: Array2i
    yw: Array2i
    zx: Array2i
    zy: Array2i
    zz: Array2i
    zw: Array2i
    wx: Array2i
    wy: Array2i
    wz: Array2i
    ww: Array2i
    xxx: Array3i
    xxy: Array3i
    xxz: Array3i
    xxw: Array3i
    xyx: Array3i
    xyy: Array3i
    xyz: Array3i
    xyw: Array3i
    xzx: Array3i
    xzy: Array3i
    xzz: Array3i
    xzw: Array3i
    xwx: Array3i
    xwy: Array3i
    xwz: Array3i
    xww: Array3i
    yxx: Array3i
    yxy: Array3i
    yxz: Array3i
    yxw: Array3i
    yyx: Array3i
    yyy: Array3i
    yyz: Array3i
    yyw: Array3i
    yzx: Array3i
    yzy: Array3i
    yzz: Array3i
    yzw: Array3i
    ywx: Array3i
    ywy: Array3i
    ywz: Array3i
    yww: Array3i
    zxx: Array3i
    zxy: Array3i
    zxz: Array3i
    zxw: Array3i
    zyx: Array3i
    zyy: Array3i
    zyz: Array3i
    zyw: Array3i
    zzx: Array3i
    zzy: Array3i
    zzz: Array3i
    zzw: Array3i
    zwx: Array3i
    zwy: Array3i
    zwz: Array3i
    zww: Array3i
    wxx: Array3i
    wxy: Array3i
    wxz: Array3i
    wxw: Array3i
    wyx: Array3i
    wyy: Array3i
    wyz: Array3i
    wyw: Array3i
    wzx: Array3i
    wzy: Array3i
    wzz: Array3i
    wzw: Array3i
    wwx: Array3i
    wwy: Array3i
    wwz: Array3i
    www: Array3i
    xxxx: Array4i
    xxxy: Array4i
    xxxz: Array4i
    xxxw: Array4i
    xxyx: Array4i
    xxyy: Array4i
    xxyz: Array4i
    xxyw: Array4i
    xxzx: Array4i
    xxzy: Array4i
    xxzz: Array4i
    xxzw: Array4i
    xxwx: Array4i
    xxwy: Array4i
    xxwz: Array4i
    xxww: Array4i
    xyxx: Array4i
    xyxy: Array4i
    xyxz: Array4i
    xyxw: Array4i
    xyyx: Array4i
    xyyy: Array4i
    xyyz: Array4i
    xyyw: Array4i
    xyzx: Array4i
    xyzy: Array4i
    xyzz: Array4i
    xyzw: Array4i
    xywx: Array4i
    xywy: Array4i
    xywz: Array4i
    xyww: Array4i
    xzxx: Array4i
    xzxy: Array4i
    xzxz: Array4i
    xzxw: Array4i
    xzyx: Array4i
    xzyy: Array4i
    xzyz: Array4i
    xzyw: Array4i
    xzzx: Array4i
    xzzy: Array4i
    xzzz: Array4i
    xzzw: Array4i
    xzwx: Array4i
    xzwy: Array4i
    xzwz: Array4i
    xzww: Array4i
    xwxx: Array4i
    xwxy: Array4i
    xwxz: Array4i
    xwxw: Array4i
    xwyx: Array4i
    xwyy: Array4i
    xwyz: Array4i
    xwyw: Array4i
    xwzx: Array4i
    xwzy: Array4i
    xwzz: Array4i
    xwzw: Array4i
    xwwx: Array4i
    xwwy: Array4i
    xwwz: Array4i
    xwww: Array4i
    yxxx: Array4i
    yxxy: Array4i
    yxxz: Array4i
    yxxw: Array4i
    yxyx: Array4i
    yxyy: Array4i
    yxyz: Array4i
    yxyw: Array4i
    yxzx: Array4i
    yxzy: Array4i
    yxzz: Array4i
    yxzw: Array4i
    yxwx: Array4i
    yxwy: Array4i
    yxwz: Array4i
    yxww: Array4i
    yyxx: Array4i
    yyxy: Array4i
    yyxz: Array4i
    yyxw: Array4i
    yyyx: Array4i
    yyyy: Array4i
    yyyz: Array4i
    yyyw: Array4i
    yyzx: Array4i
    yyzy: Array4i
    yyzz: Array4i
    yyzw: Array4i
    yywx: Array4i
    yywy: Array4i
    yywz: Array4i
    yyww: Array4i
    yzxx: Array4i
    yzxy: Array4i
    yzxz: Array4i
    yzxw: Array4i
    yzyx: Array4i
    yzyy: Array4i
    yzyz: Array4i
    yzyw: Array4i
    yzzx: Array4i
    yzzy: Array4i
    yzzz: Array4i
    yzzw: Array4i
    yzwx: Array4i
    yzwy: Array4i
    yzwz: Array4i
    yzww: Array4i
    ywxx: Array4i
    ywxy: Array4i
    ywxz: Array4i
    ywxw: Array4i
    ywyx: Array4i
    ywyy: Array4i
    ywyz: Array4i
    ywyw: Array4i
    ywzx: Array4i
    ywzy: Array4i
    ywzz: Array4i
    ywzw: Array4i
    ywwx: Array4i
    ywwy: Array4i
    ywwz: Array4i
    ywww: Array4i
    zxxx: Array4i
    zxxy: Array4i
    zxxz: Array4i
    zxxw: Array4i
    zxyx: Array4i
    zxyy: Array4i
    zxyz: Array4i
    zxyw: Array4i
    zxzx: Array4i
    zxzy: Array4i
    zxzz: Array4i
    zxzw: Array4i
    zxwx: Array4i
    zxwy: Array4i
    zxwz: Array4i
    zxww: Array4i
    zyxx: Array4i
    zyxy: Array4i
    zyxz: Array4i
    zyxw: Array4i
    zyyx: Array4i
    zyyy: Array4i
    zyyz: Array4i
    zyyw: Array4i
    zyzx: Array4i
    zyzy: Array4i
    zyzz: Array4i
    zyzw: Array4i
    zywx: Array4i
    zywy: Array4i
    zywz: Array4i
    zyww: Array4i
    zzxx: Array4i
    zzxy: Array4i
    zzxz: Array4i
    zzxw: Array4i
    zzyx: Array4i
    zzyy: Array4i
    zzyz: Array4i
    zzyw: Array4i
    zzzx: Array4i
    zzzy: Array4i
    zzzz: Array4i
    zzzw: Array4i
    zzwx: Array4i
    zzwy: Array4i
    zzwz: Array4i
    zzww: Array4i
    zwxx: Array4i
    zwxy: Array4i
    zwxz: Array4i
    zwxw: Array4i
    zwyx: Array4i
    zwyy: Array4i
    zwyz: Array4i
    zwyw: Array4i
    zwzx: Array4i
    zwzy: Array4i
    zwzz: Array4i
    zwzw: Array4i
    zwwx: Array4i
    zwwy: Array4i
    zwwz: Array4i
    zwww: Array4i
    wxxx: Array4i
    wxxy: Array4i
    wxxz: Array4i
    wxxw: Array4i
    wxyx: Array4i
    wxyy: Array4i
    wxyz: Array4i
    wxyw: Array4i
    wxzx: Array4i
    wxzy: Array4i
    wxzz: Array4i
    wxzw: Array4i
    wxwx: Array4i
    wxwy: Array4i
    wxwz: Array4i
    wxww: Array4i
    wyxx: Array4i
    wyxy: Array4i
    wyxz: Array4i
    wyxw: Array4i
    wyyx: Array4i
    wyyy: Array4i
    wyyz: Array4i
    wyyw: Array4i
    wyzx: Array4i
    wyzy: Array4i
    wyzz: Array4i
    wyzw: Array4i
    wywx: Array4i
    wywy: Array4i
    wywz: Array4i
    wyww: Array4i
    wzxx: Array4i
    wzxy: Array4i
    wzxz: Array4i
    wzxw: Array4i
    wzyx: Array4i
    wzyy: Array4i
    wzyz: Array4i
    wzyw: Array4i
    wzzx: Array4i
    wzzy: Array4i
    wzzz: Array4i
    wzzw: Array4i
    wzwx: Array4i
    wzwy: Array4i
    wzwz: Array4i
    wzww: Array4i
    wwxx: Array4i
    wwxy: Array4i
    wwxz: Array4i
    wwxw: Array4i
    wwyx: Array4i
    wwyy: Array4i
    wwyz: Array4i
    wwyw: Array4i
    wwzx: Array4i
    wwzy: Array4i
    wwzz: Array4i
    wwzw: Array4i
    wwwx: Array4i
    wwwy: Array4i
    wwwz: Array4i
    wwww: Array4i

_Array4uCp: TypeAlias = Union['Array4u', '_UIntCp', 'drjit.scalar._Array4uCp', 'drjit.llvm._Array4uCp', '_Array4iCp']

class Array4u(drjit.ArrayBase[Array4u, _Array4uCp, UInt, _UIntCp, UInt, Array4u, Array4b]):
    xx: Array2u
    xy: Array2u
    xz: Array2u
    xw: Array2u
    yx: Array2u
    yy: Array2u
    yz: Array2u
    yw: Array2u
    zx: Array2u
    zy: Array2u
    zz: Array2u
    zw: Array2u
    wx: Array2u
    wy: Array2u
    wz: Array2u
    ww: Array2u
    xxx: Array3u
    xxy: Array3u
    xxz: Array3u
    xxw: Array3u
    xyx: Array3u
    xyy: Array3u
    xyz: Array3u
    xyw: Array3u
    xzx: Array3u
    xzy: Array3u
    xzz: Array3u
    xzw: Array3u
    xwx: Array3u
    xwy: Array3u
    xwz: Array3u
    xww: Array3u
    yxx: Array3u
    yxy: Array3u
    yxz: Array3u
    yxw: Array3u
    yyx: Array3u
    yyy: Array3u
    yyz: Array3u
    yyw: Array3u
    yzx: Array3u
    yzy: Array3u
    yzz: Array3u
    yzw: Array3u
    ywx: Array3u
    ywy: Array3u
    ywz: Array3u
    yww: Array3u
    zxx: Array3u
    zxy: Array3u
    zxz: Array3u
    zxw: Array3u
    zyx: Array3u
    zyy: Array3u
    zyz: Array3u
    zyw: Array3u
    zzx: Array3u
    zzy: Array3u
    zzz: Array3u
    zzw: Array3u
    zwx: Array3u
    zwy: Array3u
    zwz: Array3u
    zww: Array3u
    wxx: Array3u
    wxy: Array3u
    wxz: Array3u
    wxw: Array3u
    wyx: Array3u
    wyy: Array3u
    wyz: Array3u
    wyw: Array3u
    wzx: Array3u
    wzy: Array3u
    wzz: Array3u
    wzw: Array3u
    wwx: Array3u
    wwy: Array3u
    wwz: Array3u
    www: Array3u
    xxxx: Array4u
    xxxy: Array4u
    xxxz: Array4u
    xxxw: Array4u
    xxyx: Array4u
    xxyy: Array4u
    xxyz: Array4u
    xxyw: Array4u
    xxzx: Array4u
    xxzy: Array4u
    xxzz: Array4u
    xxzw: Array4u
    xxwx: Array4u
    xxwy: Array4u
    xxwz: Array4u
    xxww: Array4u
    xyxx: Array4u
    xyxy: Array4u
    xyxz: Array4u
    xyxw: Array4u
    xyyx: Array4u
    xyyy: Array4u
    xyyz: Array4u
    xyyw: Array4u
    xyzx: Array4u
    xyzy: Array4u
    xyzz: Array4u
    xyzw: Array4u
    xywx: Array4u
    xywy: Array4u
    xywz: Array4u
    xyww: Array4u
    xzxx: Array4u
    xzxy: Array4u
    xzxz: Array4u
    xzxw: Array4u
    xzyx: Array4u
    xzyy: Array4u
    xzyz: Array4u
    xzyw: Array4u
    xzzx: Array4u
    xzzy: Array4u
    xzzz: Array4u
    xzzw: Array4u
    xzwx: Array4u
    xzwy: Array4u
    xzwz: Array4u
    xzww: Array4u
    xwxx: Array4u
    xwxy: Array4u
    xwxz: Array4u
    xwxw: Array4u
    xwyx: Array4u
    xwyy: Array4u
    xwyz: Array4u
    xwyw: Array4u
    xwzx: Array4u
    xwzy: Array4u
    xwzz: Array4u
    xwzw: Array4u
    xwwx: Array4u
    xwwy: Array4u
    xwwz: Array4u
    xwww: Array4u
    yxxx: Array4u
    yxxy: Array4u
    yxxz: Array4u
    yxxw: Array4u
    yxyx: Array4u
    yxyy: Array4u
    yxyz: Array4u
    yxyw: Array4u
    yxzx: Array4u
    yxzy: Array4u
    yxzz: Array4u
    yxzw: Array4u
    yxwx: Array4u
    yxwy: Array4u
    yxwz: Array4u
    yxww: Array4u
    yyxx: Array4u
    yyxy: Array4u
    yyxz: Array4u
    yyxw: Array4u
    yyyx: Array4u
    yyyy: Array4u
    yyyz: Array4u
    yyyw: Array4u
    yyzx: Array4u
    yyzy: Array4u
    yyzz: Array4u
    yyzw: Array4u
    yywx: Array4u
    yywy: Array4u
    yywz: Array4u
    yyww: Array4u
    yzxx: Array4u
    yzxy: Array4u
    yzxz: Array4u
    yzxw: Array4u
    yzyx: Array4u
    yzyy: Array4u
    yzyz: Array4u
    yzyw: Array4u
    yzzx: Array4u
    yzzy: Array4u
    yzzz: Array4u
    yzzw: Array4u
    yzwx: Array4u
    yzwy: Array4u
    yzwz: Array4u
    yzww: Array4u
    ywxx: Array4u
    ywxy: Array4u
    ywxz: Array4u
    ywxw: Array4u
    ywyx: Array4u
    ywyy: Array4u
    ywyz: Array4u
    ywyw: Array4u
    ywzx: Array4u
    ywzy: Array4u
    ywzz: Array4u
    ywzw: Array4u
    ywwx: Array4u
    ywwy: Array4u
    ywwz: Array4u
    ywww: Array4u
    zxxx: Array4u
    zxxy: Array4u
    zxxz: Array4u
    zxxw: Array4u
    zxyx: Array4u
    zxyy: Array4u
    zxyz: Array4u
    zxyw: Array4u
    zxzx: Array4u
    zxzy: Array4u
    zxzz: Array4u
    zxzw: Array4u
    zxwx: Array4u
    zxwy: Array4u
    zxwz: Array4u
    zxww: Array4u
    zyxx: Array4u
    zyxy: Array4u
    zyxz: Array4u
    zyxw: Array4u
    zyyx: Array4u
    zyyy: Array4u
    zyyz: Array4u
    zyyw: Array4u
    zyzx: Array4u
    zyzy: Array4u
    zyzz: Array4u
    zyzw: Array4u
    zywx: Array4u
    zywy: Array4u
    zywz: Array4u
    zyww: Array4u
    zzxx: Array4u
    zzxy: Array4u
    zzxz: Array4u
    zzxw: Array4u
    zzyx: Array4u
    zzyy: Array4u
    zzyz: Array4u
    zzyw: Array4u
    zzzx: Array4u
    zzzy: Array4u
    zzzz: Array4u
    zzzw: Array4u
    zzwx: Array4u
    zzwy: Array4u
    zzwz: Array4u
    zzww: Array4u
    zwxx: Array4u
    zwxy: Array4u
    zwxz: Array4u
    zwxw: Array4u
    zwyx: Array4u
    zwyy: Array4u
    zwyz: Array4u
    zwyw: Array4u
    zwzx: Array4u
    zwzy: Array4u
    zwzz: Array4u
    zwzw: Array4u
    zwwx: Array4u
    zwwy: Array4u
    zwwz: Array4u
    zwww: Array4u
    wxxx: Array4u
    wxxy: Array4u
    wxxz: Array4u
    wxxw: Array4u
    wxyx: Array4u
    wxyy: Array4u
    wxyz: Array4u
    wxyw: Array4u
    wxzx: Array4u
    wxzy: Array4u
    wxzz: Array4u
    wxzw: Array4u
    wxwx: Array4u
    wxwy: Array4u
    wxwz: Array4u
    wxww: Array4u
    wyxx: Array4u
    wyxy: Array4u
    wyxz: Array4u
    wyxw: Array4u
    wyyx: Array4u
    wyyy: Array4u
    wyyz: Array4u
    wyyw: Array4u
    wyzx: Array4u
    wyzy: Array4u
    wyzz: Array4u
    wyzw: Array4u
    wywx: Array4u
    wywy: Array4u
    wywz: Array4u
    wyww: Array4u
    wzxx: Array4u
    wzxy: Array4u
    wzxz: Array4u
    wzxw: Array4u
    wzyx: Array4u
    wzyy: Array4u
    wzyz: Array4u
    wzyw: Array4u
    wzzx: Array4u
    wzzy: Array4u
    wzzz: Array4u
    wzzw: Array4u
    wzwx: Array4u
    wzwy: Array4u
    wzwz: Array4u
    wzww: Array4u
    wwxx: Array4u
    wwxy: Array4u
    wwxz: Array4u
    wwxw: Array4u
    wwyx: Array4u
    wwyy: Array4u
    wwyz: Array4u
    wwyw: Array4u
    wwzx: Array4u
    wwzy: Array4u
    wwzz: Array4u
    wwzw: Array4u
    wwwx: Array4u
    wwwy: Array4u
    wwwz: Array4u
    wwww: Array4u

_Array4i64Cp: TypeAlias = Union['Array4i64', '_Int64Cp', 'drjit.scalar._Array4i64Cp', 'drjit.llvm._Array4i64Cp', '_Array4uCp']

class Array4i64(drjit.ArrayBase[Array4i64, _Array4i64Cp, Int64, _Int64Cp, Int64, Array4i64, Array4b]):
    xx: Array2i64
    xy: Array2i64
    xz: Array2i64
    xw: Array2i64
    yx: Array2i64
    yy: Array2i64
    yz: Array2i64
    yw: Array2i64
    zx: Array2i64
    zy: Array2i64
    zz: Array2i64
    zw: Array2i64
    wx: Array2i64
    wy: Array2i64
    wz: Array2i64
    ww: Array2i64
    xxx: Array3i64
    xxy: Array3i64
    xxz: Array3i64
    xxw: Array3i64
    xyx: Array3i64
    xyy: Array3i64
    xyz: Array3i64
    xyw: Array3i64
    xzx: Array3i64
    xzy: Array3i64
    xzz: Array3i64
    xzw: Array3i64
    xwx: Array3i64
    xwy: Array3i64
    xwz: Array3i64
    xww: Array3i64
    yxx: Array3i64
    yxy: Array3i64
    yxz: Array3i64
    yxw: Array3i64
    yyx: Array3i64
    yyy: Array3i64
    yyz: Array3i64
    yyw: Array3i64
    yzx: Array3i64
    yzy: Array3i64
    yzz: Array3i64
    yzw: Array3i64
    ywx: Array3i64
    ywy: Array3i64
    ywz: Array3i64
    yww: Array3i64
    zxx: Array3i64
    zxy: Array3i64
    zxz: Array3i64
    zxw: Array3i64
    zyx: Array3i64
    zyy: Array3i64
    zyz: Array3i64
    zyw: Array3i64
    zzx: Array3i64
    zzy: Array3i64
    zzz: Array3i64
    zzw: Array3i64
    zwx: Array3i64
    zwy: Array3i64
    zwz: Array3i64
    zww: Array3i64
    wxx: Array3i64
    wxy: Array3i64
    wxz: Array3i64
    wxw: Array3i64
    wyx: Array3i64
    wyy: Array3i64
    wyz: Array3i64
    wyw: Array3i64
    wzx: Array3i64
    wzy: Array3i64
    wzz: Array3i64
    wzw: Array3i64
    wwx: Array3i64
    wwy: Array3i64
    wwz: Array3i64
    www: Array3i64
    xxxx: Array4i64
    xxxy: Array4i64
    xxxz: Array4i64
    xxxw: Array4i64
    xxyx: Array4i64
    xxyy: Array4i64
    xxyz: Array4i64
    xxyw: Array4i64
    xxzx: Array4i64
    xxzy: Array4i64
    xxzz: Array4i64
    xxzw: Array4i64
    xxwx: Array4i64
    xxwy: Array4i64
    xxwz: Array4i64
    xxww: Array4i64
    xyxx: Array4i64
    xyxy: Array4i64
    xyxz: Array4i64
    xyxw: Array4i64
    xyyx: Array4i64
    xyyy: Array4i64
    xyyz: Array4i64
    xyyw: Array4i64
    xyzx: Array4i64
    xyzy: Array4i64
    xyzz: Array4i64
    xyzw: Array4i64
    xywx: Array4i64
    xywy: Array4i64
    xywz: Array4i64
    xyww: Array4i64
    xzxx: Array4i64
    xzxy: Array4i64
    xzxz: Array4i64
    xzxw: Array4i64
    xzyx: Array4i64
    xzyy: Array4i64
    xzyz: Array4i64
    xzyw: Array4i64
    xzzx: Array4i64
    xzzy: Array4i64
    xzzz: Array4i64
    xzzw: Array4i64
    xzwx: Array4i64
    xzwy: Array4i64
    xzwz: Array4i64
    xzww: Array4i64
    xwxx: Array4i64
    xwxy: Array4i64
    xwxz: Array4i64
    xwxw: Array4i64
    xwyx: Array4i64
    xwyy: Array4i64
    xwyz: Array4i64
    xwyw: Array4i64
    xwzx: Array4i64
    xwzy: Array4i64
    xwzz: Array4i64
    xwzw: Array4i64
    xwwx: Array4i64
    xwwy: Array4i64
    xwwz: Array4i64
    xwww: Array4i64
    yxxx: Array4i64
    yxxy: Array4i64
    yxxz: Array4i64
    yxxw: Array4i64
    yxyx: Array4i64
    yxyy: Array4i64
    yxyz: Array4i64
    yxyw: Array4i64
    yxzx: Array4i64
    yxzy: Array4i64
    yxzz: Array4i64
    yxzw: Array4i64
    yxwx: Array4i64
    yxwy: Array4i64
    yxwz: Array4i64
    yxww: Array4i64
    yyxx: Array4i64
    yyxy: Array4i64
    yyxz: Array4i64
    yyxw: Array4i64
    yyyx: Array4i64
    yyyy: Array4i64
    yyyz: Array4i64
    yyyw: Array4i64
    yyzx: Array4i64
    yyzy: Array4i64
    yyzz: Array4i64
    yyzw: Array4i64
    yywx: Array4i64
    yywy: Array4i64
    yywz: Array4i64
    yyww: Array4i64
    yzxx: Array4i64
    yzxy: Array4i64
    yzxz: Array4i64
    yzxw: Array4i64
    yzyx: Array4i64
    yzyy: Array4i64
    yzyz: Array4i64
    yzyw: Array4i64
    yzzx: Array4i64
    yzzy: Array4i64
    yzzz: Array4i64
    yzzw: Array4i64
    yzwx: Array4i64
    yzwy: Array4i64
    yzwz: Array4i64
    yzww: Array4i64
    ywxx: Array4i64
    ywxy: Array4i64
    ywxz: Array4i64
    ywxw: Array4i64
    ywyx: Array4i64
    ywyy: Array4i64
    ywyz: Array4i64
    ywyw: Array4i64
    ywzx: Array4i64
    ywzy: Array4i64
    ywzz: Array4i64
    ywzw: Array4i64
    ywwx: Array4i64
    ywwy: Array4i64
    ywwz: Array4i64
    ywww: Array4i64
    zxxx: Array4i64
    zxxy: Array4i64
    zxxz: Array4i64
    zxxw: Array4i64
    zxyx: Array4i64
    zxyy: Array4i64
    zxyz: Array4i64
    zxyw: Array4i64
    zxzx: Array4i64
    zxzy: Array4i64
    zxzz: Array4i64
    zxzw: Array4i64
    zxwx: Array4i64
    zxwy: Array4i64
    zxwz: Array4i64
    zxww: Array4i64
    zyxx: Array4i64
    zyxy: Array4i64
    zyxz: Array4i64
    zyxw: Array4i64
    zyyx: Array4i64
    zyyy: Array4i64
    zyyz: Array4i64
    zyyw: Array4i64
    zyzx: Array4i64
    zyzy: Array4i64
    zyzz: Array4i64
    zyzw: Array4i64
    zywx: Array4i64
    zywy: Array4i64
    zywz: Array4i64
    zyww: Array4i64
    zzxx: Array4i64
    zzxy: Array4i64
    zzxz: Array4i64
    zzxw: Array4i64
    zzyx: Array4i64
    zzyy: Array4i64
    zzyz: Array4i64
    zzyw: Array4i64
    zzzx: Array4i64
    zzzy: Array4i64
    zzzz: Array4i64
    zzzw: Array4i64
    zzwx: Array4i64
    zzwy: Array4i64
    zzwz: Array4i64
    zzww: Array4i64
    zwxx: Array4i64
    zwxy: Array4i64
    zwxz: Array4i64
    zwxw: Array4i64
    zwyx: Array4i64
    zwyy: Array4i64
    zwyz: Array4i64
    zwyw: Array4i64
    zwzx: Array4i64
    zwzy: Array4i64
    zwzz: Array4i64
    zwzw: Array4i64
    zwwx: Array4i64
    zwwy: Array4i64
    zwwz: Array4i64
    zwww: Array4i64
    wxxx: Array4i64
    wxxy: Array4i64
    wxxz: Array4i64
    wxxw: Array4i64
    wxyx: Array4i64
    wxyy: Array4i64
    wxyz: Array4i64
    wxyw: Array4i64
    wxzx: Array4i64
    wxzy: Array4i64
    wxzz: Array4i64
    wxzw: Array4i64
    wxwx: Array4i64
    wxwy: Array4i64
    wxwz: Array4i64
    wxww: Array4i64
    wyxx: Array4i64
    wyxy: Array4i64
    wyxz: Array4i64
    wyxw: Array4i64
    wyyx: Array4i64
    wyyy: Array4i64
    wyyz: Array4i64
    wyyw: Array4i64
    wyzx: Array4i64
    wyzy: Array4i64
    wyzz: Array4i64
    wyzw: Array4i64
    wywx: Array4i64
    wywy: Array4i64
    wywz: Array4i64
    wyww: Array4i64
    wzxx: Array4i64
    wzxy: Array4i64
    wzxz: Array4i64
    wzxw: Array4i64
    wzyx: Array4i64
    wzyy: Array4i64
    wzyz: Array4i64
    wzyw: Array4i64
    wzzx: Array4i64
    wzzy: Array4i64
    wzzz: Array4i64
    wzzw: Array4i64
    wzwx: Array4i64
    wzwy: Array4i64
    wzwz: Array4i64
    wzww: Array4i64
    wwxx: Array4i64
    wwxy: Array4i64
    wwxz: Array4i64
    wwxw: Array4i64
    wwyx: Array4i64
    wwyy: Array4i64
    wwyz: Array4i64
    wwyw: Array4i64
    wwzx: Array4i64
    wwzy: Array4i64
    wwzz: Array4i64
    wwzw: Array4i64
    wwwx: Array4i64
    wwwy: Array4i64
    wwwz: Array4i64
    wwww: Array4i64

_Array4u64Cp: TypeAlias = Union['Array4u64', '_UInt64Cp', 'drjit.scalar._Array4u64Cp', 'drjit.llvm._Array4u64Cp', '_Array4i64Cp']

class Array4u64(drjit.ArrayBase[Array4u64, _Array4u64Cp, UInt64, _UInt64Cp, UInt64, Array4u64, Array4b]):
    xx: Array2u64
    xy: Array2u64
    xz: Array2u64
    xw: Array2u64
    yx: Array2u64
    yy: Array2u64
    yz: Array2u64
    yw: Array2u64
    zx: Array2u64
    zy: Array2u64
    zz: Array2u64
    zw: Array2u64
    wx: Array2u64
    wy: Array2u64
    wz: Array2u64
    ww: Array2u64
    xxx: Array3u64
    xxy: Array3u64
    xxz: Array3u64
    xxw: Array3u64
    xyx: Array3u64
    xyy: Array3u64
    xyz: Array3u64
    xyw: Array3u64
    xzx: Array3u64
    xzy: Array3u64
    xzz: Array3u64
    xzw: Array3u64
    xwx: Array3u64
    xwy: Array3u64
    xwz: Array3u64
    xww: Array3u64
    yxx: Array3u64
    yxy: Array3u64
    yxz: Array3u64
    yxw: Array3u64
    yyx: Array3u64
    yyy: Array3u64
    yyz: Array3u64
    yyw: Array3u64
    yzx: Array3u64
    yzy: Array3u64
    yzz: Array3u64
    yzw: Array3u64
    ywx: Array3u64
    ywy: Array3u64
    ywz: Array3u64
    yww: Array3u64
    zxx: Array3u64
    zxy: Array3u64
    zxz: Array3u64
    zxw: Array3u64
    zyx: Array3u64
    zyy: Array3u64
    zyz: Array3u64
    zyw: Array3u64
    zzx: Array3u64
    zzy: Array3u64
    zzz: Array3u64
    zzw: Array3u64
    zwx: Array3u64
    zwy: Array3u64
    zwz: Array3u64
    zww: Array3u64
    wxx: Array3u64
    wxy: Array3u64
    wxz: Array3u64
    wxw: Array3u64
    wyx: Array3u64
    wyy: Array3u64
    wyz: Array3u64
    wyw: Array3u64
    wzx: Array3u64
    wzy: Array3u64
    wzz: Array3u64
    wzw: Array3u64
    wwx: Array3u64
    wwy: Array3u64
    wwz: Array3u64
    www: Array3u64
    xxxx: Array4u64
    xxxy: Array4u64
    xxxz: Array4u64
    xxxw: Array4u64
    xxyx: Array4u64
    xxyy: Array4u64
    xxyz: Array4u64
    xxyw: Array4u64
    xxzx: Array4u64
    xxzy: Array4u64
    xxzz: Array4u64
    xxzw: Array4u64
    xxwx: Array4u64
    xxwy: Array4u64
    xxwz: Array4u64
    xxww: Array4u64
    xyxx: Array4u64
    xyxy: Array4u64
    xyxz: Array4u64
    xyxw: Array4u64
    xyyx: Array4u64
    xyyy: Array4u64
    xyyz: Array4u64
    xyyw: Array4u64
    xyzx: Array4u64
    xyzy: Array4u64
    xyzz: Array4u64
    xyzw: Array4u64
    xywx: Array4u64
    xywy: Array4u64
    xywz: Array4u64
    xyww: Array4u64
    xzxx: Array4u64
    xzxy: Array4u64
    xzxz: Array4u64
    xzxw: Array4u64
    xzyx: Array4u64
    xzyy: Array4u64
    xzyz: Array4u64
    xzyw: Array4u64
    xzzx: Array4u64
    xzzy: Array4u64
    xzzz: Array4u64
    xzzw: Array4u64
    xzwx: Array4u64
    xzwy: Array4u64
    xzwz: Array4u64
    xzww: Array4u64
    xwxx: Array4u64
    xwxy: Array4u64
    xwxz: Array4u64
    xwxw: Array4u64
    xwyx: Array4u64
    xwyy: Array4u64
    xwyz: Array4u64
    xwyw: Array4u64
    xwzx: Array4u64
    xwzy: Array4u64
    xwzz: Array4u64
    xwzw: Array4u64
    xwwx: Array4u64
    xwwy: Array4u64
    xwwz: Array4u64
    xwww: Array4u64
    yxxx: Array4u64
    yxxy: Array4u64
    yxxz: Array4u64
    yxxw: Array4u64
    yxyx: Array4u64
    yxyy: Array4u64
    yxyz: Array4u64
    yxyw: Array4u64
    yxzx: Array4u64
    yxzy: Array4u64
    yxzz: Array4u64
    yxzw: Array4u64
    yxwx: Array4u64
    yxwy: Array4u64
    yxwz: Array4u64
    yxww: Array4u64
    yyxx: Array4u64
    yyxy: Array4u64
    yyxz: Array4u64
    yyxw: Array4u64
    yyyx: Array4u64
    yyyy: Array4u64
    yyyz: Array4u64
    yyyw: Array4u64
    yyzx: Array4u64
    yyzy: Array4u64
    yyzz: Array4u64
    yyzw: Array4u64
    yywx: Array4u64
    yywy: Array4u64
    yywz: Array4u64
    yyww: Array4u64
    yzxx: Array4u64
    yzxy: Array4u64
    yzxz: Array4u64
    yzxw: Array4u64
    yzyx: Array4u64
    yzyy: Array4u64
    yzyz: Array4u64
    yzyw: Array4u64
    yzzx: Array4u64
    yzzy: Array4u64
    yzzz: Array4u64
    yzzw: Array4u64
    yzwx: Array4u64
    yzwy: Array4u64
    yzwz: Array4u64
    yzww: Array4u64
    ywxx: Array4u64
    ywxy: Array4u64
    ywxz: Array4u64
    ywxw: Array4u64
    ywyx: Array4u64
    ywyy: Array4u64
    ywyz: Array4u64
    ywyw: Array4u64
    ywzx: Array4u64
    ywzy: Array4u64
    ywzz: Array4u64
    ywzw: Array4u64
    ywwx: Array4u64
    ywwy: Array4u64
    ywwz: Array4u64
    ywww: Array4u64
    zxxx: Array4u64
    zxxy: Array4u64
    zxxz: Array4u64
    zxxw: Array4u64
    zxyx: Array4u64
    zxyy: Array4u64
    zxyz: Array4u64
    zxyw: Array4u64
    zxzx: Array4u64
    zxzy: Array4u64
    zxzz: Array4u64
    zxzw: Array4u64
    zxwx: Array4u64
    zxwy: Array4u64
    zxwz: Array4u64
    zxww: Array4u64
    zyxx: Array4u64
    zyxy: Array4u64
    zyxz: Array4u64
    zyxw: Array4u64
    zyyx: Array4u64
    zyyy: Array4u64
    zyyz: Array4u64
    zyyw: Array4u64
    zyzx: Array4u64
    zyzy: Array4u64
    zyzz: Array4u64
    zyzw: Array4u64
    zywx: Array4u64
    zywy: Array4u64
    zywz: Array4u64
    zyww: Array4u64
    zzxx: Array4u64
    zzxy: Array4u64
    zzxz: Array4u64
    zzxw: Array4u64
    zzyx: Array4u64
    zzyy: Array4u64
    zzyz: Array4u64
    zzyw: Array4u64
    zzzx: Array4u64
    zzzy: Array4u64
    zzzz: Array4u64
    zzzw: Array4u64
    zzwx: Array4u64
    zzwy: Array4u64
    zzwz: Array4u64
    zzww: Array4u64
    zwxx: Array4u64
    zwxy: Array4u64
    zwxz: Array4u64
    zwxw: Array4u64
    zwyx: Array4u64
    zwyy: Array4u64
    zwyz: Array4u64
    zwyw: Array4u64
    zwzx: Array4u64
    zwzy: Array4u64
    zwzz: Array4u64
    zwzw: Array4u64
    zwwx: Array4u64
    zwwy: Array4u64
    zwwz: Array4u64
    zwww: Array4u64
    wxxx: Array4u64
    wxxy: Array4u64
    wxxz: Array4u64
    wxxw: Array4u64
    wxyx: Array4u64
    wxyy: Array4u64
    wxyz: Array4u64
    wxyw: Array4u64
    wxzx: Array4u64
    wxzy: Array4u64
    wxzz: Array4u64
    wxzw: Array4u64
    wxwx: Array4u64
    wxwy: Array4u64
    wxwz: Array4u64
    wxww: Array4u64
    wyxx: Array4u64
    wyxy: Array4u64
    wyxz: Array4u64
    wyxw: Array4u64
    wyyx: Array4u64
    wyyy: Array4u64
    wyyz: Array4u64
    wyyw: Array4u64
    wyzx: Array4u64
    wyzy: Array4u64
    wyzz: Array4u64
    wyzw: Array4u64
    wywx: Array4u64
    wywy: Array4u64
    wywz: Array4u64
    wyww: Array4u64
    wzxx: Array4u64
    wzxy: Array4u64
    wzxz: Array4u64
    wzxw: Array4u64
    wzyx: Array4u64
    wzyy: Array4u64
    wzyz: Array4u64
    wzyw: Array4u64
    wzzx: Array4u64
    wzzy: Array4u64
    wzzz: Array4u64
    wzzw: Array4u64
    wzwx: Array4u64
    wzwy: Array4u64
    wzwz: Array4u64
    wzww: Array4u64
    wwxx: Array4u64
    wwxy: Array4u64
    wwxz: Array4u64
    wwxw: Array4u64
    wwyx: Array4u64
    wwyy: Array4u64
    wwyz: Array4u64
    wwyw: Array4u64
    wwzx: Array4u64
    wwzy: Array4u64
    wwzz: Array4u64
    wwzw: Array4u64
    wwwx: Array4u64
    wwwy: Array4u64
    wwwz: Array4u64
    wwww: Array4u64

_Array4f16Cp: TypeAlias = Union['Array4f16', '_Float16Cp', 'drjit.scalar._Array4f16Cp', 'drjit.llvm._Array4f16Cp', '_Array4u64Cp']

class Array4f16(drjit.ArrayBase[Array4f16, _Array4f16Cp, Float16, _Float16Cp, Float16, Array4f16, Array4b]):
    xx: Array2f16
    xy: Array2f16
    xz: Array2f16
    xw: Array2f16
    yx: Array2f16
    yy: Array2f16
    yz: Array2f16
    yw: Array2f16
    zx: Array2f16
    zy: Array2f16
    zz: Array2f16
    zw: Array2f16
    wx: Array2f16
    wy: Array2f16
    wz: Array2f16
    ww: Array2f16
    xxx: Array3f16
    xxy: Array3f16
    xxz: Array3f16
    xxw: Array3f16
    xyx: Array3f16
    xyy: Array3f16
    xyz: Array3f16
    xyw: Array3f16
    xzx: Array3f16
    xzy: Array3f16
    xzz: Array3f16
    xzw: Array3f16
    xwx: Array3f16
    xwy: Array3f16
    xwz: Array3f16
    xww: Array3f16
    yxx: Array3f16
    yxy: Array3f16
    yxz: Array3f16
    yxw: Array3f16
    yyx: Array3f16
    yyy: Array3f16
    yyz: Array3f16
    yyw: Array3f16
    yzx: Array3f16
    yzy: Array3f16
    yzz: Array3f16
    yzw: Array3f16
    ywx: Array3f16
    ywy: Array3f16
    ywz: Array3f16
    yww: Array3f16
    zxx: Array3f16
    zxy: Array3f16
    zxz: Array3f16
    zxw: Array3f16
    zyx: Array3f16
    zyy: Array3f16
    zyz: Array3f16
    zyw: Array3f16
    zzx: Array3f16
    zzy: Array3f16
    zzz: Array3f16
    zzw: Array3f16
    zwx: Array3f16
    zwy: Array3f16
    zwz: Array3f16
    zww: Array3f16
    wxx: Array3f16
    wxy: Array3f16
    wxz: Array3f16
    wxw: Array3f16
    wyx: Array3f16
    wyy: Array3f16
    wyz: Array3f16
    wyw: Array3f16
    wzx: Array3f16
    wzy: Array3f16
    wzz: Array3f16
    wzw: Array3f16
    wwx: Array3f16
    wwy: Array3f16
    wwz: Array3f16
    www: Array3f16
    xxxx: Array4f16
    xxxy: Array4f16
    xxxz: Array4f16
    xxxw: Array4f16
    xxyx: Array4f16
    xxyy: Array4f16
    xxyz: Array4f16
    xxyw: Array4f16
    xxzx: Array4f16
    xxzy: Array4f16
    xxzz: Array4f16
    xxzw: Array4f16
    xxwx: Array4f16
    xxwy: Array4f16
    xxwz: Array4f16
    xxww: Array4f16
    xyxx: Array4f16
    xyxy: Array4f16
    xyxz: Array4f16
    xyxw: Array4f16
    xyyx: Array4f16
    xyyy: Array4f16
    xyyz: Array4f16
    xyyw: Array4f16
    xyzx: Array4f16
    xyzy: Array4f16
    xyzz: Array4f16
    xyzw: Array4f16
    xywx: Array4f16
    xywy: Array4f16
    xywz: Array4f16
    xyww: Array4f16
    xzxx: Array4f16
    xzxy: Array4f16
    xzxz: Array4f16
    xzxw: Array4f16
    xzyx: Array4f16
    xzyy: Array4f16
    xzyz: Array4f16
    xzyw: Array4f16
    xzzx: Array4f16
    xzzy: Array4f16
    xzzz: Array4f16
    xzzw: Array4f16
    xzwx: Array4f16
    xzwy: Array4f16
    xzwz: Array4f16
    xzww: Array4f16
    xwxx: Array4f16
    xwxy: Array4f16
    xwxz: Array4f16
    xwxw: Array4f16
    xwyx: Array4f16
    xwyy: Array4f16
    xwyz: Array4f16
    xwyw: Array4f16
    xwzx: Array4f16
    xwzy: Array4f16
    xwzz: Array4f16
    xwzw: Array4f16
    xwwx: Array4f16
    xwwy: Array4f16
    xwwz: Array4f16
    xwww: Array4f16
    yxxx: Array4f16
    yxxy: Array4f16
    yxxz: Array4f16
    yxxw: Array4f16
    yxyx: Array4f16
    yxyy: Array4f16
    yxyz: Array4f16
    yxyw: Array4f16
    yxzx: Array4f16
    yxzy: Array4f16
    yxzz: Array4f16
    yxzw: Array4f16
    yxwx: Array4f16
    yxwy: Array4f16
    yxwz: Array4f16
    yxww: Array4f16
    yyxx: Array4f16
    yyxy: Array4f16
    yyxz: Array4f16
    yyxw: Array4f16
    yyyx: Array4f16
    yyyy: Array4f16
    yyyz: Array4f16
    yyyw: Array4f16
    yyzx: Array4f16
    yyzy: Array4f16
    yyzz: Array4f16
    yyzw: Array4f16
    yywx: Array4f16
    yywy: Array4f16
    yywz: Array4f16
    yyww: Array4f16
    yzxx: Array4f16
    yzxy: Array4f16
    yzxz: Array4f16
    yzxw: Array4f16
    yzyx: Array4f16
    yzyy: Array4f16
    yzyz: Array4f16
    yzyw: Array4f16
    yzzx: Array4f16
    yzzy: Array4f16
    yzzz: Array4f16
    yzzw: Array4f16
    yzwx: Array4f16
    yzwy: Array4f16
    yzwz: Array4f16
    yzww: Array4f16
    ywxx: Array4f16
    ywxy: Array4f16
    ywxz: Array4f16
    ywxw: Array4f16
    ywyx: Array4f16
    ywyy: Array4f16
    ywyz: Array4f16
    ywyw: Array4f16
    ywzx: Array4f16
    ywzy: Array4f16
    ywzz: Array4f16
    ywzw: Array4f16
    ywwx: Array4f16
    ywwy: Array4f16
    ywwz: Array4f16
    ywww: Array4f16
    zxxx: Array4f16
    zxxy: Array4f16
    zxxz: Array4f16
    zxxw: Array4f16
    zxyx: Array4f16
    zxyy: Array4f16
    zxyz: Array4f16
    zxyw: Array4f16
    zxzx: Array4f16
    zxzy: Array4f16
    zxzz: Array4f16
    zxzw: Array4f16
    zxwx: Array4f16
    zxwy: Array4f16
    zxwz: Array4f16
    zxww: Array4f16
    zyxx: Array4f16
    zyxy: Array4f16
    zyxz: Array4f16
    zyxw: Array4f16
    zyyx: Array4f16
    zyyy: Array4f16
    zyyz: Array4f16
    zyyw: Array4f16
    zyzx: Array4f16
    zyzy: Array4f16
    zyzz: Array4f16
    zyzw: Array4f16
    zywx: Array4f16
    zywy: Array4f16
    zywz: Array4f16
    zyww: Array4f16
    zzxx: Array4f16
    zzxy: Array4f16
    zzxz: Array4f16
    zzxw: Array4f16
    zzyx: Array4f16
    zzyy: Array4f16
    zzyz: Array4f16
    zzyw: Array4f16
    zzzx: Array4f16
    zzzy: Array4f16
    zzzz: Array4f16
    zzzw: Array4f16
    zzwx: Array4f16
    zzwy: Array4f16
    zzwz: Array4f16
    zzww: Array4f16
    zwxx: Array4f16
    zwxy: Array4f16
    zwxz: Array4f16
    zwxw: Array4f16
    zwyx: Array4f16
    zwyy: Array4f16
    zwyz: Array4f16
    zwyw: Array4f16
    zwzx: Array4f16
    zwzy: Array4f16
    zwzz: Array4f16
    zwzw: Array4f16
    zwwx: Array4f16
    zwwy: Array4f16
    zwwz: Array4f16
    zwww: Array4f16
    wxxx: Array4f16
    wxxy: Array4f16
    wxxz: Array4f16
    wxxw: Array4f16
    wxyx: Array4f16
    wxyy: Array4f16
    wxyz: Array4f16
    wxyw: Array4f16
    wxzx: Array4f16
    wxzy: Array4f16
    wxzz: Array4f16
    wxzw: Array4f16
    wxwx: Array4f16
    wxwy: Array4f16
    wxwz: Array4f16
    wxww: Array4f16
    wyxx: Array4f16
    wyxy: Array4f16
    wyxz: Array4f16
    wyxw: Array4f16
    wyyx: Array4f16
    wyyy: Array4f16
    wyyz: Array4f16
    wyyw: Array4f16
    wyzx: Array4f16
    wyzy: Array4f16
    wyzz: Array4f16
    wyzw: Array4f16
    wywx: Array4f16
    wywy: Array4f16
    wywz: Array4f16
    wyww: Array4f16
    wzxx: Array4f16
    wzxy: Array4f16
    wzxz: Array4f16
    wzxw: Array4f16
    wzyx: Array4f16
    wzyy: Array4f16
    wzyz: Array4f16
    wzyw: Array4f16
    wzzx: Array4f16
    wzzy: Array4f16
    wzzz: Array4f16
    wzzw: Array4f16
    wzwx: Array4f16
    wzwy: Array4f16
    wzwz: Array4f16
    wzww: Array4f16
    wwxx: Array4f16
    wwxy: Array4f16
    wwxz: Array4f16
    wwxw: Array4f16
    wwyx: Array4f16
    wwyy: Array4f16
    wwyz: Array4f16
    wwyw: Array4f16
    wwzx: Array4f16
    wwzy: Array4f16
    wwzz: Array4f16
    wwzw: Array4f16
    wwwx: Array4f16
    wwwy: Array4f16
    wwwz: Array4f16
    wwww: Array4f16

_Array4fCp: TypeAlias = Union['Array4f', '_FloatCp', 'drjit.scalar._Array4fCp', 'drjit.llvm._Array4fCp', '_Array4f16Cp']

class Array4f(drjit.ArrayBase[Array4f, _Array4fCp, Float, _FloatCp, Float, Array4f, Array4b]):
    xx: Array2f
    xy: Array2f
    xz: Array2f
    xw: Array2f
    yx: Array2f
    yy: Array2f
    yz: Array2f
    yw: Array2f
    zx: Array2f
    zy: Array2f
    zz: Array2f
    zw: Array2f
    wx: Array2f
    wy: Array2f
    wz: Array2f
    ww: Array2f
    xxx: Array3f
    xxy: Array3f
    xxz: Array3f
    xxw: Array3f
    xyx: Array3f
    xyy: Array3f
    xyz: Array3f
    xyw: Array3f
    xzx: Array3f
    xzy: Array3f
    xzz: Array3f
    xzw: Array3f
    xwx: Array3f
    xwy: Array3f
    xwz: Array3f
    xww: Array3f
    yxx: Array3f
    yxy: Array3f
    yxz: Array3f
    yxw: Array3f
    yyx: Array3f
    yyy: Array3f
    yyz: Array3f
    yyw: Array3f
    yzx: Array3f
    yzy: Array3f
    yzz: Array3f
    yzw: Array3f
    ywx: Array3f
    ywy: Array3f
    ywz: Array3f
    yww: Array3f
    zxx: Array3f
    zxy: Array3f
    zxz: Array3f
    zxw: Array3f
    zyx: Array3f
    zyy: Array3f
    zyz: Array3f
    zyw: Array3f
    zzx: Array3f
    zzy: Array3f
    zzz: Array3f
    zzw: Array3f
    zwx: Array3f
    zwy: Array3f
    zwz: Array3f
    zww: Array3f
    wxx: Array3f
    wxy: Array3f
    wxz: Array3f
    wxw: Array3f
    wyx: Array3f
    wyy: Array3f
    wyz: Array3f
    wyw: Array3f
    wzx: Array3f
    wzy: Array3f
    wzz: Array3f
    wzw: Array3f
    wwx: Array3f
    wwy: Array3f
    wwz: Array3f
    www: Array3f
    xxxx: Array4f
    xxxy: Array4f
    xxxz: Array4f
    xxxw: Array4f
    xxyx: Array4f
    xxyy: Array4f
    xxyz: Array4f
    xxyw: Array4f
    xxzx: Array4f
    xxzy: Array4f
    xxzz: Array4f
    xxzw: Array4f
    xxwx: Array4f
    xxwy: Array4f
    xxwz: Array4f
    xxww: Array4f
    xyxx: Array4f
    xyxy: Array4f
    xyxz: Array4f
    xyxw: Array4f
    xyyx: Array4f
    xyyy: Array4f
    xyyz: Array4f
    xyyw: Array4f
    xyzx: Array4f
    xyzy: Array4f
    xyzz: Array4f
    xyzw: Array4f
    xywx: Array4f
    xywy: Array4f
    xywz: Array4f
    xyww: Array4f
    xzxx: Array4f
    xzxy: Array4f
    xzxz: Array4f
    xzxw: Array4f
    xzyx: Array4f
    xzyy: Array4f
    xzyz: Array4f
    xzyw: Array4f
    xzzx: Array4f
    xzzy: Array4f
    xzzz: Array4f
    xzzw: Array4f
    xzwx: Array4f
    xzwy: Array4f
    xzwz: Array4f
    xzww: Array4f
    xwxx: Array4f
    xwxy: Array4f
    xwxz: Array4f
    xwxw: Array4f
    xwyx: Array4f
    xwyy: Array4f
    xwyz: Array4f
    xwyw: Array4f
    xwzx: Array4f
    xwzy: Array4f
    xwzz: Array4f
    xwzw: Array4f
    xwwx: Array4f
    xwwy: Array4f
    xwwz: Array4f
    xwww: Array4f
    yxxx: Array4f
    yxxy: Array4f
    yxxz: Array4f
    yxxw: Array4f
    yxyx: Array4f
    yxyy: Array4f
    yxyz: Array4f
    yxyw: Array4f
    yxzx: Array4f
    yxzy: Array4f
    yxzz: Array4f
    yxzw: Array4f
    yxwx: Array4f
    yxwy: Array4f
    yxwz: Array4f
    yxww: Array4f
    yyxx: Array4f
    yyxy: Array4f
    yyxz: Array4f
    yyxw: Array4f
    yyyx: Array4f
    yyyy: Array4f
    yyyz: Array4f
    yyyw: Array4f
    yyzx: Array4f
    yyzy: Array4f
    yyzz: Array4f
    yyzw: Array4f
    yywx: Array4f
    yywy: Array4f
    yywz: Array4f
    yyww: Array4f
    yzxx: Array4f
    yzxy: Array4f
    yzxz: Array4f
    yzxw: Array4f
    yzyx: Array4f
    yzyy: Array4f
    yzyz: Array4f
    yzyw: Array4f
    yzzx: Array4f
    yzzy: Array4f
    yzzz: Array4f
    yzzw: Array4f
    yzwx: Array4f
    yzwy: Array4f
    yzwz: Array4f
    yzww: Array4f
    ywxx: Array4f
    ywxy: Array4f
    ywxz: Array4f
    ywxw: Array4f
    ywyx: Array4f
    ywyy: Array4f
    ywyz: Array4f
    ywyw: Array4f
    ywzx: Array4f
    ywzy: Array4f
    ywzz: Array4f
    ywzw: Array4f
    ywwx: Array4f
    ywwy: Array4f
    ywwz: Array4f
    ywww: Array4f
    zxxx: Array4f
    zxxy: Array4f
    zxxz: Array4f
    zxxw: Array4f
    zxyx: Array4f
    zxyy: Array4f
    zxyz: Array4f
    zxyw: Array4f
    zxzx: Array4f
    zxzy: Array4f
    zxzz: Array4f
    zxzw: Array4f
    zxwx: Array4f
    zxwy: Array4f
    zxwz: Array4f
    zxww: Array4f
    zyxx: Array4f
    zyxy: Array4f
    zyxz: Array4f
    zyxw: Array4f
    zyyx: Array4f
    zyyy: Array4f
    zyyz: Array4f
    zyyw: Array4f
    zyzx: Array4f
    zyzy: Array4f
    zyzz: Array4f
    zyzw: Array4f
    zywx: Array4f
    zywy: Array4f
    zywz: Array4f
    zyww: Array4f
    zzxx: Array4f
    zzxy: Array4f
    zzxz: Array4f
    zzxw: Array4f
    zzyx: Array4f
    zzyy: Array4f
    zzyz: Array4f
    zzyw: Array4f
    zzzx: Array4f
    zzzy: Array4f
    zzzz: Array4f
    zzzw: Array4f
    zzwx: Array4f
    zzwy: Array4f
    zzwz: Array4f
    zzww: Array4f
    zwxx: Array4f
    zwxy: Array4f
    zwxz: Array4f
    zwxw: Array4f
    zwyx: Array4f
    zwyy: Array4f
    zwyz: Array4f
    zwyw: Array4f
    zwzx: Array4f
    zwzy: Array4f
    zwzz: Array4f
    zwzw: Array4f
    zwwx: Array4f
    zwwy: Array4f
    zwwz: Array4f
    zwww: Array4f
    wxxx: Array4f
    wxxy: Array4f
    wxxz: Array4f
    wxxw: Array4f
    wxyx: Array4f
    wxyy: Array4f
    wxyz: Array4f
    wxyw: Array4f
    wxzx: Array4f
    wxzy: Array4f
    wxzz: Array4f
    wxzw: Array4f
    wxwx: Array4f
    wxwy: Array4f
    wxwz: Array4f
    wxww: Array4f
    wyxx: Array4f
    wyxy: Array4f
    wyxz: Array4f
    wyxw: Array4f
    wyyx: Array4f
    wyyy: Array4f
    wyyz: Array4f
    wyyw: Array4f
    wyzx: Array4f
    wyzy: Array4f
    wyzz: Array4f
    wyzw: Array4f
    wywx: Array4f
    wywy: Array4f
    wywz: Array4f
    wyww: Array4f
    wzxx: Array4f
    wzxy: Array4f
    wzxz: Array4f
    wzxw: Array4f
    wzyx: Array4f
    wzyy: Array4f
    wzyz: Array4f
    wzyw: Array4f
    wzzx: Array4f
    wzzy: Array4f
    wzzz: Array4f
    wzzw: Array4f
    wzwx: Array4f
    wzwy: Array4f
    wzwz: Array4f
    wzww: Array4f
    wwxx: Array4f
    wwxy: Array4f
    wwxz: Array4f
    wwxw: Array4f
    wwyx: Array4f
    wwyy: Array4f
    wwyz: Array4f
    wwyw: Array4f
    wwzx: Array4f
    wwzy: Array4f
    wwzz: Array4f
    wwzw: Array4f
    wwwx: Array4f
    wwwy: Array4f
    wwwz: Array4f
    wwww: Array4f

_Array4f64Cp: TypeAlias = Union['Array4f64', '_Float64Cp', 'drjit.scalar._Array4f64Cp', 'drjit.llvm._Array4f64Cp', '_Array4fCp']

class Array4f64(drjit.ArrayBase[Array4f64, _Array4f64Cp, Float64, _Float64Cp, Float64, Array4f64, Array4b]):
    xx: Array2f64
    xy: Array2f64
    xz: Array2f64
    xw: Array2f64
    yx: Array2f64
    yy: Array2f64
    yz: Array2f64
    yw: Array2f64
    zx: Array2f64
    zy: Array2f64
    zz: Array2f64
    zw: Array2f64
    wx: Array2f64
    wy: Array2f64
    wz: Array2f64
    ww: Array2f64
    xxx: Array3f64
    xxy: Array3f64
    xxz: Array3f64
    xxw: Array3f64
    xyx: Array3f64
    xyy: Array3f64
    xyz: Array3f64
    xyw: Array3f64
    xzx: Array3f64
    xzy: Array3f64
    xzz: Array3f64
    xzw: Array3f64
    xwx: Array3f64
    xwy: Array3f64
    xwz: Array3f64
    xww: Array3f64
    yxx: Array3f64
    yxy: Array3f64
    yxz: Array3f64
    yxw: Array3f64
    yyx: Array3f64
    yyy: Array3f64
    yyz: Array3f64
    yyw: Array3f64
    yzx: Array3f64
    yzy: Array3f64
    yzz: Array3f64
    yzw: Array3f64
    ywx: Array3f64
    ywy: Array3f64
    ywz: Array3f64
    yww: Array3f64
    zxx: Array3f64
    zxy: Array3f64
    zxz: Array3f64
    zxw: Array3f64
    zyx: Array3f64
    zyy: Array3f64
    zyz: Array3f64
    zyw: Array3f64
    zzx: Array3f64
    zzy: Array3f64
    zzz: Array3f64
    zzw: Array3f64
    zwx: Array3f64
    zwy: Array3f64
    zwz: Array3f64
    zww: Array3f64
    wxx: Array3f64
    wxy: Array3f64
    wxz: Array3f64
    wxw: Array3f64
    wyx: Array3f64
    wyy: Array3f64
    wyz: Array3f64
    wyw: Array3f64
    wzx: Array3f64
    wzy: Array3f64
    wzz: Array3f64
    wzw: Array3f64
    wwx: Array3f64
    wwy: Array3f64
    wwz: Array3f64
    www: Array3f64
    xxxx: Array4f64
    xxxy: Array4f64
    xxxz: Array4f64
    xxxw: Array4f64
    xxyx: Array4f64
    xxyy: Array4f64
    xxyz: Array4f64
    xxyw: Array4f64
    xxzx: Array4f64
    xxzy: Array4f64
    xxzz: Array4f64
    xxzw: Array4f64
    xxwx: Array4f64
    xxwy: Array4f64
    xxwz: Array4f64
    xxww: Array4f64
    xyxx: Array4f64
    xyxy: Array4f64
    xyxz: Array4f64
    xyxw: Array4f64
    xyyx: Array4f64
    xyyy: Array4f64
    xyyz: Array4f64
    xyyw: Array4f64
    xyzx: Array4f64
    xyzy: Array4f64
    xyzz: Array4f64
    xyzw: Array4f64
    xywx: Array4f64
    xywy: Array4f64
    xywz: Array4f64
    xyww: Array4f64
    xzxx: Array4f64
    xzxy: Array4f64
    xzxz: Array4f64
    xzxw: Array4f64
    xzyx: Array4f64
    xzyy: Array4f64
    xzyz: Array4f64
    xzyw: Array4f64
    xzzx: Array4f64
    xzzy: Array4f64
    xzzz: Array4f64
    xzzw: Array4f64
    xzwx: Array4f64
    xzwy: Array4f64
    xzwz: Array4f64
    xzww: Array4f64
    xwxx: Array4f64
    xwxy: Array4f64
    xwxz: Array4f64
    xwxw: Array4f64
    xwyx: Array4f64
    xwyy: Array4f64
    xwyz: Array4f64
    xwyw: Array4f64
    xwzx: Array4f64
    xwzy: Array4f64
    xwzz: Array4f64
    xwzw: Array4f64
    xwwx: Array4f64
    xwwy: Array4f64
    xwwz: Array4f64
    xwww: Array4f64
    yxxx: Array4f64
    yxxy: Array4f64
    yxxz: Array4f64
    yxxw: Array4f64
    yxyx: Array4f64
    yxyy: Array4f64
    yxyz: Array4f64
    yxyw: Array4f64
    yxzx: Array4f64
    yxzy: Array4f64
    yxzz: Array4f64
    yxzw: Array4f64
    yxwx: Array4f64
    yxwy: Array4f64
    yxwz: Array4f64
    yxww: Array4f64
    yyxx: Array4f64
    yyxy: Array4f64
    yyxz: Array4f64
    yyxw: Array4f64
    yyyx: Array4f64
    yyyy: Array4f64
    yyyz: Array4f64
    yyyw: Array4f64
    yyzx: Array4f64
    yyzy: Array4f64
    yyzz: Array4f64
    yyzw: Array4f64
    yywx: Array4f64
    yywy: Array4f64
    yywz: Array4f64
    yyww: Array4f64
    yzxx: Array4f64
    yzxy: Array4f64
    yzxz: Array4f64
    yzxw: Array4f64
    yzyx: Array4f64
    yzyy: Array4f64
    yzyz: Array4f64
    yzyw: Array4f64
    yzzx: Array4f64
    yzzy: Array4f64
    yzzz: Array4f64
    yzzw: Array4f64
    yzwx: Array4f64
    yzwy: Array4f64
    yzwz: Array4f64
    yzww: Array4f64
    ywxx: Array4f64
    ywxy: Array4f64
    ywxz: Array4f64
    ywxw: Array4f64
    ywyx: Array4f64
    ywyy: Array4f64
    ywyz: Array4f64
    ywyw: Array4f64
    ywzx: Array4f64
    ywzy: Array4f64
    ywzz: Array4f64
    ywzw: Array4f64
    ywwx: Array4f64
    ywwy: Array4f64
    ywwz: Array4f64
    ywww: Array4f64
    zxxx: Array4f64
    zxxy: Array4f64
    zxxz: Array4f64
    zxxw: Array4f64
    zxyx: Array4f64
    zxyy: Array4f64
    zxyz: Array4f64
    zxyw: Array4f64
    zxzx: Array4f64
    zxzy: Array4f64
    zxzz: Array4f64
    zxzw: Array4f64
    zxwx: Array4f64
    zxwy: Array4f64
    zxwz: Array4f64
    zxww: Array4f64
    zyxx: Array4f64
    zyxy: Array4f64
    zyxz: Array4f64
    zyxw: Array4f64
    zyyx: Array4f64
    zyyy: Array4f64
    zyyz: Array4f64
    zyyw: Array4f64
    zyzx: Array4f64
    zyzy: Array4f64
    zyzz: Array4f64
    zyzw: Array4f64
    zywx: Array4f64
    zywy: Array4f64
    zywz: Array4f64
    zyww: Array4f64
    zzxx: Array4f64
    zzxy: Array4f64
    zzxz: Array4f64
    zzxw: Array4f64
    zzyx: Array4f64
    zzyy: Array4f64
    zzyz: Array4f64
    zzyw: Array4f64
    zzzx: Array4f64
    zzzy: Array4f64
    zzzz: Array4f64
    zzzw: Array4f64
    zzwx: Array4f64
    zzwy: Array4f64
    zzwz: Array4f64
    zzww: Array4f64
    zwxx: Array4f64
    zwxy: Array4f64
    zwxz: Array4f64
    zwxw: Array4f64
    zwyx: Array4f64
    zwyy: Array4f64
    zwyz: Array4f64
    zwyw: Array4f64
    zwzx: Array4f64
    zwzy: Array4f64
    zwzz: Array4f64
    zwzw: Array4f64
    zwwx: Array4f64
    zwwy: Array4f64
    zwwz: Array4f64
    zwww: Array4f64
    wxxx: Array4f64
    wxxy: Array4f64
    wxxz: Array4f64
    wxxw: Array4f64
    wxyx: Array4f64
    wxyy: Array4f64
    wxyz: Array4f64
    wxyw: Array4f64
    wxzx: Array4f64
    wxzy: Array4f64
    wxzz: Array4f64
    wxzw: Array4f64
    wxwx: Array4f64
    wxwy: Array4f64
    wxwz: Array4f64
    wxww: Array4f64
    wyxx: Array4f64
    wyxy: Array4f64
    wyxz: Array4f64
    wyxw: Array4f64
    wyyx: Array4f64
    wyyy: Array4f64
    wyyz: Array4f64
    wyyw: Array4f64
    wyzx: Array4f64
    wyzy: Array4f64
    wyzz: Array4f64
    wyzw: Array4f64
    wywx: Array4f64
    wywy: Array4f64
    wywz: Array4f64
    wyww: Array4f64
    wzxx: Array4f64
    wzxy: Array4f64
    wzxz: Array4f64
    wzxw: Array4f64
    wzyx: Array4f64
    wzyy: Array4f64
    wzyz: Array4f64
    wzyw: Array4f64
    wzzx: Array4f64
    wzzy: Array4f64
    wzzz: Array4f64
    wzzw: Array4f64
    wzwx: Array4f64
    wzwy: Array4f64
    wzwz: Array4f64
    wzww: Array4f64
    wwxx: Array4f64
    wwxy: Array4f64
    wwxz: Array4f64
    wwxw: Array4f64
    wwyx: Array4f64
    wwyy: Array4f64
    wwyz: Array4f64
    wwyw: Array4f64
    wwzx: Array4f64
    wwzy: Array4f64
    wwzz: Array4f64
    wwzw: Array4f64
    wwwx: Array4f64
    wwwy: Array4f64
    wwwz: Array4f64
    wwww: Array4f64

_ArrayXbCp: TypeAlias = Union['ArrayXb', '_BoolCp', 'drjit.scalar._ArrayXbCp', 'drjit.llvm._ArrayXbCp']

class ArrayXb(drjit.ArrayBase[ArrayXb, _ArrayXbCp, Bool, _BoolCp, Bool, ArrayXb, ArrayXb]):
    pass

_ArrayXi8Cp: TypeAlias = Union['ArrayXi8', '_Int8Cp', 'drjit.scalar._ArrayXi8Cp', 'drjit.llvm._ArrayXi8Cp']

class ArrayXi8(drjit.ArrayBase[ArrayXi8, _ArrayXi8Cp, Int8, _Int8Cp, Int8, ArrayXi8, ArrayXb]):
    pass

_ArrayXu8Cp: TypeAlias = Union['ArrayXu8', '_UInt8Cp', 'drjit.scalar._ArrayXu8Cp', 'drjit.llvm._ArrayXu8Cp']

class ArrayXu8(drjit.ArrayBase[ArrayXu8, _ArrayXu8Cp, UInt8, _UInt8Cp, UInt8, ArrayXu8, ArrayXb]):
    pass

_ArrayXiCp: TypeAlias = Union['ArrayXi', '_IntCp', 'drjit.scalar._ArrayXiCp', 'drjit.llvm._ArrayXiCp', '_ArrayXbCp']

class ArrayXi(drjit.ArrayBase[ArrayXi, _ArrayXiCp, Int, _IntCp, Int, ArrayXi, ArrayXb]):
    pass

_ArrayXuCp: TypeAlias = Union['ArrayXu', '_UIntCp', 'drjit.scalar._ArrayXuCp', 'drjit.llvm._ArrayXuCp', '_ArrayXiCp']

class ArrayXu(drjit.ArrayBase[ArrayXu, _ArrayXuCp, UInt, _UIntCp, UInt, ArrayXu, ArrayXb]):
    pass

_ArrayXi64Cp: TypeAlias = Union['ArrayXi64', '_Int64Cp', 'drjit.scalar._ArrayXi64Cp', 'drjit.llvm._ArrayXi64Cp', '_ArrayXuCp']

class ArrayXi64(drjit.ArrayBase[ArrayXi64, _ArrayXi64Cp, Int64, _Int64Cp, Int64, ArrayXi64, ArrayXb]):
    pass

_ArrayXu64Cp: TypeAlias = Union['ArrayXu64', '_UInt64Cp', 'drjit.scalar._ArrayXu64Cp', 'drjit.llvm._ArrayXu64Cp', '_ArrayXi64Cp']

class ArrayXu64(drjit.ArrayBase[ArrayXu64, _ArrayXu64Cp, UInt64, _UInt64Cp, UInt64, ArrayXu64, ArrayXb]):
    pass

_ArrayXf16Cp: TypeAlias = Union['ArrayXf16', '_Float16Cp', 'drjit.scalar._ArrayXf16Cp', 'drjit.llvm._ArrayXf16Cp', '_ArrayXu64Cp']

class ArrayXf16(drjit.ArrayBase[ArrayXf16, _ArrayXf16Cp, Float16, _Float16Cp, Float16, ArrayXf16, ArrayXb]):
    pass

_ArrayXfCp: TypeAlias = Union['ArrayXf', '_FloatCp', 'drjit.scalar._ArrayXfCp', 'drjit.llvm._ArrayXfCp', '_ArrayXf16Cp']

class ArrayXf(drjit.ArrayBase[ArrayXf, _ArrayXfCp, Float, _FloatCp, Float, ArrayXf, ArrayXb]):
    pass

_ArrayXf64Cp: TypeAlias = Union['ArrayXf64', '_Float64Cp', 'drjit.scalar._ArrayXf64Cp', 'drjit.llvm._ArrayXf64Cp', '_ArrayXfCp']

class ArrayXf64(drjit.ArrayBase[ArrayXf64, _ArrayXf64Cp, Float64, _Float64Cp, Float64, ArrayXf64, ArrayXb]):
    pass

_Array22bCp: TypeAlias = Union['Array22b', '_Array2bCp', 'drjit.scalar._Array22bCp', 'drjit.llvm._Array22bCp']

class Array22b(drjit.ArrayBase[Array22b, _Array22bCp, Array2b, _Array2bCp, Array2b, Array22b, Array22b]):
    pass

_Array22f16Cp: TypeAlias = Union['Array22f16', '_Array2f16Cp', 'drjit.scalar._Array22f16Cp', 'drjit.llvm._Array22f16Cp']

class Array22f16(drjit.ArrayBase[Array22f16, _Array22f16Cp, Array2f16, _Array2f16Cp, Array2f16, Array22f16, Array22b]):
    pass

_Array22fCp: TypeAlias = Union['Array22f', '_Array2fCp', 'drjit.scalar._Array22fCp', 'drjit.llvm._Array22fCp', '_Array22f16Cp']

class Array22f(drjit.ArrayBase[Array22f, _Array22fCp, Array2f, _Array2fCp, Array2f, Array22f, Array22b]):
    pass

_Array22f64Cp: TypeAlias = Union['Array22f64', '_Array2f64Cp', 'drjit.scalar._Array22f64Cp', 'drjit.llvm._Array22f64Cp', '_Array22fCp']

class Array22f64(drjit.ArrayBase[Array22f64, _Array22f64Cp, Array2f64, _Array2f64Cp, Array2f64, Array22f64, Array22b]):
    pass

_Matrix2f16Cp: TypeAlias = Union['Matrix2f16', '_Array2f16Cp', 'drjit.scalar._Matrix2f16Cp', 'drjit.llvm._Matrix2f16Cp']

class Matrix2f16(drjit.ArrayBase[Matrix2f16, _Matrix2f16Cp, Array2f16, _Array2f16Cp, Array2f16, Array22f16, Array22b]):
    pass

_Matrix2fCp: TypeAlias = Union['Matrix2f', '_Array2fCp', 'drjit.scalar._Matrix2fCp', 'drjit.llvm._Matrix2fCp', '_Matrix2f16Cp']

class Matrix2f(drjit.ArrayBase[Matrix2f, _Matrix2fCp, Array2f, _Array2fCp, Array2f, Array22f, Array22b]):
    pass

_Matrix2f64Cp: TypeAlias = Union['Matrix2f64', '_Array2f64Cp', 'drjit.scalar._Matrix2f64Cp', 'drjit.llvm._Matrix2f64Cp', '_Matrix2fCp']

class Matrix2f64(drjit.ArrayBase[Matrix2f64, _Matrix2f64Cp, Array2f64, _Array2f64Cp, Array2f64, Array22f64, Array22b]):
    pass

_Array33bCp: TypeAlias = Union['Array33b', '_Array3bCp', 'drjit.scalar._Array33bCp', 'drjit.llvm._Array33bCp']

class Array33b(drjit.ArrayBase[Array33b, _Array33bCp, Array3b, _Array3bCp, Array3b, Array33b, Array33b]):
    pass

_Array33f16Cp: TypeAlias = Union['Array33f16', '_Array3f16Cp', 'drjit.scalar._Array33f16Cp', 'drjit.llvm._Array33f16Cp']

class Array33f16(drjit.ArrayBase[Array33f16, _Array33f16Cp, Array3f16, _Array3f16Cp, Array3f16, Array33f16, Array33b]):
    pass

_Array33fCp: TypeAlias = Union['Array33f', '_Array3fCp', 'drjit.scalar._Array33fCp', 'drjit.llvm._Array33fCp', '_Array33f16Cp']

class Array33f(drjit.ArrayBase[Array33f, _Array33fCp, Array3f, _Array3fCp, Array3f, Array33f, Array33b]):
    pass

_Array33f64Cp: TypeAlias = Union['Array33f64', '_Array3f64Cp', 'drjit.scalar._Array33f64Cp', 'drjit.llvm._Array33f64Cp', '_Array33fCp']

class Array33f64(drjit.ArrayBase[Array33f64, _Array33f64Cp, Array3f64, _Array3f64Cp, Array3f64, Array33f64, Array33b]):
    pass

_Matrix3f16Cp: TypeAlias = Union['Matrix3f16', '_Array3f16Cp', 'drjit.scalar._Matrix3f16Cp', 'drjit.llvm._Matrix3f16Cp']

class Matrix3f16(drjit.ArrayBase[Matrix3f16, _Matrix3f16Cp, Array3f16, _Array3f16Cp, Array3f16, Array33f16, Array33b]):
    pass

_Matrix3fCp: TypeAlias = Union['Matrix3f', '_Array3fCp', 'drjit.scalar._Matrix3fCp', 'drjit.llvm._Matrix3fCp', '_Matrix3f16Cp']

class Matrix3f(drjit.ArrayBase[Matrix3f, _Matrix3fCp, Array3f, _Array3fCp, Array3f, Array33f, Array33b]):
    pass

_Matrix3f64Cp: TypeAlias = Union['Matrix3f64', '_Array3f64Cp', 'drjit.scalar._Matrix3f64Cp', 'drjit.llvm._Matrix3f64Cp', '_Matrix3fCp']

class Matrix3f64(drjit.ArrayBase[Matrix3f64, _Matrix3f64Cp, Array3f64, _Array3f64Cp, Array3f64, Array33f64, Array33b]):
    pass

_Array44bCp: TypeAlias = Union['Array44b', '_Array4bCp', 'drjit.scalar._Array44bCp', 'drjit.llvm._Array44bCp']

class Array44b(drjit.ArrayBase[Array44b, _Array44bCp, Array4b, _Array4bCp, Array4b, Array44b, Array44b]):
    pass

_Array44f16Cp: TypeAlias = Union['Array44f16', '_Array4f16Cp', 'drjit.scalar._Array44f16Cp', 'drjit.llvm._Array44f16Cp']

class Array44f16(drjit.ArrayBase[Array44f16, _Array44f16Cp, Array4f16, _Array4f16Cp, Array4f16, Array44f16, Array44b]):
    pass

_Array44fCp: TypeAlias = Union['Array44f', '_Array4fCp', 'drjit.scalar._Array44fCp', 'drjit.llvm._Array44fCp', '_Array44f16Cp']

class Array44f(drjit.ArrayBase[Array44f, _Array44fCp, Array4f, _Array4fCp, Array4f, Array44f, Array44b]):
    pass

_Array44f64Cp: TypeAlias = Union['Array44f64', '_Array4f64Cp', 'drjit.scalar._Array44f64Cp', 'drjit.llvm._Array44f64Cp', '_Array44fCp']

class Array44f64(drjit.ArrayBase[Array44f64, _Array44f64Cp, Array4f64, _Array4f64Cp, Array4f64, Array44f64, Array44b]):
    pass

_Matrix4f16Cp: TypeAlias = Union['Matrix4f16', '_Array4f16Cp', 'drjit.scalar._Matrix4f16Cp', 'drjit.llvm._Matrix4f16Cp']

class Matrix4f16(drjit.ArrayBase[Matrix4f16, _Matrix4f16Cp, Array4f16, _Array4f16Cp, Array4f16, Array44f16, Array44b]):
    pass

_Matrix4fCp: TypeAlias = Union['Matrix4f', '_Array4fCp', 'drjit.scalar._Matrix4fCp', 'drjit.llvm._Matrix4fCp', '_Matrix4f16Cp']

class Matrix4f(drjit.ArrayBase[Matrix4f, _Matrix4fCp, Array4f, _Array4fCp, Array4f, Array44f, Array44b]):
    pass

_Matrix4f64Cp: TypeAlias = Union['Matrix4f64', '_Array4f64Cp', 'drjit.scalar._Matrix4f64Cp', 'drjit.llvm._Matrix4f64Cp', '_Matrix4fCp']

class Matrix4f64(drjit.ArrayBase[Matrix4f64, _Matrix4f64Cp, Array4f64, _Array4f64Cp, Array4f64, Array44f64, Array44b]):
    pass

_Array41bCp: TypeAlias = Union['Array41b', '_Array1bCp', 'drjit.scalar._Array41bCp', 'drjit.llvm._Array41bCp']

class Array41b(drjit.ArrayBase[Array41b, _Array41bCp, Array1b, _Array1bCp, Array1b, Array41b, Array41b]):
    pass

_Array41f16Cp: TypeAlias = Union['Array41f16', '_Array1f16Cp', 'drjit.scalar._Array41f16Cp', 'drjit.llvm._Array41f16Cp']

class Array41f16(drjit.ArrayBase[Array41f16, _Array41f16Cp, Array1f16, _Array1f16Cp, Array1f16, Array41f16, Array41b]):
    pass

_Array41fCp: TypeAlias = Union['Array41f', '_Array1fCp', 'drjit.scalar._Array41fCp', 'drjit.llvm._Array41fCp', '_Array41f16Cp']

class Array41f(drjit.ArrayBase[Array41f, _Array41fCp, Array1f, _Array1fCp, Array1f, Array41f, Array41b]):
    pass

_Array41f64Cp: TypeAlias = Union['Array41f64', '_Array1f64Cp', 'drjit.scalar._Array41f64Cp', 'drjit.llvm._Array41f64Cp', '_Array41fCp']

class Array41f64(drjit.ArrayBase[Array41f64, _Array41f64Cp, Array1f64, _Array1f64Cp, Array1f64, Array41f64, Array41b]):
    pass

_Array441bCp: TypeAlias = Union['Array441b', '_Array41bCp', 'drjit.scalar._Array441bCp', 'drjit.llvm._Array441bCp']

class Array441b(drjit.ArrayBase[Array441b, _Array441bCp, Array41b, _Array41bCp, Array41b, Array441b, Array441b]):
    pass

_Array441f16Cp: TypeAlias = Union['Array441f16', '_Array41f16Cp', 'drjit.scalar._Array441f16Cp', 'drjit.llvm._Array441f16Cp']

class Array441f16(drjit.ArrayBase[Array441f16, _Array441f16Cp, Array41f16, _Array41f16Cp, Array41f16, Array441f16, Array441b]):
    pass

_Array441fCp: TypeAlias = Union['Array441f', '_Array41fCp', 'drjit.scalar._Array441fCp', 'drjit.llvm._Array441fCp', '_Array441f16Cp']

class Array441f(drjit.ArrayBase[Array441f, _Array441fCp, Array41f, _Array41fCp, Array41f, Array441f, Array441b]):
    pass

_Array441f64Cp: TypeAlias = Union['Array441f64', '_Array41f64Cp', 'drjit.scalar._Array441f64Cp', 'drjit.llvm._Array441f64Cp', '_Array441fCp']

class Array441f64(drjit.ArrayBase[Array441f64, _Array441f64Cp, Array41f64, _Array41f64Cp, Array41f64, Array441f64, Array441b]):
    pass

_Matrix41f16Cp: TypeAlias = Union['Matrix41f16', '_Array41f16Cp', 'drjit.scalar._Matrix41f16Cp', 'drjit.llvm._Matrix41f16Cp']

class Matrix41f16(drjit.ArrayBase[Matrix41f16, _Matrix41f16Cp, Array41f16, _Array41f16Cp, Array41f16, Array441f16, Array441b]):
    pass

_Matrix41fCp: TypeAlias = Union['Matrix41f', '_Array41fCp', 'drjit.scalar._Matrix41fCp', 'drjit.llvm._Matrix41fCp', '_Matrix41f16Cp']

class Matrix41f(drjit.ArrayBase[Matrix41f, _Matrix41fCp, Array41f, _Array41fCp, Array41f, Array441f, Array441b]):
    pass

_Matrix41f64Cp: TypeAlias = Union['Matrix41f64', '_Array41f64Cp', 'drjit.scalar._Matrix41f64Cp', 'drjit.llvm._Matrix41f64Cp', '_Matrix41fCp']

class Matrix41f64(drjit.ArrayBase[Matrix41f64, _Matrix41f64Cp, Array41f64, _Array41f64Cp, Array41f64, Array441f64, Array441b]):
    pass

_Array43bCp: TypeAlias = Union['Array43b', '_Array3bCp', 'drjit.scalar._Array43bCp', 'drjit.llvm._Array43bCp']

class Array43b(drjit.ArrayBase[Array43b, _Array43bCp, Array3b, _Array3bCp, Array3b, Array43b, Array43b]):
    pass

_Array43f16Cp: TypeAlias = Union['Array43f16', '_Array3f16Cp', 'drjit.scalar._Array43f16Cp', 'drjit.llvm._Array43f16Cp']

class Array43f16(drjit.ArrayBase[Array43f16, _Array43f16Cp, Array3f16, _Array3f16Cp, Array3f16, Array43f16, Array43b]):
    pass

_Array43fCp: TypeAlias = Union['Array43f', '_Array3fCp', 'drjit.scalar._Array43fCp', 'drjit.llvm._Array43fCp', '_Array43f16Cp']

class Array43f(drjit.ArrayBase[Array43f, _Array43fCp, Array3f, _Array3fCp, Array3f, Array43f, Array43b]):
    pass

_Array43f64Cp: TypeAlias = Union['Array43f64', '_Array3f64Cp', 'drjit.scalar._Array43f64Cp', 'drjit.llvm._Array43f64Cp', '_Array43fCp']

class Array43f64(drjit.ArrayBase[Array43f64, _Array43f64Cp, Array3f64, _Array3f64Cp, Array3f64, Array43f64, Array43b]):
    pass

_Array443bCp: TypeAlias = Union['Array443b', '_Array43bCp', 'drjit.scalar._Array443bCp', 'drjit.llvm._Array443bCp']

class Array443b(drjit.ArrayBase[Array443b, _Array443bCp, Array43b, _Array43bCp, Array43b, Array443b, Array443b]):
    pass

_Array443f16Cp: TypeAlias = Union['Array443f16', '_Array43f16Cp', 'drjit.scalar._Array443f16Cp', 'drjit.llvm._Array443f16Cp']

class Array443f16(drjit.ArrayBase[Array443f16, _Array443f16Cp, Array43f16, _Array43f16Cp, Array43f16, Array443f16, Array443b]):
    pass

_Array443fCp: TypeAlias = Union['Array443f', '_Array43fCp', 'drjit.scalar._Array443fCp', 'drjit.llvm._Array443fCp', '_Array443f16Cp']

class Array443f(drjit.ArrayBase[Array443f, _Array443fCp, Array43f, _Array43fCp, Array43f, Array443f, Array443b]):
    pass

_Array443f64Cp: TypeAlias = Union['Array443f64', '_Array43f64Cp', 'drjit.scalar._Array443f64Cp', 'drjit.llvm._Array443f64Cp', '_Array443fCp']

class Array443f64(drjit.ArrayBase[Array443f64, _Array443f64Cp, Array43f64, _Array43f64Cp, Array43f64, Array443f64, Array443b]):
    pass

_Matrix43f16Cp: TypeAlias = Union['Matrix43f16', '_Array43f16Cp', 'drjit.scalar._Matrix43f16Cp', 'drjit.llvm._Matrix43f16Cp']

class Matrix43f16(drjit.ArrayBase[Matrix43f16, _Matrix43f16Cp, Array43f16, _Array43f16Cp, Array43f16, Array443f16, Array443b]):
    pass

_Matrix43fCp: TypeAlias = Union['Matrix43f', '_Array43fCp', 'drjit.scalar._Matrix43fCp', 'drjit.llvm._Matrix43fCp', '_Matrix43f16Cp']

class Matrix43f(drjit.ArrayBase[Matrix43f, _Matrix43fCp, Array43f, _Array43fCp, Array43f, Array443f, Array443b]):
    pass

_Matrix43f64Cp: TypeAlias = Union['Matrix43f64', '_Array43f64Cp', 'drjit.scalar._Matrix43f64Cp', 'drjit.llvm._Matrix43f64Cp', '_Matrix43fCp']

class Matrix43f64(drjit.ArrayBase[Matrix43f64, _Matrix43f64Cp, Array43f64, _Array43f64Cp, Array43f64, Array443f64, Array443b]):
    pass

_Array34bCp: TypeAlias = Union['Array34b', '_Array4bCp', 'drjit.scalar._Array34bCp', 'drjit.llvm._Array34bCp']

class Array34b(drjit.ArrayBase[Array34b, _Array34bCp, Array4b, _Array4bCp, Array4b, Array34b, Array34b]):
    pass

_Array34f16Cp: TypeAlias = Union['Array34f16', '_Array4f16Cp', 'drjit.scalar._Array34f16Cp', 'drjit.llvm._Array34f16Cp']

class Array34f16(drjit.ArrayBase[Array34f16, _Array34f16Cp, Array4f16, _Array4f16Cp, Array4f16, Array34f16, Array34b]):
    pass

_Array34fCp: TypeAlias = Union['Array34f', '_Array4fCp', 'drjit.scalar._Array34fCp', 'drjit.llvm._Array34fCp', '_Array34f16Cp']

class Array34f(drjit.ArrayBase[Array34f, _Array34fCp, Array4f, _Array4fCp, Array4f, Array34f, Array34b]):
    pass

_Array34f64Cp: TypeAlias = Union['Array34f64', '_Array4f64Cp', 'drjit.scalar._Array34f64Cp', 'drjit.llvm._Array34f64Cp', '_Array34fCp']

class Array34f64(drjit.ArrayBase[Array34f64, _Array34f64Cp, Array4f64, _Array4f64Cp, Array4f64, Array34f64, Array34b]):
    pass

_Array334bCp: TypeAlias = Union['Array334b', '_Array34bCp', 'drjit.scalar._Array334bCp', 'drjit.llvm._Array334bCp']

class Array334b(drjit.ArrayBase[Array334b, _Array334bCp, Array34b, _Array34bCp, Array34b, Array334b, Array334b]):
    pass

_Array334f16Cp: TypeAlias = Union['Array334f16', '_Array34f16Cp', 'drjit.scalar._Array334f16Cp', 'drjit.llvm._Array334f16Cp']

class Array334f16(drjit.ArrayBase[Array334f16, _Array334f16Cp, Array34f16, _Array34f16Cp, Array34f16, Array334f16, Array334b]):
    pass

_Array334fCp: TypeAlias = Union['Array334f', '_Array34fCp', 'drjit.scalar._Array334fCp', 'drjit.llvm._Array334fCp', '_Array334f16Cp']

class Array334f(drjit.ArrayBase[Array334f, _Array334fCp, Array34f, _Array34fCp, Array34f, Array334f, Array334b]):
    pass

_Array334f64Cp: TypeAlias = Union['Array334f64', '_Array34f64Cp', 'drjit.scalar._Array334f64Cp', 'drjit.llvm._Array334f64Cp', '_Array334fCp']

class Array334f64(drjit.ArrayBase[Array334f64, _Array334f64Cp, Array34f64, _Array34f64Cp, Array34f64, Array334f64, Array334b]):
    pass

_Matrix34f16Cp: TypeAlias = Union['Matrix34f16', '_Array34f16Cp', 'drjit.scalar._Matrix34f16Cp', 'drjit.llvm._Matrix34f16Cp']

class Matrix34f16(drjit.ArrayBase[Matrix34f16, _Matrix34f16Cp, Array34f16, _Array34f16Cp, Array34f16, Array334f16, Array334b]):
    pass

_Matrix34fCp: TypeAlias = Union['Matrix34f', '_Array34fCp', 'drjit.scalar._Matrix34fCp', 'drjit.llvm._Matrix34fCp', '_Matrix34f16Cp']

class Matrix34f(drjit.ArrayBase[Matrix34f, _Matrix34fCp, Array34f, _Array34fCp, Array34f, Array334f, Array334b]):
    pass

_Matrix34f64Cp: TypeAlias = Union['Matrix34f64', '_Array34f64Cp', 'drjit.scalar._Matrix34f64Cp', 'drjit.llvm._Matrix34f64Cp', '_Matrix34fCp']

class Matrix34f64(drjit.ArrayBase[Matrix34f64, _Matrix34f64Cp, Array34f64, _Array34f64Cp, Array34f64, Array334f64, Array334b]):
    pass

_Array444bCp: TypeAlias = Union['Array444b', '_Array44bCp', 'drjit.scalar._Array444bCp', 'drjit.llvm._Array444bCp']

class Array444b(drjit.ArrayBase[Array444b, _Array444bCp, Array44b, _Array44bCp, Array44b, Array444b, Array444b]):
    pass

_Array444f16Cp: TypeAlias = Union['Array444f16', '_Array44f16Cp', 'drjit.scalar._Array444f16Cp', 'drjit.llvm._Array444f16Cp']

class Array444f16(drjit.ArrayBase[Array444f16, _Array444f16Cp, Array44f16, _Array44f16Cp, Array44f16, Array444f16, Array444b]):
    pass

_Array444fCp: TypeAlias = Union['Array444f', '_Array44fCp', 'drjit.scalar._Array444fCp', 'drjit.llvm._Array444fCp', '_Array444f16Cp']

class Array444f(drjit.ArrayBase[Array444f, _Array444fCp, Array44f, _Array44fCp, Array44f, Array444f, Array444b]):
    pass

_Array444f64Cp: TypeAlias = Union['Array444f64', '_Array44f64Cp', 'drjit.scalar._Array444f64Cp', 'drjit.llvm._Array444f64Cp', '_Array444fCp']

class Array444f64(drjit.ArrayBase[Array444f64, _Array444f64Cp, Array44f64, _Array44f64Cp, Array44f64, Array444f64, Array444b]):
    pass

_Matrix44f16Cp: TypeAlias = Union['Matrix44f16', '_Array44f16Cp', 'drjit.scalar._Matrix44f16Cp', 'drjit.llvm._Matrix44f16Cp']

class Matrix44f16(drjit.ArrayBase[Matrix44f16, _Matrix44f16Cp, Array44f16, _Array44f16Cp, Array44f16, Array444f16, Array444b]):
    pass

_Matrix44fCp: TypeAlias = Union['Matrix44f', '_Array44fCp', 'drjit.scalar._Matrix44fCp', 'drjit.llvm._Matrix44fCp', '_Matrix44f16Cp']

class Matrix44f(drjit.ArrayBase[Matrix44f, _Matrix44fCp, Array44f, _Array44fCp, Array44f, Array444f, Array444b]):
    pass

_Matrix44f64Cp: TypeAlias = Union['Matrix44f64', '_Array44f64Cp', 'drjit.scalar._Matrix44f64Cp', 'drjit.llvm._Matrix44f64Cp', '_Matrix44fCp']

class Matrix44f64(drjit.ArrayBase[Matrix44f64, _Matrix44f64Cp, Array44f64, _Array44f64Cp, Array44f64, Array444f64, Array444b]):
    pass

_Complex2fCp: TypeAlias = Union['Complex2f', '_FloatCp', 'drjit.scalar._Complex2fCp', 'drjit.llvm._Complex2fCp']

class Complex2f(drjit.ArrayBase[Complex2f, _Complex2fCp, Float, _FloatCp, Float, Array2f, Array2b]):
    pass

_Complex2f64Cp: TypeAlias = Union['Complex2f64', '_Float64Cp', 'drjit.scalar._Complex2f64Cp', 'drjit.llvm._Complex2f64Cp', '_Complex2fCp']

class Complex2f64(drjit.ArrayBase[Complex2f64, _Complex2f64Cp, Float64, _Float64Cp, Float64, Array2f64, Array2b]):
    pass

_Quaternion4f16Cp: TypeAlias = Union['Quaternion4f16', '_Float16Cp', 'drjit.scalar._Quaternion4f16Cp', 'drjit.llvm._Quaternion4f16Cp']

class Quaternion4f16(drjit.ArrayBase[Quaternion4f16, _Quaternion4f16Cp, Float16, _Float16Cp, Float16, Array4f16, Array4b]):
    pass

_Quaternion4fCp: TypeAlias = Union['Quaternion4f', '_FloatCp', 'drjit.scalar._Quaternion4fCp', 'drjit.llvm._Quaternion4fCp', '_Quaternion4f16Cp']

class Quaternion4f(drjit.ArrayBase[Quaternion4f, _Quaternion4fCp, Float, _FloatCp, Float, Array4f, Array4b]):
    pass

_Quaternion4f64Cp: TypeAlias = Union['Quaternion4f64', '_Float64Cp', 'drjit.scalar._Quaternion4f64Cp', 'drjit.llvm._Quaternion4f64Cp', '_Quaternion4fCp']

class Quaternion4f64(drjit.ArrayBase[Quaternion4f64, _Quaternion4f64Cp, Float64, _Float64Cp, Float64, Array4f64, Array4b]):
    pass

_TensorXbCp: TypeAlias = Union['TensorXb', bool, 'drjit.llvm._TensorXbCp']

class TensorXb(drjit.ArrayBase[TensorXb, _TensorXbCp, TensorXb, _TensorXbCp, TensorXb, Bool, TensorXb]):
    pass

_TensorXi8Cp: TypeAlias = Union['TensorXi8', int, 'drjit.llvm._TensorXi8Cp']

class TensorXi8(drjit.ArrayBase[TensorXi8, _TensorXi8Cp, TensorXi8, _TensorXi8Cp, TensorXi8, Int8, TensorXb]):
    pass

_TensorXiCp: TypeAlias = Union['TensorXi', int, 'drjit.llvm._TensorXiCp', '_TensorXbCp']

class TensorXi(drjit.ArrayBase[TensorXi, _TensorXiCp, TensorXi, _TensorXiCp, TensorXi, Int, TensorXb]):
    pass

_TensorXi64Cp: TypeAlias = Union['TensorXi64', int, 'drjit.llvm._TensorXi64Cp']

class TensorXi64(drjit.ArrayBase[TensorXi64, _TensorXi64Cp, TensorXi64, _TensorXi64Cp, TensorXi64, Int64, TensorXb]):
    pass

_TensorXu8Cp: TypeAlias = Union['TensorXu8', int, 'drjit.llvm._TensorXu8Cp']

class TensorXu8(drjit.ArrayBase[TensorXu8, _TensorXu8Cp, TensorXu8, _TensorXu8Cp, TensorXu8, UInt8, TensorXb]):
    pass

_TensorXuCp: TypeAlias = Union['TensorXu', int, 'drjit.llvm._TensorXuCp', '_TensorXiCp']

class TensorXu(drjit.ArrayBase[TensorXu, _TensorXuCp, TensorXu, _TensorXuCp, TensorXu, UInt, TensorXb]):
    pass

_TensorXu64Cp: TypeAlias = Union['TensorXu64', int, 'drjit.llvm._TensorXu64Cp', '_TensorXi64Cp']

class TensorXu64(drjit.ArrayBase[TensorXu64, _TensorXu64Cp, TensorXu64, _TensorXu64Cp, TensorXu64, UInt64, TensorXb]):
    pass

_TensorXf16Cp: TypeAlias = Union['TensorXf16', float, 'drjit.llvm._TensorXf16Cp', '_TensorXu64Cp']

class TensorXf16(drjit.ArrayBase[TensorXf16, _TensorXf16Cp, TensorXf16, _TensorXf16Cp, TensorXf16, Float16, TensorXb]):
    pass

_TensorXfCp: TypeAlias = Union['TensorXf', float, 'drjit.llvm._TensorXfCp', '_TensorXf16Cp']

class TensorXf(drjit.ArrayBase[TensorXf, _TensorXfCp, TensorXf, _TensorXfCp, TensorXf, Float, TensorXb]):
    pass

_TensorXf64Cp: TypeAlias = Union['TensorXf64', float, 'drjit.llvm._TensorXf64Cp', '_TensorXfCp']

class TensorXf64(drjit.ArrayBase[TensorXf64, _TensorXf64Cp, TensorXf64, _TensorXf64Cp, TensorXf64, Float64, TensorXb]):
    pass

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
    def __init__(self, size: int = 1, initstate: UInt64 = UInt64(0x853c49e6748fea9b), initseq: UInt64 = UInt64(0xda3e39cb94b95bdb)) -> None:
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

    def seed(self, initstate: UInt64 = UInt64(0x853c49e6748fea9b), initseq: UInt64 = UInt64(0xda3e39cb94b95bdb)) -> None:
        """
        Seed the random number generator with the given initial state and sequence ID.

        The ``initstate`` and ``initseq`` inputs determine the initial state and increment
        of the linear congruential generator. Their values are the defaults from the
        original implementation.
        """

    @overload
    def next_uint32(self) -> UInt:
        """
        Generate a uniformly distributed unsigned 32-bit random number

        Two overloads of this function exist: the masked variant does not advance
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def next_uint32(self, arg: Bool, /) -> UInt: ...

    @overload
    def prev_uint32(self) -> UInt:
        """
        Generate the previous uniformly distributed unsigned 32-bit random number
        by stepping the PCG32 state backwards.

        Two overloads of this function exist: the masked variant does not
        regress the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def prev_uint32(self, arg: Bool, /) -> UInt: ...

    def next_uint32_bounded(self, bound: int, mask: Bool = Bool(True)) -> UInt:
        r"""
        Generate a uniformly distributed 32-bit integer number on the
        interval :math:`[0, \texttt{bound})`.

        To ensure an unbiased result, the implementation relies on an iterative
        scheme that typically finishes after 1-2 iterations.
        """

    @overload
    def next_uint64(self) -> UInt64:
        """
        Generate a uniformly distributed unsigned 64-bit random number

        Internally, the function calls :py:func:`next_uint32` twice.

        Two overloads of this function exist: the masked variant does not advance
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def next_uint64(self, arg: Bool, /) -> UInt64: ...

    @overload
    def prev_uint64(self) -> UInt64:
        """
        Generate the previous uniformly distributed unsigned 64-bit random number
        by stepping the PCG32 state backwards.

        Internally, the function calls :py:func:`prev_uint32` twice.

        Two overloads of this function exist: the masked variant does not regress
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def prev_uint64(self, arg: Bool, /) -> UInt64: ...

    def next_uint64_bounded(self, bound: int, mask: Bool = Bool(True)) -> UInt64:
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
    def next_float16(self) -> Float16:
        """
        Generate a uniformly distributed half precision floating point number on the
        interval :math:`[0, 1)`.

        Two overloads of this function exist: the masked variant does not advance
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def next_float16(self, arg: Bool, /) -> Float16: ...

    @overload
    def prev_float16(self) -> Float16:
        """
        Generate the previous uniformly distributed half precision floating point number
        on the half-open interval :math:`[0, 1)` by stepping the PCG32 state backwards.

        Two overloads of this function exist: the masked variant does not regress
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def prev_float16(self, arg: Bool, /) -> Float16: ...

    @overload
    def next_float32(self) -> Float:
        """
        Generate a uniformly distributed single precision floating point number on the
        interval :math:`[0, 1)`.

        Two overloads of this function exist: the masked variant does not advance
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def next_float32(self, arg: Bool, /) -> Float: ...

    @overload
    def prev_float32(self) -> Float:
        """
        Generate the previous uniformly distributed single precision floating point number
        on the half-open interval :math:`[0, 1)` by stepping the PCG32 state backwards.

        Two overloads of this function exist: the masked variant does not regress
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def prev_float32(self, arg: Bool, /) -> Float: ...

    @overload
    def next_float64(self) -> Float64:
        """
        Generate a uniformly distributed double precision floating point number on the
        interval :math:`[0, 1)`.

        Two overloads of this function exist: the masked variant does not advance
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def next_float64(self, arg: Bool, /) -> Float64: ...

    @overload
    def prev_float64(self) -> Float64:
        """
        Generate the previous uniformly distributed double precision floating point number
        on the half-open interval :math:`[0, 1)` by stepping the PCG32 state backwards.

        Two overloads of this function exist: the masked variant does not regress
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def prev_float64(self, arg: Bool, /) -> Float64: ...

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
    def next_float16_normal(self) -> Float16:
        """
        Generate a (standard) normally distributed half precision floating point number.

        Two overloads of this function exist: the masked variant does not advance
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def next_float16_normal(self, arg: Bool, /) -> Float16: ...

    @overload
    def prev_float16_normal(self) -> Float16:
        """
        Generate the previous (standard) normally distributed half precision floating
        point number by stepping the PCG32 state backwards.

        Two overloads of this function exist: the masked variant does not regress
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def prev_float16_normal(self, arg: Bool, /) -> Float16: ...

    @overload
    def next_float32_normal(self) -> Float:
        """
        Generate a (standard) normally distributed single precision floating point number.

        Two overloads of this function exist: the masked variant does not advance
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def next_float32_normal(self, arg: Bool, /) -> Float: ...

    @overload
    def prev_float32_normal(self) -> Float:
        """
        Generate the previous (standard) normally distributed single precision floating
        point number by stepping the PCG32 state backwards.

        Two overloads of this function exist: the masked variant does not regress
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def prev_float32_normal(self, arg: Bool, /) -> Float: ...

    @overload
    def next_float64_normal(self) -> Float64:
        """
        Generate a (standard) normally distributed double precision floating point number.

        Two overloads of this function exist: the masked variant does not advance
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def next_float64_normal(self, arg: Bool, /) -> Float64: ...

    @overload
    def prev_float64_normal(self) -> Float64:
        """
        Generate the previous (standard) normally distributed double precision floating
        point number by stepping the PCG32 state backwards.

        Two overloads of this function exist: the masked variant does not regress
        the PRNG state of entries ``i`` where ``mask[i] == False``.
        """

    @overload
    def prev_float64_normal(self, arg: Bool, /) -> Float64: ...

    def __add__(self, arg: Int64, /) -> PCG32:
        """
        Advance the pseudorandom number generator.

        This function implements a multi-step advance function that is equivalent to
        (but more efficient than) calling the random number generator ``arg`` times
        in sequence.

        This is useful to advance a newly constructed PRNG to a certain known state.
        """

    def __iadd__(self, arg: Int64, /) -> PCG32:
        """In-place addition operator based on :py:func:`__add__`."""

    @overload
    def __sub__(self, arg: Int64, /) -> PCG32:
        """
        Rewind the pseudorandom number generator.

        This function implements the opposite of ``__add__`` to step a PRNG backwards.
        It can also compute the *difference* (as counted by the number of internal
        ``next_uint32`` steps) between two :py:class:`PCG32` instances. This assumes
        that the two instances were consistently seeded.
        """

    @overload
    def __sub__(self, arg: PCG32, /) -> Int64: ...

    def __isub__(self, arg: Int64, /) -> PCG32: # type: ignore
        """In-place subtraction operator based on :py:func:`__sub__`."""

    @property
    def state(self) -> UInt64:
        """
        Sequence state of the PCG32 PRNG (an unsigned 64-bit integer or integer array). Please see the original paper for details on this field.
        """

    @state.setter
    def state(self, arg: UInt64, /) -> None: ...

    @property
    def inc(self) -> UInt64:
        """
        Sequence increment of the PCG32 PRNG (an unsigned 64-bit integer or integer array). Please see the original paper for details on this field.
        """

    @inc.setter
    def inc(self, arg: UInt64, /) -> None: ...

    DRJIT_STRUCT: dict = {'state' : UInt64, 'inc' : UInt64}

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
    def __init__(self, seed: UInt64, counter_0: UInt, counter_1: UInt = 0, counter_2: UInt = 0, iterations: int = 7) -> None:
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

    def next_uint32x4(self, mask: Bool = True) -> Array4u:
        """
        Generate 4 random 32-bit unsigned integers.

        Advances the internal counter and applies the Philox mapping to
        produce 4 independent 32-bit random values.

        Args:
            mask: Optional mask to control which lanes are updated

        Returns:
            Array of 4 random 32-bit unsigned integers
        """

    def next_uint64x2(self, mask: Bool = True) -> Array2u64:
        """
        Generate 2 random 64-bit unsigned integers.

        Advances the internal counter and applies the Philox mapping to
        produce 4 independent 64-bit random values.

        Args:
            mask: Optional mask to control which lanes are updated

        Returns:
            Array of 2 random 64-bit unsigned integers
        """

    def next_float16x4(self, mask: Bool = True) -> Array4f16:
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

    def next_float32x4(self, mask: Bool = True) -> Array4f:
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

    def next_float64x2(self, mask: Bool = True) -> Array2f64:
        """
        Generate 2 random double-precision floats in :math:`[0, 1)`.

        Generates 2 random 64-bit unsigned integers and converts them to
        floats uniformly distributed on the half-open interval :math:`[0, 1)`.

        Args:
            mask: Optional mask to control which lanes are updated

        Returns:
            Array of 2 random floats on the half-open interval :math:`[0, 1)`
        """

    def next_float16x4_normal(self, mask: Bool = True) -> Array4f16:
        """
        Generate 4 normally distributed single-precision floats

        Advances the internal counter and applies the Philox mapping to produce 4
        single precision floats following a standard normal distribution.

        Args:
            mask: Optional mask to control which lanes are updated

        Returns:
            Array of 4 random floats from a standard normal distribution
        """

    def next_float32x4_normal(self, mask: Bool = True) -> Array4f:
        """
        Generate 4 normally distributed single-precision floats

        Advances the internal counter and applies the Philox mapping to produce 4
        single precision floats following a standard normal distribution.

        Args:
            mask: Optional mask to control which lanes are updated

        Returns:
            Array of 4 random floats from a standard normal distribution
        """

    def next_float64x2_normal(self, mask: Bool = True) -> Array2f64:
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

    def set_value(self, value: Float16, migrate: bool = False) -> None:
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

    def value(self) -> Float16:
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
    def eval(self, pos: Array1f, active: Bool | None = Bool(True)) -> list[Float]:
        """Evaluate the linear interpolant represented by this texture."""

    @overload
    def eval(self, pos: Array1f16, active: Bool | None = Bool(True)) -> list[Float16]: ...

    @overload
    def eval(self, pos: Array1f64, active: Bool | None = Bool(True)) -> list[Float64]: ...

    @overload
    def eval_fetch(self, pos: Array1f, active: Bool | None = Bool(True)) -> list[list[Float]]:
        """
        Fetch the texels that would be referenced in a texture lookup with
        linear interpolation without actually performing this interpolation.
        """

    @overload
    def eval_fetch(self, pos: Array1f16, active: Bool | None = Bool(True)) -> list[list[Float16]]: ...

    @overload
    def eval_fetch(self, pos: Array1f64, active: Bool | None = Bool(True)) -> list[list[Float64]]: ...

    @overload
    def eval_cubic(self, pos: Array1f, active: Bool | None = Bool(True), force_nonaccel: bool = False) -> list[Float]:
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
    def eval_cubic(self, pos: Array1f16, active: Bool | None = Bool(True), force_nonaccel: bool = False) -> list[Float16]: ...

    @overload
    def eval_cubic(self, pos: Array1f64, active: Bool | None = Bool(True), force_nonaccel: bool = False) -> list[Float64]: ...

    @overload
    def eval_cubic_grad(self, pos: Array1f, active: Bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_grad(self, pos: Array1f16, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_grad(self, pos: Array1f64, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array1f, active: Bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient and hessian matrix of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_hessian(self, pos: Array1f16, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array1f64, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_helper(self, pos: Array1f, active: Bool | None = Bool(True)) -> list[Float]:
        """
        Helper function to evaluate a clamped cubic B-Spline interpolant

        This is an implementation detail and should only be called by the
        :py:func:`eval_cubic()` function to construct an AD graph. When only the cubic
        evaluation result is desired, the :py:func:`eval_cubic()` function is faster
        than this simple implementation
        """

    @overload
    def eval_cubic_helper(self, pos: Array1f16, active: Bool | None = Bool(True)) -> list[Float16]: ...

    @overload
    def eval_cubic_helper(self, pos: Array1f64, active: Bool | None = Bool(True)) -> list[Float64]: ...

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

    def set_value(self, value: Float16, migrate: bool = False) -> None:
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

    def value(self) -> Float16:
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
    def eval(self, pos: Array2f, active: Bool | None = Bool(True)) -> list[Float]:
        """Evaluate the linear interpolant represented by this texture."""

    @overload
    def eval(self, pos: Array2f16, active: Bool | None = Bool(True)) -> list[Float16]: ...

    @overload
    def eval(self, pos: Array2f64, active: Bool | None = Bool(True)) -> list[Float64]: ...

    @overload
    def eval_fetch(self, pos: Array2f, active: Bool | None = Bool(True)) -> list[list[Float]]:
        """
        Fetch the texels that would be referenced in a texture lookup with
        linear interpolation without actually performing this interpolation.
        """

    @overload
    def eval_fetch(self, pos: Array2f16, active: Bool | None = Bool(True)) -> list[list[Float16]]: ...

    @overload
    def eval_fetch(self, pos: Array2f64, active: Bool | None = Bool(True)) -> list[list[Float64]]: ...

    @overload
    def eval_cubic(self, pos: Array2f, active: Bool | None = Bool(True), force_nonaccel: bool = False) -> list[Float]:
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
    def eval_cubic(self, pos: Array2f16, active: Bool | None = Bool(True), force_nonaccel: bool = False) -> list[Float16]: ...

    @overload
    def eval_cubic(self, pos: Array2f64, active: Bool | None = Bool(True), force_nonaccel: bool = False) -> list[Float64]: ...

    @overload
    def eval_cubic_grad(self, pos: Array2f, active: Bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_grad(self, pos: Array2f16, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_grad(self, pos: Array2f64, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array2f, active: Bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient and hessian matrix of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_hessian(self, pos: Array2f16, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array2f64, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_helper(self, pos: Array2f, active: Bool | None = Bool(True)) -> list[Float]:
        """
        Helper function to evaluate a clamped cubic B-Spline interpolant

        This is an implementation detail and should only be called by the
        :py:func:`eval_cubic()` function to construct an AD graph. When only the cubic
        evaluation result is desired, the :py:func:`eval_cubic()` function is faster
        than this simple implementation
        """

    @overload
    def eval_cubic_helper(self, pos: Array2f16, active: Bool | None = Bool(True)) -> list[Float16]: ...

    @overload
    def eval_cubic_helper(self, pos: Array2f64, active: Bool | None = Bool(True)) -> list[Float64]: ...

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

    def set_value(self, value: Float16, migrate: bool = False) -> None:
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

    def value(self) -> Float16:
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
    def eval(self, pos: Array3f, active: Bool | None = Bool(True)) -> list[Float]:
        """Evaluate the linear interpolant represented by this texture."""

    @overload
    def eval(self, pos: Array3f16, active: Bool | None = Bool(True)) -> list[Float16]: ...

    @overload
    def eval(self, pos: Array3f64, active: Bool | None = Bool(True)) -> list[Float64]: ...

    @overload
    def eval_fetch(self, pos: Array3f, active: Bool | None = Bool(True)) -> list[list[Float]]:
        """
        Fetch the texels that would be referenced in a texture lookup with
        linear interpolation without actually performing this interpolation.
        """

    @overload
    def eval_fetch(self, pos: Array3f16, active: Bool | None = Bool(True)) -> list[list[Float16]]: ...

    @overload
    def eval_fetch(self, pos: Array3f64, active: Bool | None = Bool(True)) -> list[list[Float64]]: ...

    @overload
    def eval_cubic(self, pos: Array3f, active: Bool | None = Bool(True), force_nonaccel: bool = False) -> list[Float]:
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
    def eval_cubic(self, pos: Array3f16, active: Bool | None = Bool(True), force_nonaccel: bool = False) -> list[Float16]: ...

    @overload
    def eval_cubic(self, pos: Array3f64, active: Bool | None = Bool(True), force_nonaccel: bool = False) -> list[Float64]: ...

    @overload
    def eval_cubic_grad(self, pos: Array3f, active: Bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_grad(self, pos: Array3f16, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_grad(self, pos: Array3f64, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array3f, active: Bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient and hessian matrix of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_hessian(self, pos: Array3f16, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array3f64, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_helper(self, pos: Array3f, active: Bool | None = Bool(True)) -> list[Float]:
        """
        Helper function to evaluate a clamped cubic B-Spline interpolant

        This is an implementation detail and should only be called by the
        :py:func:`eval_cubic()` function to construct an AD graph. When only the cubic
        evaluation result is desired, the :py:func:`eval_cubic()` function is faster
        than this simple implementation
        """

    @overload
    def eval_cubic_helper(self, pos: Array3f16, active: Bool | None = Bool(True)) -> list[Float16]: ...

    @overload
    def eval_cubic_helper(self, pos: Array3f64, active: Bool | None = Bool(True)) -> list[Float64]: ...

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

    def set_value(self, value: Float, migrate: bool = False) -> None:
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

    def value(self) -> Float:
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
    def eval(self, pos: Array1f, active: Bool | None = Bool(True)) -> list[Float]:
        """Evaluate the linear interpolant represented by this texture."""

    @overload
    def eval(self, pos: Array1f16, active: Bool | None = Bool(True)) -> list[Float16]: ...

    @overload
    def eval(self, pos: Array1f64, active: Bool | None = Bool(True)) -> list[Float64]: ...

    @overload
    def eval_fetch(self, pos: Array1f, active: Bool | None = Bool(True)) -> list[list[Float]]:
        """
        Fetch the texels that would be referenced in a texture lookup with
        linear interpolation without actually performing this interpolation.
        """

    @overload
    def eval_fetch(self, pos: Array1f16, active: Bool | None = Bool(True)) -> list[list[Float16]]: ...

    @overload
    def eval_fetch(self, pos: Array1f64, active: Bool | None = Bool(True)) -> list[list[Float64]]: ...

    @overload
    def eval_cubic(self, pos: Array1f, active: Bool | None = Bool(True), force_nonaccel: bool = False) -> list[Float]:
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
    def eval_cubic(self, pos: Array1f16, active: Bool | None = Bool(True), force_nonaccel: bool = False) -> list[Float16]: ...

    @overload
    def eval_cubic(self, pos: Array1f64, active: Bool | None = Bool(True), force_nonaccel: bool = False) -> list[Float64]: ...

    @overload
    def eval_cubic_grad(self, pos: Array1f, active: Bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_grad(self, pos: Array1f16, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_grad(self, pos: Array1f64, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array1f, active: Bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient and hessian matrix of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_hessian(self, pos: Array1f16, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array1f64, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_helper(self, pos: Array1f, active: Bool | None = Bool(True)) -> list[Float]:
        """
        Helper function to evaluate a clamped cubic B-Spline interpolant

        This is an implementation detail and should only be called by the
        :py:func:`eval_cubic()` function to construct an AD graph. When only the cubic
        evaluation result is desired, the :py:func:`eval_cubic()` function is faster
        than this simple implementation
        """

    @overload
    def eval_cubic_helper(self, pos: Array1f16, active: Bool | None = Bool(True)) -> list[Float16]: ...

    @overload
    def eval_cubic_helper(self, pos: Array1f64, active: Bool | None = Bool(True)) -> list[Float64]: ...

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

    def set_value(self, value: Float, migrate: bool = False) -> None:
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

    def value(self) -> Float:
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
    def eval(self, pos: Array2f, active: Bool | None = Bool(True)) -> list[Float]:
        """Evaluate the linear interpolant represented by this texture."""

    @overload
    def eval(self, pos: Array2f16, active: Bool | None = Bool(True)) -> list[Float16]: ...

    @overload
    def eval(self, pos: Array2f64, active: Bool | None = Bool(True)) -> list[Float64]: ...

    @overload
    def eval_fetch(self, pos: Array2f, active: Bool | None = Bool(True)) -> list[list[Float]]:
        """
        Fetch the texels that would be referenced in a texture lookup with
        linear interpolation without actually performing this interpolation.
        """

    @overload
    def eval_fetch(self, pos: Array2f16, active: Bool | None = Bool(True)) -> list[list[Float16]]: ...

    @overload
    def eval_fetch(self, pos: Array2f64, active: Bool | None = Bool(True)) -> list[list[Float64]]: ...

    @overload
    def eval_cubic(self, pos: Array2f, active: Bool | None = Bool(True), force_nonaccel: bool = False) -> list[Float]:
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
    def eval_cubic(self, pos: Array2f16, active: Bool | None = Bool(True), force_nonaccel: bool = False) -> list[Float16]: ...

    @overload
    def eval_cubic(self, pos: Array2f64, active: Bool | None = Bool(True), force_nonaccel: bool = False) -> list[Float64]: ...

    @overload
    def eval_cubic_grad(self, pos: Array2f, active: Bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_grad(self, pos: Array2f16, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_grad(self, pos: Array2f64, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array2f, active: Bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient and hessian matrix of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_hessian(self, pos: Array2f16, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array2f64, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_helper(self, pos: Array2f, active: Bool | None = Bool(True)) -> list[Float]:
        """
        Helper function to evaluate a clamped cubic B-Spline interpolant

        This is an implementation detail and should only be called by the
        :py:func:`eval_cubic()` function to construct an AD graph. When only the cubic
        evaluation result is desired, the :py:func:`eval_cubic()` function is faster
        than this simple implementation
        """

    @overload
    def eval_cubic_helper(self, pos: Array2f16, active: Bool | None = Bool(True)) -> list[Float16]: ...

    @overload
    def eval_cubic_helper(self, pos: Array2f64, active: Bool | None = Bool(True)) -> list[Float64]: ...

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

    def set_value(self, value: Float, migrate: bool = False) -> None:
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

    def value(self) -> Float:
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
    def eval(self, pos: Array3f, active: Bool | None = Bool(True)) -> list[Float]:
        """Evaluate the linear interpolant represented by this texture."""

    @overload
    def eval(self, pos: Array3f16, active: Bool | None = Bool(True)) -> list[Float16]: ...

    @overload
    def eval(self, pos: Array3f64, active: Bool | None = Bool(True)) -> list[Float64]: ...

    @overload
    def eval_fetch(self, pos: Array3f, active: Bool | None = Bool(True)) -> list[list[Float]]:
        """
        Fetch the texels that would be referenced in a texture lookup with
        linear interpolation without actually performing this interpolation.
        """

    @overload
    def eval_fetch(self, pos: Array3f16, active: Bool | None = Bool(True)) -> list[list[Float16]]: ...

    @overload
    def eval_fetch(self, pos: Array3f64, active: Bool | None = Bool(True)) -> list[list[Float64]]: ...

    @overload
    def eval_cubic(self, pos: Array3f, active: Bool | None = Bool(True), force_nonaccel: bool = False) -> list[Float]:
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
    def eval_cubic(self, pos: Array3f16, active: Bool | None = Bool(True), force_nonaccel: bool = False) -> list[Float16]: ...

    @overload
    def eval_cubic(self, pos: Array3f64, active: Bool | None = Bool(True), force_nonaccel: bool = False) -> list[Float64]: ...

    @overload
    def eval_cubic_grad(self, pos: Array3f, active: Bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_grad(self, pos: Array3f16, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_grad(self, pos: Array3f64, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array3f, active: Bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient and hessian matrix of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_hessian(self, pos: Array3f16, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array3f64, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_helper(self, pos: Array3f, active: Bool | None = Bool(True)) -> list[Float]:
        """
        Helper function to evaluate a clamped cubic B-Spline interpolant

        This is an implementation detail and should only be called by the
        :py:func:`eval_cubic()` function to construct an AD graph. When only the cubic
        evaluation result is desired, the :py:func:`eval_cubic()` function is faster
        than this simple implementation
        """

    @overload
    def eval_cubic_helper(self, pos: Array3f16, active: Bool | None = Bool(True)) -> list[Float16]: ...

    @overload
    def eval_cubic_helper(self, pos: Array3f64, active: Bool | None = Bool(True)) -> list[Float64]: ...

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

    def set_value(self, value: Float64, migrate: bool = False) -> None:
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

    def value(self) -> Float64:
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
    def eval(self, pos: Array1f, active: Bool | None = Bool(True)) -> list[Float]:
        """Evaluate the linear interpolant represented by this texture."""

    @overload
    def eval(self, pos: Array1f16, active: Bool | None = Bool(True)) -> list[Float16]: ...

    @overload
    def eval(self, pos: Array1f64, active: Bool | None = Bool(True)) -> list[Float64]: ...

    @overload
    def eval_fetch(self, pos: Array1f, active: Bool | None = Bool(True)) -> list[list[Float]]:
        """
        Fetch the texels that would be referenced in a texture lookup with
        linear interpolation without actually performing this interpolation.
        """

    @overload
    def eval_fetch(self, pos: Array1f16, active: Bool | None = Bool(True)) -> list[list[Float16]]: ...

    @overload
    def eval_fetch(self, pos: Array1f64, active: Bool | None = Bool(True)) -> list[list[Float64]]: ...

    @overload
    def eval_cubic(self, pos: Array1f, active: Bool | None = Bool(True), force_nonaccel: bool = False) -> list[Float]:
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
    def eval_cubic(self, pos: Array1f16, active: Bool | None = Bool(True), force_nonaccel: bool = False) -> list[Float16]: ...

    @overload
    def eval_cubic(self, pos: Array1f64, active: Bool | None = Bool(True), force_nonaccel: bool = False) -> list[Float64]: ...

    @overload
    def eval_cubic_grad(self, pos: Array1f, active: Bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_grad(self, pos: Array1f16, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_grad(self, pos: Array1f64, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array1f, active: Bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient and hessian matrix of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_hessian(self, pos: Array1f16, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array1f64, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_helper(self, pos: Array1f, active: Bool | None = Bool(True)) -> list[Float]:
        """
        Helper function to evaluate a clamped cubic B-Spline interpolant

        This is an implementation detail and should only be called by the
        :py:func:`eval_cubic()` function to construct an AD graph. When only the cubic
        evaluation result is desired, the :py:func:`eval_cubic()` function is faster
        than this simple implementation
        """

    @overload
    def eval_cubic_helper(self, pos: Array1f16, active: Bool | None = Bool(True)) -> list[Float16]: ...

    @overload
    def eval_cubic_helper(self, pos: Array1f64, active: Bool | None = Bool(True)) -> list[Float64]: ...

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

    def set_value(self, value: Float64, migrate: bool = False) -> None:
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

    def value(self) -> Float64:
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
    def eval(self, pos: Array2f, active: Bool | None = Bool(True)) -> list[Float]:
        """Evaluate the linear interpolant represented by this texture."""

    @overload
    def eval(self, pos: Array2f16, active: Bool | None = Bool(True)) -> list[Float16]: ...

    @overload
    def eval(self, pos: Array2f64, active: Bool | None = Bool(True)) -> list[Float64]: ...

    @overload
    def eval_fetch(self, pos: Array2f, active: Bool | None = Bool(True)) -> list[list[Float]]:
        """
        Fetch the texels that would be referenced in a texture lookup with
        linear interpolation without actually performing this interpolation.
        """

    @overload
    def eval_fetch(self, pos: Array2f16, active: Bool | None = Bool(True)) -> list[list[Float16]]: ...

    @overload
    def eval_fetch(self, pos: Array2f64, active: Bool | None = Bool(True)) -> list[list[Float64]]: ...

    @overload
    def eval_cubic(self, pos: Array2f, active: Bool | None = Bool(True), force_nonaccel: bool = False) -> list[Float]:
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
    def eval_cubic(self, pos: Array2f16, active: Bool | None = Bool(True), force_nonaccel: bool = False) -> list[Float16]: ...

    @overload
    def eval_cubic(self, pos: Array2f64, active: Bool | None = Bool(True), force_nonaccel: bool = False) -> list[Float64]: ...

    @overload
    def eval_cubic_grad(self, pos: Array2f, active: Bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_grad(self, pos: Array2f16, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_grad(self, pos: Array2f64, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array2f, active: Bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient and hessian matrix of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_hessian(self, pos: Array2f16, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array2f64, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_helper(self, pos: Array2f, active: Bool | None = Bool(True)) -> list[Float]:
        """
        Helper function to evaluate a clamped cubic B-Spline interpolant

        This is an implementation detail and should only be called by the
        :py:func:`eval_cubic()` function to construct an AD graph. When only the cubic
        evaluation result is desired, the :py:func:`eval_cubic()` function is faster
        than this simple implementation
        """

    @overload
    def eval_cubic_helper(self, pos: Array2f16, active: Bool | None = Bool(True)) -> list[Float16]: ...

    @overload
    def eval_cubic_helper(self, pos: Array2f64, active: Bool | None = Bool(True)) -> list[Float64]: ...

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

    def set_value(self, value: Float64, migrate: bool = False) -> None:
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

    def value(self) -> Float64:
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
    def eval(self, pos: Array3f, active: Bool | None = Bool(True)) -> list[Float]:
        """Evaluate the linear interpolant represented by this texture."""

    @overload
    def eval(self, pos: Array3f16, active: Bool | None = Bool(True)) -> list[Float16]: ...

    @overload
    def eval(self, pos: Array3f64, active: Bool | None = Bool(True)) -> list[Float64]: ...

    @overload
    def eval_fetch(self, pos: Array3f, active: Bool | None = Bool(True)) -> list[list[Float]]:
        """
        Fetch the texels that would be referenced in a texture lookup with
        linear interpolation without actually performing this interpolation.
        """

    @overload
    def eval_fetch(self, pos: Array3f16, active: Bool | None = Bool(True)) -> list[list[Float16]]: ...

    @overload
    def eval_fetch(self, pos: Array3f64, active: Bool | None = Bool(True)) -> list[list[Float64]]: ...

    @overload
    def eval_cubic(self, pos: Array3f, active: Bool | None = Bool(True), force_nonaccel: bool = False) -> list[Float]:
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
    def eval_cubic(self, pos: Array3f16, active: Bool | None = Bool(True), force_nonaccel: bool = False) -> list[Float16]: ...

    @overload
    def eval_cubic(self, pos: Array3f64, active: Bool | None = Bool(True), force_nonaccel: bool = False) -> list[Float64]: ...

    @overload
    def eval_cubic_grad(self, pos: Array3f, active: Bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_grad(self, pos: Array3f16, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_grad(self, pos: Array3f64, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array3f, active: Bool | None = Bool(True)) -> tuple:
        """
        Evaluate the positional gradient and hessian matrix of a cubic B-Spline

        This implementation computes the result directly from explicit
        differentiated basis functions. It has no autodiff support.

        The resulting gradient and hessian have been multiplied by the spatial extents
        to count for the transformation from the unit size volume to the size of its
        shape.
        """

    @overload
    def eval_cubic_hessian(self, pos: Array3f16, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_hessian(self, pos: Array3f64, active: Bool | None = Bool(True)) -> tuple: ...

    @overload
    def eval_cubic_helper(self, pos: Array3f, active: Bool | None = Bool(True)) -> list[Float]:
        """
        Helper function to evaluate a clamped cubic B-Spline interpolant

        This is an implementation detail and should only be called by the
        :py:func:`eval_cubic()` function to construct an AD graph. When only the cubic
        evaluation result is desired, the :py:func:`eval_cubic()` function is faster
        than this simple implementation
        """

    @overload
    def eval_cubic_helper(self, pos: Array3f16, active: Bool | None = Bool(True)) -> list[Float16]: ...

    @overload
    def eval_cubic_helper(self, pos: Array3f64, active: Bool | None = Bool(True)) -> list[Float64]: ...

    IsTexture: bool = True

Float32: TypeAlias = Float

Int32: TypeAlias = Int

UInt32: TypeAlias = UInt
