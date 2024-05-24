#print the sum of n numbers
"""
num = int(input("enter a number: "))
sum = 0
for numbers in range(1,num+1):
    sum += numbers
    print(sum)      #here i print sum for my self to check number in sum
print("total sum is : ", sum)


#print the sum of n numbers
num = int(input("enter a number: "))
sum = 0
i = 1
while i<=num:
    sum += i
    i+=1
print("total sum is : ", sum)
"""

#write a program to find the first n numbersfactorial using for
#fctorial of 5 = 5*4*4*2*1
num = int(input("enter a number: "))
i = 1
factorial = 1
for numbers in range(1,num+1):
    factorial *=i
    i+=1
print("factorial :", factorial)
