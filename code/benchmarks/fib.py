def fib(n):
    if n == 0 or n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

def main():
    fib(40)

if __name__ == '__main__':
    main()
