import copy
import time
from runner import go


def process(input: str):
    return input.split("\n")


def part1(input):
    machines = []
    for l in input:
        tokens = l.split(" ")
        indicator = tokens[0]
        buttons = tokens[1:-1]
        machines.append((indicator, buttons))

    total = 0
    for machine in machines:
        print(f"Machine {machine}")
        indicator, buttons = machine
        target = 0
        for c in reversed(indicator[1:-1]): # Reverse to make the first button the lsb
            target = (target << 1) + (c == "#")


        print(bin(target))
        seen = {0}
        gen = 0
        found = False
        while not found:
            n = set()
            for state in seen:
                for button in buttons:
                    mask = 0
                    print(button)
                    for b in button[1:-1].split(","):
                        mask |= 1 << int(b)
                    new_state = state ^ mask
                    print(bin(mask), bin(new_state))
                    if new_state == target:
                        print(bin(target), bin(new_state))
                        found = True; 
                        break
                    n.add(new_state)
                    # time.sleep(1)
                if found: break
            seen = n
            gen += 1
           

        print(f"Found in {gen} presses")
        total += gen
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