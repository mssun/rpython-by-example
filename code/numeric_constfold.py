def numeric_constfold():
    """Constant folding on numeric."""
    x = -1024
    y = 42

    j = 1j       # yield an imaginary number (complex number with zero real part)
    print "complex: 1j =", j
    print "divmod(x, y) =", divmod(x, y)  # the pair (x // y, x % y)
    print "pow(x, y) =", pow(x, y)        # x to the power y

def numeric_no_constfold(x, y):
    """RPython cannot do constant folding on x and y"""
    print "divmod(x, y) =", divmod(x, y)  # the pair (x // y, x % y)
    print "pow(x, y) =", pow(x, y)        # x to the power y

def entry_point(argv):
    numeric_constfold()
    # numeric_no_constfold(int(argv[1]), int(argv[2]))    # compilation error, comment this function to try constant folding
    return 0

def target(*args): return entry_point
if __name__ == "__main__": import sys; entry_point(sys.argv)
