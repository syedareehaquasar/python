#assignment 1
# s = ["Reeha","Saba","MommyDaddy"]
# s = list(map(str,input().strip().split()))[:3]

# def removevowels(word):
#     vowels = ('a','e','i','o','u')
#     return ''.join(x for x in word if x.lower() not in vowels)

# def string1(s : str) -> str:
#     for x in "aeiouAEIOU":
#         s[0] = s[0].replace(x,"$")
#     return s[0]

# def string2(s : str) -> str:
#     for x in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ":
#         s[1] = s[1].replace(x,"#")
#     return s[1]

# def string3(s : str) -> str:
#     return s[2].upper()

# def concatenate(s : str) -> str:
#     s = string1(s) + string2(s) + string3(s)
#     return s

# print(concatenate(s))

# in one function only
# # def assignment1(s : str) -> str:
# #     for ch in s[0]:
# #         if ch.lower() in "aeiou":
# #             s[0] = s[0].replace(ch,"$")
# #     for ch in s[1]:
# #         if ch.lower() not in "aeiou":
# #             s[1] = s[1].replace(ch,"#")
# #     s[2] = s[2].upper()
# #     s = s[0] + s[1] + s[2]
# #     return s

# # print(assignment1(s))

# def modification(s):
#     for x in s[0]:
#         if is_vowel(x):
#             s[0] = s[0].replace(x,"$")
#     for x in s[1]:
#         if not is_vowel(x):
#             s[1] = s[1].replace(x,"#")
#     s[2] = s[2].upper()
#     s = s[0] + s[1] + s[2]
#     return s

# def is_vowel(x : str) -> bool:
#     return True if x.lower() in "aeiou" else False

# def is_consonant(x : str) -> bool:
#     return True if x.lower() in "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ" else False

# def string1(s : str) -> str:
#     for x in s[0]:
#         if is_vowel(x):
#             s[0] = s[0].replace(x,"$")
#     return s[0]

# def string2(s : str) -> str:
#     for x in s[1]:
#         if is_consonant(x):
#             s[1] = s[1].replace(x,"#")
#     return s[1]

# def string3(s : str) -> str:
#     return s[2].upper()

# def concatenate(s : str) -> str:
#     s = string1(s) + string2(s) + string3(s)
#     return s

# s = ["Syeda" , "Reeha" , "Quasar"]
# print(concatenate(s))

# print(modification(s))