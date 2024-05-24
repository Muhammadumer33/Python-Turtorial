#write function to print the lengthh of the list
"""
name = ["umer", "azam", 33, "math", "A+",88,44]
heroes = ["umer", "azam", "nazakat", "math", "aloi", "sana", "ibrahim","ahmed"]

def print_length(list):
    print(len(list))

print_length(name)
print_length(heroes)

#write function to print the elements of  la list in a single line(list is the paramaeter)
def elements(list):
    for item in list:
        print(item,end= " ")

elements(heroes)
"""

#program to find factorial of n using functions here we saw simple fac prgram
"""
num = int(input("enter a number : ", ))
factorial = 1
for i in range(1,num+1):
    factorial = factorial*i
print(factorial)

#usig functions
def cal_fact(num):
    fact = 1
    for i in range(1, num+1):
        fact = fact*i
    print(fact)

cal_fact(7)


#program to convert USD to INR,,,1 usd = 83 inr,,,2 usd = 166inr
def converter(usd_val):
    inr_val = usd_val*83
    print(usd_val,"USD =",inr_val,"INR")

converter(5)
"""

#write function to check even or odd numberrs
def check(num):
    if num%2==0:
        print("even")
    else:
        print("odd")

check(10)


