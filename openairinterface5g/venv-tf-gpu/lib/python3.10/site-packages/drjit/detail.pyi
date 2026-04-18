from collections.abc import Callable, Sequence
import enum
from typing import Type, overload

import drjit
import drjit.cuda
import drjit.llvm
import drjit.nn as nn
import drjit.scalar


class scoped_rtld_deepbind:
    """
    Python context manager to import extensions with RTLD_DEEPBIND if needed
    """

    def __enter__(self): ...

    def __exit__(self, exc_type, exc_val, exc_tb): ...

class IntrusiveBase:
    """Base class with intrusive combined C++/Python reference counting."""

class dr_iterator:
    def __iter__(self, /):
        """Implement iter(self)."""

    def __next__(self, /):
        """Implement next(self)."""

class TraversableBase:
    pass

class FrozenFunction:
    def __init__(self, arg0: Callable, arg1: int, arg2: int, arg3: drjit.JitBackend, arg4: bool, /) -> None: ...

    @property
    def n_cached_recordings(self) -> int: ...

    @property
    def n_recordings(self) -> int: ...

    def clear(self) -> None: ...

    def __call__(self, arg: dict, /) -> object: ...

class ADScope(enum.Enum):
    Invalid = 0

    Suspend = 1

    Resume = 2

    Isolate = 3

class NullContextManager:
    def __init__(self) -> None: ...

    def __enter__(self) -> None: ...

    def __exit__(self, arg0: object | None, arg1: object | None, arg2: object | None) -> None: ...

class ADContextManager:
    def __init__(self, arg0: ADScope, arg1: Sequence[int], /) -> None: ...

    def __enter__(self) -> None: ...

    def __exit__(self, arg0: object | None, arg1: object | None, arg2: object | None) -> None: ...

def new_grad(arg: object, /) -> object: ...

def collect_indices(arg: object, /) -> list[int]:
    """
    Return Dr.Jit variable indices associated with the provided data structure.

    This function traverses Dr.Jit arrays, tensors, :ref:`PyTree <pytrees>` (lists,
    tuples, dictionaries, custom data structures) and returns the indices of all detected
    variables (in the order of traversal, may contain duplicates). The index
    information is returned as a list of encoded 64 bit integers, where each
    contains the AD variable index in the upper 32 bits and the JIT variable
    index in the lower 32 bit.

    This function exists for Dr.Jit-internal use. You probably should not
    call it in your own application code.
    """

def update_indices(value: object, indices: Sequence[int]) -> object:
    """
    Create a copy of the provided input while replacing Dr.Jit variables
    with new ones based on a provided set of indices.

    This function works analogously to ``collect_indices``, except that it
    consumes an index array and produces an updated output.

    It recursively traverses and copies an input object that may be a Dr.Jit
    array, tensor, or :ref:`PyTree <pytrees>` (list, tuple, dict, custom data
    structure) while replacing any detected Dr.Jit variables with new ones based
    on the provided index vector. The function returns the resulting object,
    while leaving the input unchanged. The output array object borrows the
    provided array references as opposed to stealing them.

    This function exists for Dr.Jit-internal use. You probably should not call
    it in your own application code.
    """

def copy(value: object) -> object:
    """
    Create a deep copy of a PyTree

    This function recursively traverses PyTrees and replaces Dr.Jit arrays with
    copies created via the ordinary copy constructor. It also rebuilds tuples,
    lists, dictionaries, and custom data structures. The purpose of this function
    is isolate the inputs of :py:func:`drjit.while_loop()` and
    :py:func:`drjit.if_stmt()` from changes.

    This function exists for Dr.Jit-internal use. You probably should not call
    it in your own application code.
    """

def check_compatibility(arg0: object, arg1: object, arg2: bool, arg3: str, /) -> None:
    """
    Traverse two PyTrees in parallel and ensure that they have an identical
    structure.

    Raises an exception is a mismatch is found (e.g., different types, arrays with
    incompatible numbers of elements, dictionaries with different keys, etc.)

    When the ``width_consistency`` argument is enabled, an exception will also be
    raised if there is a mismatch of the vectorization widths of any Dr.Jit type
    in the pytrees.
    """

def reset(arg: object, /) -> object:
    """
    Release all Jit variables in a PyTree

    This function recursively traverses PyTrees and replaces Dr.Jit arrays with
    empty instances of the same type. :py:func:`drjit.while_loop` uses this
    function internally to release references held by a temporary copy of the
    state tuple.
    """

def llvm_version() -> tuple: ...

def cuda_version() -> tuple: ...

def trace_func(frame: object, event: object, arg: object | None = None) -> object: ...

def clear_registry() -> None:
    """
    Clear all instances that are currently registered with Dr.Jit's instance
    registry. This is may be needed in a very specific corner case: when a large
    program (e.g., a test suite) dispatches function calls via instance arrays, and
    when such a test suite raises exceptions internally and holds on to them (which
    is e.g., what PyTest does to report errors all the way at the end), then the
    referenced instances may remain alive beyond their usual lifetime. This can
    have an unintended negative effect by influencing subsequent tests that must
    now also consider the code generated by these instances (in particular,
    failures due to unimplemented functions
    """

