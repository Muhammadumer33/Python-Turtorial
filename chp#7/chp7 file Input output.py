"""pytho can be used to perform operation on a file    read and write
types of files
1   text files:: .txt, .docx, .log, etc
2  binary file:: mp4, .mov, .png, .jpeg etc
we store files in ssd or hhd ,,, variables of files stores in ram
files stores in system in the form of 0 and 1
"""
#open read and close
#we have to open a file before reading or writing
"""
f = open("2nd program.txt", "r")
data =f.read()
print(data)
print(type(data))
f.close()


#if we want to read first 6 characters
f = open("2nd program.txt", "r")
data =f.read(6)
print(data)
print(type(data))
f.close()
"""
#if we want to read file line by line  read one line at a time
f = open("2nd program.txt", "r")
line1 =f.readline()
print(line1)
line2 =f.readline()
print(line2)
f.close()