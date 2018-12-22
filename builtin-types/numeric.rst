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

Bitwise Operations on Integer Types
-----------------------------------

Bitwise operations in RPython are same as Python.

.. literalinclude:: ../code/numeric_bitwise.py
