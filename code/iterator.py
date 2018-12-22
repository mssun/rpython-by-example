class Counter():
    c = 100

    def __iter__(self):
        return self

    def next(self):
        t = self.c
        self.c += 1
        return t

def iterator():
    l = [1, 2, 3, 4, 5]

    it = iter(l)    # return an iterator object on the list l
    print it.next() # get next item from the list

    c = Counter()

    it = c.__iter__()
    print it.next()
    print next(it)

def iterator_unsupported():
    l = [1, 2, 3, 4, 5]

    # __iter__() method for list is not supported in RPython
    it = l.__iter__()
    print it.next()

def entry_point(argv):
    iterator()
    return 0

def target(*args): return entry_point

if __name__ == "__main__":
    import sys
    entry_point(sys.argv)
    iterator_unsupported()
