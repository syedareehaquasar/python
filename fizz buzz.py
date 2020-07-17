def fb_q(x :int) -> string:
    if x%3== 0 and x%5 == 0:
        return x = "Fizz Buzz"
    elif x%3 == 0:
        return x = "Fizz"
    elif x%5 == 0:
        return x = "Buzz"
    else:
        return x

while(a<=100):
    print(fb_q(a))
    a+=1