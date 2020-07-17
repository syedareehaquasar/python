def IsSpecialNumber(n):
    return True if digit_fac(n) == n else False

def factorial(n):
   if n == 1:  
       return n  
   else:  
       return n*factorial(n-1)

def digit_fac(n):
    ans = 0
    while n>0:
        x = n%10
        ans += factorial(x)
        n //=10
    return ans

print(IsSpecialNumber(145))