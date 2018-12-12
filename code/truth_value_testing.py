def truth_value_testing():

    if None  or \
       False or \
       0     or \
       0L    or \
       0.0   or \
       ''    or \
       ()    or \
       []    or \
       {}:
        print("Some values are True.")
    else:
        print("None, False, 0, 0L, 0.0, '', (), [], {} are considered False.")

def entry_point(argv):
    truth_value_testing()
    return 0

def target(*args):
    return entry_point

if __name__ == "__main__":
    import sys
    entry_point(sys.argv)
