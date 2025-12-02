import sys


def o():
    text = open(f"inputs/{sys.argv[0][:-3]}.txt", "r").read()
    return text


def l():
    return o().split("\n")


def c():
    return o().split(",")
