# def is_prime(n:int)->bool:
#     if n == 1:
#         return False
#     if n in {2,3,5,7}:
#         return True
#     elif n%2 == 0:
#         return False
#     else:
#         r=3
#         while r*r <=n:
#             if n%r==0:
#                 return False
#             r += 2
#         return True

def isPrime(n):
    if n <2:
        return False
    if n in {2,3,5,7}:
        return True
    elif n%2 == 0 or n%3==0:
        return False
    else:
        r = 5
        while r*r <=n:
            if n%r == 0:
                return False
            r += 2
            if n%r == 0:
                return False
            r += 4
        return True

def twinPrimes(start, limit):
    if start<1 or limit<1:
        return -1
    elif start >= limit:
        return -2
    Primes = []
    for x in range(start,limit):
        if isPrime(x):
            s = x+1
            while not isPrime(s) and x<limit:
                s += 1
            t = (x,s)
            if s < limit and (s-x) == 2:
                Primes.append(t)
    return Primes if Primes else -3

print(twinPrimes(1,20))
