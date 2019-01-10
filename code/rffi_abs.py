from rpython.rtyper.lltypesystem import rffi
from rpython.translator.tool.cbuild import ExternalCompilationInfo
from rpython.rlib.rarithmetic import r_int32, r_int64, r_longlong

eci = ExternalCompilationInfo(
    includes=['stdlib.h'],
)

# int abs(int j);
c_abs = rffi.llexternal('abs',                     # function name
                        [rffi.INT],                # argument types
                        rffi.INT,                  # return type
                        compilation_info=eci)

# long int labs(long int j);
c_labs = rffi.llexternal('labs',                   # function name
                         [rffi.LONG],              # argument types
                         rffi.LONG,                # return type
                         compilation_info=eci)

# long long int llabs(long long int j);
c_llabs = rffi.llexternal('llabs',                 # function name
                         [rffi.LONGLONG],          # argument types
                         rffi.LONGLONG,            # return type
                         compilation_info=eci)

def rffi_example():
    int_number = r_int32(-10)
    print c_abs(int_number)

    long_number = r_int64(-10)
    print c_labs(long_number)

    longlong_number = r_longlong(-10)
    print c_llabs(longlong_number)

def entry_point(argv): rffi_example(); return 0
def target(*args): return entry_point
