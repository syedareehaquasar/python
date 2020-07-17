def solution(s : str) -> str:
    if len(s) < 3:
        return s
    return s[0] + s[1:-1:2] + s[-1] 


tc = int(input())
for i in range(tc):
    s = input()
    print(solution(s))