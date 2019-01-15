from rpython.rlib.rsre import rsre_re as re

def rsre_example():
    # scan through string looking for the first location where the regular
    # expression pattern produces a match
    print re.search('x*', 'axx').span(0)

    # if zero or more characters at the beginning of string match the regular
    # expression pattern
    print re.match('a+', 'xxx')

    # split string by the occurrences of pattern
    print re.split(":", ":a:b::c")

    # return all non-overlapping matches of pattern in string, as a list of
    # strings
    print re.findall(":+", "a:b::c:::d")

def entry_point(argv): rsre_example(); return 0
def target(*args): return entry_point
