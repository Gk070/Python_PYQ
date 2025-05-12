# WAP to find the roots of a quadratic equation

import math

a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))

d = b ** 2 - 4 * a * c
if d > 0:
    x1 = (-b + math.sqrt(d)) / (2 * a)
    x2 = (-b - math.sqrt(d)) / (2 * a)
    print("Roots are", x1, x2)
elif d == 0:
    x1 = -b / (2 * a)
    print("Roots are", x1)
else:
    print("No real roots")