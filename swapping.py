def swapping(x,y):
    # temp = x
    # x = y
    # y = x
    # print('New x is: ' + x )
    # print('New y is ' + y)
    x , y = y , x
    print('New number 1 is: ' + str(x) )
    print('New number 2  is ' + str(y))

print('Enter the numbers needed to be swapped')
num1 = int(input('enter number 1 '))
num2 = int(input('Enter number 2 '))
print('---------------------------------------------------------')
swapping(num1,num2)