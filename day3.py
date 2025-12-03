"""
Turn on TWO BATTERIES in each bank
1234
2 AND 4 on makes 24 Joltage
"""

from utils import l

banks = [int(a) for a in l()]
total = 0
for bank in banks:
    volts = []
    while bank > 0:
        volts.insert(0, bank % 10)
        bank = bank // 10
    
    left = 0
    q = []
    for p in range(len(volts)-12, len(volts)):
        if left == p:
            q.append(volts[left])
            left += 1
            continue
        m = max(volts[left:p+1])
        i = left + volts[left:p+1].index(m)
        q.append(m)
        left = i+1

    n = 0
    q.reverse()
    for i in range(12):
        n += q[i] * (10**i)
    total += n

print(total)