def import_tensor(tensor: object, ad: bool = False) -> object: ...

def any_symbolic(arg: object, /) -> bool:
    """
    Returns ``true`` if any of the values in the provided PyTree are symbolic variables.
    """

def reduce_identity(dtype: Type[drjit.ArrayT], op: drjit.ReduceOp, size: int = 1, /) -> drjit.ArrayT:
    """
    Return the identity element for a reduction with the desired variable type
    and operation.
    """

def can_scatter_reduce(arg0: type[drjit.ArrayBase], arg1: drjit.ReduceOp, /) -> bool:
    """
    Check if the underlying backend supports a desired flavor of
    scatter-reduction for the given array type.
    """

def cuda_compute_capability() -> int: ...

def new_scope(backend: drjit.JitBackend) -> int:
    """
    Set a new scope identifier to separate basic blocks.

    Several steps of Dr.Jit's compilation rely on the definition of
    a "basic block", which marks the boundary for certain optimizations
    and re-orderings to take place (e.g., common subexpression elimination).

    When executing Dr.Jit computation on different threads, the user
    has to ensure that basic blocks are separated between threads.
    Before a thread T2 references Dr.Jit arrays created by another thread T1,
    it must create a new scope to guarantee that dependencies between them
    are correctly tracked and ordered during the compilation process. Dr.Jit
    checks for violations of this condition and will raise an exception when
    attempting to evaluate incorrectly ordered expressions.

    This function sets a unique, new scope identifier (a simple 32 bit integer)
    to separate any of the following computation from the previous basic block.
    """

def scope(backend: drjit.JitBackend) -> int:
    """Queries the scope identifier (see :py:func:`drjit.detail.new_scope())"""

def set_scope(backend: drjit.JitBackend, scope: int) -> None:
    """
    Manually sets a scope identifier (see :py:func:`drjit.detail.new_scope())
    """

def leak_warnings() -> bool:
    """
    Query whether leak warnings are enabled. See :py:func:`drjit.detail.set_leak_warnings()`.
    """

def set_leak_warnings(arg: bool, /) -> None:
    """
    Dr.Jit tracks and can report leaks of various types (Python instance leaks,
    Dr.Jit-Core variable leaks, AD variable leaks). Since benign warnings can
    sometimes occur, they are disabled by default for PyPI release builds.
    Use this function to enable/disable them explicitly.
    """

def traverse_py_cb_ro(arg0: object, arg1: Callable, /) -> None: ...

def traverse_py_cb_rw(arg0: object, arg1: Callable, /) -> None: ...

class AllocType(enum.Enum):
    Host = 0

    HostAsync = 1

    HostPinned = 2

    Device = 3

def malloc_watermark(arg: AllocType, /) -> int:
    """Return the peak memory usage (watermark) for a given allocation type"""

def malloc_clear_statistics() -> None:
    """Clear memory allocation statistics"""

def launch_stats() -> tuple:
    """Return kernel launch statistics (launches, soft_misses, hard_misses)"""

class IndexVector:
    """
    Reference-counted index vector. This class stores references to Dr.Jit
    variables and generally behaves like a ``list[int]``. The main difference
    is that it holds references to the elements so that they cannot expire.

    The main purpose of this class is to represent the inputs and outputs of
    :py:func:`drjit.detail.VariableTracker.read` and
    :py:func:`drjit.detail.VariableTracker.write`.
    """

    def __init__(self) -> None: ...

    def append(self, arg: int, /) -> None: ...

    def clear(self) -> None: ...

    def __len__(self) -> int: ...

    def __getitem__(self, arg: int, /) -> int: ...

    def __setitem__(self, arg0: int, arg1: int, /) -> None: ...

