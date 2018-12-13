Comparisons
===========

Comparison operations in RPython are similar with Python, which contain:
``<``, ``<=``, ``>``, ``>=``, ``==``, ``!=``, ``is``, ``is not``. Note that
``is`` and ``is not`` are operations to compare object identity.

Non-identical instances of a class normally compare as non-equal unless the
class defines the ``__eq__()`` method.

.. warning::
    One exception should be noted is that the comparisons of instances of same class
    or other types of object by defining ``__lt__()``, ``__le__()``, ``__gt__()``,
    ``__ge__()``, and ``__cmp__()`` method was not supported in RPython.

The following example shows the comparisons between integers and instances.

.. literalinclude:: ../code/comparisons.py
