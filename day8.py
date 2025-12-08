from math import sqrt
from runner import go


def process(input: str):
    return [(int(a), int(b), int(c)) for a, b, c in [l.split(",") for l in input.split("\n")]]


def part1(input):
    distances = []
    for i in range(len(input)-1):
        for j in range(i+1, len(input)):
            a = input[i]
            b = input[j]
            dist = sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)
            distances.append((dist, i, j))
    distances.sort(key=lambda x: x[0])

    boxes = {}

    i = iter(distances)
    for _ in range(1000):
        _, a, b = next(i)

        a_circ = boxes.get(a)
        b_circ = boxes.get(b)

        if a_circ and b_circ and a_circ == b_circ:
            continue

        if a_circ and b_circ:
            # Both boxes are on a circuit already
            new_circ = a_circ.union(b_circ)
            for u in new_circ:
                boxes[u] = new_circ
        elif a_circ:
            # only box a is on a circuit
            boxes[a].add(b)
            boxes[b] = boxes[a]
        elif b_circ:
            # only box b is on a circuit
            boxes[b].add(a)
            boxes[a] = boxes[b]
        else:
            # neither box as a circuit
            new_circ = {a, b}
            boxes[a] = new_circ
            boxes[b] = new_circ

    lengths = []
    seen = set()
    for circuit in list(boxes.values()):
        if seen - circuit == seen:
            lengths.append(len(circuit))
            seen = seen.union(circuit)

    lengths.sort(reverse=True)
    return lengths[0] * lengths[1] * lengths[2]


def part2(input):
    distances = []
    for i in range(len(input)-1):
        for j in range(i+1, len(input)):
            a = input[i]
            b = input[j]
            dist = sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2 + (a[2]-b[2])**2)
            distances.append((dist, i, j))
    distances.sort(key=lambda x: x[0])

    boxes = {}

    for _, a, b in distances:
        a_circ = boxes.get(a)
        b_circ = boxes.get(b)

        if a_circ and b_circ and a_circ == b_circ:
            continue
        
        if a_circ and b_circ:
            # Both boxes are on a circuit already
            new_circ = a_circ.union(b_circ)
            for u in new_circ:
                boxes[u] = new_circ
        elif a_circ:
            # only box a is on a circuit
            boxes[a].add(b)
            boxes[b] = boxes[a]
        elif b_circ:
            # only box b is on a circuit
            boxes[b].add(a)
            boxes[a] = boxes[b]
        else:
            # neither box as a circuit
            new_circ = {a, b}
            boxes[a] = new_circ
            boxes[b] = new_circ

        if len(boxes[a]) == len(input):
            return input[a][0] * input[b][0]


go(process, part1, part2)