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

from functools import cache
from utils import c


def part1():
    total = 0
    i = iter([r for r in sorted([(int(a), int(b)) for a, b in [r.split("-") for r in c()]], key=lambda x: x[0]) if not (digits(r[0]) % 2 == 1 and (digits(r[0]) == digits(r[1])))])
    n = 1
    r = next(i)
    while r:
        d = digits(n)
        num = (n*(10**d))+n
        if num >= r[0] and num <= r[1]: total += num
        elif num > r[1]: r = next(i, None); continue
        n += 1
    return total

@cache
def digits(num):
    i = 1
    while num > 9:
        i += 1
        num = num // 10
    return i


print(part1())
