Classes
=======

Classes in RPython are very similar with Python. You can inherit a class
and override methods.

.. attention::
   There are some restrictions in RPython: 1) methods and other class attributes
   do not change after startup, 2) only single inheritance is supported.

.. literalinclude:: ../code/classes.py

Multiple inheritance only supported with *mixin*.

.. attention::
   use ``rpython.rlib.objectmodel.import_from_mixin(M)`` in a class body to copy
   the whole content of a class M. This can be used to implement mixins:
   functions and staticmethods are duplicated (the other class attributes are
   just copied unmodified).

.. literalinclude:: ../code/classes_mixin.py
