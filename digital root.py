def digital_root(n):
    new = n
    # while n%10 == 0 or n%10 == 1 or n%10 == 2 or n%10 == 3 or n%10 == 4 or n%10 == 5 or n%10 == 6 or n%10 == 7 or n%10 == 8 or n%10 == 9:
    while digits(n) != 1:
        new = add_num(n)
        n = new
    return new

def add_num(n):
    new = 0
    while n>0:
        a = n%10
        new += a
        n//=10
    return new
            
def digits(n):
    digit = 0
    while n > 0:
        digit += 1
        n//=10
    return digit

print(digital_root(45893))