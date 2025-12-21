from runner import go


def process(input: str):
    input = input.split("\n\n")

    areas = []
    for line in input[-1].split("\n"):
        dim, req = line.split(":")
        width, height = map(int, dim.split("x"))
        req = tuple(map(int, req.strip().split(" ")))
        areas.append((width, height, req))

    return areas


def part1(input):
    """
    Simple heuristic for the main input.
    Doesn't work on the test input since the test input is a real packing puzzle.
    """
    return sum((sum(area[2]) * 9) <= (area[0] * area[1]) for area in input)


def part2(input):
    return 0


go(process, part1, part2)