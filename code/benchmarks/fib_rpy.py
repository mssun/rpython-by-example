def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

# n should not be a constant, otherwise RPython will optimize it
def main(n):
    ret = fib(n)
    # output the result, otherwise RPython will optimize out the above call
    # (the `transform_dead_op_vars` pass)
    print ret

def target(*args):              # we need a target function
    return entry_point, None

def entry_point(argv):
    main(int(argv[1]))          # get n from the arguments
    return 0
