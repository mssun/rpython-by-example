################### UNSUPPORTED IN RPYTHON ######################

def sets_unsupported():
    s1 = set(['foo', 'bar', 'baz', 'foo'])
    s2 = set(['foo', 'hello', 'world', 'foo'])
    if 'fooo' not in s1: print 'fooo is not in the set s1'
    if 'foo' in s1: print 'foo is in the set s1'
    print s1

    # union
    print s1.union(s2)
    print s1 | s2

    # intersection
    print s1.intersection(s2)
    print s1 & s2

    # difference
    print s1.difference(s2)
    print s1 - s2

    # symmetric difference
    print s1.symmetric_difference(s2)
    print s1 ^ s2

    # whether or not two sets have any elements in common
    print s1.isdisjoint(s2)

    # whether one set is a subset/superset of the other
    print s1.issubset(s2)
    print s1 <= s2
    print s1.issubset(s2)
    print s1 >= s2

    # whether on set is a proper subset/superset of the other
    print s1 < s2
    print s1 > s2

    # modifying a set
    s1 |= s2
    s1.update(['fob', 'bah'])
    s1.add('boz')
    s1.remove('boz')
    s1.pop()
    s2.clear()
    print s1

    fs = frozenset(['foo', 'bar', 'baz'])    # frozenset is immutable
    print fs

def entry_point(argv):
    sets_unsupported()
    return 0

def target(*args): return entry_point
if __name__ == "__main__":
    import sys
    entry_point(sys.argv)
