def numeric():
    x = -1024    # plain integer
    y = 42
    f = 3.14     # yield float
    l = 1L       # yield a long integer
    j = 1j       # yield an imaginary number (complex number with zero real part)

    print "int: -1024 =", x
    print "float: 3.14 =", f
    print "long: 1L =", l
    print "complex: 1j =", j

    print "x + y =", x + y      # sum of x and y
    print "x - y =", x - y      # difference of x and y
    print "x * y =", x * y      # product of x and y
    print "x / y =", x / y      # quotient of x and y
    print "x // y =", x // y    # (floored) quotient of x and y
    print "x % y =", x % y      # remainder of x / y
    print "-x =", -x            # x negated
    print "+x =", +x            # x unchanged

    print "abs(x) =", abs(x)              # absolute value or magnitude of x
    print "int(x) =", int(f)              # x converted to integer
    print "float(x) =", float(y)          # x converted to floating point
    print "divmod(x, y) =", divmod(x, y)  # the pair (x // y, x % y)
    print "pow(x, y) =", pow(x, y)        # x to the power y

def entry_point(argv):
    numeric()
    return 0

def target(*args):
    return entry_point

if __name__ == "__main__":
    import sys
    entry_point(sys.argv)
