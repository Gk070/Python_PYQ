# Given the value of x, WAP to evaluate the following series upto n terms
# 1 + x + x^2/2! + x^3/3! ...

import math
sum = 0
x = int(input("Enter x : "))
n = int(input("Enter range : "))
for i in range(n + 1):
    sum += (x ** i / math.factorial(i))
print("Sum is : ", sum)