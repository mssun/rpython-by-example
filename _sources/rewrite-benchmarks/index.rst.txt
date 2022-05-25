Rewriting Python Benchmarks
===========================

To understand the performance of RPython, we are trying to rewrite some `Python
benchmarks <https://bitbucket.org/pypy/benchmarks>`_ with RPython. In this
section, we use several examples (fibonacci number and binary tree) to
illustrate tips to rewrite Python code with RPython. As you will see, rewriting
Python with RPython doesn't require much effort, and we will gain a lot of
performance improvements.

Fibonacci Number
----------------

The following code is to calculate fibonacci number recursively.

.. literalinclude:: /code/benchmarks/fib.py

To run this benchmark, we should add a target function to tell RPython the entry
point. Also, we change to get ``n`` from arguments instead of hard-coding a
constant to avoid optimization. The following code can be compiled by RPython.

.. literalinclude:: /code/benchmarks/fib_rpy.py
   :linenos:
   :emphasize-lines: 6-11,13-14,16-18

.. note::
   There are some passes to `simplify flow graph
   <https://bitbucket.org/pypy/pypy/src/default/rpython/translator/simplify.py>`_
   for optimization. These passes include
   ``transform_dead_op_vars``, ``eliminate_empty_blocks``, ``remove_assertion_errors``,
   ``remove_identical_vars_SSA``, ``constfold_exitswitch``, ``remove_trivial_links``,
   ``SSA_to_SSI``, ``coalesce_bool``, ``transform_ovfcheck``, ``simplify_exceptions``,
   ``transform_xxxitem``, and ``remove_dead_exceptions``.

Here, we simply use the GNU ``time`` command to measure the execution time and
maximum resident set size during the process's lifetime.

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

Rewriting the binary tree benchmark needs a little more efforts. In the Python
version, it uses a tuple of tuples to represent nodes the the tree. Since
RPython doesn't allow variable length tuples and mixed types tuples, we write a
new ``Node`` class to represent nodes in binary trees. In addition, we
rewrite the ``sum`` built-in function. The following code only shows ``diff`` of
original Python code and modified RPython version.

.. literalinclude:: ../code/benchmarks/binary-tree_rpy.py
   :diff: ../code/benchmarks/binary-tree.py

Let us measure execution times of the binary tree benchmark with Python and
PyPy, and RPython rewrite as well.

.. code-block:: text

   $ /usr/bin/time -f "%C\t%U\t%M" python binary-tree.py > /dev/null
   python binary-tree.py   10.45   60432

   $ /usr/bin/time -f "%C\t%U\t%M" pypy binary-tree.py > /dev/null
   pypy binary-tree.py     1.60    187256

   $ /usr/bin/time -f "%C\t%U\t%M" ./binary-tree_rpy-c 17 > /dev/null
   ./binary-tree_rpy-c 17  0.38    68312

Spectral Norm
-------------

For the spectral norm benchmark, we made the following changes:

* rewrite map function
* rewrite generators
* use list instead of tuple
* use loop to rewrite izip function

.. literalinclude:: ../code/benchmarks/spectral-norm_rpy.py
   :diff: ../code/benchmarks/spectral-norm.py

.. code-block:: text

   $ /usr/bin/time -f "%C\t%U\t%M" python spectral-norm.py > /dev/null
   python spectral-norm.py 34.83   6140

   $ /usr/bin/time -f "%C\t%U\t%M" pypy spectral-norm.py > /dev/null
   pypy spectral-norm.py   1.20    81016

   $ /usr/bin/time -f "%C\t%U\t%M" ./spectral-norm_rpy-c 17 > /dev/null
   ./spectral-norm_rpy-c 400       0.26    7892

Benchmark Results
-----------------

In addition to "fibonacci number" and "binary tree", we also rewrite some other
benchmarks (`source code
<https://github.com/mesalock-linux/rpython-by-example/tree/master/code/benchmarks>`_).
The following table summarize the benchmark results.

+-----------------+-----------------+----------+-------------+----------+----------+----------+----------+
|                 |  Python 2.7.15  | PyPy2 v6.0.0           |   RPython (PyPy2 v6.0.0)                  |
+=================+=================+==========+=============+==========+=====================+==========+
|                 |Time (s)         |Time (s)  |Speedup      |Time (s)  |Speedup              |          |
|                 |                 |          |             |          |                     |Size (KB) |
+-----------------+-----------------+----------+-------------+----------+---------------------+----------+
|fib.py           |18.21            |4.77      |3.82         |0.40      |45.53                |282       |
+-----------------+-----------------+----------+-------------+----------+---------------------+----------+
|binary-tree.py   |10.45            |1.60      |6.53         |0.38      |27.50                |301       |
+-----------------+-----------------+----------+-------------+----------+---------------------+----------+
|float.py         |11.47            |1.51      |7.60         |0.57      |20.12                |277       |
+-----------------+-----------------+----------+-------------+----------+---------------------+----------+
|fannkuch.py      |3.91             |0.54      |7.24         |0.32      |12.22                |282       |
+-----------------+-----------------+----------+-------------+----------+---------------------+----------+
|buffer.py        |1.23             |0.64      |1.92         |0.52      |2.37                 |284       |
+-----------------+-----------------+----------+-------------+----------+---------------------+----------+
|spectral-norm.py |34.83            |1.20      |29.03        |0.26      |133.96               |307       |
+-----------------+-----------------+----------+-------------+----------+---------------------+----------+

As you can see, the average speedup of RPython compared to Python 2.7.15 is
about 21. Moreover, compared to the very large Python interpreter, the size of
RPython binary is pretty small.