class VariableTracker:
    """
    Helper class for tracking state variables during control flow operations.

    This class reads and writes state variables as part of control flow
    operations such as :py:func:`dr.while_loop() <while_loop>` and
    :py:func:`dr.if_stmt() <if_stmt>`. It checks that each variable remains
    consistent across this multi-step process.

    Consistency here means that:

    - The tree structure of the :ref:`PyTree <pytrees>` PyTree is preserved
      across calls to :py:func:`read()`` and :py:func:`write()``.

    - The type of every PyTree element is similarly preserved.

    - The sizes of Dr.Jit arrays in the PyTree remain compatible across calls to
      :py:func:`read()` and :py:func:`write()`. The sizes of two arrays ``a``
      and ``b`` are considered compatible if ``a+b`` is well-defined (it's okay
      if this involves an intermediate broadcasting step.)

    In the case of an inconsistency, the implementation generates an error
    message that identifies the problematic variable by name.
    """

    def __init__(self, strict: bool = True, check_size: bool = True) -> None:
        """
        Create a new variable tracker.

        The constructor accepts two parameters:

        - ``strict``: Certain types of Python objects (e.g. custom Python classes
          without ``DRJIT_STRUCT`` field, scalar Python numeric types) are not
          traversed by the variable tracker. If ``strict`` mode is enabled, any
          inconsistency here will cause the implementation to immediately give up
          with an error message. This is not always desired, hence this behavior
          is configurable.

        - ``check_size``: If set to ``true``, the tracker will ensure that
          variables remain size-compatible. The one case in Dr.Jit where this is
          not desired are evaluated loops with compression enabled (i.e.,
          inactive elements are pruned, which causes the array size to
          progressively shrink).
        """

    def write(self, state: object, indices: IndexVector, preserve_dirty: bool = False, labels: Sequence[str] = (), default_label: str = 'state') -> None:
        """
        Traverse a PyTree and write its variable indices.

        This function recursively traverses the PyTree ``state`` and updates the
        encountered Dr.Jit arrays with indices from the ``indices`` argument.
        It performs numerous consistency checks during this
        process to ensure that variables remain consistent over time.

        When ``preserve_dirty`` is set to ``true``, the function leaves
        dirty arrays (i.e., ones with pending side effects) unchanged.

        The ``labels`` argument optionally identifies the top-level variable
        names tracked by this instance. This is recommended to obtain actionable
        error messages in the case of inconsistencies. Otherwise,
        ``default_label`` is prefixed to variable names.
        """

    def read(self, state: object, labels: Sequence[str] = (), default_label: str = 'state') -> IndexVector:
        """
        Traverse a PyTree and read its variable indices.

        This function recursively traverses the PyTree ``state`` and appends the
        indices of encountered Dr.Jit arrays to the reference-counted output
        vector ``indices``. It performs numerous consistency checks during this
        process to ensure that variables remain consistent over time.

        The ``labels`` argument optionally identifies the top-level variable
        names tracked by this instance. This is recommended to obtain actionable
        error messages in the case of inconsistencies. Otherwise,
        ``default_label`` is prefixed to variable names.
        """

    def verify_size(self, arg: int, /) -> None: ...

    def clear(self) -> None:
        """Clear all variable state stored by the variable tracker."""

    def restore(self, labels: Sequence[str] = (), default_label: str = 'state') -> object:
        """
        Undo all changes and restore tracked variables to their original state.
        """

    def rebuild(self, labels: Sequence[str] = (), default_label: str = 'state') -> object:
        """
        Create a new copy of the PyTree representing the final
        version of the PyTree following a symbolic operation.

        This function returns a PyTree representing the latest state. This PyTree
        is created lazily, and it references the original one whenever values
        were unchanged. This function also propagates in-place updates when
        they are detected.
        """

    class Context:
        pass

class Resampler:
    @overload
    def __init__(self, source_res: int, target_res: int, filter: str, filter_radius: float | None = None, convolve: bool = False) -> None: ...

    @overload
    def __init__(self, source_res: int, target_res: int, filter: Callable[float, float], filter_radius: float, convolve: bool = False) -> None: ...

    @overload
    def resample_fwd(self, source: drjit.cuda.Float16, stride: int) -> drjit.cuda.Float16: ...

    @overload
    def resample_fwd(self, source: drjit.cuda.Float, stride: int) -> drjit.cuda.Float: ...

    @overload
    def resample_fwd(self, source: drjit.cuda.Float64, stride: int) -> drjit.cuda.Float64: ...

    @overload
    def resample_fwd(self, source: drjit.llvm.Float16, stride: int) -> drjit.llvm.Float16: ...

    @overload
    def resample_fwd(self, source: drjit.llvm.Float, stride: int) -> drjit.llvm.Float: ...

    @overload
    def resample_fwd(self, source: drjit.llvm.Float64, stride: int) -> drjit.llvm.Float64: ...

    @overload
    def resample_fwd(self, source: drjit.scalar.ArrayXf16, stride: int) -> drjit.scalar.ArrayXf16: ...

    @overload
    def resample_fwd(self, source: drjit.scalar.ArrayXf, stride: int) -> drjit.scalar.ArrayXf: ...

    @overload
    def resample_fwd(self, source: drjit.scalar.ArrayXf64, stride: int) -> drjit.scalar.ArrayXf64: ...

    @overload
    def resample_bwd(self, target: drjit.cuda.Float16, stride: int) -> drjit.cuda.Float16: ...

    @overload
    def resample_bwd(self, target: drjit.cuda.Float, stride: int) -> drjit.cuda.Float: ...

    @overload
    def resample_bwd(self, target: drjit.cuda.Float64, stride: int) -> drjit.cuda.Float64: ...

    @overload
    def resample_bwd(self, target: drjit.llvm.Float16, stride: int) -> drjit.llvm.Float16: ...

    @overload
    def resample_bwd(self, target: drjit.llvm.Float, stride: int) -> drjit.llvm.Float: ...

    @overload
    def resample_bwd(self, target: drjit.llvm.Float64, stride: int) -> drjit.llvm.Float64: ...

    @property
    def source_res(self) -> int: ...

    @property
    def target_res(self) -> int: ...

    def __repr__(self) -> str: ...
