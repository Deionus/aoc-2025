from utils import l


def part1():
    dial = 50
    c = 0
    for d, n in [(1 if l[0] == "R" else -1, int(l[1:])) for l in l()]:
        dial = (dial + n * d) % 100
        if dial == 0: c += 1
    return c


def part2():
    dial = 50
    c = 0
    for d, n in [(1 if l[0] == "R" else -1, int(l[1:])) for l in l()]:
        c += abs(n // 100)
        n = (n % 100) * d
        dial = dial + n
        if (dial <= 0 or dial > 99) and dial - n != 0: c += 1
        dial = dial % 100
    return c

print(part1())
print(part2())
