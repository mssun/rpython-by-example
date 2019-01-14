def numeric(x, y, f, l):
    print "int: -1024 =", x
    print "float: 3.14 =", f
    print "long: 1L =", l

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
    # print "divmod(x, y) =", divmod(x, y)  # the pair (x // y, x % y)
    # print "pow(x, y) =", pow(x, y)        # x to the power y

def entry_point(argv):
    x = -1024    # plain integer
    y = 42
    f = 3.14     # float
    l = 1L       # a long integer
    numeric(x, y, f, l)
    return 0

def target(*args): return entry_point
if __name__ == "__main__": import sys; entry_point(sys.argv)
