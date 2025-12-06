from runner import go


def calculate(volts, batteries):
    left = 0
    q = []
    for p in range(len(volts)-batteries, len(volts)):
        if left == p: q.extend(volts[left:]); break
        q.append(max(volts[left:p+1]))
        left += volts[left:p+1].index(q[-1]) + 1
    return int("".join(str(i) for i in q))


def process(input):
    return [[int(i) for i in list(a)] for a in input.split("\n")]


def part1(input):
    return sum(calculate(volts, 2) for volts in input)


def part2(input):
    return sum(calculate(volts, 12) for volts in input)


go(process, part1, part2)