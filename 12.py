# WAP to generate the following type of pattern for the given N rows where N <= 26
# A
# A B
# A B C
# A B C D

n = int(input("Enter number : "))
if(n >= 26):
    print("N should be greater than 26")
else:
    for i in range(n):
        for j in range(i + 1):
            print(chr(65 + j), end=" ")
        print()