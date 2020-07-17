# x = int(input())
# lst = []
# fair = []
# for i in range(x):
#     arr = [int(i) for i in input().split()]
#     fair.append(arr)

# def is_possible(x:[int]):
#     for j in range((x[1]-x[2]),(x[1]+x[2])+1):
#         if x[0]*j >= (x[3]-x[4]) and x[0]*j <= (x[3]+x[4]):
#             return "Yes"
#     return "No"
#     # return "Yes" if (x[0]*(x[1]-x[2])) >= (x[3]-x[4]) and (x[0]*(x[1]-x[2])) <= (x[3]+x[4]) or (x[0]*(x[1]+x[2])) >= (x[3]-x[4]) and (x[0]*(x[1]+x[2])) <= (x[3]+x[4]) else "No"

# for j in fair:
#     print(is_possible(j))

def expand(num:int) -> str:
    ans = ""
    n = int(str(num)[::-1])
    while n > 0:
        ans += str((n%10) * (10**(len(str(n)) - 1)))
        if len(str(n)) != 1:
            ans += " + "
        n //= 10
    return ans

print(expand(13))



