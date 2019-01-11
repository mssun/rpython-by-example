from rpython.rlib.rarithmetic import *

def rarithmetic_example():
    # integer types in C
    i = r_int(0)               # 32
    u = r_uint(0)              # 32
    i32 = r_int32(0)           # 32
    u32 = r_uint32(0)          # 32
    i64 = r_int64(0)           # 64
    u64 = r_uint64(0)          # 64
    ll = r_longlong(0)         # 64
    ull = r_ulonglong(0)       # 64
    lll = r_longlonglong(0)    # 128

    print intmask(longlongmax)

    # convert little endian to big endian and vice versa
    print byteswap(1)

    # perform an add/sub/mul between two regular integers, but assumes that
    # they fit inside signed 32-bit ints and raises OverflowError if the result
    # no longer does
    print ovfcheck_int32_add(10000, 1000)
    print ovfcheck_int32_sub(10000, 1000)
    print ovfcheck_int32_mul(10000, 1000)

    # convert to an integer or raise OverflowError
    try:
        print ovfcheck_float_to_int(9223372036854775296.0 + 1)
    except OverflowError:
        print "Exception: OverflowError"
    # convert to a longlong or raise OverflowError
    try:
        print ovfcheck_float_to_longlong(9223372036854775296.0 + 1)
    except OverflowError:
        print "Exception: OverflowError"

    # utility to converts a string to an integer
    print string_to_int("10", base=10)
    print string_to_int("A", base=16)
    print string_to_int("1010", base=2)
    print string_to_int("1_000", base=10, allow_underscores=True)


def entry_point(argv): rarithmetic_example(); return 0
def target(*args): return entry_point
