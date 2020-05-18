armstrong number
def number_of_digits(x):
    digits = 0
    while x>0:
        digits +=1
        x //=10
    return digits

def is_armstrong(x):
    n = x
    new_num = 0
    digits = number_of_digits(x)
    while n>0:
        a = n % 10
        new_num += a**digits
        n //= 10
    return new_num == x
n = 22 
# while n%10 == 1 or n%10 == 2:
#     n+=7
# print(n)
new = 0
while n>0:
            a = n%10
            new += a
            n//=10
print(new)
# def armstrong_series(a,b):
#     return i for i in range (a,b) if is_armstrong(i):


x = int(input())
print(armstrong_series(x))
start = int(input())
limit = int(input())
def armstrong_series(a : int , b : int) -> int:
    return [i for i in range(a,b) if is_armstrong(i) ]

def is_armstrong(x):
    return x

print(armstrong_series(start,limit))