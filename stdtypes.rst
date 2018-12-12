Built-in Types
==============

Python provides various `built-in types <https://docs.python.org/2/library/stdtypes.html>`_
such as numerics, sequences, mappings, files, classes, instance and exceptions.
Let's see how do these types behave in RPython. Note that, in this document, we
only focus on Python 2.7. The built-in types in Python 3 may be a little
different, but most of types are same.

Truth Value Testing
-------------------

The truth value testing of RPython is similar with Python.

Any object can be tested for truth value, for use in an if or while condition or
as operand of the Boolean operations below. The following values are considered
false:


* ``None``
* ``False``
* zero of any numeric type, for example, ``0``, ``0L``, ``0.0``.
* any empty sequence, for example, ``''``, ``()``, ``[]``.
* any empty mapping, for example, ``{}``.

All other values are considered true — so objects of many types are always true.

Operations and built-in functions that have a Boolean result always return ``0`` or
``False`` for false and 1 or ``True`` for true, unless otherwise stated. (Important
exception: the Boolean operations ``or`` and ``and`` always return one of their
operands.)

.. literalinclude:: code/truth_value_testing.py

However, there is one inconsistency. In Python, the following values are
considered false:

* instances of user-defined classes, if the class defines a ``__nonzero__()`` or
  ``__len__()`` method, when that method returns the integer zero or ``bool`` value
  ``False``.

In RPython, the above values are considered true.

For example, we have two classes: ``ZeroLen`` and ``NonZero``. They define
``__len__()`` and ``__nonzero__()`` methods respectively.

.. literalinclude:: code/truth_value_testing_inconsistency.py

However, the execution results are inconsistent using RPython and Python

.. code-block:: shell

    $ rpython truth_value_testing_inconsistency.py    # compile with RPython
    $ ./truth_value_testing_inconsistency-c
    zero_len is True in RPython.
    non_zero is True in RPython.

    $ python truth_value_testing_inconsistency.py    # interpret with Python
    zero_len is False in Python.
    non_zero is False in Python.

Boolean Operations
------------------

Comparisons
-----------

Numeric Types
-------------

* int
* float
* long
* complex

Iterator Types
--------------

Sequence Types
--------------

* str
* unicode
* list
* tuple
* bytearray
* buffer
* xrange

Set Types
---------

* set
* frozenset

Mapping Types
-------------

* dict

File Objects
------------

* file

memoryview type
---------------

* memoryview

Context Manager Types
---------------------

* contextmanager

Other Built-in Types
--------------------

* modules
* classes and class instances
* functions
* methods
* code objects
* type objects
* the null object
* the ellipsis object
* the NotImplemented object
* boolean values
* internal objects

Special Attributes
------------------
