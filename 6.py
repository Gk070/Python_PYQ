# WAP to find distance between two points (x1, y1) and (x2, y2)

import math

x1 = int(input("Enter x1 : "))
y1 = int(input("Enter y1 : "))
x2 = int(input("Enter x2 : "))
y2 = int(input("Enter y2 : "))

dist = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print("Distance is : ", dist)