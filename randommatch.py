import random

toChooseFrom = "abcdefghijklmnopqrstuvwxyz "

def randomStrs(x):
    return "".join([random.choice(toChooseFrom) for i in range(x)])
    # return random.choices(toChooseFrom, k = 28)


s = input()
_ = 1
while randomStrs(28) != s:
    if _ % 1000 == 0:
        print(_ , randomStrs(28))
    _ += 1
print(_, s, "best")