def sum_in_range(x,y):
    num_list = range(x,y+1)
    final_sum = sum(num_list)
    print(final_sum)

num1 = int(input('Enter the the lower limit : '))
num2 = int(input('Enter the upper limit : '))
print('Sum of numbers is: ')
sum_in_range(num1,num2)