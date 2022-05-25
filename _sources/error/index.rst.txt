Compilation Errors
==================

Since RPython is only designed for PyPy at the first place, the compilation error
messages are a bit confusing. Sometime, you need some knowledge of compiler
design to understand what's going on. In this section, we show some common
error messages you will see when compiler fails to compile the RPython sources.

This is a very common error message caused by mixing different types.

.. literalinclude:: ../code/union_error.py

The following is a very verbose and confusing error message (which can be
greatly improved). The RPython compiler will print out the stack trace like
other exceptions in Python. You can find out types, error description, and other
useful information of the error in the highlighted part below. In addition,
the RPython compiler will give you a Pdb for debugging.

.. code-block:: text
   :emphasize-lines: 34-46

   [translation:info] Error:
      File "/pypy/rpython/translator/goal/translate.py", line 318, in main
        drv.proceed(goals)
      File "/pypy/rpython/translator/driver.py", line 554, in proceed
        result = self._execute(goals, task_skip = self._maybe_skip())
      File "/pypy/rpython/translator/tool/taskengine.py", line 114, in _execute
        res = self._do(goal, taskcallable, *args, **kwds)
      File "/pypy/rpython/translator/driver.py", line 278, in _do
        res = func()
      File "/pypy/rpython/translator/driver.py", line 315, in task_annotate
        s = annotator.build_types(self.entry_point, self.inputtypes)
      File "/pypy/rpython/annotator/annrpython.py", line 92, in build_types
        return self.build_graph_types(flowgraph, inputs_s, complete_now=complete_now)
      File "/pypy/rpython/annotator/annrpython.py", line 140, in build_graph_types
        self.complete()
      File "/pypy/rpython/annotator/annrpython.py", line 229, in complete
        self.complete_pending_blocks()
      File "/pypy/rpython/annotator/annrpython.py", line 224, in complete_pending_blocks
        self.processblock(graph, block)
      File "/pypy/rpython/annotator/annrpython.py", line 398, in processblock
        self.flowin(graph, block)
      File "/pypy/rpython/annotator/annrpython.py", line 572, in flowin
        self.follow_link(graph, link, constraints)
      File "/pypy/rpython/annotator/annrpython.py", line 603, in follow_link
        self.addpendingblock(graph, link.target, inputs_s)
      File "/pypy/rpython/annotator/annrpython.py", line 189, in addpendingblock
        self.mergeinputargs(graph, block, cells)
      File "/pypy/rpython/annotator/annrpython.py", line 435, in mergeinputargs
        unions = [annmodel.unionof(c1,c2) for c1, c2 in zip(oldcells,inputcells)]
      File "/pypy/rpython/annotator/model.py", line 775, in unionof
        s1 = pair(s1, s2).union()
      File "/pypy/rpython/annotator/binaryop.py", line 93, in union
        raise UnionError(obj1, obj2)
   [translation:ERROR] UnionError:

   Offending annotations:
     SomeString(const='', no_nul=True)
     SomeInteger(const=1, knowntype=int, nonneg=True, unsigned=False)

   In <FunctionGraph of (error:1)compiler_error at 0x5b895c8>:
   <return block>
   Processing block:
   block@9[arg_0] is a <class 'rpython.flowspace.flowcontext.SpamBlock'>
   in (error:1)compiler_error
   containing the following operations:
         v0 = bool(arg_0)
   --end--
   [translation] start debugger...
   > /pypy/rpython/annotator/binaryop.py(93)union()
   -> raise UnionError(obj1, obj2)
   (Pdb+)

Basically, there are two common errors (i.e., compiler exceptions)
``AnnotatorError``, ``FlowingError``.


``AnnotatorError``
------------------

``AnnotatorError`` is a class of compiler errors happens in annotating a RPython
program. There are several specific errors in this class:

* ``UnionError`` (``annotator/module.py``): annotator complains on type conflicts
* ``TooLateForChange`` (``annotator/listdef.py``): not documented
* ``ListChangeUnallowed`` (``annotator/listdef.py``): not documented
* ``NoSuchAttrError`` (``annotator/classdesc.py``): attributes not found in a class
* ``SignatureError`` (``annotator/signature.py``): function declaration signature difference

