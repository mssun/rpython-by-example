from rpython.rtyper.lltypesystem import rffi
from rpython.rtyper.lltypesystem import lltype
from rpython.translator import cdir
from rpython.tool.udir import udir
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

########################### callback #################################

h_source_3 = """
#ifndef _CALLBACK_H
#define _CALLBACK_H
RPY_EXTERN Signed compute(Signed arg, Signed(*callback)(Signed));
#endif /* _CALLBACK_H */
"""
h_include_3 = udir.join("callback.h")
h_include_3.write(h_source_3)

c_source_3 = """
#include "src/precommondefs.h"

RPY_EXTERN Signed compute(Signed arg, Signed(*callback)(Signed))
{
    Signed res = callback(arg);
    if (res == -1)
        return -1;
    return res;
}
"""

eci = ExternalCompilationInfo(includes=['callback.h'],
                              include_dirs=[str(udir), cdir],
                              separate_module_sources=[c_source_3])

args = [rffi.SIGNED, rffi.CCallback([rffi.SIGNED], rffi.SIGNED)]
compute = rffi.llexternal('compute', args, rffi.SIGNED,
                          compilation_info=eci)

########################### callback end #############################

def rffi_callback():
    def g(i): return i + 3
    print compute(1, g)

def rffi_more_examples():
    rffi_strlen()
    rffi_strcpy()
    rffi_callback()

def entry_point(argv): rffi_more_examples(); return 0
def target(*args): return entry_point
