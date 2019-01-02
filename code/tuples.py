def tuples():
    t = (1, 2)
    i, j = t    # "unpack" a tuple
    print t, i, j
    t = (1, "123") # mixing types in a tuple
    print t

    l = [1, 2]
    t = (l[0], l[1])    # manually convert from a list to a tuple
    print t


def tuples_unsupported():
    l = [1, "123"]   # mixing types in lists is not supported in RPython
    t = tuple(l)     # converting from list to tuple is unsupported
    print t

def entry_point(argv):
    tuples()
    return 0

def target(*args): return entry_point
if __name__ == "__main__":
    import sys; entry_point(sys.argv)
    tuples_unsupported()
