def compiler_error(arg):
    n = 10 * (1/0)
    return n

def entry_point(argv): compiler_error(argv[1]); return 0
def target(*args): return entry_point
