from utils import l

BANKS = [[int(i) for i in list(a)] for a in l()]

def calculate(volts, batteries):
    left = 0
    q = []
    for p in range(len(volts)-batteries, len(volts)):
        if left == p: q.extend(volts[left:]); break
        q.append(max(volts[left:p+1]))
        left += volts[left:p+1].index(q[-1]) + 1
    return int("".join(str(i) for i in q))

print(sum(calculate(volts, 2) for volts in BANKS))
print(sum(calculate(volts, 12) for volts in BANKS))
