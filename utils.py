import sys, collections


ADJACENT = ((-1, -1), (-1, 0), (-1, 1), (0, -1), (0,1), (1,-1), (1,0), (1,1))


def o():
    text = open(f"inputs/{sys.argv[0][:-3]}.txt", "r").read()
    return text


def l():
    return o().split("\n")


def c():
    return o().split(",")


def g():
    return [list(line) for line in l()]


def dg(default):
    a = g()
    return collections.defaultdict(default, {(i,j): a[i][j] for i in range(len(a)) for j in range(len(a[0]))})