class Box():
    content = []

    def add(self, cat):
        self.content.append(cat)

    def __iter__(self):
        for i in self.content:
            yield i

def iterator():
    b = Box()
    b.add("Tiger")
    b.add("Kitty")

    it = b.__iter__()
    print it.next()

    for i in b:
        print i

def entry_point(argv):
    iterator()
    return 0

def target(*args): return entry_point
if __name__ == "__main__": import sys; entry_point(sys.argv)
