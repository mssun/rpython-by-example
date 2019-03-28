class B(Exception):
    pass

class C(B):
    pass

class D(C):
    pass

def exceptions():
    for cls in [B, C, D]:
        try:
            raise cls()
        except D:
            print("exception D")
        except C:
            print("exception C")
        except B:
            print("exception B")
        finally:
            print("put clean-up actions here")

def entry_point(argv):
    exceptions()
    return 0

def target(*args): return entry_point
if __name__ == "__main__": import sys; entry_point(sys.argv)
