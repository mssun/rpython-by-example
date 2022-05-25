Mapping Types
=============

There is currently only one standard mapping type in Python, the dictionary.
Operations and methods of the dict type in RPython are similar with Python.

.. literalinclude:: ../code/dict.py

As you can see, most methods of dictionary are supported in RPython. However,
there are some exceptions.

.. attention::
   * dicts with a unique key type only, provided it is hashable
   * custom hash functions and custom equality will not be honored. Use
     ``rpython.rlib.objectmodel.r_dict`` for custom hash functions.
   * the dictionary view object is not supported in RPython.

.. literalinclude:: ../code/dict_unsupported.py
