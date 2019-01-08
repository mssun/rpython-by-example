from rpython.rlib import rtime

def rtime_example():
    # Return the time in seconds since the epoch as a floating point number.
    print rtime.time()

    # Suspend execution of the calling thread for the given number of seconds.
    rtime.sleep(3)

    # On Unix, return the current processor time as a floating point number
    # expressed in seconds.
    print rtime.clock()

def entry_point(argv): rtime_example(); return 0
def target(*args): return entry_point
