Flow Control
============

.. todo:: This section is not finished yet. Provides more examples and
          explanations.

Variables
---------

Variables should contain values of at most *one type* at each control flow
point. For example, this means that joining control paths using the same
variable to contain both a string and a int must be avoided.

Let's look at this example code.

.. literalinclude:: ../code/union_error.py

The control flow graph of the ``compiler_error`` function is shown in the
following figure.

.. figure:: ../images/union_error.png
   :width: 60%
   :align: center

   Merge point of a control flow with different types.

As you can see, at the merge point (highlighted in green), ``v2`` can be
either integer ``1`` or an empty string ``''``. this violate the RPython's
restriction.

It is allowed to mix ``None`` with many other types: wrapped objects, class
instances, lists, dicts, strings, etc., but not with int, floats or tuples.

.. literalinclude:: ../code/flow_control_variables.py

Constants
---------

.. note::
    All module globals are considered constants. Their binding must not be
    changed at run-time. Moreover, global (i.e. prebuilt) lists and dictionaries
    are supposed to be immutable: modifying e.g. a global list will give
    inconsistent results. However, global instances don’t have this restriction,
    so if you need mutable global state, store it in the attributes of some
    prebuilt singleton instance.

Control structures
------------------

.. note::
    All allowed, for loops restricted to builtin types, generators very restricted.

Range
-----

.. note::
    Range and xrange are identical. range does not necessarily create an array,
    only if the result is modified. It is allowed everywhere and completely
    implemented. The only visible difference to CPython is the inaccessibility
    of the xrange fields start, stop and step.

Definitions
-----------

.. note::
    Run-time definition of classes or functions is not allowed.

Generators
----------

.. note::
    Generators are supported, but their exact scope is very limited. you can’t
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
