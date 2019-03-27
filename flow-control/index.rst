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

exceptions

    fully supported. see below Exception rules for restrictions on exceptions
    raised by built-in operations
