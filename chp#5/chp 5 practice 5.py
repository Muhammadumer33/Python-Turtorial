#print the following list using a loop and also find number x
"""
num = (1,4,9,16,25,36,49,64,81,100,49)
x = 49
index = 0
for numbers in num:
    if(numbers==x):
        print("x is found at index", index)
    index +=1
"""
#if we check when num is found break the program
num = (1,4,9,16,25,36,49,64,81,100,49)
x = 49
index = 0
for numbers in num:
    if(numbers==x):
        print("x is found at index", index)
        break
    index +=1