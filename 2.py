# WAP that accepts the lengths of three sides of a triangle as inputs and utputs whether or not the triangle is right triangle

def is_right_triangle(a, b, c):
    sides = sorted([a, b, c])
    a, b, c = sides
    return a ** 2 + b ** 2 == c ** 2

a = int(input("Enter side 1 : "))
b = int(input("Enter side 2 : "))
c = int(input("Enter side 3 : "))
if is_right_triangle(a, b, c):
    print("Right Triangle")
else:
    print("Not a Right Triangle")