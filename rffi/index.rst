Foreign Function Interface (rffi)
=================================

The foreign function interface of RPython is called rffi. With rffi, you can
declaring low-level external C function, registering function as external,
defining C types, etc.

Call Functions in libc
----------------------

The following example shows how to use rffi to call math function in libc.

.. literalinclude:: ../code/rffi_abs.py

Separate Module Source
----------------------

You can also write C function directly. The C build tool of RPython translator
will automatically compile and link with the C functions.

.. literalinclude:: ../code/rffi_separate_module_sources.py

More Examples
-------------

Here are three more examples on handling string and callback functions.

.. literalinclude:: ../code/rffi_more.py

.. note::
   More examples of handling built-in types, string, unicode, opaque type,
   struct, pre-built constant, callback, and buffer can be found in
   `rffi's tests <https://bitbucket.org/pypy/pypy/src/default/rpython/rtyper/lltypesystem/test/test_rffi.py>`_.

Usage of ExternalCompilationInfo
--------------------------------

As you can see ``rpython.translator.tool.cbuild.ExternalCompilationInfo`` is a
pretty useful utility to interacting with external function through C ffi.
Let us read the detailed explanation on the attributes of
``ExternalCompilationInfo`` in the source code
(``rpython/translator/tool/cbuild.py``).

* ``pre_include_bits``: list of pieces of text that should be put at the top of the
  generated .c files, before any #include. They shouldn't contain an #include
  themselves. (Duplicate pieces are removed.)
* ``includes``: list of .h file names to be #include'd from the generated .c files.
* ``include_dirs``: list of dir names that is passed to the C compiler
* ``post_include_bits``: list of pieces of text that should be put at the top of the
  generated .c files, after the #includes. (Duplicate pieces are removed.)
* ``libraries``: list of library names that is passed to the linker
* ``library_dirs``: list of dir names that is passed to the linker
* ``separate_module_sources``: list of multiline strings that are each written to a
  .c file and compiled separately and linked later on. (If function prototypes
  are needed for other .c files to access this, they can be put in
  post_include_bits.)
* ``separate_module_files``: list of .c file names that are compiled separately and
  linked later on. (If an .h file is needed for other .c files to access this,
  it can be put in includes.)
* ``compile_extra``: list of parameters which will be directly passed to the
  compiler
* ``link_extra``: list of parameters which will be directly passed to the linker
* ``frameworks``: list of Mac OS X frameworks which should passed to the linker. Use
  this instead of the 'libraries' parameter if you want to link to a framework
  bundle. Not suitable for unix-like .dylib installations.
* ``link_files``: list of file names which will be directly passed to the linker
* ``testonly_libraries``: list of libraries that are searched for during testing
  only, by ll2ctypes. Useful to search for a name in a dynamic library during
  testing but use the static library for compilation.
* ``use_cpp_linker``: a flag to tell if g++ should be used instead of gcc when
  linking (a bit custom so far)
* ``platform``: an object that can identify the platform
