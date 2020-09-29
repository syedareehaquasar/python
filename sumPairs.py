def sumPairs(arr : [int], givenSum : int) -> []:
    s = set()
    pairs = []
    for element in arr:
        x = givenSum - element
        if x in s:
            pairs.append((element, x))
        if min(arr.count(x), arr.count(element)) > 1:
            pairs.append((element, x))
        s.add(element)
    return pairs if pairs else "There are no such pairs"

print(sumPairs([1, 5, 7, -1], 6)) #[(5, 1), (-1, 7)]
print(sumPairs([1, 5, 7, -1, 5], 6)) #[(5, 1), (-1, 7), (5, 1)]
print(sumPairs([1, 1, 1, 1], 2)) #3! pairs of (1, 1)
print(sumPairs([1, 1, 1, 1], 6)) #no return case
print(sumPairs([1, 1, 1, 2], 2))
