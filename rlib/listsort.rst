listsort
========

To sort a list in RPython, you can use the `rpython.rlib.listsort` module which
provides a Timsort sorting algorithm. `Timsort
<https://en.wikipedia.org/wiki/Timsort>`_ is a hybrid stable sorting algorithm,
derived from merge sort and insertion sort, designed to perform well on many
kinds of real-world data. Many programming languages' standard libraries use
Timsort to sort arrays of non-primitive type.

.. literalinclude:: ../code/listsort.py
