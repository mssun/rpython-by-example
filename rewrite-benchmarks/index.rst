Rewriting Python Benchmarks
===========================

We are trying to rewrite some Python benchmarks with RPython. As you will see,
rewriting Python with RPython doesn't require much effort, and we will gain a
lot of performance improvements.

Fibonacci Number
----------------

.. literalinclude:: /code/benchmarks/fib.py

.. literalinclude:: /code/benchmarks/fib_rpy.py
   :linenos:
   :emphasize-lines: 6-11,13-14,16-18

There are some passes to `simplify flow graph
<https://bitbucket.org/pypy/pypy/src/default/rpython/translator/simplify.py>`_
for optimization. These passes include
``transform_dead_op_vars``, ``eliminate_empty_blocks``, ``remove_assertion_errors``,
``remove_identical_vars_SSA``, ``constfold_exitswitch``, ``remove_trivial_links``,
``SSA_to_SSI``, ``coalesce_bool``, ``transform_ovfcheck``, ``simplify_exceptions``,
``transform_xxxitem``, and ``remove_dead_exceptions``.

.. code-block:: text

   $ /usr/bin/time -f "%C\t%U\t%M" python fib.py > /dev/null
   python fib.py   18.21   5956

   $ /usr/bin/time -f "%C\t%U\t%M" pypy fib.py > /dev/null
   pypy fib.py     4.77    112960

   $ rpython fib_rpy.py

   $ /usr/bin/time -f "%C\t%U\t%M" ./fib-c 40 > /dev/null
   ./fib_rpy-c 40  0.40    1704

Binary Tree
-----------

.. literalinclude:: ../code/benchmarks/binary-tree_rpy.py
   :diff: ../code/benchmarks/binary-tree.py

.. code-block:: text

   $ /usr/bin/time -f "%C\t%U\t%M" python binary-tree.py > /dev/null
   python binary-tree.py   10.45   60432

   $ /usr/bin/time -f "%C\t%U\t%M" pypy binary-tree.py > /dev/null
   pypy binary-tree.py     1.60    187256

   $ /usr/bin/time -f "%C\t%U\t%M" ./binary-tree_rpy-c 17 > /dev/null
   ./binary-tree_rpy-c 17  0.38    68312

Benchmark Results
-----------------

References:
  * `The Computer Language Benchmarks Game <https://benchmarksgame-team.pages.debian.net/benchmarksgame/>`_
