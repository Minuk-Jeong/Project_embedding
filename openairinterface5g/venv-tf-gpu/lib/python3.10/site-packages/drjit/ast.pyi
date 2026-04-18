from collections.abc import Callable as _Callable
from typing import Literal, TypeVar, Union, overload as _overload


T = TypeVar("T")

T2 = TypeVar("T2")

@_overload
def syntax(f: None = None, *, recursive: bool = False, print_ast: bool = False, print_code: bool = False) -> _Callable[[T], T]:
    """
    Syntax decorator for vectorized loops and conditionals.

    This decorator provides *syntax sugar*. It allows users to write natural
    Python code that it then turns into native Dr.Jit constructs. It *does not
    JIT-compile* or otherwise change the behavior of the function.

    The :py:func:`@drjit.syntax <drjit.syntax>` decorator introduces two
    specific changes:

    1. It rewrites ``while`` loops so that they still work when the loop
       condition is a Dr.Jit array. In that case, each element of the array
       may want to run a different number of loop iterations.

    2. Analogously, it rewrites ``if`` statements so that they work when the
       conditional expression is a Dr.Jit array. In that case, only a subset of
       array elements may want to execute the body of the ``if`` statement.

    Other control flow statements are unaffected. The transformed function may
    call other functions, whether annotated by :py:func:`drjit.syntax` or
    not. The introduced transformations only affect the annotated function.

    Internally, function turns ``while`` loops and ``if`` statements into calls
    to :py:func:`drjit.while_loop` and :py:func:`drjit.if_stmt`. It is tedious
    to write large programs in this way, which is why the decorator exists.

    For example, consider the following function that raises a floating point
    array to an integer power.

    .. code-block:: python

       import drjit as dr
       from drjit.cuda import Int, Float

       @dr.syntax
       def ipow(x: Float, n: Int):
           result = Float(1)

           while n != 0:
               if n & 1 != 0:
                   result *= x
               x *= x
               n >>= 1

           return result

    Note that this function is *vectorized*: its inputs (of types
    :py:class:`drjit.cuda.Int` and :py:class:`drjit.cuda.Float`) represent
    dynamic arrays that could contain large numbers of elements.

    The resulting code looks natural thanks to the :py:func:`@drjit.syntax
    <drjit.syntax>` decorator. Following application of this decorator, the
    function (roughly) expands into the following native Python code that
    determines relevant state variables and wraps conditionals and blocks into
    functions passed to :py:func:`drjit.while_loop` and
    :py:func:`drjit.if_stmt`. These transformations enable Dr.Jit to
    symbolically compile and automatically differentiate the implementation in
    both forward and reverse modes (if desired).

    .. code-block:: python

       def ipow(x: Float, n: Int):
           # Loop condition wrapped into a callable for ``drjit.while_loop``
           def loop_cond(n, x, result):
               return n != 0

           # Loop body wrapped into a callable for ``drjit.while_loop``
           def loop_body(n, x, result):
               # Conditional expression wrapped into callable for drjit.if_stmt
               def if_cond(n, x, result):
                   return n & 1 != 0

               # Conditional body wrapped into callable for drjit.if_stmt
               def if_body(n, x, result):
                   result *= x

                   # Return updated state following conditional stmt
                   return (n, x, result)

               # Map the 'n', 'x', and 'result' variables though the conditional
               n, x, result = dr.if_stmt(
                   (n, x, result),
                   if_cond,
                   if_body
               )

               # Rest of the loop body copy-pasted (no transformations needed here)
               x *= x
               n >>= 1

               # Return updated loop state
               return (n, x, result)

           result = Float(1)

           # Execute the loop and assign the final loop state to local variables
           n, x, result = dr.while_loop(
               (n, x, result)
               loop_cond,
               loop_body
           )

           return result

    The :py:func:`@drjit.syntax <drjit.syntax>` decorator runs *once* when
    the function is first defined. Calling the resulting function does not
    involve additional transformation steps. The transformation preserves line
    number information so that debugging works and exeptions/error messages are
    tied to the right locations in the corresponding *untransformed* function.

    Note that this decorator can only be used when the code to be transformed
    is part of a function. It cannot be applied to top-level statements on the
    Python REPL, or in a Jupyter notebook cell (unless that cell defines a
    function and applies the decorator to it).

    The two optional keyword arguments ``print_ast`` and ``print_code`` are
    both disabled by default. Set them to ``True`` to inspect the function
    before/after the transformation, either using an AST dump or via generated
    Python code

    .. code-block:: python

       @dr.syntax(print_code=True)
       def ipow(x: Float, n: Int):
           # ...

    (This feature is mostly relevant for developers working on Dr.Jit
    internals).

    Note that the functions :py:func:`if_stmt` and :py:func:`while_loop` even
    work when the loop condition is *scalar* (a Python `bool`). Since they
    don't do anything special in that case and may add (very) small overheads,
    you may want to avoid the transformation altogether. You can provide such
    control flow hints using :py:func:`drjit.hint`. Other hints can also be
    provided to request compilation using evaluated/symbolic mode, or to
    specify a maximum number of loop iteration for reverse-mode automatic
    differentiation.

    .. code-block:: python

       @dr.syntax
       def foo():
           i = 0 # 'i' is a Python 'int' and therefore does not need special
                 # handling introduced by @dr.syntax

           # Disable the transformation by @dr.syntax to avoid overheads
           while dr.hint(i < 10, mode='scalar'):
               i += 1

    Complex Python codebases often involve successive application of multiple
    decorators to a function (e.g., combinations of ``@pytest.parameterize`` in
    a test suite). If one of these decorators is :py:func:`@drjit.syntax
    <drjit.syntax>`, then be sure to place it *closest* to the ``def``
    statement defining the function. Usually, decorators wrap one function into
    another one, but :py:func:`@drjit.syntax <drjit.syntax>` is special in that
    it rewrites the underlying code. If, *hypothetically*,
    :py:func:`@drjit.syntax <drjit.syntax>` was placed *above*
    ``@pytest.parameterize``, then it would rewrite the PyTest parameterization
    wrapper instead of the actual function definition, which is almost
    certainly not wanted.

    When :py:func:`@drjit.syntax <drjit.syntax>` decorates a function
    containing *nested* functions, it only transforms the outermost function by
    default. Specify the ``recursive=True`` parameter to process them as well.

    One last point: :py:func:`@dr.syntax <drjit.syntax>` may seem
    reminiscent of function--level transformations in other frameworks like
    ``@jax.jit`` (JAX) or ``@tf.function`` (TensorFlow). There is a key
    difference: these tools create a JIT compilation wrapper that intercepts
    calls and then invokes the nested function with placeholder arguments to
    compile and cache a kernel for each encountered combination of argument
    types. :py:func:`@dr.syntax <drjit.syntax>` is not like that: it
    merely rewrites the syntax of certain loop and conditional expressions and
    has no further effect following the function definition.
    """

