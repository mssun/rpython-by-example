def numeric_unsupported():
    """Operations and functions supported in Python but not supported in RPython."""
    x = -1024
    y = 42

    print "long(x) =", long(x)    # x converted to long integer

    re = 1
    im = 2
    # a complex number with real part re, imaginary part im. im defaults to zero.
    print "complex(x) =", complex(re, im)

    c = 0
    # conjugate of the complex number c. (Identity on real numbers)
    print "c.conjugate() =", c.conjugate()

    print "x ** y =", x ** y     # x to the power y

    # float also accepts the strings "nan" and "inf" with an optional prefix
    # "+" or "-" for Not a Number (NaN) and positive or negative infinity.
    print "float(inf) =", float("inf")
    print "float(+inf) =", float("+inf")
    print "float(-inf) =", float("-inf")

    print "float(nan) =", float("nan")
    print "float(+nan) =", float("+nan")
    print "float(-nan) =", float("-nan")

def entry_point(argv):
    numeric_unsupported()
    return 0

def target(*args):
    return entry_point

if __name__ == "__main__":
    import sys
    entry_point(sys.argv)
