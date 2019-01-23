from rpython.rtyper.lltypesystem import rffi
from rpython.translator.tool.cbuild import ExternalCompilationInfo

# Calculate the total length of strings in the list
c_source = """
#include <string.h>

int strlen_list(char *args[]) {
    char **p = args;         // CHARPP in RPython
    int l = 0;
    while (*p) {
        l += strlen(*p);
        p++;
    }
    return l;
}
"""
eci = ExternalCompilationInfo(separate_module_sources=[c_source])
c_strlen_list = rffi.llexternal('strlen_list',           # function name
                                [rffi.CCHARPP],          # parameters
                                rffi.SIGNED,             # return value
                                compilation_info=eci)

def rffi_list_example():
    l = ["Hello", ",", "World", "!"]
    l_charpp = rffi.liststr2charpp(l)
    r = c_strlen_list(l_charpp)
    rffi.free_charpp(l_charpp)
    print r

def entry_point(argv): rffi_list_example(); return 0
def target(*args): return entry_point
