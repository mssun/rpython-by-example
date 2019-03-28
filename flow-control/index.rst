Flow Control
============

.. todo:: This section is not finished yet. Provides more examples and
          explanations.

variables

    variables should contain values of at most one type as described in Object
    restrictions at each control flow point, that means for example that joining
    control paths using the same variable to contain both a string and a int
    must be avoided. It is allowed to mix None (basically with the role of a
    null pointer) with many other types: wrapped objects, class instances,
    lists, dicts, strings, etc. but not with int, floats or tuples.

constants

    all module globals are considered constants. Their binding must not be
    changed at run-time. Moreover, global (i.e. prebuilt) lists and dictionaries
    are supposed to be immutable: modifying e.g. a global list will give
    inconsistent results. However, global instances don’t have this restriction,
    so if you need mutable global state, store it in the attributes of some
    prebuilt singleton instance.

control structures

    all allowed, for loops restricted to builtin types, generators very restricted.

range

    range and xrange are identical. range does not necessarily create an array,
    only if the result is modified. It is allowed everywhere and completely
    implemented. The only visible difference to CPython is the inaccessibility
    of the xrange fields start, stop and step.

definitions

    run-time definition of classes or functions is not allowed.

generators

    generators are supported, but their exact scope is very limited. you can’t
    merge two different generator in one control point.

Exceptions
----------

Python exceptions are fully supported. For example, you can catch exceptions by
the ``except`` keyword following a specific exception class.

.. literalinclude:: ../code/errors_exceptions.py

You can also use the ``raise`` keyword to raise exceptions. The ``finally`` keyword
is used to do some cleanup actions.

.. literalinclude:: ../code/handle_exceptions.py

.. attention::
   There is one special difference in the exception handling on "simple cases".
   In `RPython document
   <https://rpython.readthedocs.io/en/latest/rpython.html#exception-rules>`_, it
   says by default, **code with no exception handlers does
   not raise exceptions**. By supplying an exception handler, you ask for error
   checking. Without, you assure the system that the operation cannot fail. This
   rule does not apply to function calls: any called function is assumed to be
   allowed to raise any exception.

.. todo::
   MesaPy added mandatory ``IndexError`` checks. Give some details here.
