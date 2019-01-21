JIT
===

Simple Example
--------------

The following example is a interpreter of `brainfuck
<https://en.wikipedia.org/wiki/Brainfuck>`_ language with JIT.
There is a detailed tutorial (`part1
<https://morepypy.blogspot.com/2011/04/tutorial-writing-interpreter-with-pypy.html>`_,
`part2 <https://morepypy.blogspot.com/2011/04/tutorial-part-2-adding-jit.html>`_) on
how to write a simple interpreter with RPython.
Here, we briefly introduce some JIT-related data structures, functions, and decorators.

.. literalinclude:: ../code/bf.py
   :linenos:

JitDriver
-------------

JIT Decorators and Functions
----------------------------

* elidable
* hint
* promote
* promote_string
* dont_look_inside
* look_inside
* look_inside_iff
* unroll_safe
* loop_invariant
* elidable_promote
* oopspec
* not_in_trace
* isconstant
* isvirtual
* loop_unroll_heuristic
* we_are_jitted

JIT Parameters
--------------

* ``threshold``: number of times a loop has to run for it to become hot
* ``function_threshold``: number of times a function must run for it to become traced from start
* ``trace_eagerness``: number of times a guard has to fail before we start compiling a bridge
* ``decay``: amount to regularly decay counters by (0=none, 1000=max)
* ``trace_limit``: number of recorded operations before we abort tracing with ABORT_TOO_LONG
* ``inlining``: inline python functions or not (1/0)
* ``loop_longevity``: a parameter controlling how long loops will be kept before being freed, an estimate
* ``retrace_limit``: how many times we can try retracing before giving up
* ``max_retrace_guards``: number of extra guards a retrace can cause
* ``max_unroll_loops``: number of extra unrollings a loop can cause
* ``disable_unrolling``: after how many operations we should not unroll
* ``enable_opts``: internal use only (may not work or lead to crashes): optimizations
  to enable, or all = intbounds:rewrite:virtualize:string:pure:earlyforce:heap:unroll
* ``max_unroll_recursion``: how many levels deep to unroll a recursive function
* ``vec``: turn on the vectorization optimization (vecopt). Supports x86 (SSE 4.1), powerpc (SVX), s390x SIMD
* ``vec_cost``: threshold for which traces to bail. Unpacking increases the counter, vector operation decrease the cost,
* ``vec_all``: try to vectorize trace loops that occur outside of the numpypy library

The default parameters are:

.. code-block:: python

   PARAMETERS = {'threshold': 1039, # just above 1024, prime
                 'function_threshold': 1619, # slightly more than one above, also prime
                 'trace_eagerness': 200,
                 'decay': 40,
                 'trace_limit': 6000,
                 'inlining': 1,
                 'loop_longevity': 1000,
                 'retrace_limit': 0,
                 'max_retrace_guards': 15,
                 'max_unroll_loops': 0,
                 'disable_unrolling': 200,
                 'enable_opts': 'all',
                 'max_unroll_recursion': 7,
                 'vec': 0,
                 'vec_all': 0,
                 'vec_cost': 0,
                 }
