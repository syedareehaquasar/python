# from itertools import permutations

# def is_palindrome(x:int) -> bool:
#     return True if str(x)[::-1] == str(x) else False

# def is_palindrome_possible(s):
#     if is_palindrome(s):
#         return True
#     return any(is_palindrome(i) for i in possible_rearrangements(s)[1:]) if len(s)%2 != 0 else False

# def possible_rearrangements(s):
#     perm = permutations(list(s))
#     return ["".join(i) for i in list(perm)]

# def occurence_of_each_letter(letter,word):
#     return word.count(letter)

def is_palindrome_possible(word):
    return sum([word.count(letter) %2 == 1 for letter in set(word)]) <=1
    
s = "ababa"
print(is_palindrome_possible(s))