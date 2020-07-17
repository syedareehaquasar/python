limit = 10

def pick10(s: str, n: int) -> str:
    ans = ""
    i = 0
    while len(ans) != limit:
        ans += s[n]
        i += 1
        n += i
        if n >= len(s):
            s = s+s
    return ans

print(pick10("ABC",1))
