Sequence Types
==============

There are seven sequence types: strings, Unicode strings, lists, tuples,
bytearrays, buffers, and xrange objects. For other containers see the
built in dict and set classes. These types can be used in RPython same
as in Python.

.. literalinclude:: ../code/sequence.py

Most operations for sequence types are supported in RPython, but some have
restrictions. Such as slicing with negative indexes and min/max builtin methods.

.. literalinclude:: ../code/sequence_unsupported.py

string
------

Only a few string methods are supported in RPython. Besides the limited methods
in RPython, there are also some restrictions of indexing, slicing, and string
formating. Also, note that the type of items in a list should be same, and you
cannot mix types in a RPython list.
The following examples show some supported methods and usages in RPython.

.. literalinclude:: ../code/strings.py

.. attention::
   * Not all string methods are supported and those that are supported, not
     necesarilly accept all arguments.
   * Indexes can be negative. In case they are not, then you get slightly more
     efficient code if the translator can prove that they are non-negative. When
     slicing a string it is necessary to prove that the slice start and stop
     indexes are non-negative.
   * No implicit str-to-unicode cast.
   * Simple string formatting using the ``%`` operator works, as long as the
     format string is known at translation time; the only supported formatting
     specifiers are ``%s``, ``%d``, ``%x``, ``%o``, ``%f``, plus ``%r`` but only
     for user-defined instances
   * Modifiers such as conversion flags, precision, length etc. are not
     supported.
   * It is forbidden to mix unicode and strings when formatting.

The following examples show some unsupported methods and usages in RPython, but
can be used in a normal Python implementation.

.. literalinclude:: ../code/strings_unsupported.py

list
----

Most list operations and methods are supported in RPython. However, methods
may have some restrictions. The following examples illustrate usages of the list
in RPython and some unsupported operations as well.

.. literalinclude:: ../code/lists.py

.. attention::
   lists are used as an allocated array.  Lists are over-allocated, so list.append()
   is reasonably fast. However, if you use a fixed-size list, the code
   is more efficient. Annotator can figure out most of the time that your
   list is fixed-size, even when you use list comprehension.
   Negative or out-of-bound indexes are only allowed for the
   most common operations, as follows:

   - *indexing*:
     positive and negative indexes are allowed. Indexes are checked when requested
     by an IndexError exception clause.

   - *slicing*:
     the slice start must be within bounds. The stop doesn't need to, but it must
     not be smaller than the start.  All negative indexes are disallowed, except for
     the [:-1] special case.  No step.  Slice deletion follows the same rules.

   - *slice assignment*:
     only supports ``lst[x:y] = sublist``, if ``len(sublist) == y - x``.
     In other words, slice assignment cannot change the total length of the list,
     but just replace items.

   - *other operators*:
     ``+``, ``+=``, ``in``, ``*``, ``*=``, ``==``, ``!=`` work as expected.

   - *methods*:
     append, index, insert, extend, reverse, pop.  The index used in pop() follows
     the same rules as for *indexing* above.  The index used in insert() must be within
     bounds and not negative.

.. literalinclude:: ../code/lists_unsupported.py

tuple
-----

Tuples in RPython are very different. There are many restrictions to use tuples.

.. literalinclude:: ../code/tuples.py

The restrictions can be summarized as follows.

.. attention::
   * no variable-length tuples; use them to store or return pairs or n-tuples of
     values. Each combination of types for elements and length constitute a
     separate and not mixable type.
   * There is no general way to convert a list into a tuple, because the length
     of the result would not be known statically. (You can of course do
     ``t = (lst[0], lst[1], lst[2])`` if you know that lst has got 3 items.)

xrange
------

The following examples illustrate the usage of ``range`` and ``xrange`` in
RPython. ``range`` and ``xrange`` are identical. ``range`` does not necessarily
create an array, only if the result is modified.

.. literalinclude:: ../code/xrange.py
