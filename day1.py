from itertools import accumulate
from runner import go


def process(input: str):
    return [int(l) for l in input.replace("R", "").replace("L", "-").split("\n")]


def part1(input):
    return sum(n == 0 for n in accumulate([50, *input], lambda a, b: (a+b)%100))


def part2(input):
    return sum(a[0] for a in accumulate([(sum(abs(n) // 100 for n in input), 50), *[(abs(n) % 100) * (-1 if n < 0 else 1) for n in input]], lambda a,b: ((a[1]+b <= 0 or a[1]+b > 99) and a[1] != 0, (a[1] + b) % 100)))


go(process, part1, part2)