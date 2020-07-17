def solution(arr, n):
    even, odd, wo, we = 0, 0, 0, 0
    for i in range(n):
        if i % 2 == 0:
            if arr[i] % 2 == 0:
                even += 1
            else:
                we += 1
        else:
            if arr[i] % 2 == 0:
                wo += 1
            else:
                odd += 1
    if n % 2 == 0:
        if we + odd == wo + even:
            return we
        return -1
    else:
        if we + odd + 1 == wo + even:
            return wo
        return -1


tc = int(input())
for i in range(tc):
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(solution(arr, n))
    

