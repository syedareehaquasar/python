def aliquot(n: int) -> int:
    aliq = 1
    for factor in range(2, n):
        if n % factor == 0:
            aliq += factor
    return aliq

def aliquot2(n: int) -> int:
    aliq = 1
    factor = 2
    while factor * factor < n:
        if n % factor == 0:
            aliq += factor + n//factor
        factor += 1
    if n % factor == 0:
        aliq += factor
    return aliq


def amicables(limit: int) -> [int]:
    amicable_pairs = []
    for a in range(1, limit):
        for b in range(a+1, limit):
            if aliquot(a) == b and aliquot(b) == a:
                amicable_pairs.append((a, b))
    return amicable_pairs

import datetime
now = datetime.datetime.now
for i in range(1, 100000, 5000):
    for n in range(2, i):
        aliq = aliquot(n)
    print(now(), i)

for i in range(1, 100000, 5000):
    for n in range(2, i):
        aliq = aliquot2(n)
    print(now(), i)



