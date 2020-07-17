def roman(x: str) -> int:
    roman_symbol = {'I': 1, 'V': 5, 'X': 10, 'IV': 4, 'IX': 9, 'L': 50,
                    'C': 100, 'D': 500, 'M': 1000, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
    ans = 0
    for i in range(len(x)):
        if x[i:i+2] in roman_symbol:
            ans += roman_symbol[x[i:i+2]]
        else:
            ans += roman_symbol[x[i]]
    return ans


print(roman("III"))
