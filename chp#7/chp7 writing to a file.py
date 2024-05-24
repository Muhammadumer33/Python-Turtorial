"""
hm file ko 2 trha write kr skty hain agr w sy ooen kr k write kry to data overwrite ho jay ga mtlb
phla data remove ho jy ga or age a sy open kr k write krty hain to wo file ma akhir pr add ho jay ga
mgr file ka phla data remove nhe ho ga

f = open("2nd program.txt","a")
f.write("\ni am student")
f.close()

f1 = open("sample.txt","w")
data = f1.write("my name is raja umar")
print(data)
f1.close()                           #bakhud create ho jay ge
"""

#in w mood file trunkaate mtlb file ka data delete ho jata ha
# if we use r+ mode then overwrite start from star
f1 = open("sample.txt","r+")
f1.write("rj")
print(f1.read())
f1.close()
"""
#in w+ mood file is open for read and write but file trunkate
f1 = open("2nd program.txt","w+")
f1.write("rj")
print(f1.read())
f1.close()
"""
"""
#myself checking
f1 = open("2nd program.txt","a")
#data =f1.write("rj")
f1.write("\n i am a student")
f1.close()
"""
"""
r for read only and we only print file in r mood only such as print(data)
w for write only in which trunkates
a for append means file open to write at the end
r+ for read and overwrite at the first of file but file does not trunkate we can also print data in r+ mood/
w+ for read and write but file trunkate
a+ read and write but file does not trunkate
agr hmy file bnani ha to just a ya w k sath us file open kry to file automatically create ho jy ge"""