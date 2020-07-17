def sol(x, y, z):
    if x == y and y == z:
        return "YES\n" + str(x) + " " + str(y) + " " + str(z)
    if x == y or y == z or z == z:
        l = [x, y, z]
        l = sorted(l)
    if l[1] == l[2]:
        return "YES\n" + str(l[2]) + " " + str(l[0]) + " 1"
    return "NO"


n = int(input())
for i in range(n):
    x, y, z = map(int, input().split())
    print(sol(x, y, z))