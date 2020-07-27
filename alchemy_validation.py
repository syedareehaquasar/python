def sol(n, seq):
    if  abs(seq.count("A") - seq.count("B")) != 1:
        return "N"
    return "Y"


tc = int(input())
_ = tc + 1
f = open("c.txt", 'w')
while tc > 0:
    n = int(input())
    seq = input()
    f.write("Case #" + str(_ - tc) + ": " + sol(n, seq) + "\n")
    print("Case #" + str(_ - tc) + ": " + sol(n, seq))
    tc -= 1

f.close()