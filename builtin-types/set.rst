Set Types
=========

A set object is an unordered collection of distinct hashable objects. Common
uses include membership testing, removing duplicates from a sequence, and
computing mathematical operations such as intersection, union, difference, and
symmetric difference. There are two built-in types in Python: ``set`` and
``frozenset``. *However, both types are not supported in RPython*.

.. attention::
   sets are not directly supported in RPython. Instead you should use a plain
   dict and fill the values with None. Values in that dict will not consume
   space.

Right now, we can use dict to simulate a set.

.. literalinclude:: ../code/sets.py

All set operations and methods in the following code are *not supported* in
RPython.

.. literalinclude:: ../code/sets_unsupported.py
