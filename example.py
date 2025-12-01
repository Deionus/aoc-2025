"""Example solution (day 1, 2024) to explore util methods and file structure."""

from collections import defaultdict
from utils import l


def part1():
    a = [l.split() for l in l()]
    print(
        sum(
            [
                abs(a - b)
                for a, b in zip(
                    sorted([int(i[0]) for i in a]), sorted([int(i[1]) for i in a])
                )
            ]
        )
    )


def part2():
    a = [l.split() for l in l()]
    c1 = defaultdict(int)
    c2 = defaultdict(int)
    for i, j in a:
        c1[int(i)] += 1
        c2[int(j)] += 1
    score = 0
    for k, v in c1.items():
        score += k * v * c2[k]
    print(score)


part1()
part2()
