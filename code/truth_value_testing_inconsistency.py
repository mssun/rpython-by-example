class ZeroLen():
    def __len__(self):
        return 0

class NonZero():
    def __nonzero__(self):
        return False

def truth_value_testing_inconsistency():
    zero_len = ZeroLen()
    non_zero = NonZero()

    if zero_len:
        print("zero_len is True in RPython.")     # RPython
    else:
        print("zero_len is False in Python.")     # Python

    if non_zero:
        print("non_zero is True in RPython.")     # RPtyhon
    else:
        print("non_zero is False in Python.")     # Python

def entry_point(argv):
    truth_value_testing_inconsistency()
    return 0

def target(*args):
    return entry_point

if __name__ == "__main__":
    import sys
    entry_point(sys.argv)