In addition to above specific errors, there are many common annotator errors
which are not raised by above error classes.

For instance, this is a common annotator error:

.. literalinclude:: ../code/annotator_error.py

Here is the error message, which is very informative. In line 3, there is a
signature mismatch. Specifically, the function takes no argument but 1 argument
given in line 3.

.. code-block:: text

    [translation:ERROR] AnnotatorError:

    signature mismatch: func() takes no arguments (1 given)


    Occurred processing the following simple_call:
      function func <signature_error.py, line 1> returning

        v0 = simple_call((function func), (1))

    In <FunctionGraph of (signature_error:2)compiler_error at 0x658a528>:
    Happened at file signature_error.py line 3

    ==>     func(1)

    Known variable annotations:

    Processing block:
    block@6[arg_0] is a <class 'rpython.flowspace.flowcontext.SpamBlock'>
    in (signature_error:2)compiler_error
    containing the following operations:
          v0 = simple_call((function func), (1))
    --end--

``UnionError``
~~~~~~~~~~~~~~

``UnionError`` represents there is a type conflict when annotating types. In the
above example, the variable ``v`` can be an integer type and a string type
depends on the ``arg`` function parameter. Let us look at the error message again.

.. code-block:: text
   :emphasize-lines: 4,5,7

   [translation:ERROR] UnionError:

   Offending annotations:
     SomeString(const='', no_nul=True)
     SomeInteger(const=1, knowntype=int, nonneg=True, unsigned=False)

   In <FunctionGraph of (error:1)compiler_error at 0x5b895c8>:
   <return block>
   Processing block:
   block@9[arg_0] is a <class 'rpython.flowspace.flowcontext.SpamBlock'>
   in (error:1)compiler_error
   containing the following operations:
         v0 = bool(arg_0)

It tells you that there is a type conflict. The RPython annotator gives you the
offending annotations, the ``SomeString`` type and the ``SomeInteger``
type, which cannot be unified. And this conflict is in the ``compiler_error``
function.

``FlowingError``
----------------

``FlowingError`` is all about errors when RPython compiler building control flow
graphs. Here are some common causes for ``FlowingError``.

  * unsupported operations
  * invalid exception class
  * cannot import modules
  * local variable referenced before assignment
  * global name is not defined
  * etc.

The flowing gives a simple example to illustrate ``FlowingError``.

.. literalinclude:: ../code/flowing_error.py

In addition to report ``FlowingError``, the compiler will give you some detailed
explanation.

.. code-block:: text
   :emphasize-lines: 3

    [translation:ERROR] FlowingError:

    global name 'v' is not defined

    In <FunctionGraph of (flowing_error:1)compiler_error at 0x717bde0>:
    Happened at file flowing_error.py line 2

            return v

    Processing block:
    block@9[argv_0] is a <class 'rpython.flowspace.flowcontext.SpamBlock'>
    in (flowing_error:4)entry_point
    containing the following operations:
          v0 = getitem(argv_0, (1))
          v1 = simple_call((function compiler_error), v0)
    --end--

When RPython detected a control flow which always raise an exception, it will
report ``FlowingError``.

.. literalinclude:: ../code/flowing2_error.py

In the above example, ``1/0`` always raises a ``ZeroDivisionError`` exception.

.. code-block:: text
   :emphasize-lines: 3

    [translation:ERROR] FlowingError:

    div(1, 0) always raises <type 'exceptions.ZeroDivisionError'>: integer division by zero

    In <FunctionGraph of (flowing2_error:1)compiler_error at 0x66bd1d8>:
    Happened at file flowing2_error.py line 2

            n = 10 * (1/0)

    Processing block:
    block@9[argv_0] is a <class 'rpython.flowspace.flowcontext.SpamBlock'>
    in (flowing2_error:5)entry_point
    containing the following operations:
          v0 = getitem(argv_0, (1))
          v1 = simple_call((function compiler_error), v0)
    --end--
