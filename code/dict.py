def rdict():
    def print_dict(d):
        for k, v in d.iteritems(): print k, v

    d = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}
    print_dict(d)

    print "len: ", len(d)
    print "d[key]: ", d['one']

    d['one'] = 3
    print "d[key] = value: ", d['one']

    del d['one']
    try:
        print "d[key] = value: ", d['one']
    except KeyError:
        print "KeyError: not found."

    if 'one' not in d:
        print "'one' is not in d"

    # iterator over a dictionary
    for i in iter(d): print i
    for i in d.iterkeys(): print i
    for i in d.itervalues(): print i
    for i in d.keys(): print i
    for i in d.values(): print i

    d.pop('five')
    k, v = d.popitem()
    print k, v

    d.update({'five': 55})

def entry_point(argv):
    rdict()
    return 0

def target(*args): return entry_point
if __name__ == "__main__": import sys; entry_point(sys.argv)
