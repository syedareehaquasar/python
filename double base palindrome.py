
double base q2
def is_palindrome(x:int) -> bool:
    return True if str(x)[::-1] == str(x) else False

# def binary(x):

def binary(n):  
    x = bin(n).replace("0b", "")
    return True if is_palindrome(x) else False

def isDoubleBasePalindrome(n):
    return True if is_palindrome(n) and binary(n) else False

# def DecimalToBinary1(num): 
#     if num > 1: 
#         DecimalToBinary1(num // 2) 
#     print(num % 2, end = '') 

print(isDoubleBasePalindrome(585))