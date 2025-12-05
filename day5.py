from utils import o

input = o()
a, b = input.split("\n\n")
a = a.split("\n")
b = b.split("\n")

ranges = sorted([(int(mini), int(maxi)) for mini, maxi in [i.split("-") for i in a]], key=lambda x: x[0])


def part1():
    fresh = 0
    for i in b:
        i = int(i)
        for mini, maxi in ranges:
            if mini <= i <= maxi: fresh += 1; break
    return fresh


def part2():
    new_ranges = []
    r = ranges[0]
    for i in range(1, len(ranges)):
        r2 = ranges[i]
        if r2[0] <= r[1]:
            r = (r[0], max(r2[1], r[1]))
            i += 1
        else:
            new_ranges.append(r)
            r = r2
    new_ranges.append(r)
    return sum(maxi-mini+1 for mini, maxi in new_ranges)


p1 = part1()
p2 = part2()
print(p1)
print(p2)