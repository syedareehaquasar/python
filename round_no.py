tc = int(input())
for i in range(tc):
    x = int(input())
    s = str(x)
    if x in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        print(1)
        print(int(s))
    else:
        print(len(s) - s.count("0"))
        for _ in s:
            if int(_) != 0:
                print(10**(len(s) - (s.index(_) + 1)) * int(_), end = " ")