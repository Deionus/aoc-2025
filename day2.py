from functools import cache
from utils import c

RANGES = sorted([(int(a), int(b)) for a, b in [r.split("-") for r in c()]], key=lambda x: x[0])
def solve(generator, skip):
    total = 0
    n = 1
    i = iter(RANGES)
    r = next(i)
    while r:
        if skip(n): n+=1; continue
        num = generator(n)
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

totals = [
    solve(gen, skip) for gen, skip in 
    [
        (lambda n: (n*(10**digits(n)))+n, lambda _: False),
        (lambda n: (n*(100**digits(n))) + (n*(10**digits(n))) + n, lambda n: n % 11 == 0),
        (lambda n: (n*(10000**digits(n))) + (n*(1000**digits(n))) + (n*(100**digits(n))) + (n*(10**digits(n))) + n, lambda n: n % 11 == 0),
        (lambda n: (n*(1000000**digits(n))) + (n*(100000**digits(n))) + (n*(10000**digits(n))) + (n*(1000**digits(n))) + (n*(100**digits(n))) + (n*(10**digits(n))) + n, lambda _: False),
    ]
]

part1 = totals[0]
part2 = sum(totals)
print(part1)
print(part2)