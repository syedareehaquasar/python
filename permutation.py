from itertools import permutations
perm = permutations(['a','b' ,'c' ]) 
for i in list(perm):
    print("".join(i))