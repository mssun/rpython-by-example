# -*- coding: utf-8 -*-
# The Computer Language Benchmarks Game
# http://shootout.alioth.debian.org/
#
# contributed by Antoine Pitrou
# modified by Dominique Wahli and Daniel Nanz

import math

class Node(object):
    """
    Represent nodes in a binary tree.
    """
    def __init__(self, value, left, right):
        self.value = value
        self.left = left     # left node
        self.right = right   #  right node

def make_tree(i, d):

    if d > 0:
        i2 = i + i
        d -= 1
        return Node(i, make_tree(i2 - 1, d), make_tree(i2, d))
    return Node(i, None, None)    # use Node instead of tuple


def check_tree(node):

    (i, l, r) = (node.value, node.left, node.right)
    if l is None:
        return i
    else:
        return i + check_tree(l) - check_tree(r)


def make_check(itde, make=make_tree, check=check_tree):

    i, d = itde
    return check(make(i, d))


def get_argchunks(i, d, chunksize=5000):

    assert chunksize % 2 == 0
    chunk = []
    for k in range(1, i + 1):
        chunk.extend([(k, d), (-k, d)])
        if len(chunk) == chunksize:
            yield chunk
            chunk = []
    if len(chunk) > 0:
        yield chunk


def main(n, min_depth=4):

    max_depth = max(min_depth + 2, n)
    stretch_depth = max_depth + 1

    print 'stretch tree of depth %d\t check: %d' % (
          stretch_depth, make_check((0, stretch_depth)))

    long_lived_tree = make_tree(0, max_depth)

    mmd = max_depth + min_depth
    for d in range(min_depth, stretch_depth, 2):
        i = int(math.pow(2, (mmd - d)))    # use math.pow instead of built-in pow
        cs = 0
        for argchunk in get_argchunks(i,d):    # write the sum built-in function
            s = 0
            for a in argchunk:
                s += make_check(a)
            cs += s
        print '%d\t trees of depth %d\t check: %d' % (i*2, d, cs)

    print 'long lived tree of depth %d\t check: %d' % (
          max_depth, check_tree(long_lived_tree))

if __name__ == '__main__':
    main(17)

def entry_point(argv):
    main(int(argv[1]))    # get argument from input to avoid optimization
    return 0

# add a target
def target(*args): return entry_point, None
