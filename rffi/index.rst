Foreign Function Interface (rffi)
=================================

The foreign function interface of RPython is called rffi. With rffi, you can
declaring low-level external C function, registering function as external,
defining C types, etc.


The following example shows how to use rffi to call math function in libc.

.. literalinclude:: ../code/rffi_abs.py

You can also write C function directly. The C build tool of RPython translator
will automatically compile and link with the C functions.

.. literalinclude:: ../code/rffi_separate_module_sources.py
