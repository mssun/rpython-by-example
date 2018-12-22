Numeric Types
=============

Same as Python, there are four numeric types: plain integers (also called
integers), long integers, floating point numbers, and complex numbers.

.. todo::
   The precision difference of plain integers and long integers in RPython is
   not clear and needs to be further investigated.

All built-in numeric types support the following operations.

.. literalinclude:: ../code/numeric.py

.. attention::
   Some operations or built-in functions can be used in Python but currently not
   supported in RPython such as ``long()``, ``complex()``, ``conjugate()``,
   ``x ** y``, and ``float(nan)``.

The following code illustrated some unsupported operations in RPython.

.. literalinclude:: ../code/numeric_unsupported.py

Bitwise Operations
------------------

Bitwise operations on integer types in RPython are same as Python.

.. literalinclude:: ../code/numeric_bitwise.py

Additional Methods
------------------

In Python, there are several `additional methods
<https://docs.python.org/2/library/stdtypes.html#additional-methods-on-integer-types>`_
on integer and float types.
However, *all* these methods are not supported in RPython. For example,
``int.bit_length()`` and ``long.bit_length()`` can be used to get the number
of bits to present an integer. Others like ``float.as_integer_ratio()``,
``float.is_integer()``, ``float.hex()``, and ``float.fronhex(S)`` are also
not supported.

.. attention::
   *All* additional methods on numeric types are not supported in RPython
