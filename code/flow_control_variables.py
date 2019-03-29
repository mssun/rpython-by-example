class Obj():
    pass

def flow_control_variables_unsupported(arg):
    """
    int, floats or tuples cannot be mixed with None.
    """
    i = None    # integer
    f = None    # float
    t = None    # tuple

    if arg:
        i = None
        f = None
        t = None
    else:
        i = 0
        f = 0.0
        t = (1, 2, 3)

    return i, f, t

def flow_control_variables(arg):
    """
    It is allowed to mix None with many other types: wrapped objects, class
    instances, lists, dicts, strings, etc.
    """
    o = None    # object instance
    l = None    # list
    d = None    # dict
    s = None    # string

    if arg:
        o = None
        l = None
        d = None
        s = None
    else:
        o = Obj()
        l = [1, 2, 3]
        d = {1: "123"}
        s = "hello"

    if o and l and d and s:
        print o, l, d[1], s

    return o, l, d, s

def entry_point(argv): flow_control_variables(int(argv[1])); return 0
def target(*args): return entry_point
