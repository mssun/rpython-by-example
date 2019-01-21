# -*- coding: utf-8 -*-
# The Computer Language Benchmarks Game
# http://shootout.alioth.debian.org/
# Contributed by Sebastien Loisel
# Fixed by Isaac Gouy
# Sped up by Josh Goldfoot
# Dirtily sped up by Simon Descarpentries
# Concurrency by Jason Stitt

def eval_A (i, j):
    return 1.0 / ((i + j) * (i + j + 1) / 2 + i + 1)

def eval_A_times_u (u):
    args = []
    for i in range(len(u)):
        args.append((i, u))
    ret = []
    for i in args:
        ret.append(part_A_times_u(i))
    return ret

def eval_At_times_u (u):
    args = []
    for i in range(len(u)):
        args.append((i, u))
    ret = []
    for i in args:
        tmp = part_At_times_u(i)
        ret.append(tmp)
    return ret

def eval_AtA_times_u (u):
    return eval_At_times_u (eval_A_times_u (u))

def part_A_times_u((i,u)):
    partial_sum = 0
    for j, u_j in enumerate(u):
        partial_sum += eval_A (i, j) * u_j
    return partial_sum

def part_At_times_u((i,u)):
    partial_sum = 0
    for j, u_j in enumerate(u):
        partial_sum += eval_A (j, i) * u_j
    return partial_sum

DEFAULT_N = 130

def main(n):
    for i in range(n):
        v = []
        u = [1] * DEFAULT_N

        for dummy in xrange (10):
            v = eval_AtA_times_u (u)
            u = eval_AtA_times_u (v)

        vBv = vv = 0

        l = 0
        if len(u) > len(v): l = len(u)
        else: l = len(v)
        for i in range(l):
            vBv += u[i] * v[i]
            vv  += v[i] * v[i]
        print vBv, vv

if __name__ == "__main__":
    main(400)

def entry_point(argv):
    main(int(argv[1]))
    return 0

def target(*args):
    return entry_point, None
