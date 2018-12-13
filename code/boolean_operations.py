def boolean_operations():
    t = True
    f = False
    empty_dict = {}

    if t or f: print("True or False is True")

    if t and f: pass
    else: print("True and False is False")

    if not empty_dict: print("not {} is True")

def entry_point(argv):
    boolean_operations()
    return 0

def target(*args):
    return entry_point
