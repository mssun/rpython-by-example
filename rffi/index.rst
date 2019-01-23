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

String Operations
-----------------

There are several functions to handle string conversion including ASCII and
unicode encodings:

.. code-block:: text

   * str2charp, free_charp, charp2str,
     get_nonmovingbuffer, free_nonmovingbuffer, get_nonmovingbuffer_final_null,
     alloc_buffer, str_from_buffer, keep_buffer_alive_until_here,
     charp2strn, charpsize2str, str2chararray, str2rawmem,

   * unicode2wcharp, free_wcharp, wcharp2unicode,
     get_nonmoving_unicodebuffer, free_nonmoving_unicodebuffer,
     alloc_unicodebuffer, unicode_from_buffer, keep_unicodebuffer_alive_until_here,
     wcharp2unicoden, wcharpsize2unicode, unicode2wchararray, unicode2rawmem,

Here are two examples illustrate the usage of ``str2charp`` and ``charp2str``.

.. literalinclude:: ../code/rffi_str.py

List Conversion
---------------

List of strings is commonly used in some cases, there are two pair of functions:
``liststr2charpp`` and ``charpp2liststr``. Remember to free the list using
``free_charpp``.

.. code-block:: text

   * liststr2charpp: list[str] -> char**, NULL terminated
   * free_charpp: frees list of char**, NULL terminated
   * charpp2liststr: char** NULL terminated -> list[str].  No freeing is done.

Here is an example of calculating the total length of a list of strings.

.. literalinclude:: ../code/rffi_liststr.py

Other Functions
---------------

There are other useful functions like scoped str conversion and buffer allocation.

.. todo:: Need more detailed examples and explanation.

.. code-block:: text

   * size_and_sign, sizeof, offsetof
   * structcopy
   * setintfiled, getintfield
   * scoped_str2charp, scoped_unicode2wcharp, scoped_nonmovingbuffer,
     scoped_view_charp, schoped_nonmoving_unicodebuffer, scoped_alloc_buffer,
     scoped_alloc_unicodebuffer
   * c_memcpy, c_memset
   * get_raw_address_of_string

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

FFI Types
---------

Since there is no formal definitions of FFI types in docs and source code (some
definitions are dynamically generated), here is a dump of all definitions in
RPython FFI types. It is quit easy to understand the types based on the names.

.. todo:: Need more detailed examples and explanation.

.. code-block:: text

   # type definitions
   AroundFnPtr
   CCHARP
   CCHARPP
   CHAR
   CONST_CCHARP
   CWCHARP
   CWCHARPP
   DOUBLE
   DOUBLEP
   FLOAT
   FLOATP
   INT
   INTMAX_T
   INTMAX_TP
   INTP
   INTPTR_T
   INTPTR_TP
   INT_FAST16_T
   INT_FAST16_TP
   INT_FAST32_T
   INT_FAST32_TP
   INT_FAST64_T
   INT_FAST64_TP
   INT_FAST8_T
   INT_FAST8_TP
   INT_LEAST16_T
   INT_LEAST16_TP
   INT_LEAST32_T
   INT_LEAST32_TP
   INT_LEAST64_T
   INT_LEAST64_TP
   INT_LEAST8_T
   INT_LEAST8_TP
   INT_real
   LONG
   LONGDOUBLE
   LONGDOUBLEP
   LONGLONG
   LONGLONGP
   LONGP
   LONG_BIT
   MODE_T
   MODE_TP
   NULL
   PID_T
   PID_TP
   PTRDIFF_T
   PTRDIFF_TP
   SHORT
   SHORTP
   SIGNED
   SIGNEDCHAR
   SIGNEDCHARP
   SIGNEDP
   SIGNEDPP
   SIZE_T
   SIZE_TP
   SSIZE_T
   SSIZE_TP
   TIME_T
   TIME_TP
   UCHAR
   UCHARP
   UINT
   UINTMAX_T
   UINTMAX_TP
   UINTP
   UINTPTR_T
   UINTPTR_TP
   UINT_FAST16_T
   UINT_FAST16_TP
   UINT_FAST32_T
   UINT_FAST32_TP
   UINT_FAST64_T
   UINT_FAST64_TP
   UINT_FAST8_T
   UINT_FAST8_TP
   UINT_LEAST16_T
   UINT_LEAST16_TP
   UINT_LEAST32_T
   UINT_LEAST32_TP
   UINT_LEAST64_T
   UINT_LEAST64_TP
   UINT_LEAST8_T
   UINT_LEAST8_TP
   ULONG
   ULONGLONG
   ULONGLONGP
   ULONGP
   USHORT
   USHORTP
   VOID*
   VOID*P
   VOIDP
   VOIDPP
   WCHAR_T
   WCHAR_TP
   __INT128_T
   __INT128_TP

   # functions/classes to create a type
   CArray
   CArrayPtr
   CCallback
   CConstant
   CExternVariable
   CFixedArray
   COpaque
   COpaquePtr
   CStruct
   CStructPtr
