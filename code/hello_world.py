def entry_point(argv):
    print "Hello, World!"
    return 0

# The target function is the main function of a RPython program. It takes
# command line arguments as inputs and return an entry point function.
def target(*args):
    return entry_point
