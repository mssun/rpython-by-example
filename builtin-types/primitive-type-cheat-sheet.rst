Primitive Type Cheat Sheet
==========================

The following table summarizes RPython's primitive types and corresponding
low-level types, FFI types, and C types.

+-------------------------+----------------------+--------------+----------------------+
|RPython Type (Primitive) |LL Type               |FFI Type      |C Type (64-bit Linux) |
+=========================+======================+==============+======================+
|``int``                  |``Signed``            |``SIGNED``    |``long``              |
+-------------------------+----------------------+--------------+----------------------+
|``long``                 |``Signed``            |``LONG``      |``long``              |
+-------------------------+----------------------+--------------+----------------------+
|``r_uint``               |``Unsigned``          |``UINT``      |``unsigned long``     |
+-------------------------+----------------------+--------------+----------------------+
|``r_ulonglong``          |``UnsignedLongLong``  |``ULONGLONG`` |``unsigned long``     |
+-------------------------+----------------------+--------------+----------------------+
|``r_longlong``           |``SignedLongLong``    |``LONGLONG``  |``long long``         |
+-------------------------+----------------------+--------------+----------------------+
|``r_longlonglong``       |``SignedLongLongLong``|``__INT128_T``|``__int128_t``        |
+-------------------------+----------------------+--------------+----------------------+
|``r_singlefloat``        |``SingleFloat``       |``FLOAT``     |``float``             |
+-------------------------+----------------------+--------------+----------------------+
|``float``                |``Float``             |``DOUBLE``    |``double``            |
+-------------------------+----------------------+--------------+----------------------+
|``r_longfloat``          |``LongFloat``         |``LONGDOUBLE``|``long double``       |
+-------------------------+----------------------+--------------+----------------------+
|``char``                 |``Char``              |``CHAR``      |``char``              |
+-------------------------+----------------------+--------------+----------------------+
|``bool``                 |``Bool``              | N/A          |``boot_t``            |
+-------------------------+----------------------+--------------+----------------------+
|``NoneType``             |``Void``              |``VOID``      |``void``              |
+-------------------------+----------------------+--------------+----------------------+
|``unicode``              |``UniChar``           |``WCHAR_T``   |``wchar_t``           |
+-------------------------+----------------------+--------------+----------------------+

* RPython types start with ``r_`` can be imported from the ``rpython.rlib.rarithmetic`` module.
* Low-level types can be imported from the ``rpython.rtyper.lltypesystem.lltype`` module.
* FFI types can be imported from the ``rpython.rtyper.lltypesystem.rffi`` module.

The definitions of these types can be found in the following source code.

* Arithmetic type (``r_*``): `rpython/rlib/rarithmetic.py <https://bitbucket.org/pypy/pypy/src/default/rpython/rlib/rarithmetic.py>`_
* LL type: `rpython/rtyper/lltypesystem/lltype.py <https://bitbucket.org/pypy/pypy/src/default/rpython/rtyper/lltypesystem/lltype.py>`_
* FFI type: `rpython/rtyper/lltypesystem/rffi.py <https://bitbucket.org/pypy/pypy/src/default/rpython/rtyper/lltypesystem/lltype.py>`_
* C type: `rpython/translator/c/primitive.py <https://bitbucket.org/pypy/pypy/src/default/rpython/translator/c/primitive.py>`_

In addition to these primitive types, there are other types like pointer types for FFI.

