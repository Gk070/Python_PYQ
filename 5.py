# WAP to print all prime numbers less than 1000

for i in range(2, 1001):
    isPrime = 1
    for j in range(2, i):
        if(i % j == 0):
            isPrime = 0
            break
    if(isPrime == 1):
        print(i)