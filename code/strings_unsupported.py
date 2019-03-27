# -*- coding: utf-8 -*-

################### UNSUPPORTED IN RPYTHON ######################
def strings_unsupported():
    s = "this is a string"

    print s.capitalize()
    print s.center(30)

    s_utf8 = "你好".decode("utf-8")
    print s_utf8

    print '01\t012\t0123\t01234'.expandtabs()

    print "The sum of 1 + 2 is {0}".format(1+2)
    print s.index("is")

    s5 = "this is lowercased string"
    if s5.islower(): print "s5 is lowercased"

    s6 = "         "
    if s6.isspace(): print "s6 contains only whitespaces"

    s7 = "This Is A Title String"
    if s7.istitle(): print "s7 is a title cased string"

    s8 = "THIS IS A SUPPER STRING"
    if s8.isupper(): print "s8 is all cased characters"

    print s.ljust(10)
    print s.partition(" ")
    print s.replace("this", "that")
    print s.rindex("is")
    print s.rjust(10)
    print s.rpartition(" ")
    print s.swapcase()
    print "they're bill's friends from the UK".title()
    print s.zfill(20)
    print "Hello, %(name)s" % {"name": "world"}

def entry_point(argv):
    strings_unsupported()
    return 0

def target(*args): return entry_point
if __name__ == "__main__":
    import sys; entry_point(sys.argv)
    strings_unsupported()
