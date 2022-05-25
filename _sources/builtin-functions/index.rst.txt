Built-in Functions
==================

The Python interpreter has a number of
`built-in functions <https://docs.python.org/2/library/functions.html>`_,
but only few of them are supported by RPython.

.. literalinclude:: ../code/builtin.py

.. attention::
   Built-in functions are very limited in RPython. For instance, ``sum()`` is
   not supported in RPython. Moreover, supported functions like ``min()`` do not
   provide the same functionalities in Python. The ``min()`` function in RPython
   can only compare two values, but in Python, it can be used to find the
   minimum value in a list.
