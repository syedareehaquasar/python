from itertools import chain, combinations
 
 
def div_Subsets(a, x):
    ans = 0
    for e in chain.from_iterable(combinations(a, r) for r in range(len(a)+1)):
        if sum(e) % x != 0:
            if len(e) > ans:
                ans = len(e)
    if ans == 0:
        return -1
    return ans
 
 
tc = int(input())
 
for t in range(tc):
    a, x = [int(x) for x in input().split()]
    ele = [int(e) for e in input().split()]
    print(div_Subsets(ele, x))
