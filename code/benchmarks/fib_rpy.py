def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def main(n):
    ret = fib(n)
    print ret

def target(*args):
    return entry_point, None

def entry_point(argv):
    main(int(argv[1]))
    return 0
