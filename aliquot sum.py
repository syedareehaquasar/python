# def aliquotSum(n : int):
#         return sum(factors(n))

# def factors(n : int):
#     return [x for x in range(1,n) if n%x == 0]

# def factor4p(n):
#     return " , ".join([str(ele) for ele in factors(n)])

# def classify(n:int):
#     if aliquotSum(n)<n:
#         return "Alpha" + " (Factor of " + str(n) + " are " + str(factor4p(n)) + " and sum of them is equals to " + str(aliquotSum(n))
#     elif aliquotSum(n) == n:
#         return "Gamma" " (Factor of " + str(n) + " are " + str(factor4p(n)) + " and sum of them is equals to " + str(aliquotSum(n))
#     else:
#         return "Beta" " (Factor of " + str(n) + " are " + str(factor4p(n)) + " and sum of them is equals to " + str(aliquotSum(n))
# print(classify(0))

#...................................................................................................................................


#...........................................................................................
# def aliquotSum(n):
#     sums = 0
#     for i in range(1,n):
#         if n%i == 0:
#             sums += i
#     return sums

# def classify(n):
#     d = aliquotSum(n)
#     if d<n:
#         return "Alpha"
#     elif d>n:
#         return "Beta"
#     else:
#         return "Gamma"
        
# print(classify(6))
#.....................................................................................................................

# def aliquotSum(n : int):
#         return sum(factors(n))

# def factors(n : int):
#     return [x for x in range(1,n) if n%x == 0]

# def factor4p(n):
#     return " , ".join([str(ele) for ele in factors(n)])
    
# def classify(n:int):
#     if aliquotSum(n)<n:
#         return "Alpha" + " (Factor of " + str(n) + " are " + str(factor4p(n)) + " and sum of them is equals to " + str(aliquotSum(n))
#     elif aliquotSum(n) == n:
#         return "Gamma" " (Factor of " + str(n) + " are " + str(factor4p(n)) + " and sum of them is equals to " + str(aliquotSum(n))
#     else:
#         return "Beta" " (Factor of " + str(n) + " are " + str(factor4p(n)) + " and sum of them is equals to " + str(aliquotSum(n))
# print(classify(0))