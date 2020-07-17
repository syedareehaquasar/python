upto20 = ["" , "one " , "two " , "three ","four ","five ","six ","seven ","eight ","nine ","ten ","eleven ","twelve ","thirteen ","fourteen ","fifteen ","sixteen ","seventeen ","eighteen ","nineteen "]
tens = ["","","twenty ","thirty ","fourty ","fifty ","sixty ","seventy ","eighty ","ninety "]
international = ["","","","hundred ","thousand ","ten thousand ","million ","billion ","trillion "]
indian = ["","","","hundred ", "thousand ","ten thousands ","lakh ","ten lakhs ","crores ","arab "]
# which_to_use = {2:tens}

def fig2words(n: int) -> str:
    if n == 0:
        return "Zero"
    if n <= len(upto20):
        return upto20[n]
    if n<100:
        return tens[n//10] + upto20[n%10]
    i = len(str(n))
    return fix_and((upto20[n//10**(i-1)] + indian[i] + upto20[n%(10**i-1)]),i)

def fix_and(s:str,n:int) -> str:
    if indian[n] in s and not s.endswith(indian[n]):
        return s.replace(indian[n],indian[n] + "and ")
    return s
    
print(fig2words(1000))