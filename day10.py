import sys
import time
from collections import deque
from runner import go


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
    return 0

    # Too slow for the real input!
    machines = []
    for l in input:
        tokens = l.split(" ")
        joltage = tokens[-1]
        buttons = tokens[1:-1]
        machines.append((joltage, buttons))

    total = 0
    for joltage, buttons in machines:
        buttons = [b[1:-1].split(",") for b in buttons]
        print(buttons)

        joltage = list(map(int, joltage[1:-1].split(",")))
        print(joltage)

        count = [0] * len(joltage)
        print(count)

        history = set()
        seen = {tuple(count)}
        found = False
        gen = 0
        while not found:
            new_seen = set()
            for state in seen:
                if state in history: continue
                for b_set in buttons:
                    new_state = list(state)
                    for b in b_set:
                        new_state[int(b)] += 1

                    # print(state, new_state)
                    if new_state == joltage: found = True; break
                    new_seen.add(tuple(new_state))

                if found: break
            history.union(seen)
            seen = new_seen
            gen +=1
        
        total += gen

    return total


go(process, part1, part2)