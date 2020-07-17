def compressString(s):
    new = ""
    for i in s:
        x = s.count(str(i))
        if x>=3:
            new += str(x) + str(i)
            s = s.strip(str(i))
    return new

def compressString(s):
    new = ""
    for i in groupstring(s):
        if len(i) >2:
            new+= str(len(group)) + group[0]
        else:
            new += group[0]*len(group)
    return new
    
def groupstring(s):
    groups = []
    for k,g in itertools.groupby(s):
        groups.append(list(g))
    return groups

print(compressString("AAAABBBCCDAA"))