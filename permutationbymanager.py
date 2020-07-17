n = int(input())
for i in range(n):
    size  = int(input())
    arr = [int(i) for i in input().split()]
    ans = []
    for e in range(len(arr)):
        if arr[e] not in ans:
            ans.append(arr[e])
    for k in ans:
        print(k, end = " ")