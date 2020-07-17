def multiplication_table(x):
    for i in range(1,11):
        print(str(x) + " X " + str(i) + " = " + str(x*i))

num = int(input('enter the number whose multiplication table is needed'))
print('multiplication table of : ' + str(num))
multiplication_table(num)