rows = int(input("Enter the number of rows : "))
for i in range(0, rows):
    coff = 1
    for j in range(1, rows-i):
        print("  ", end="")
    
    for k in range(0, i+1):
        print("  ", coff, end="")
        coff = int(coff * (i - k) / (k + 1))
    print()

from math import factorial

def pascal_row(row):
    return " ".join(str(factorial(row)//(factorial(i)*factorial(row-i))) for i in range(row+1))

print(pascal_row(4))