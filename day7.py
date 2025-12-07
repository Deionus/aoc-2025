import collections
from runner import go


def process(input: str):
    return input.split("\n")


def part1(input):
    beams = {input[0].index("S")}
    splits = 0
    for line in input[1:-1]:
        new = [{b-1, b+1} if line[b] == "^" else {b} for b in beams]
        splits += sum(len(n) > 1 for n in new)
        beams = set().union(*new)
    return splits


def part2(input):
    beams = collections.defaultdict(int, {input[0].index("S"): 1})
    for line in input[1:-1]:
        for b in list(beams.keys()):
            if line[b] == "^":
                beams[b-1] += beams[b]
                beams[b+1] += beams[b]
                beams[b] = 0
    return sum(beams.values())


go(process, part1, part2)