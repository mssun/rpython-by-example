class Animal(object):
    def __init__(self, name):
        self.name = name

    def greet(self):
        self.say("I'm " + self.name + ".")

    def say(self, msg): pass

class Cat(Animal):
    def say(self, msg):
        print "Meow, " + msg

class Dog(Animal):
    def say(self, msg):
        print "Wuff, " + msg

class Playground(object):
    def __init__(self, size):
        self._item = [None] * size

    def __setitem__(self, index, animal):
        self._item[index] = animal

    def __getitem__(self, index):
        return self._item[index]

def classes():
    c = Cat("Kitty")
    c.greet()           # Meow, I'm Kitty.

    d = Dog("Buddy")
    d.greet()           # Wuff, I'm Buddy.

    p = Playground(3)   # create a playground with size of 3
    p[0] = c
    p[1] = d

    p[0].greet()        # Meow, I'm Kitty.
    p[1].greet()        # Wuff, I'm Buddy.

def entry_point(argv):
    classes()
    return 0

def target(*args): return entry_point
if __name__ == "__main__": import sys; entry_point(sys.argv)
