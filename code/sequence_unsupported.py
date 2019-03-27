# Operations which are not supported by RPython.
def sequence_unsupported():
    l = ["this", "is", "a", "list", "of", "strings"]

    print "slice of l from 3rd to end:", l[2:-1]
    # s[i:j:k]: slice of s from i to j with step k
    print "slice of l from 1st to 4th with 2 steps:", l[0:5:2]

    # min(s): smallest item of s
    list_number = [1, 2, 3]
    print "smallest item of s", min(list_number)

    # max(s): largest item of s
    print "largest item of s", max(list_number)

def entry_point(argv):
    sequence_unsupported()
    return 0

def target(*args): return entry_point
if __name__ == "__main__": import sys; entry_point(sys.argv)
