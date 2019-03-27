def compiler_error(arg):
    v = 0              # v is an integer
    if arg:
        v = 1          # assign integer 1 to v
    else:
        v = ""         # assign string "" to v
    return v

def entry_point(argv): compiler_error(argv[1]); return 0
def target(*args): return entry_point
