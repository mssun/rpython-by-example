def rfile():
    with open ("file.py", "r") as f:
        c = f.read(10)
    for line in c.split("\n"):
        print line

    f = open("file.py", "r") # open a file
    c = f.readline()         # read one entire line from the file
    print f.tell()           # return the file's current position
    print f.fileno()         # return the integer "file descriptor"
    print f.isatty()         # return True if the file is connected to a tty(-like) device
    f.close()                # close a file

def entry_point(argv):
    rfile()
    return 0

def target(*args): return entry_point
if __name__ == "__main__": import sys; entry_point(sys.argv)
