from utils import l


def part1():
    dial = 50
    c = 0
    for line in l():
        dial = (dial + int(line[1:]) * (1 if line[0] == "R" else -1)) % 100
        if dial == 0:
            c += 1
    return c


def part2():
    dial = 50
    c = 0
    for line in l():
        rot = int(line[1:])
        c += abs(rot // 100)
        rot = (rot % 100) * (1 if line[0] == "R" else -1)
        dial = dial + rot
        if (dial <= 0 or dial > 99) and dial - rot != 0:
            c += 1
        dial = dial % 100
    return c


print(part1())
print(part2())
