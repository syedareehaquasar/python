# from math import factorial
# def zeros(n:int) -> int:
#     x = factorial(n)
#     zero = 0
#     while x > 0:
#         s = x % 10
#         if s == 0:
#             zero += 1
#         else:
#             return zero
#         x //= 10

# def factorial(n):
#     if( n == 1):
#         return n
#     else:
#         return n*factorial(n-1)
# x = int(input('Enter the number whose factorial is required: '))
# if( x <0):
#     print('Enter a positive number')
# elif(x == 0):
#     print('Factorial is 1 ')
# else:
#     print('Factorial is : ' + str(factorial(x)))


from math import factorial
def zeros(x : str) -> int:
    return str(factorial(x)).count('0')

print(factorial(17))
print(zeros(17))