def func(): return 0
def compiler_error(arg):
    func(1)

def entry_point(argv): compiler_error(argv[1]); return 0
def target(*args): return entry_point
