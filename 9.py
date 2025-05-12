# WAP to display the sum of odd numbers between aa programmer specified upper and lower bound

sum = 0
for i in range(1, 10):
    if( i % 2 != 0):
        sum += i
print("Sum is : ", sum)