.. dump some data structures of lltype, ffi, c types
.. {'AroundFnPtr': <* Func (  ) -> Void>,
 'CConstant': <class 'rpython.rtyper.lltypesystem.rffi.CConstant'>,
 'CallbackHolder': <class rpython.rtyper.lltypesystem.rffi.CallbackHolder at 0x0000000004080750>,
 'CompilationError': <class 'rpython.translator.platform.CompilationError'>,
 'ExtRegistryEntry': <class 'rpython.rtyper.extregistry.ExtRegistryEntry'>,
 'ExternalCompilationInfo': <class 'rpython.translator.tool.cbuild.ExternalCompilationInfo'>,
 'INT': <INT>,
 'INTMAX_T': <Signed>,
 'INTMAX_TP': <* Array of Signed >,
 'INTP': <* Array of INT >,
 'INTPTR_T': <Signed>,
 'INTPTR_TP': <* Array of Signed >,
 'INT_FAST16_T': <Signed>,
 'INT_FAST16_TP': <* Array of Signed >,
 'INT_FAST32_T': <Signed>,
 'INT_FAST32_TP': <* Array of Signed >,
 'INT_FAST64_T': <Signed>,
 'INT_FAST64_TP': <* Array of Signed >,
 'INT_FAST8_T': <SIGNEDCHAR>,
 'INT_FAST8_TP': <* Array of SIGNEDCHAR >,
 'INT_LEAST16_T': <SHORT>,
 'INT_LEAST16_TP': <* Array of SHORT >,
 'INT_LEAST32_T': <INT>,
 'INT_LEAST32_TP': <* Array of INT >,
 'INT_LEAST64_T': <Signed>,
 'INT_LEAST64_TP': <* Array of Signed >,
 'INT_LEAST8_T': <SIGNEDCHAR>,
 'INT_LEAST8_TP': <* Array of SIGNEDCHAR >,
 'INT_real': <INT>,
 'LONG': <Signed>,
 'LONGLONG': <Signed>,
 'LONGLONGP': <* Array of Signed >,
 'LONGP': <* Array of Signed >,
 'LONG_BIT': 64,
 'MODE_T': <INT>,
 'MODE_TP': <* Array of INT >,
 'NUMBER_TYPES': [<SHORT>,
                  <USHORT>,
                  <INT>,
                  <UINT>,
                  <Signed>,
                  <Unsigned>,
                  <SIGNEDCHAR>,
                  <UCHAR>,
                  <Signed>,
                  <Unsigned>,
                  <Unsigned>,
                  <Signed>,
                  <INT>,
                  <Unsigned>,
                  <Signed>,
                  <Signed>,
                  <SignedLongLongLong>,
                  <INT>,
                  <INT>,
                  <Signed>,
                  <Signed>,
                  <SIGNEDCHAR>,
                  <UCHAR>,
                  <SHORT>,
                  <USHORT>,
                  <INT>,
                  <UINT>,
                  <Signed>,
                  <Unsigned>,
                  <SIGNEDCHAR>,
                  <UCHAR>,
                  <Signed>,
                  <Unsigned>,
                  <Signed>,
                  <Unsigned>,
                  <Signed>,
                  <Unsigned>,
                  <Signed>,
                  <Unsigned>,
                  <INT>],
 'PID_T': <INT>,
 'PID_TP': <* Array of INT >,
 'PTRDIFF_T': <Signed>,
 'PTRDIFF_TP': <* Array of Signed >,
 'RFFI_ALT_ERRNO': 64,
 'RFFI_ERR_ALL': 27,
 'RFFI_ERR_NONE': 0,
 'RFFI_FULL_ERRNO': 3,
 'RFFI_FULL_ERRNO_ZERO': 5,
 'RFFI_FULL_LASTERROR': 24,
 'RFFI_READSAVED_ERRNO': 2,
 'RFFI_READSAVED_LASTERROR': 16,
 'RFFI_SAVE_ERRNO': 1,
 'RFFI_SAVE_LASTERROR': 8,
 'RFFI_SAVE_WSALASTERROR': 32,
 'RFFI_ZERO_ERRNO_BEFORE': 4,
 'SHORT': <SHORT>,
 'SHORTP': <* Array of SHORT >,
 'SIGNEDCHAR': <SIGNEDCHAR>,
 'SIGNEDCHARP': <* Array of SIGNEDCHAR >,
 'SIZE_T': <Unsigned>,
 'SIZE_TP': <* Array of Unsigned >,
 'SSIZE_T': <Signed>,
 'SSIZE_TP': <* Array of Signed >,
 'SomePtr': <class 'rpython.rtyper.lltypesystem.lltype.SomePtr'>,
 'StackCounter': <class rpython.rtyper.lltypesystem.rffi.StackCounter at 0x0000000004080778>,
 'StringBuilder': <class 'rpython.rlib.rstring.StringBuilder'>,
 'Symbolic': <class 'rpython.rlib.objectmodel.Symbolic'>,
 'TIME_T': <Signed>,
 'TIME_TP': <* Array of Signed >,
 'TYPES': ['short',
           'unsigned short',
           'int',
           'unsigned int',
           'long',
           'unsigned long',
           'signed char',
           'unsigned char',
           'long long',
           'unsigned long long',
           'size_t',
           'time_t',
           'wchar_t',
           'uintptr_t',
           'intptr_t',
           'void*',
           '__int128_t',
           'mode_t',
           'pid_t',
           'ssize_t',
           'ptrdiff_t',
           'int_least8_t',
           'uint_least8_t',
           'int_least16_t',
           'uint_least16_t',
           'int_least32_t',
           'uint_least32_t',
           'int_least64_t',
           'uint_least64_t',
           'int_fast8_t',
           'uint_fast8_t',
           'int_fast16_t',
           'uint_fast16_t',
           'int_fast32_t',
           'uint_fast32_t',
           'int_fast64_t',
           'uint_fast64_t',
           'intmax_t',
           'uintmax_t'],
 'UCHAR': <UCHAR>,
 'UCHARP': <* Array of UCHAR >,
 'UINT': <UINT>,
 'UINTMAX_T': <Unsigned>,
 'UINTMAX_TP': <* Array of Unsigned >,
 'UINTP': <* Array of UINT >,
 'UINTPTR_T': <Unsigned>,
 'UINTPTR_TP': <* Array of Unsigned >,
 'UINT_FAST16_T': <Unsigned>,
 'UINT_FAST16_TP': <* Array of Unsigned >,
 'UINT_FAST32_T': <Unsigned>,
 'UINT_FAST32_TP': <* Array of Unsigned >,
 'UINT_FAST64_T': <Unsigned>,
 'UINT_FAST64_TP': <* Array of Unsigned >,
 'UINT_FAST8_T': <UCHAR>,
 'UINT_FAST8_TP': <* Array of UCHAR >,
 'UINT_LEAST16_T': <USHORT>,
 'UINT_LEAST16_TP': <* Array of USHORT >,
 'UINT_LEAST32_T': <UINT>,
 'UINT_LEAST32_TP': <* Array of UINT >,
 'UINT_LEAST64_T': <Unsigned>,
 'UINT_LEAST64_TP': <* Array of Unsigned >,
 'UINT_LEAST8_T': <UCHAR>,
 'UINT_LEAST8_TP': <* Array of UCHAR >,
 'ULONG': <Unsigned>,
 'ULONGLONG': <Unsigned>,
 'ULONGLONGP': <* Array of Unsigned >,
 'ULONGP': <* Array of Unsigned >,
 'USHORT': <USHORT>,
 'USHORTP': <* Array of USHORT >,
 'UnicodeBuilder': <class 'rpython.rlib.rstring.UnicodeBuilder'>,
 'VOID*': <Signed>,
 'VOID*P': <* Array of Signed >,
 'WCHAR_T': <INT>,
 'WCHAR_TP': <* Array of INT >,
 '_IsLLPtrEntry': <class 'rpython.rtyper.lltypesystem.rffi._IsLLPtrEntry'>,
 '_KEEPER_CACHE': {},
 '__INT128_T': <SignedLongLongLong>,
 '__INT128_TP': <* Array of SignedLongLongLong >,
 '__builtins__': <module '__builtin__' (built-in)>,
 '__cached__': '/home/mssun/rpython/pypy/rpython/rtyper/lltypesystem/__pycache__/rffi.pypy-41.pyc',
 '__doc__': None,
 '__file__': '/home/mssun/rpython/pypy/rpython/rtyper/lltypesystem/rffi.py',
 '__name__': 'rpython.rtyper.lltypesystem.rffi',
 '__package__': 'rpython.rtyper.lltypesystem',
 '_isfunctype': <function _isfunctype at 0x0000000004064458>,
 '_isllptr': <function _isllptr at 0x0000000004064098>,
 '_keeper_for_type': <function _keeper_for_type at 0x00000000040646b0>,
 '_make_wrapper_for': <function _make_wrapper_for at 0x0000000004064548>,
 '_name': 'long',
 'annmodel': <module 'rpython.annotator.model' from '/home/mssun/rpython/pypy/rpython/annotator/model.py'>,
 'assert_str0': <function assert_str0 at 0x000000000479bf88>,
 'cast_ptr_to_adr': <function cast_ptr_to_adr at 0x000000000387b178>,
 'enforceargs': <function enforceargs at 0x0000000003690200>,
 'func_with_new_name': <function func_with_new_name at 0x0000000003690188>,
 'generate_macro_wrapper': <function generate_macro_wrapper at 0x0000000004064638>,
 'get_keepalive_object': <function get_keepalive_object at 0x00000000040647a0>,
 'itemoffsetof': <function itemoffsetof at 0x0000000003765790>,
 'jit': <module 'rpython.rlib.jit' from '/home/mssun/rpython/pypy/rpython/rlib/jit.py'>,
 'keepalive_until_here': <function keepalive_until_here at 0x0000000003690548>,
 'll2ctypes': <module 'rpython.rtyper.lltypesystem.ll2ctypes' from '/home/mssun/rpython/pypy/rpython/rtyper/lltypesystem/ll2ctypes.py'>,
 'llexternal': <function llexternal at 0x00000000040644d0>,
 'llexternal_use_eci': <function llexternal_use_eci at 0x00000000040645c0>,
 'llhelper': <function llhelper at 0x0000000003abbb50>,
 'llmemory': <module 'rpython.rtyper.lltypesystem.llmemory' from '/home/mssun/rpython/pypy/rpython/rtyper/lltypesystem/llmemory.py'>,
 'lltype': <module 'rpython.rtyper.lltypesystem.lltype' from '/home/mssun/rpython/pypy/rpython/rtyper/lltypesystem/lltype.py'>,
 'lltype_to_annotation': <function lltype_to_annotation at 0x0000000003950c50>,
 'maxint': 9223372036854775807,
 'name': 'unsigned long',
 'os': <module 'os' from '/usr/lib/pypy/lib-python/2.7/os.py'>,
 'platform': <rpython.rtyper.tool.rfficache.Platform instance at 0x00000000047948e0>,
 'populate_inttypes': <function populate_inttypes at 0x0000000004064110>,
 'pprint': <module 'pprint' from '/usr/lib/pypy/lib-python/2.7/pprint.py'>,
 'py': <ApiModule 'py' version='1.4.29' from '/home/mssun/rpython/pypy/py/__init__.py'>,
 'r___int128_t': <class 'rpython.rlib.rarithmetic.r_longlonglong'>,
 'r_int': <class 'rpython.rlib.rarithmetic.r_int32'>,
 'r_int_fast16_t': <class 'rpython.rlib.rarithmetic.r_int'>,
 'r_int_fast32_t': <class 'rpython.rlib.rarithmetic.r_int'>,
 'r_int_fast64_t': <class 'rpython.rlib.rarithmetic.r_int'>,
 'r_int_fast8_t': <class 'rpython.rlib.rarithmetic.r_SIGNEDCHAR'>,
 'r_int_least16_t': <class 'rpython.rlib.rarithmetic.r_SHORT'>,
 'r_int_least32_t': <class 'rpython.rlib.rarithmetic.r_int32'>,
 'r_int_least64_t': <class 'rpython.rlib.rarithmetic.r_int'>,
 'r_int_least8_t': <class 'rpython.rlib.rarithmetic.r_SIGNEDCHAR'>,
 'r_int_real': <class 'rpython.rlib.rarithmetic.r_int_real'>,
 'r_intmax_t': <class 'rpython.rlib.rarithmetic.r_int'>,
 'r_intptr_t': <class 'rpython.rlib.rarithmetic.r_int'>,
 'r_long': <class 'rpython.rlib.rarithmetic.r_int'>,
 'r_longlong': <class 'rpython.rlib.rarithmetic.r_int'>,
 'r_mode_t': <class 'rpython.rlib.rarithmetic.r_int32'>,
 'r_pid_t': <class 'rpython.rlib.rarithmetic.r_int32'>,
 'r_ptrdiff_t': <class 'rpython.rlib.rarithmetic.r_int'>,
 'r_short': <class 'rpython.rlib.rarithmetic.r_SHORT'>,
 'r_signedchar': <class 'rpython.rlib.rarithmetic.r_SIGNEDCHAR'>,
 'r_size_t': <class 'rpython.rlib.rarithmetic.r_uint'>,
 'r_ssize_t': <class 'rpython.rlib.rarithmetic.r_int'>,
 'r_time_t': <class 'rpython.rlib.rarithmetic.r_int'>,
 'r_uchar': <class 'rpython.rlib.rarithmetic.r_UCHAR'>,
 'r_uint': <class 'rpython.rlib.rarithmetic.r_uint32'>,
 'r_uint_fast16_t': <class 'rpython.rlib.rarithmetic.r_uint'>,
 'r_uint_fast32_t': <class 'rpython.rlib.rarithmetic.r_uint'>,
 'r_uint_fast64_t': <class 'rpython.rlib.rarithmetic.r_uint'>,
 'r_uint_fast8_t': <class 'rpython.rlib.rarithmetic.r_UCHAR'>,
 'r_uint_least16_t': <class 'rpython.rlib.rarithmetic.r_USHORT'>,
 'r_uint_least32_t': <class 'rpython.rlib.rarithmetic.r_uint32'>,
 'r_uint_least64_t': <class 'rpython.rlib.rarithmetic.r_uint'>,
 'r_uint_least8_t': <class 'rpython.rlib.rarithmetic.r_UCHAR'>,
 'r_uintmax_t': <class 'rpython.rlib.rarithmetic.r_uint'>,
 'r_uintptr_t': <class 'rpython.rlib.rarithmetic.r_uint'>,
 'r_ulong': <class 'rpython.rlib.rarithmetic.r_uint'>,
 'r_ulonglong': <class 'rpython.rlib.rarithmetic.r_uint'>,
 'r_ushort': <class 'rpython.rlib.rarithmetic.r_USHORT'>,
 'r_void*': <class 'rpython.rlib.rarithmetic.r_int'>,
 'r_wchar_t': <class 'rpython.rlib.rarithmetic.r_int32'>,
 'rarithmetic': <module 'rpython.rlib.rarithmetic' from '/home/mssun/rpython/pypy/rpython/rlib/rarithmetic.py'>,
 'register_keepalive': <function register_keepalive at 0x0000000004064728>,
 'rgc': <module 'rpython.rlib.rgc' from '/home/mssun/rpython/pypy/rpython/rlib/rgc.py'>,
 'setup': <function setup at 0x0000000004064890>,
 'sizeof_c_type': <function sizeof_c_type at 0x0000000003c0bf10>,
 'specialize': <rpython.rlib.objectmodel._Specialize object at 0x0000000003671088>,
 'stackcounter': <rpython.rtyper.lltypesystem.rffi.StackCounter instance at 0x000000000407c7c0>,
 'sys': <module 'sys' (built-in)>,
 'unregister_keepalive': <function unregister_keepalive at 0x0000000004064818>,
 'unrolling_iterable': <class 'rpython.rlib.unroll.unrolling_iterable'>,
 'we_are_translated': <function we_are_translated at 0x00000000035a89f8>,
 'we_are_translated_to_c': <function we_are_translated_to_c at 0x00000000036903e0>}

