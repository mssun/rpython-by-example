def sequence():
    s = "this is a string"
    u = u"this is a unicode string"
    l = ["this", "is", "a", "list", "of", "strings"]
    t = ("first", "second")
    ba = bytearray(b"\x44\x45\x41\x44\x42\x45\x45\x46")
    buf = buffer(s, 10, 6)
    r = xrange(0, 5, 2)

    print s; print u; print l; print t; print ba; print buf
    for i in r: print i

    # x in s: True if an item of s is equal to x, else False
    if 't' in s:
        print "t is in string", s

    # x not in s:  False if an item of s is equal to x, else True
    if 'b' not in u:
        print "b is not in unicode string", u

    # s + t: the concatenation of s and t
    print l + [":)"]

    # s * n, n * s: equivalent to adding s to itself n times
    print t * 2

    # s[i]: ith item of s, origin 0
    print "3rd item of l is:", l[2]

    # s[i:j]: slice of s from i to j
    print "slice of s:", s[2:-1]

    # len(s): length of s
    print "length of ba is", len(ba)

    # s.index(x): index of the first occurrence of x in s
    print l.index("of")

    # s.count(x): total number of occurrences of x in s
    print s.count("is")

def entry_point(argv):
    sequence()
    return 0

def target(*args): return entry_point
if __name__ == "__main__": import sys; entry_point(sys.argv)
