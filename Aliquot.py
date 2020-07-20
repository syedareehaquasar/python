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


def amicables(limit: int) -> [int]:             #O(n * O(f)) + O(n)
    amicable_pairs = [] #O(1)
    for a in range(1, limit):      #O(n)
        for b in range(a+1, limit):           #O(n)
            if aliquot(a) == b and aliquot(b) == a:      #O(n + n)
                amicable_pairs.append((a, b))       #O(1)
    return amicable_pairs        #O(1)

def amicable2(limit : int, f) -> [int]:       #O(n^2)
    amicable_pairs = []    #O(1)
    for a in range(1, limit):
        b = f(a)
        if b > a:    #O(n)
            if a == f(b):
                amicable_pairs.append((a, b))    #O(1)
        return amicable_pairs     #O(1)


# def amicable3(limit : int, f) -> [int]: #O(n * O(f))
#     amicable_pairs = []
#     aliqs = {}
#     for a in range(1, limit):
#         aliqs[a] = f(a)

#     # for n in range(1, limit):
#     #     m = aliqs[n]
#     #     if n < m:
#     #         if m in aliqs:
#     #             if n == aliqs[m]:
#     #                 amicable_pairs.append((n, m))

#     return amicable_pairs

def iamamicables(limit, f):
    amicable_pairs = []
    aliqs = {}
    for a in range(1, limit):
        aliqs[a] = f(a)
    return [(n, aliqs[n]) for n in aliqs if aliqs[n] in aliqs and aliqs[aliqs[n]] == n and n != aliqs[n] ]
    # for m in aliqs.values():
    #     if m in aliqs:
    #         n = aliqs[m]
    #         if n == m:


    
print(iamamicables(1000, aliquot2))
# import datetime
# now = datetime.datetime.now
# for i in range(1, 100000, 5000):
#     for n in range(2, i):
#         aliq = aliquot(n)
#     print(now(), i)

# for i in range(1, 100000, 5000):
#     for n in range(2, i):
#         aliq = aliquot2(n)
#     print(now(), i)









