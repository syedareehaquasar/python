def sumPairs(arr : [int], givenSum : int) -> [(int, int)]:
    s = set()
    pairs = []
    for element in arr:
        x = givenSum - element
        if x in s:
            pairs.append((element, x))
        s.add(element)
    return pairs

print(sumPairs([1, 5, 7, -1], 6))
print(sumPairs([1, 5, 7, -1, 5], 6))
print(sumPairs([1, 1, 1, 1], 2))
