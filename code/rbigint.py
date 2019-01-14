from rpython.rlib.rbigint import rbigint

def rbigint_example():
    r1 = rbigint.fromint((1 << 63 - 1))
    r2 = rbigint.fromint(1 << 32)
    print r1.add(r2).str()
    print r1.sub(r2).str()
    print r1.mul(r2).str()
    print r1.div(r2).str()
    print r1.digit(1)    # Return the x'th digit, as an int
    r2.setdigit(1, 5)
    r3 = rbigint.fromstr("1234567890000")
    print r3.str()
    r4 = rbigint.fromstr("1234567890000", base=16)
    print r4.str()

    print r3.lt(r4)    # less than

def entry_point(argv): rbigint_example(); return 0
def target(*args): return entry_point
