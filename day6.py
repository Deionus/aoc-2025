from runner import go

def process(input: str):
    lines = input.split("\n")
    return lines

def part1(input):
    ops = [l for l in input[-1].split(" ") if len(l) > 0]
    nums = [l.split(" ") for l in input[:-1]]
    nums = [[int(n) for n in l if len(n) > 0] for l in nums]
    grand_total = 0
    for i in range(len(ops)):
        op = ops[i]
        total = 0 if op == "+" else 1
        for l in nums:
            if op == "+":
                total += l[i]
            else:
                total *= l[i]

        grand_total += total
    return grand_total

def part2(input):
    grand_total = 0
    col = len(input[0])-1
    nums = []
    while col > -1:
        num = ""
        for l in input[:-1]:
            num += l[col]

        num = num.strip().replace(" ", "0")
        if num:
            n = int(num)
            if n:
                nums.append(n)

        if input[-1][col] in ["*", "+"]:
            op = input[-1][col]
            total = 0 if op == "+" else 1
            for num in nums:
                if op == "+":
                    total += num
                else:
                    total *= num
            grand_total += total
            nums = []

        col -= 1

    return grand_total

go(process, part1, part2)