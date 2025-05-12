# WAP to find X^Y or POW(X^Y) without using standart function

x = int(input("Enter x : "))
y = int(input("Enter y : "))
result = 1
for i in range(y):
    result *= x
print(x)