@_overload
def syntax(f: T, *, recursive: bool = False, print_ast: bool = False, print_code: bool = False) -> T: ...

def hint(arg: T, /, *, mode: Literal[scalar, evaluated, symbolic, None] = None, max_iterations: Union[int, None] = None, label: Union[str, None] = None, include: Union[list[object], None] = None, exclude: Union[list[object], None] = None, strict: bool = True) -> T:
    """
    Within ordinary Python code, this function is unremarkable: it returns the
    positional-only argument ``arg`` while ignoring any specified keyword
    arguments.

    The main purpose of :py:func:`drjit.hint()` is to provide *hints* that
    influence the transformation performed by the :py:func:`@drjit.syntax
    <drjit.syntax>` decorator. The following kinds of hints are supported:

    1. ``mode`` overrides the compilation mode of a ``while``
       loop or ``if`` statement. The following choices are available:

       - ``mode='scalar'`` disables code transformations, which is permitted
         when the predicate of a loop or ``if`` statement is a scalar Python
         ``bool``.

         .. code-block:: python

            i: int = 0
            while dr.hint(i < 10, mode='scalar'):
               # ...

         Routing such code through :py:func:`drjit.while_loop` or
         :py:func:`drjit.if_stmt` still works but may add small overheads,
         which motivates the existence of this flag. Note that this annotation
         does *not* cause ``mode=scalar`` to be passed
         :py:func:`drjit.while_loop`, and :py:func:`drjit.if_stmt` (which
         happens to be a valid input of both). Instead, it disables the code
         transformation altogether so that the above example translates into
         ordinary Python code:

         .. code-block:: python

            i: int = 0
            while i < 10:
               # ...

       - ``mode='evaluated'`` forces execution in *evaluated* mode and causes
         the code transformation to forward this argument to the relevant
         :py:func:`drjit.while_loop` or :py:func:`drjit.if_stmt` call.

         Refer to the discussion of :py:func:`drjit.while_loop`,
         :py:attr:`drjit.JitFlag.SymbolicLoops`, :py:func:`drjit.if_stmt`, and
         :py:attr:`drjit.JitFlag.SymbolicConditionals` for details.

       - ``mode='symbolic'`` forces execution in *symbolic* mode and causes
         the code transformation to forward this argument to the relevant
         :py:func:`drjit.while_loop` or :py:func:`drjit.if_stmt` call.

         Refer to the discussion of :py:func:`drjit.while_loop`,
         :py:attr:`drjit.JitFlag.SymbolicLoops`, :py:func:`drjit.if_stmt`, and
         :py:attr:`drjit.JitFlag.SymbolicConditionals` for details.

    2. The optional ``strict=False`` reduces the strictness of variable
       consistency checks.

       Consider the following snippet:

       .. code-block:: python

          from drjit.llvm import UInt32

          @dr.syntax
          def f(x: UInt32):
              if x < 4:
                  y = 3
              else:
                  y = 5
              return y

       This code will raise an exception.

       .. code-block:: pycon

          >> f(UInt32(1))
          RuntimeError: drjit.if_stmt(): the non-array state variable 'y' of type 'int' changed from '5' to '10'.
          Please review the interface and assumptions of 'drjit.while_loop()' as explained in the documentation
          (https://drjit.readthedocs.io/en/latest/reference.html#drjit.while_loop).

       This is because the computed variable ``y`` of type ``int`` has an
       inconsistent value depending on the taken branch. Furthermore, ``y`` is
       a scalar Python type that isn't tracked by Dr.Jit. The fix here is to
       initialize ``y`` with ``UInt32(<integer value>)``.

       However, there may also be legitimate situations where such an
       inconsistency is needed by the implementation. This can be fine as ``y``
       is not used below the ``if`` statement. In this case, you can annotate
       the conditional or loop with ``dr.hint(..., strict=False)``, which disables the check.

    3. ``max_iterations`` specifies a maximum number of loop iterations for
       reverse-mode automatic differentiation.

       Naive reverse-mode differentiation of loops (unless replaced by a
       smarter problem-specific strategy via :py:class:`drjit.custom` and
       :py:class:`drjit.CustomOp`) requires allocation of large buffers that
       hold loop state for all iterations.

       Dr.Jit requires an upper bound on the maximum number of loop iterations
       so that it can allocate such buffers, which can be provided via this
       hint. Otherwise, reverse-mode differentiation of loops will fail with an
       error message.

    4. ``label`` provovides a descriptive label.

       Dr.Jit will include this label as a comment in the generated
       intermediate representation, which can be helpful when debugging the
       compilation of large programs.

    5. ``include`` and ``exclude`` indicates to the :py:func:`@drjit.syntax
       <drjit.syntax>` decorator that a local variable *should* or *should not*
       be considered to be part of the set of state variables passed to
       :py:func:`drjit.while_loop` or :py:func:`drjit.if_stmt`.

       While transforming a function, the :py:func:`@drjit.syntax
       <drjit.syntax>` decorator sequentially steps through a program to
       identify the set of read and written variables. It then forwards
       referenced variables to recursive :py:func:`drjit.while_loop` and
       :py:func:`drjit.if_stmt` calls. In rare cases, it may be useful to
       manually include or exclude a local variable from this process---
       specify a list of such variables to the :py:func:`drjit.hint`
       annotation to do so.
    """
