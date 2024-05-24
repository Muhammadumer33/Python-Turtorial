#when a function call itself repeatedly
#function which call itself again and agian is called recursion
#recursive function
"""
def show(n):
    if(n==0):
        return      #we want to pritn 5 4 3 2 1 using recurison not loops
    print(n)
    show(n-1)       #here wee have function call inside function
show(5)


#factorial      factorial is n! = n*(n-1)!
def fact(n):
    if(n==0 or n==1):
        return 1
    else:
        return  n*fact(n-1)
print(fact(5))

in first execution of 0 or 1 return 1*0!
then in case of 2 * 1! = 2
in third iteration 3 *2!=6
in fourth iteratin 4 *3!=24
in fifth iteration 5*4!=120



#practoce section
#write a recursive functin to calculate the sum of first n natural numbers
def cal_sum(n):
    if(n==0):
        return 0
    return cal_sum(n-1) + n
sum = cal_sum(5)
print(sum)
"""

#print all elements in a list , use list and index as parametes
def print_list(list,idx=0):
    if(idx== len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)

fruis= ["magno", "lichai", "apple", 3 , 5 , "jam"]
print_list(fruis)