RPython By Example
==================

RPython by Example (RPyBE) is a collection of runnable examples that illustrate
various RPython concepts and libraries.

Please use following commands to install dependencies, build RPyBE in HTML/PDF, and run example code.

.. code-block:: shell

   $ pip install sphinx sphinx_rtd_theme    # install Sphinx
   $ make html                              # generate webpages in _build/html

   $ sudo apt-get install texlive-full      # install TeX Live for generating PDF
   $ make latexpdf                          # generate a PDF in _build/latex

   $ cd code                                # change to the directory of code examples
   $ export RPY=$(PATH_TO_PYPY)/rpython/bin/rpython
                                            # setup the RPython compiler path
   $ make                                   # compile all RPython code
   $ make hello_world                       # compile a specific example
   $ ./hello_world-c                        # run the example
