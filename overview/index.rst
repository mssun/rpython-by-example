Overview
========

RPython by Example (RPyBE) is a collection of runnable examples that illustrate
various RPython concepts and libraries. RPyBE starts with a hello world example
and built-in types in RPython, then dives into RPython libraries, and build a
simple application at last.

Since RPython is based on the Python syntax, most concepts in RPython are
similar with Python. However, there are still some notable differences in
built-in types. Firstly, RPython is strong typed. This imposes some restrictions
on using built-in types such as list and dict. In addition, some implementation
differences also bring us restrictions to a certain degree. For instance, the
set type is not implemented in RPython, and we have to use dict to simulate the
set type. Since there are many differences scattered here and there, we
highlight the differences, inconsistencies, and usage suggestions in admonition
boxes within the paragraphs.

In RPyBE, we give plentiful examples on RPython's builtin types, RPython
modules, and FFI. Also, to demonstrate the capabilities of RPython, we use it to
design and implement a toy language with JIT. In a nutshell, RPyBE will help you
to understand RPython's restrictions and quickly get started with it.

.. note::
   All example source code in the book can be found in the RPyBE repository
   under the ``code`` directory. Note that file names with the ``unsupported``
   suffix are code which supported by CPython but not RPython. And file names with
   the ``error`` suffix are code to illustrate RPython compiler errors. You can
   use the ``make`` to compile a specific RPython source. For instance, to compile
   the hello world example, you need to setup ``$RPY`` path first, run ``make
   hello_world``, and execute with ``./hello_world-c``.
