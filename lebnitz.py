# import sys
def change_sign(sign: int) -> int:
    return -1 * sign

def sum_leibniz(n_terms: int) -> float:
    sign = 1
    quarterPi = 0
    for denominator in range(1, 2 * n_terms, 2):
        quarterPi += sign * (1/denominator)
        sign = change_sign(sign)
    return quarterPi

# .......................................................................................................

# N = int(sys.argv[1])
N = int(input())
pi = 3.141592653589793
print("Accuracy = ", abs(pi/4 - sum_leibniz(N)))