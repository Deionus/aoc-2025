from runner import go

def process(input: str):
    return input.split("\n")

def part1(input):
    return sum(eval(p[-1].join(p[:-1])) for p in zip(*[[i for i in l.split(" ") if i] for l in input]))

def part2(input):
    return sum([eval(p[0].replace(":", p[1])) for p in zip(":".join(["".join(a).strip() for a in zip(*input[:-1])]).split("::"), [op for op in input[-1].split(" ") if op])])

go(process, part1, part2)