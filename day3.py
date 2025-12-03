"""
Turn on TWO BATTERIES in each bank
1234
2 AND 4 on makes 24 Joltage
"""

from utils import l

banks = [int(a) for a in l()]
total = 0
for bank in banks:
    num = bank
    ones_place = num % 10
    num = num // 10
    tens_place = num % 10
    num = num // 10

    while num > 0:
        v = num % 10
        if v >= tens_place:
            if tens_place > ones_place:
                ones_place = tens_place
            tens_place = v
        num = num // 10
    
    n = (tens_place*10) + ones_place
    print(n)
    total += n

print(total)
