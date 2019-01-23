from rpython.rtyper.lltypesystem import rffi
from rpython.rtyper.lltypesystem import lltype
from rpython.translator import cdir
from rpython.tool.udir import udir
from rpython.translator.tool.cbuild import ExternalCompilationInfo

########################### callback #################################

h_source_callback = """
#ifndef _CALLBACK_H
#define _CALLBACK_H
RPY_EXTERN Signed compute(Signed arg, Signed(*callback)(Signed));
#endif /* _CALLBACK_H */
"""
h_include_callback = udir.join("callback.h")
h_include_callback.write(h_source_callback)

c_source_callback = """
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
                              separate_module_sources=[c_source_callback])

args = [rffi.SIGNED, rffi.CCallback([rffi.SIGNED], rffi.SIGNED)]
compute = rffi.llexternal('compute', args, rffi.SIGNED,
                          compilation_info=eci)

########################### callback end #############################

def rffi_callback():
    def g(i): return i + 3
    print compute(1, g)

def rffi_more_examples():
    rffi_callback()

def entry_point(argv): rffi_more_examples(); return 0
def target(*args): return entry_point
