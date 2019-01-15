from rpython.rtyper.lltypesystem import rffi
from rpython.rtyper.lltypesystem import lltype
from rpython.translator.tool.cbuild import ExternalCompilationInfo

########################### str2charp ################################

eci1 = ExternalCompilationInfo(includes=['string.h'])
c_strlen = rffi.llexternal('strlen',
                            [rffi.CCHARP],
                            lltype.Signed,
                            compilation_info=eci1)

def rffi_strlen():
    s = rffi.str2charp("Hello, World!")    # alloc a string buffer
    res = c_strlen(s)
    print res
    rffi.free_charp(s)                     # free the string buffer

########################### charp2str ################################

c_source_2 = """
#include <string.h>
#include <src/mem.h>

void my_strcpy(char *target, char* arg)
{
    strcpy(target, arg);
}
"""
eci2 = ExternalCompilationInfo(separate_module_sources=[c_source_2],
                               post_include_bits=['void my_strcpy(char*,char*);'])
c_my_strcpy = rffi.llexternal('my_strcpy',
                              [rffi.CCHARP, rffi.CCHARP],
                              lltype.Void,
                              compilation_info=eci2)

def rffi_strcpy():
    s = rffi.str2charp("Hello, World!")    # alloc a string buffer
    l_res = lltype.malloc(rffi.CCHARP.TO, 32, flavor='raw')    # alloc a raw buffer
    c_my_strcpy(l_res, s)
    res = rffi.charp2str(l_res)         # convert C string (char*) to RPython string
    print res
    lltype.free(l_res, flavor='raw')    # free the raw buffer
    rffi.free_charp(s)                  # free the string buffer

def rffi_more_examples():
    rffi_strlen()
    rffi_strcpy()

def entry_point(argv): rffi_more_examples(); return 0
def target(*args): return entry_point
