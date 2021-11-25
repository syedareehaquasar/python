class Solution:
    def isThree(self, n: int) -> bool:
        divisors = 2
        for i in range(2, int(n**0.5) + 1):
            # print(i)
            if divisors > 3:
                return False
            if n % i == 0:
                # print("incrementing", divisors)
                divisors += 1
            if n % (n//i) == 0 and (n//i) != i:
                divisors += 1
        if divisors == 3:
                return True
        return False
        
