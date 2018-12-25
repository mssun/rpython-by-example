# -*- coding: utf-8 -*-
def strings():
    s = "this is a string"

    print s.count("this", 0, len(s))

    if s.endswith("ing"): print "s ends with string"

    if s.find("is"): print "found is in s"

    s2 = "thisisastring2"
    if s2.isalnum(): print "s2 is alnum"

    s3 = "thisisastringthree"
    if s3.isalpha(): print "s3 is alpha"

    s4 = "12345"
    if s4.isdigit(): print "s4 is digit"

    l = ["this", "is", "a", "string"]
    print " ".join(l)

    print "THI IS A STRING".lower()
    print '   spacious   '.lstrip()
    print s.rfind("is")
    print s.rsplit(" ")
    print s.split(" ")

    s_lines = "This is a string.\nAnd another string."
    print s_lines.splitlines()

    if s.startswith("this"): print "s starts with this"

    print '   spacious   '.strip()
    print s.upper()

    print "%s, %d, %x, %o, %f" % ("string", 1, 16, 9, 3.14)

def entry_point(argv):
    strings()
    return 0

def target(*args): return entry_point
if __name__ == "__main__":
    import sys; entry_point(sys.argv)
