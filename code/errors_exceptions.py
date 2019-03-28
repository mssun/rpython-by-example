def exceptions(x, y):
    try:
        n = x / y
    except ZeroDivisionError:
        print "division by zero"

def entry_point(argv):
    exceptions(int(argv[1]), int(argv[2]))
    return 0

def target(*args): return entry_point
if __name__ == "__main__": import sys; entry_point(sys.argv)
