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

part2:
Sequence must be repeated **At Least** twice
1 digit: None
2 digit: 11, 22, etc.
3 digit: 111, 222, 333... 999
4 digit: 1111 (1,1,1,1 OR 11,11)
5 digit: 11111 (1,1,1,1,1)
6 digit: 111111 (111,111 OR 11,11,11 OR 1,1,1,1,1,1)
    12,12,12
7 digit: 1111111(1,1,1,1,1,1,1)
8 digit: 11111111 (1111,1111 OR 11,11,11,11 OR 1,1,1,1,1,1,1,1)
9 digit: 111111111 (111,111,111 OR 1,1,1,1,1,1,1,1,1)
10 digit: 1111111111 (11111,11111 OR 11,11,11,11,11 OR 1,1,1,1,1,1,1,1,1,1)

If my range is 1000,9999
I know my target value has 4 digits, (factors 1, 2, 4)
Factors 2 & 4 are >= 2, so those are the repititions I should look for
Need to be careful not to double count nums (any repition of 4 is also a rep of 2)
"""

from functools import cache
from utils import c


def part1():
    print("Doubles, Quads")
    total = 0
    i = iter(get_ranges())
    n = 1
    r = next(i)
    while r:
        d = digits(n)
        num = (n*(10**d))+n
        if num >= r[0] and num <= r[1]: total += num; print(f"Invalid Id! {num}")
        elif num > r[1]: r = next(i, None); continue
        n += 1
    return total

def part2():
    total = part1()
    print("Triples")
    i = iter(get_ranges())
    r = next(i)
    n = 1
    while r:
        if n % 11 == 0: n += 1; continue
        d = digits(n)
        num = (n*(100**d)) + (n*(10**d)) + n
        if num >= r[0] and num <= r[1]: total += num; print(f"Invalid Id! {num}")
        elif num > r[1]: r = next(i, None); continue
        n += 1
    return septs(quints(total))

def quints(total):
    print("Quints")
    i = iter(get_ranges())
    r = next(i)
    n = 1
    while r:
        if n % 11 == 0: n+=1; continue
        d = digits(n)
        num = (n*(10000**d)) + (n*(1000**d)) + (n*(100**d)) + (n*(10**d)) + n
        if num >= r[0] and num <= r[1]: total += num; print(f"Invalid Id! {num}")
        elif num > r[1]: r = next(i, None); continue
        n += 1
    return total

def septs(total):
    print("Septs")
    i = iter(get_ranges())
    r = next(i)
    n = 1
    while r:
        d = digits(n)
        num = (n*(1000000**d)) + (n*(100000**d)) + (n*(10000**d)) + (n*(1000**d)) + (n*(100**d)) + (n*(10**d)) + n
        if num >= r[0] and num <= r[1]: total += num; print(f"Invalid Id! {num}")
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


def get_ranges():
    return sorted([(int(a), int(b)) for a, b in [r.split("-") for r in c()]], key=lambda x: x[0])

print(part2())
