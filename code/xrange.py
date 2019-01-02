def rrange():
    # range and xrange are same in RPython
    for i in range(0, 10, 2):
        print i
    for i in xrange(0, 10, 3):
        print i

def entry_point(argv):
    rrange()
    return 0

def target(*args): return entry_point
if __name__ == "__main__": import sys; entry_point(sys.argv)
