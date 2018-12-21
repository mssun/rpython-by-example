Numeric Types
=============

There are four numeric types: plain integers (also just called integers), long
integers, floating point numbers, and complex numbers.

All built-in numeric types support the following operations.

.. literalinclude:: ../code/numeric.py

.. warning::
   Some operations or built-in functions can be used in Python but currently not
   supported in RPython such as ``long()``, ``complex()``, ``conjugate()``,
   ``x ** y``, and ``float(nan)``.

.. literalinclude:: ../code/numeric_unsupported.py

Bitwise Operations on Integer Types
-----------------------------------

