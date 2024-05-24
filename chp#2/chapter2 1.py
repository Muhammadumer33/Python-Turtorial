#strings : strings is data type that stores a swquence of charactes

#umar + azam = umarazam this process is concatenation
"""str1 = "umar"
str2 = "azam"
str3 = str1+ " k " +str2   #str3 = str1 + " " + str2  ,,,str3 = str1 + str2
print(str3)  # or print(str1 + str2)

#length of string can be find using len(str)
print(len(str3))"""



#access character from index
str = "LAIBA MIR"
print(len(str))
print(str[3])
print(str[4])       #str[4] = S is not allowed



#slicing: access parts of a string

print(str[1:4])
#slicing [1:4] it give us part of string from 1 to 4 means 1 2 3 index includ
#ending index not include
#if we wanna go to last index we use
print(str[6:])
print(str[:5])      #compiler understand we wanna start from from zero




#slicing negative index
rj = "apple"
print(rj[-4:-1])