# WAP to count no:of even numbers and odd numbers in a given set of n numbers

num = [1,2,3,4,5,6,7,8,9,10]
even_num = []
odd_num = []

for i in range(len(num)):
    if(num[i] % 2 == 0):
        even_num.append(num[i])
    else:
        odd_num.append(num[i])

print("Number of odd numbers is : ", len(odd_num))
print("Number of even numbers is : ", len(even_num))