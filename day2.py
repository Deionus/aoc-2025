"""
Invalid IDs are IDs with 2 repeated parts
55 = 5 & 5
6464 = 64 & 64
123123 = 123 & 123

Find all the IDs in the ranges and add them up
1 digit: None
2 digit: 11, 22, 33... 99
3 digit: None
4 digit: 1010, 1111, 1212, 1313, etc.
5 digit: none
6 digit: 100100, 101101, etc.
"""

from utils import c


def part1():
    ranges = [r.split("-") for r in c()]
    total = 0
    for min, max in ranges:
        for i in range(int(min), int(max) + 1):
            d = digits(i)
            if d % 2 == 1:
                continue

            right = i // (10 ** (d / 2))
            left = i % (10 ** (d / 2))

            if right == left:
                total += i

    return total


def digits(num):
    i = 1
    while num > 9:
        i += 1
        num = num // 10
    return i


print(part1())
