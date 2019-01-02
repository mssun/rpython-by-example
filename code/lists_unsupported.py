def lists_unsupported():
    l = [0, 1, 2, 3, 4]

    # In RPython, stop doesn't need to within bounds, but it must not be
    # smaller than the start
    print l[3:2]

    # In RPython, all negative indexes are disallowed, except for the [:-1]
    # special case.
    print l[0:-2]

    # No step in RPython
    print l[0:-1:2]

    # Slice assignment cannot change the total length of the list, but just
    # replace items
    l[0:2] = [100, 101, 102, 103]
    print l

    # The sort() and count() methods are not supported
    l.sort()
    print l.count(103)

def entry_point(argv):
    lists_unsupported()
    return 0

def target(*args): return entry_point
if __name__ == "__main__":
    import sys; entry_point(sys.argv)
    lists_unsupported()
