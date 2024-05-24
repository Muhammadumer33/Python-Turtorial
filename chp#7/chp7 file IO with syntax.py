with open("2nd program.txt","r")as f:
    data = f.read()
    print(data)
#with syntax ko jb use kry to file ko close nhe krna prta

with open("2nd program.txt","w") as f:
    f.write("my name is rajjjjjjuuuuuu")        #over write the file with my name is rajj..


"""deleting a file 
using the os module
module like a code library is a file weitten by another programmer that generally has a functions we can use)
import os
      os.remove(filename)
"""
f= open("ali.txt","w")

import os
# os.remove("ali.txt")   if i run this line ali.txt file will be deleted