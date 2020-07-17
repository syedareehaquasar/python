def no_more():
    s="No more letter"
    while len(s)>0:
        for i in list("ABCDEFGHIIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"):
            s.replace(i,"")
            print(s, i)