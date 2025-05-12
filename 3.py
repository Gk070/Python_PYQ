# WAP to reverse a number and also find the sum of digits of the number. Prompt the user for input

num = input("Enter number : ")
rev = num[::-1]
print("Reversed number is : ", rev)

n = int(num)
sum = 0
while n > 0:
    rem = n % 10
    sum += rem
    n //= 10

print("Sum is : ", sum)