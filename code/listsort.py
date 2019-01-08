from rpython.rlib.listsort import TimSort

def listsort():
    lst = [10, 1, 9, 2, 8, 3, 7, 4, 5, 6]
    TimSort(lst).sort()
    print lst

def entry_point(argv):
    listsort()
    return 0

def target(*args): return entry_point
