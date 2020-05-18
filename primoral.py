def getPrimoral(number):
    result = 1
    for x in pnum(number):
        result *= x
    return result
        
def is_prime(n):
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

def pnum(n):
    p = 0
    x = 2
    num = []
    while p != n:
        if is_prime(x):
            p += 1
            num.append(x)
        x += 1
    return num

print(getPrimoral(3))
print(is_prime(4))
print(pnum(3))