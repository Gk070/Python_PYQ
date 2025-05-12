# WAP to check whether a number is Armstrong number or not.

num = int(input("Enter number : "))
n = num
sum = 0
length = len(str(num))
while n > 0:
    rem = n % 10
    sum += rem ** length
    n //= 10
if(num == sum):
    print(num, " is amrmstrong number")   
else:
    print("Not a armstrong number")