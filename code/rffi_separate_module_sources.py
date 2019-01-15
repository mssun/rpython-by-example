from rpython.rtyper.lltypesystem import rffi
from rpython.rtyper.lltypesystem.lltype import Signed
from rpython.translator.tool.cbuild import ExternalCompilationInfo

c_source = """
int someexternalfunction(int x)
{
    return (x + 3);
}
"""

eci = ExternalCompilationInfo(separate_module_sources=[c_source])
c_someexternalfunction = rffi.llexternal('someexternalfunction',
                                         [Signed],
                                         Signed,
                                         compilation_info=eci)

def rffi_example():
    print c_someexternalfunction(1)

def entry_point(argv): rffi_example(); return 0
def target(*args): return entry_point
