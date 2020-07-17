# def generate_encrypted_string (string):
#     new = ""
#     for x in string:
#         if ord(x)>=65 and ord(x)<=90 or ord(x)>=97 and ord(x)<=122:
#             if (ord(x)>=65 and ord(x)<=77) or (ord(x)>=97 and ord(x)<=110):
#                 new += chr(ord(x)+13)
#             else:
#                 new += chr(ord(x)-13)
#         else:
#             new += x
#     return new

# print(generate_encrypted_string("this is a SENTENCE"))

#....................................................................................................

# def encrypt(input_word):
#     x = input_word[::-1]
#     x = x.replace("a","0")
#     x = x.replace("e","1")
#     x = x.replace("o","2")
#     x = x.replace("u","3")
#     return str(x)+"aca"

# def encode(ch : str) -> str:
#     Replace = {'a' : }
# print(encrypt("apple"))

#....................................................................................................

# def generate_encrypted_string (string):
#     new = "nopqrstuvwxyzabcdefghijklmNOPQRSTUVWXYZABCDEFGHIJKLM"
#     alphabets = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     ans = ""
#     for x in string:
#         if x in alphabets:
#             z = alphabets.index(x)
#             ans += new[z]
#         else:
#             ans += x
#     return ans

# print(generate_encrypted_string("this is a SENTENCE"))