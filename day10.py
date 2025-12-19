import sys
from collections import deque
from runner import go
from scipy.optimize import linprog


def process(input: str):
    lines = input.split("\n")
    machines = []
    for l in lines:
        tokens = l.split(" ")
        indicator = tokens[0]
        buttons = tokens[1:-1]
        counter = tokens[-1]
        machines.append((indicator, buttons, counter))

    return machines


def part1(input):
    total = 0
    for indicator, buttons, _ in input:
        target = 0
        for c in reversed(indicator[1:-1]): # Reverse to make the first button the lsb
            target <<= 1
            target += c == "#"

        masks = []
        for button in buttons:
            mask = 0
            for b in button[1:-1].split(","):
                mask |= 1 << int(b)
            masks.append(mask)

        def calc():
            seen = {0}
            q = deque([(0, 0)])
            while q:
                state, presses = q.popleft()
                for mask in masks:
                    new_state = state ^ mask
                    if new_state == target: return presses+1
                    if new_state not in seen: q.append((new_state, presses+1))
                    seen.add(new_state)
            else:
                print("No solution found!")
                sys.exit()

        total += calc()
    return total


def part2(input):
    total = 0
    for _, buttons, counters in input:
        counters = list(map(int, counters[1:-1].split(",")))
        buttons = [tuple(map(int, b[1:-1].split(","))) for b in buttons]
        buttons = [[int(i in b) for i in range(len(counters))] for b in buttons]
        
        c = [1] * len(buttons) # Coefficients to minimize. So count of each button press?
        a = list(zip(*buttons)) # Linear eqs, transposed

        res = linprog(c, A_eq=a, b_eq=counters, integrality=1)
        total += res.fun

    return int(total)


go(process, part1, part2)
