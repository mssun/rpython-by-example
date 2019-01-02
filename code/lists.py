def lists():
    l = [0, 1, 2, 3, 4]
    print l[3]
    print l[-1]

    # Indexes are checked when requested by an IndexError exception clause.
    try:
        print l[100]
    except IndexError:
        print "IndexError"

    print l[3:5]
    print l[0:-1]

    l[0:2] = [100, 101, 102]
    print l

    # other operators: +, +=, in, *, *=, ==, != work as expected.

    l = [0] + [1]    # [0, 1]
    l *= 2           # [0, 1, 0, 1]

    # append, index, insert, extend, reverse, pop. The index used in pop()
    # follows the same rules as for indexing above. The index used in insert()
    # must be within bounds and not negative.
    l = []
    l.append(0)          # [0]
    print l.index(0)
    l.insert(1, 1)       # [0, 1]
    l.extend([2, 3, 4])  # [0, 1, 2, 3, 4]
    l.reverse()          # [4, 3, 2, 1, 0]
    l.pop()              # [4, 3, 2, 1]
    del l[0:1]           # [3, 2, 1]
    l.remove(1)          # [3, 2]
    print l

def entry_point(argv):
    lists()
    return 0

def target(*args): return entry_point
if __name__ == "__main__":
    import sys; entry_point(sys.argv)