.. ['AroundFnPtr',
 'CArray',
 'CArrayPtr',
 'CCHARP',
 'CCHARPP',
 'CCallback',
 'CConstant',
 'CExternVariable',
 'CFixedArray',
 'CHAR',
 'CONST_CCHARP',
 'COpaque',
 'COpaquePtr',
 'CStruct',
 'CStructPtr',
 'CWCHARP',
 'CWCHARPP',
 'CallbackHolder',
 'CompilationError',
 'DOUBLE',
 'DOUBLEP',
 'ExtRegistryEntry',
 'ExternalCompilationInfo',
 'FLOAT',
 'FLOATP',
 'INT',
 'INTMAX_T',
 'INTMAX_TP',
 'INTP',
 'INTPTR_T',
 'INTPTR_TP',
 'INT_FAST16_T',
 'INT_FAST16_TP',
 'INT_FAST32_T',
 'INT_FAST32_TP',
 'INT_FAST64_T',
 'INT_FAST64_TP',
 'INT_FAST8_T',
 'INT_FAST8_TP',
 'INT_LEAST16_T',
 'INT_LEAST16_TP',
 'INT_LEAST32_T',
 'INT_LEAST32_TP',
 'INT_LEAST64_T',
 'INT_LEAST64_TP',
 'INT_LEAST8_T',
 'INT_LEAST8_TP',
 'INT_real',
 'LONG',
 'LONGDOUBLE',
 'LONGDOUBLEP',
 'LONGLONG',
 'LONGLONGP',
 'LONGP',
 'LONG_BIT',
 'MODE_T',
 'MODE_TP',
 'MakeEntry',
 'NULL',
 'NUMBER_TYPES',
 'PID_T',
 'PID_TP',
 'PTRDIFF_T',
 'PTRDIFF_TP',
 'RFFI_ALT_ERRNO',
 'RFFI_ERR_ALL',
 'RFFI_ERR_NONE',
 'RFFI_FULL_ERRNO',
 'RFFI_FULL_ERRNO_ZERO',
 'RFFI_FULL_LASTERROR',
 'RFFI_READSAVED_ERRNO',
 'RFFI_READSAVED_LASTERROR',
 'RFFI_SAVE_ERRNO',
 'RFFI_SAVE_LASTERROR',
 'RFFI_SAVE_WSALASTERROR',
 'RFFI_ZERO_ERRNO_BEFORE',
 'RawBytes',
 'SHORT',
 'SHORTP',
 'SIGNED',
 'SIGNEDCHAR',
 'SIGNEDCHARP',
 'SIGNEDP',
 'SIGNEDPP',
 'SIZE_T',
 'SIZE_TP',
 'SSIZE_T',
 'SSIZE_TP',
 'SomePtr',
 'StackCounter',
 'StringBuilder',
 'Symbolic',
 'TEST_RAW_ADDR_KEEP_ALIVE',
 'TIME_T',
 'TIME_TP',
 'TYPES',
 'UCHAR',
 'UCHARP',
 'UINT',
 'UINTMAX_T',
 'UINTMAX_TP',
 'UINTP',
 'UINTPTR_T',
 'UINTPTR_TP',
 'UINT_FAST16_T',
 'UINT_FAST16_TP',
 'UINT_FAST32_T',
 'UINT_FAST32_TP',
 'UINT_FAST64_T',
 'UINT_FAST64_TP',
 'UINT_FAST8_T',
 'UINT_FAST8_TP',
 'UINT_LEAST16_T',
 'UINT_LEAST16_TP',
 'UINT_LEAST32_T',
 'UINT_LEAST32_TP',
 'UINT_LEAST64_T',
 'UINT_LEAST64_TP',
 'UINT_LEAST8_T',
 'UINT_LEAST8_TP',
 'ULONG',
 'ULONGLONG',
 'ULONGLONGP',
 'ULONGP',
 'USHORT',
 'USHORTP',
 'UnicodeBuilder',
 'VOID*',
 'VOID*P',
 'VOIDP',
 'VOIDPP',
 'WCHAR_T',
 'WCHAR_TP',
 '_IsLLPtrEntry',
 '_KEEPER_CACHE',
 '__INT128_T',
 '__INT128_TP',
 '__builtins__',
 '__cached__',
 '__doc__',
 '__file__',
 '__name__',
 '__not_usable',
 '__package__',
 '_get_structcopy_fn',
 '_isfunctype',
 '_isllptr',
 '_keeper_for_type',
 '_make_wrapper_for',
 '_name',
 'alloc_buffer',
 'alloc_unicodebuffer',
 'annmodel',
 'assert_str0',
 'c_memcpy',
 'c_memset',
 'cast',
 'cast_ptr_to_adr',
 'charp2str',
 'charp2strn',
 'charpp2liststr',
 'charpsize2str',
 'enforceargs',
 'free_charp',
 'free_charpp',
 'free_nonmoving_unicodebuffer',
 'free_nonmovingbuffer',
 'free_wcharp',
 'func_with_new_name',
 'generate_macro_wrapper',
 'get_keepalive_object',
 'get_nonmoving_unicodebuffer',
 'get_nonmovingbuffer',
 'get_nonmovingbuffer_final_null',
 'get_raw_address_of_string',
 'getintfield',
 'itemoffsetof',
 'jit',
 'keep_buffer_alive_until_here',
 'keep_unicodebuffer_alive_until_here',
 'keepalive_until_here',
 'liststr2charpp',
 'll2ctypes',
 'll_liststr2charpp',
 'llexternal',
 'llexternal_use_eci',
 'llhelper',
 'llmemory',
 'lltype',
 'lltype_to_annotation',
 'make',
 'make_string_mappings',
 'maxint',
 'name',
 'offsetof',
 'os',
 'platform',
 'populate_inttypes',
 'pprint',
 'ptradd',
 'py',
 'r___int128_t',
 'r_int',
 'r_int_fast16_t',
 'r_int_fast32_t',
 'r_int_fast64_t',
 'r_int_fast8_t',
 'r_int_least16_t',
 'r_int_least32_t',
 'r_int_least64_t',
 'r_int_least8_t',
 'r_int_real',
 'r_intmax_t',
 'r_intptr_t',
 'r_long',
 'r_longlong',
 'r_mode_t',
 'r_pid_t',
 'r_ptrdiff_t',
 'r_short',
 'r_signedchar',
 'r_singlefloat',
 'r_size_t',
 'r_ssize_t',
 'r_time_t',
 'r_uchar',
 'r_uint',
 'r_uint_fast16_t',
 'r_uint_fast32_t',
 'r_uint_fast64_t',
 'r_uint_fast8_t',
 'r_uint_least16_t',
 'r_uint_least32_t',
 'r_uint_least64_t',
 'r_uint_least8_t',
 'r_uintmax_t',
 'r_uintptr_t',
 'r_ulong',
 'r_ulonglong',
 'r_ushort',
 'r_void*',
 'r_wchar_t',
 'rarithmetic',
 'register_keepalive',
 'rgc',
 'scoped_alloc_buffer',
 'scoped_alloc_unicodebuffer',
 'scoped_nonmoving_unicodebuffer',
 'scoped_nonmovingbuffer',
 'scoped_str2charp',
 'scoped_unicode2wcharp',
 'scoped_view_charp',
 'setintfield',
 'setup',
 'size_and_sign',
 'sizeof',
 'sizeof_c_type',
 'specialize',
 'stackcounter',
 'str2chararray',
 'str2charp',
 'str2rawmem',
 'str_from_buffer',
 'structcopy',
 'sys',
 'unicode2rawmem',
 'unicode2wchararray',
 'unicode2wcharp',
 'unicode_from_buffer',
 'unregister_keepalive',
 'unrolling_iterable',
 'wcharp2unicode',
 'wcharp2unicoden',
 'wcharpsize2unicode',
 'we_are_translated',
 'we_are_translated_to_c']

