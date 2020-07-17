...........................................................................................

# def sum_of_holes(limit):
#     # if limit % 10 == 0:
#     #     return (limit//10)*6
#     return sum(holes(x) for x in range(limit+1))
    
# def holes(x):
#     if x in [0,4,6,9]:
#         return 1
#     elif x == 8:
#         return 2
#     elif x in [1,2,3,5,7]:
#         return 0
#     ans,n = 0,0
#     while x!=0:
#         n = x % 10
#         ans += holes(n)
#         x //= 10
#     return ans

print(sum_of_holes(14))
print(holes(14))

def sum_of_holes(limit):
    # if limit % 10 == 0:
    #     return (limit//10)*6
    return sum(holes(x) for x in range(limit))
    
def holes(x):
    if x in [0,4,6,9]:
        return 1
    elif x == 8:
        return 2
    ans,n = 0,0
    while x!=0:
        n = x % 10
        ans += holes(n)
        x //= 10
    return ans

print(sum_of_holes(14))