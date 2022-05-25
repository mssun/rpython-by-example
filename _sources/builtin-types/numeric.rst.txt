Numeric Types
=============

Built-in numeric types
----------------------

There are three numeric types: plain integers (also called integers), long
integers, floating point numbers.

.. attention::
   Complex numbers are not supported as built-in types in RPython. However, you can
   use RPython libraries to handle complex numbers.

This table describes the details of RPython's built-in types: low-level (LL)
types, corresponding C types and sizes in memory (64-bit).

+-----------+---------+--------+---------------+---------------+
| Type      | LL Type | C Type | Size (32-bit) | Size (64-bit) |
+===========+=========+========+===============+===============+
| ``int``   | Signed  | long   |            32 |            64 |
+-----------+---------+--------+---------------+---------------+
| ``long``  | Signed  | long   |            32 |            64 |
+-----------+---------+--------+---------------+---------------+
| ``float`` | Float   | double |            64 |            64 |
+-----------+---------+--------+---------------+---------------+

For more primitive types, you can find them in the
:doc:`primitive type cheat sheet <primitive-type-cheat-sheet>` section.

Note that the ``int`` type and ``long`` type are same type in RPython, which
have same low level representation and size.

All built-in numeric types support the following operations.

.. literalinclude:: ../code/numeric.py

.. attention::
   Some operations or built-in functions can be used in Python but currently not
   supported in RPython such as ``long()``, ``complex()``, ``conjugate()``,
   ``x ** y``, ``divmode(x, y)``, ``pow(x, y)`` and ``float(nan)``. However,
   RPython's math library provided some mathematical functions.

   Also, it's worth noting that RPython do constant folding at the compilation
   time. Therefore, you may found that some built-in functions work with
   RPython's code in some scenarios. For example, you can write ``pow(123, 456)``
   in RPython code and the compiler will calculate the value at the compilation
   time.

The code snippet shows that although RPython does not support above mentioned
built-in functions, it still can do constant folding. For instance, ``divmod(x, y)``
will not yield any compilation error if x and y are constants.

.. literalinclude:: ../code/numeric_constfold.py

In addition to above functions, the following code illustrated some other
unsupported operations in RPython but supported in CPython.

.. literalinclude:: ../code/numeric_unsupported.py

.. attention::
   Besides these three built-in numeric types, RPython provides more types such as
   ``r_uint``, ``r_int32``, ``r_longlong``, etc in the arithmetic module. For more
   information, please refer to :doc:`/rlib/rarithmetic` in the rlib section

   Not like Python, RPython will not automatically use big integer when
   appropriate. The big integer type and corresponding operations are provided
   in the ``rbigint`` library, please refer to :doc:`/rlib/rbigint` in the rlib
   section.

Bitwise operations
------------------

Bitwise operations on integer types in RPython are same as Python.

.. literalinclude:: ../code/numeric_bitwise.py

Additional methods
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
   *All* additional methods such as ``int.bit_length()`` and
   ``float.float.as_integer_ratio()`` on numeric types are not supported in
   RPython.

Math functions
--------------

In Python, the ``math`` module provides access to the mathematical functions
defined by the C standard. For RPython, you can call math functions in the
similar way.

The math functions contain
``fabs``, ``log``, ``log10``, ``log1p``, ``copysign``, ``atan2``, ``frexp``,
``modf``, ``ldexp``, ``pow``, ``fmod``, ``hypot``, ``floor``, ``sqrt``, ``sin``,
``cos``, ``acos``, ``asin``, ``atan``, ``ceil``, ``cosh``, ``exp``, ``fabs``,
``sinh``, ``tan``, ``tanh``, ``acosh``, ``asinh``, ``atanh``, ``expm1``.
These math functions will call corresponding C functions in libc.

.. literalinclude:: ../code/numeric_math.py
