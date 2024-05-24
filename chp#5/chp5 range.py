#range functions returns a sequence of numbers starting from 0 by default and increaments by 1
#and stop before a special number   range(start?,stop,step?)
"""
seq = range(10)
print(type(seq))
for i in seq:
    print("for first iteration",i)

#or we can do upper code as
for j in range(15):
    print("for 2nd iteation",j)

#range syntax
for k in range(2,15,3):     #range(start , stop, stepsize) stepsizre mean start from 2 and then jump to 5 and then 8
    print("for 3rd iteation", k)
"""
#print even numbers
for l in range(2,101,2):
    print("even",l)

#print odd numbers
for m in range(1,101,2):
    print("odd",m)
