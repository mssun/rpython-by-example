def numeric_bitwise():
    x = 2
    y = 4
    n = 1

    print "x = ", x, ", y = ", y
    # the bitwise operations sorted in ascending priority
    print "x | y =", x | y      # bitwise or of x and y
    print "x ^ y =", x ^ y      # bitwise exclusive or of x and y
    print "x & y =", x & y      # bitwise and of x and y
    print "x << n =", x << n    # x shifted left by n bits
    print "x >> n =", x >> n    # x shifted right by n bits
    print "~x =", ~x            # the bits of x inverted


def entry_point(argv):
    numeric_bitwise()
    return 0

def target(*args): return entry_point
if __name__ == "__main__": import sys; entry_point(sys.argv)
