from functools import cache
from utils import c
from runner import go


@cache
def digits(num):
    i = 1
    while num > 9:
        i += 1
        num = num // 10
    return i


def solve(ranges, generator, skip):
    total = 0
    n = 1
    i = iter(ranges)
    r = next(i)
    while r:
        if skip(n): n+=1; continue
        num = generator(n)
        if num >= r[0] and num <= r[1]: total += num
        elif num > r[1]: r = next(i, None); continue
        n += 1
    return total


GENERATORS = [
    (lambda n: (n*(10**digits(n)))+n, lambda _: False),
    (lambda n: (n*(100**digits(n))) + (n*(10**digits(n))) + n, lambda n: n % 11 == 0),
    (lambda n: (n*(10000**digits(n))) + (n*(1000**digits(n))) + (n*(100**digits(n))) + (n*(10**digits(n))) + n, lambda n: n % 11 == 0),
    (lambda n: (n*(1000000**digits(n))) + (n*(100000**digits(n))) + (n*(10000**digits(n))) + (n*(1000**digits(n))) + (n*(100**digits(n))) + (n*(10**digits(n))) + n, lambda _: False),
]


def process(input: str):
    return sorted([(int(a), int(b)) for a, b in [r.split("-") for r in input.split(",")]], key=lambda x: x[0])


def part1(input):
    return sum(solve(input, gen, skip) for gen, skip in GENERATORS[:1])


def part2(input):
    return sum(solve(input, gen, skip) for gen, skip in GENERATORS)


go(process, part1, part2)