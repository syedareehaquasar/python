def sp(s : str) -> [str]:
    ans = []
    paranthesis = 0
    for i in list(s.split("(")):
        if i == "":
            paranthesis += 1
    ans.append("(" * paranthesis + ")" * paranthesis)
    return ans

print(sp("((()))(())()()(()())"))