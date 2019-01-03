def dict_unsupported():
    d1 = dict(one=1, two=2, three=3)
    d2 = dict({'one': 1, 'two': 2, 'three': 3})
    d3 = dict([('two', 2), ('one', 1), ('three', 3)])
    d4 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))
    print d1
    print d2
    print d3
    print d4

    # There is no dictionary view objects in RPython
    d5 = dict({'three': 3, 'four': 4, 'five': 5})
    v1 = d1.viewkeys()
    v5 = d5.viewkeys()
    print v1 & v5
    print v1 | v5
    print v1 - v5
    print v1 ^ v5

    # keys in different types are note supported in RPython
    d6 = dict({1: 1, 'two': 2})
    print d6[1], d6['two']

def entry_point(argv):
    dict_unsupported()
    return 0

def target(*args): return entry_point
if __name__ == "__main__": import sys; entry_point(sys.argv)
