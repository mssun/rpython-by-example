def compiler_error(arg):
    return v

def entry_point(argv): compiler_error(argv[1]); return 0
def target(*args): return entry_point
