# ASSIGNMENT 4 (Q1)
from itertools import permutations
def circular_prime(x) -> bool:
    perm = permutations(list(str(x)))
    for i in list(perm):
        z = ("".join(i))
        if not is_prime(int(z)):
            return False
    return True

def circular_prime(n) -> bool:
    num = n
    c = digits(n)
    while is_prime(num):
        rem = num%10
        div = num // 10
        num = (int)(((10**(c-1))* rem)+ div)
        if num == n:
            return True
    return False

def circular(x):
    n = str(x)
    while (is_prime(int(n))):
        n = n[1:] + n[0]
        if n == str(x):
            return True
    return False

def circular_numbers(x):
    s = []
    n = str(x)
    while (is_prime(int(n))):
        n = n[1:] + n[0]
        s.append(int(n))
        if n == str(x):
            return s
    return s

def is_circular(x) -> bool:
    s = circular_numbers(str(x))
    for i in s:
        if not is_prime(i) or s == []:
            return False
    return True

def digits(n:int):
    return len(str(n))



def isCircularPrime(num):
    n = str(num)
    if len(n) == 1:
        return False
    while (is_prime(int(n))):
        n = n[1:] + n[0]
        if n == str(num):
            return True
    return False

    
def isCircularPrime(n):
    num = n
    c = digits(n)
    while (is_prime(int(num))):
        rem = num % 10
        div = num // 10
        num = (int)(((10**(c-1))* rem)+ div)
        if num == n:
            return True
    return False

def digits(n:int):
    return len(str(n))

print(isCircularPrime(197))
perm = permutations(list(str(197)))
for i in list(perm):
    print("".join(i) if is_prime(int("".join(i))) else "*")
print(circular_prime(918))
print(circular(918))
print(circular_numbers(918))
print(is_circular(918))



# def make_cirular(x):
#     s = str(x)
#     for i in range(len(s)):
#         yield int(s[i:] + s[:i])

# def h(x):
#     return any([d in "024568" for d in str(x)] )

# print(h(23))

# print(make_cirular(178))