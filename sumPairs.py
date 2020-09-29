def sumPairs(arr : [int], givenSum : int) -> [(int, int)]:
    s = []
    t = []
    pairs = []
    for element in arr:
        x = givenSum - element
        if x in s:
            pairs.append((element, x))
            if arr.count(x) > 2 and arr.count(element) > 2:
                t.append(element)
        else:
            s.append(element)
    if t:
        for element in t:
            x = givenSum - element
            if x in arr:
                pairs.append((element, x))
    return pairs

print(sumPairs([1, 5, 7, -1], 6)) #[(5, 1), (-1, 7)]
print(sumPairs([1, 5, 7, -1, 5], 6)) #[(5, 1), (-1, 7), (5, 1)]
print(sumPairs([1, 1, 1, 1], 2))

