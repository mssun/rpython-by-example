from rpython.rlib.rrandom import Random

def rrandom_example():
    rnd1 = Random()

    print rnd1.genrand32()    # get a 32-bit random number
    print rnd1.random()       # get a float random number x, 0.0 <= x < 1.0

    seed = 1546979228
    rnd2 = Random(seed)     # set a seed
    print rnd2.random()

    print rnd1.state    # you can access the internal state of the generator

    # change the internal state to one different from and likely far away from
    # the current state, n is a non-negative integer which is used to scramble
    # the current state vector.
    n = 10
    rnd1.jumpahead(n)
    rnd1.random()

def entry_point(argv):
    rrandom_example()
    return 0

def target(*args): return entry_point
