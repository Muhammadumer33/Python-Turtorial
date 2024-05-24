"""create a new file practice.txt using python add the following data in it
hi everyone
we are learning file io
using java
i like programming in java"""
"""
f = open("practice.txt","w")
f.write("hi everyone \nwe are learning file io\nusing java\ni like programming in java")
f.close()
"""
"""
#write program that replace occurance of java with python in above file
with open("practice.txt","r") as f:
    data = f.read()         #first we read and the replace
    #print(data,"\n\n")

newdata = data.replace("java","python")
print(newdata)
#now overwrite with new data
with open("practice.txt","w") as f:
    f.write(newdata)

"""
"""
#search if the word learing is exist or not
word = "learning"
with open("practice.txt","r") as f:
    data = f.read()
    if(data.find(word) != -1):
        print("found")
    else:
        print("not found")
"""


#write a program to find in which line of the file does the word "learning" occour first.
#print -1 if the word not found

def check_for_line():
    word = "umar"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no+=1
    return -1
print(check_for_line())


#from a file containg a number separated by comma, print the count of even nymbers:
with open("data.txt","w") as f1:
    f1.write("1,2,76,84,90,101")
    #in this portin we crater a file and write data in it
with open("data.txt","r") as f1:
    data= f1.read()
    print(data)

#basic tareeqa
num =""
for i in range(len(data)):
    if(data[i] == ","):
        print(int(num))
        num = ""
    else:
        num+=data[i]

#using split operats
count = 0
with open("data.txt","r") as f1:
    data= f1.read()
    nums = data.split(",")
    print(nums)
    for val in nums:
        if(int(val) % 2 == 0):
            count +=1

print(count)