.. ['BaseIntTypeEntry',
 'BaseIntValueEntry',
 'Constant',
 'For_r_singlefloat_type_Entry',
 'For_r_singlefloat_values_Entry',
 'INT_MAX',
 'INT_MIN',
 'LONGLONGLONG_BIT',
 'LONGLONGLONG_MASK',
 'LONGLONGLONG_TEST',
 'LONGLONG_BIT',
 'LONGLONG_MASK',
 'LONGLONG_TEST',
 'LONG_BIT',
 'LONG_BIT_SHIFT',
 'LONG_MASK',
 'LONG_TEST',
 'SHRT_MAX',
 'SHRT_MIN',
 'UINT_MAX',
 'USHRT_MAX',
 '__builtins__',
 '__cached__',
 '__doc__',
 '__file__',
 '__name__',
 '__package__',
 '_get_bitsize',
 '_get_long_bit',
 '_inttypes',
 '_long_typecode',
 '_should_widen_type',
 'base_int',
 'build_int',
 'byteswap',
 'compute_restype',
 'const',
 'extregistry',
 'get_long_pattern',
 'highest_bit',
 'int_between',
 'int_c_div',
 'int_c_mod',
 'int_force_ge_zero',
 'intmask',
 'is_emulated_long',
 'is_signed_integer_type',
 'is_valid_int',
 'longlonglongmask',
 'longlongmask',
 'longlongmax',
 'math',
 'maxint',
 'most_neg_value_of',
 'most_neg_value_of_same_type',
 'most_pos_value_of',
 'most_pos_value_of_same_type',
 'normalizedinttype',
 'not_rpython',
 'objectmodel',
 'ovfcheck',
 'ovfcheck_float_to_int',
 'ovfcheck_float_to_longlong',
 'ovfcheck_int32_add',
 'ovfcheck_int32_mul',
 'ovfcheck_int32_sub',
 'r_int',
 'r_int32',
 'r_int64',
 'r_longfloat',
 'r_longlong',
 'r_longlonglong',
 'r_singlefloat',
 'r_uint',
 'r_uint32',
 'r_uint64',
 'r_ulonglong',
 'register_flow_sc',
 'sc_r_uint',
 'signed_int',
 'signedtype',
 'specialize',
 'string_to_int',
 'struct',
 'sys',
 'unsigned_int',
 'widen']

.. {<Signed>: 'Signed @',
 <Unsigned>: 'Unsigned @',
 <SignedLongLongLong>: '__int128_t @',
 <INT>: 'int @',
 <USHORT>: 'unsigned short @',
 <UCHAR>: 'unsigned char @',
 <UINT>: 'unsigned int @',
 <SIGNEDCHAR>: 'signed char @',
 <SHORT>: 'short @',
 <INT>: 'int @',
 <Address>: 'void* @',
 <SingleFloat>: 'float @',
 <Float>: 'double @',
 <LongFloat>: 'long double @',
 <Char>: 'char @',
 <Bool>: 'bool_t @',
 <Void>: 'void @',
 <UniChar>: 'wchar_t @',
 <* GCREF (gcopaque)>: 'void* @'}
