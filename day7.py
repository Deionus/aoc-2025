import collections
from runner import go


def process(input: str):
    return input.split("\n")


def part1(input):
    beams = {input[0].index("S")}
    splits = 0
    for line in input[1:-1]:
        to_add = set()
        for b in beams:
            if line[b] == "^":
                to_add.add(b-1)
                to_add.add(b+1)
                splits += 1
            else:
                to_add.add(b)
        beams = to_add
    return splits


def part2(input):
    beams = collections.defaultdict(int)
    beams[input[0].index("S")] = 1 
    for line in input[1:-1]:
        for b in list(beams.keys()):
            if line[b] == "^":
                v = beams[b]
                beams[b-1] += v
                beams[b+1] += v
                beams[b] = 0
    return sum(beams.values())


go(process, part1, part2)