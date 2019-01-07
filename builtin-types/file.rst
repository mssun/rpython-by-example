File Objects
============

File operations in RPython are very similar with Python. The following example
shows some simple use cases.

.. literalinclude:: ../code/file.py

.. attention::
   In addition to these operations and methods of the built-in file objects,
   RPython's libraries (``rpython.rlib.rfile``)also provides some advanced
   operations such as ``create_stdio()`` and ``create_temp_rfile()``.
