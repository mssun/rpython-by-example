def builtin_functions():
    print bool(1)
    print int(1.0)
    print float(1)
    print chr(65)
    print str(53)
    print unichr(97)
    print unicode('abc')
    print bytearray('abc')
    print list('abc')
    for i in range(3):
        print i
    for i in xrange(3):
        print i
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    for i in enumerate(seasons):
        print i
    print min(1, 2)
    print max(1, 2)
    for i in reversed([1, 2, 3]):
        print i

def entry_point(argv):
    builtin_functions()
    return 0

def target(*args): return entry_point
if __name__ == "__main__": import sys; entry_point(sys.argv)
