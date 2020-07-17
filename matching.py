# def matches(s1, s2):
#     match = 0
#     x = len(s1)
#     y = len(s2)
#     if x<=y:
#         for i in range(x):
#             if s1[i] == s2[i]:
#                 match+=1
#     else:
#         for i in range(y):
#             if s2[i] == s1[i]:
#                 match += 1
#     return match

#...........................................................................................
def match(s1,s2):
    return sum(int(a==b) for a,b in zip(s1,s2))

#...........................................................................................
print(match("HELLO","OLLEH"))