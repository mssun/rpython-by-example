from rpython.rlib.objectmodel import import_from_mixin

class ActivityMixin(object):
    def eat(self, food):
        print "Eating " + food

class Animal(object):
    import_from_mixin(ActivityMixin)    # import ActivityMixin

    def __init__(self, name):
        self.name = name

    def greet(self):
        self.say("I'm " + self.name + ".")

    def say(self, msg): pass

class Cat(Animal):
    def say(self, msg):
        print "Meow, " + msg

# class Cat2(Animal, ActivityMixin):    # multiple inheritance only supported with mixin
#     pass

class Dog(Animal):
    def say(self, msg):
        print "Wuff, " + msg

def classes():
    c = Cat("Kitty")
    c.greet()           # Meow, I'm Kitty.
    c.eat("cat food")

def entry_point(argv):
    classes()
    return 0

def target(*args): return entry_point
if __name__ == "__main__": import sys; entry_point(sys.argv)
