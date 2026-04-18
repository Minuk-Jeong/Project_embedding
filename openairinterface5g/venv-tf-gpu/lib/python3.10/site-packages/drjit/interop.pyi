from collections.abc import Callable
import types
from typing import TypeVar, Union


def wrap_into_dr_tensor(value):
    """Helper to transform a PyTree's members to Dr.Jit tensors"""

def wrap_into_tf_tensor(value):
    """Helper to transform a PyTree's members to TF tensors"""

T = TypeVar("T")

def wrap(source: Union[str, types.ModuleType], target: Union[str, types.ModuleType]) -> Callable[[T], T]:
    """
    Differentiable bridge between Dr.Jit and other array programming
    frameworks.

    This function wraps computation performed using one array programming
    framework to expose it in another. Currently, `PyTorch
    <https://pytorch.org>`__, `TensorFlow <https://tensorflow.org>`__,
    and `JAX <https://jax.readthedocs.io>`__ are supported, though other
    frameworks may be added in the future.

    Annotating a function with :py:func:`@drjit.wrap <wrap>` adds code
    that suitably converts arguments and return values. Furthermore, it
    stitches the operation into the *automatic differentiation* (AD) graph of
    the other framework to ensure correct gradient propagation.

    When exposing code written using another framework, the wrapped function
    can take and return any :ref:`PyTree <pytrees>` including flat or nested
    Dr.Jit arrays, tensors, and arbitrary nested lists/tuples, dictionaries,
    and custom data structures. The arguments don't need to be
    differentiable---for example, integer/boolean arrays that don't carry
    derivative information can be passed as well.

    The wrapped function should be *pure*: in other words, it should read its
    input(s) and compute an associated output so that re-evaluating the
    function again produces the same answer. Multi-framework derivative
    tracking of impure computation will likely not behave as expected.

    The following table lists the currently supported conversions:

    .. |nbsp| unicode:: 0xA0
       :trim:

    .. list-table::
       :widths: 1 5 5 5 50
       :header-rows: 1

       * - Direction
         - Primal
         - Forward-mode |nbsp| AD
         - Reverse-mode |nbsp| AD
         - Remarks

       * - ``drjit`` → ``torch``
         - .. centered:: ✅
         - .. centered:: ✅
         - .. centered:: ✅
         - Everything just works.

       * - ``torch`` → ``drjit``
         - .. centered:: ✅
         - .. centered:: ✅
         - .. centered:: ✅

         - **Limitation**: The passed/returned :ref:`PyTrees <pytrees>` can
           contain arbitrary arrays or tensors, but other types
           (e.g., a custom Python object not understood by PyTorch) will
           raise errors when differentiating in *forward mode* (backward mode
           works fine).

           An `issue <https://github.com/pytorch/pytorch/issues/117491>`__ was
           filed on the PyTorch bugtracker.

       * - ``drjit`` → ``tf``
         - .. centered:: ✅
         - .. centered:: ✅
         - .. centered:: ✅
         - You may want to further annotate the wrapped function with
           ``tf.function`` to trace and just-in-time compile it in the
           Tensorflow environment, i.e.,

           .. code-block:: python

              @dr.wrap(source='drjit', target='tf')
              @tf.function(jit_compile=False) # Set to True for XLA mode

           **Limitation**: There is an issue for tf.int32 tensors which are
           wrongly placed on CPU by DLPack. This can lead to inconsistent device
           placement of tensors.

           An `issue <https://github.com/tensorflow/tensorflow/issues/78091>`__
           was filed on the TensorFlow bugtracker.

       * - ``tf`` → ``drjit``
         - .. centered:: ✅
         - .. centered:: ❌
         - .. centered:: ✅
         - TensorFlow has some limitiations with respect to custom gradients
           in foward-mode AD.

           **Limitation**: TensorFlow does not allow for non-tensor
           input structures in fuctions with
           `custom gradients
           <https://www.tensorflow.org/api_docs/python/tf/custom_gradient>`__.

           TensorFlow has a bug for functions with custom gradients and
           keyword arguments.

           An `issue <https://github.com/tensorflow/tensorflow/issues/77559>`__
           was filed on the TensorFlow bugtracker.

       * - ``drjit`` → ``jax``
         - .. centered:: ✅
         - .. centered:: ✅
         - .. centered:: ✅
         - You may want to further annotate the wrapped function with
           ``jax.jit`` to trace and just-in-time compile it in the JAX
           environment, i.e.,

           .. code-block:: python

              @dr.wrap(source='drjit', target='jax')
              @jax.jit

           **Limitation**: The passed/returned :ref:`PyTrees <pytrees>` can
           contain arbitrary arrays or Python scalar types, but other types
           (e.g., a custom Python object not understood by JAX) will raise
           errors.

       * - ``jax`` → ``drjit``
         - .. centered:: ❌
         - .. centered:: ❌
         - .. centered:: ❌
         - This direction is currently unsupported. We plan to add it in
           the future.

    Please also refer to the documentation sections on :ref:`multi-framework
    differentiation <interop_ad>` :ref:`associated caveats <interop_caveats>`.

    .. note::

       Types that have no equivalent on the other side (e.g. a quaternion
       array) will convert to generic tensors.

       Data exchange is limited to representations that exist on both sides.
       There are a few limitations:

       - PyTorch `lacks support for most unsigned integer types
         <https://github.com/pytorch/pytorch/issues/58734>`__ (``uint16``,
         ``uint32``, or ``uint64``-typed arrays). Use signed integer types to
         work around this issue.

       - TensorFlow has limitations with respect to forward-mode AD for
         functions with custom gradients.There is also an `issue for functions
         with keyword arguments
         <https://github.com/tensorflow/tensorflow/issues/77559>`__.

       - Dr.Jit currently lacks support for most 8- and 16-bit numeric types
         (besides half precision floats).

       - JAX `refuses to exchange
         <https://github.com/google/jax/issues/19352>`__ boolean-valued
         tensors with other frameworks.

    Args:
        source (str | module): The framework used *outside* of the wrapped
          function. The argument is currently limited to either ``'drjit'``,
          ``'torch'``, ``'tf'``, or ``jax'``. For convenience, the associated Python
          module can be specified as well.

        target (str | module): The framework used *inside* of the wrapped
          function. The argument is currently limited to either ``'drjit'``,
          ``'torch'``, ``'tf'``, or ``'jax'``. For convenience, the associated Python
          module can be specified as well.

    Returns:
        The decorated function.
    """
