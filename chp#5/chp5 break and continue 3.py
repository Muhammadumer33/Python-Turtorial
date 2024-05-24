#break : breeak are use to terminate the loop when encountered
#continue: terminates execution in the current itteration  and continues execution of the loop with next iteration
"""
i= 1
while i <= 5:
    print(i)
    if(i==3):
        break
    i +=1
print("end of loop")
"""

tuple = (1,4,9,16,25,36,49,64,81,100)
x = 36      #we have to find x
k = 0
while k < len(tuple):
    if(tuple[k] == x):
        print("found a number at index", k)
        break
    else:
        print("finding")
    k += 1
print("end of loop")


#continue
i= 0
while i <= 5:
    if(i==3):
        i += 1 #when i = 3 compiler add i = i +1 and then print 4
        continue    #i==3 skip
    print(i)
    i+=1


#print ddd numbers
j= 0
while j <= 10:
    if(j%2==0):
        j += 1
        continue    #if codition true then skip the even numbers and print odd numbers
    print(j)
    j+=1


#print even numbers
k= 0
while k <= 10:
    if(k%2 != 0):
        k += 1
        continue
    print(k)
    k+=1

