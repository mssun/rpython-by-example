class Cat:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def __eq__(self, other):
        return self.name == other.name and self.height == other.height

    def __cmp__(self, other):
        return self.height - other.height

    def __gt__(self, other):
        return self.height > other.height

def comparisons():
    if 1 < 2: print("<: 1 is strictly less than 2")
    if 1 <= 2: print("<=: 1 is less than or equal to 2")
    if 2 > 1: print(">: 2 is strictly greater than 1")
    if 2 >= 1: print(">=: 2 is greater than or equal 1")
    if 1 == 1: print ("==: 1 is equal to 1")
    if 1 != 2: print("!=: 1 is not equal to 2")

    tiger = Cat("Tiger", 9.1)
    kitty = Cat("Kitty", 9.8)
    puss = tiger

    if tiger is puss: print("is: Tiger and Puss are same cat")
    if tiger is not kitty: print("is not: Tiger and Kitty are different cats")

    # Even though __cmp__() and __gt__() are defined in the Cat class, we still
    # cannot compare two Cat instances in RPython. Uncomment the following line
    # to compile with RPython and you will get an unimplemented operation: 'gt'
    # error.

    # if kitty > tiger: print(">: Kitty is taller than Kitty")
    # if tiger != kitty: print("==: Tiger and Kitty are same cats")

def entry_point(argv):
    comparisons()
    return 0

def target(*args):
    return entry_point

if __name__ == "__main__":
    import sys
    entry_point(sys.argv)
