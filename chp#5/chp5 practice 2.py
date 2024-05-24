#print number from 1 to 100
"""
num = 1
while num <= 100:
    print(num)
    num += 1

#print number from 100 to 1
num1 = 100
while num1 >= 1:
    print(num1)
    num1 -=1

#print multiplication table of number n
n = int(input("enter any number : "))
i = 1
while i <= 10:
    print(n*i)
    i+=1


#print the elements of the following lsit using a loop:
#[1,4,9,16,25,36,49,64,81,100]
nums = [1,4,9,16,25,36,49,64,81,100]
i = 0
while i < len(nums):
    print(nums[i])
    i+=1
heroes = ["raja", "umar", "azam", "khan", "rajpoot", "son", "rj"]
j=0
while j<len(heroes):
    print(heroes[j])
    j+=1
"""


#search for a number x in this tuple using loop
#(1,4,9,16,25,36,49,64,81,100)
#we have to find num 36
tuple = (1,4,9,16,25,36,49,64,81,100)
x = 36      #we have to find x
k = 0
while k < len(tuple):
    if(tuple[k] == x):
        print("found a number at index", k)
    else:
        print("finding")
    k += 1