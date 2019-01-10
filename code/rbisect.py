from rpython.rlib.rbisect import bisect_left, bisect_right

def rbisect_example():
    l = [1, 1, 2, 2, 3]

    # Locate the leftmost value exactly equal to 1
    i = bisect_left(l, 1, len(l))
    if i != len(l) and l[i] == 1:
        print "The index of leftmost value exactly equal to 1: ", i

    # Find leftmost value greater than 1
    i = bisect_right(l, 1, len(l))
    if i != len(l):
        print "The index of leftmost value greater than 1: ", i

def entry_point(argv):
    rbisect_example()
    return 0

def target(*args): return entry_point
if __name__ == "__main__": import sys; entry_point(sys.argv)
