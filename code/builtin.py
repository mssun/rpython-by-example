def builtin_functions():
    print bool(1)     # return a boolean value
    print int(1.0)    # return an integer value
    print float(1)    # return a float value
    print chr(65)     # return a string of one character whose ASCII code is the input
    print str(53)     # return a string containing a nicely printable representation of an object
    print unichr(97)  # return the Unicode string of one character whose Unicode code is the integer input
    print unicode('abc')    # return the Unicode string version of object
    print bytearray('abc')  # return a new array of bytes
    print list('abc')       # return a list whose items are the same and in the same order as iterable’s items
    for i in range(3):      # create a list containing arithmetic progressions
        print i
    for i in xrange(3):
        print i
    seasons = ['Spring', 'Summer', 'Fall', 'Winter']
    for i in enumerate(seasons):    # return an enumerate object
        print i
    print min(1, 2)    # return the smallest of two arguments
    print max(1, 2)    # return the largest of two arguments
    for i in reversed([1, 2, 3]):    # return a reverse iterator
        print i

def entry_point(argv):
    builtin_functions()
    return 0

def target(*args): return entry_point
if __name__ == "__main__": import sys; entry_point(sys.argv)
