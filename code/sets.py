def sets():
    # Since set is not supported in RPython, we use dict with None as values to
    # simulate a set.
    s1 = {'foo': None, 'bar': None, 'baz': None, 'foo': None, 'baz': None}
    if 'fooo' not in s1: print 'fooo is not in the set s1'
    if 'foo' in s1: print 'foo is in the set s1'
    for i in s1: print i

    s2 = {'foo': None, 'hello': None, 'world': None, 'foo': None}

    # union
    def set_union(s1, s2):
        s3 = s1.copy()
        s3.update(s2)
        return s3

    print 'union:'
    s3 = set_union(s1, s2)
    for i in s3: print i

    # intersection:
    def set_intersection(s1, s2):
        s3 = {}
        for i in s1:
            if i in s2:
                s3.update({i: None})

        for i in s2:
            if i in s1:
                s3.update({i: None})
        return s3

    print 'intersection:'
    s3 = set_intersection(s1, s2)
    for i in s3: print i

def entry_point(argv):
    sets()
    return 0

def target(*args): return entry_point
if __name__ == "__main__":
    import sys
    entry_point(sys.argv)
