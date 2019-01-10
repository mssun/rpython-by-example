from rpython.rlib import rtimer

def rtimer_example():
    t1 = rtimer.read_timestamp()
    print rtimer.get_timestamp_unit()
    t2 = rtimer.read_timestamp()
    print t2 - t1

def entry_point(argv): rtimer_example(); return 0
def target(*args): return entry_point
