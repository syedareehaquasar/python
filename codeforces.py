def solution(a, b):
    if a == b:
        return "Yes"
    elif sorted(a) != sorted(b):
        return "No"
    elif sorted(a) != sorted(b): 
        x = 1
        while x <= len(a)//2:
            a[:x], a[:len(a)-x] = a[:len(a)-x], a[:x]
            if a == b :
                return "Yes"
            x += 1
    return "No"

tc = int(input())
for i in range(tc):
    size = int(input())
    a = [int(x) for x in input().split()]
    b = [int(x) for x in input().split()]
    print(solution(a, b))
