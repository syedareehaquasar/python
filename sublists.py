assignment 5
from itertools import chain , combinations
def sublist(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s,r) for r in range(len(s)+1))

from itertools import combinations

def sublists(x):
    temp = []
    subsets = []
    for i in range(1,len(x)+1):
        temp.append(list(combinations(x,i)))
    for l in temp:
        for a in l:
            subsets.append(list(a))
    return subsets

def sublist(x:[int] , k:int):
    a = []
    for i in sublists(x):
        if sum(i) == k:
            a.append(list(i))
    if len(a)==1:
        return a[0]
    return a if a else None

print(sublist([12, 1, 61, 5, 9,2],24))
print(sublists([12, 1, 61, 5, 9, 2]))