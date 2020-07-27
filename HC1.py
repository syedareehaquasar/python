def sol(n, i, o):
    

tc = int(input())
_ = tc + 1
while tc > 0:
    n = int(input())
    i = input()
    o = input()
    print("Case #" + (_ - tc) + ": " sol(n, i, o))