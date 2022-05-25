Iterator Types
==============

The iterator type in RPython is similar with Python, it can help to iterator
over containers. The iterator objects should support ``__iter__()`` and
``next()`` methods. These two methods form the *iterator protocol*.

.. literalinclude:: ../code/iterator.py

.. attention::
   You cannot get an iterator object of a list using the ``__iter__()`` method
   in RPython.

If a container object's ``__iter__()`` method is implemented as a generator, it
will automatically return an iterator object with the ``__iter__()`` and
``next()`` method. Here is an example of a customized container object
implemented the *iterator protocol* using generator.

.. literalinclude:: ../code/iterator_generator.py
