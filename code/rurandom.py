from rpython.rlib import rurandom

def rurandom_example():
    r = rurandom.urandom(None, 100)
    print r

    # The call can be interrupted by a signal, you can define a callback
    # function for status checking
    r = rurandom.urandom(None, 100, signal_checker)

def signal_checker():
    print "Checking signal"

def entry_point(argv):
    rurandom_example()
    return 0

def target(*args): return entry_point
