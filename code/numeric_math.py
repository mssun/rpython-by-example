import math

def numeric_math():
    print math.exp(1e-5) - 1
    print math.pi
    print math.log(10)
    print math.floor(1.5)
    print math.sqrt(2)

def entry_point(argv):
    numeric_math()
    return 0

def target(*args): return entry_point
if __name__ == "__main__": import sys; entry_point(sys.argv)
