#block of statements that perform a spcific tassk
#def func_name(param1, param 2):        function defination
#some work
"""
a= 5
b = 10
sum = a+b
print(sum)
if we have to repeat sum again and again we use function call without writtin same lines for sum again
and again
"""
#function decrease the rpeatability of code, reduntant means repetition
def calc_sum(a,b):      #here we made funcion with parameter a and b
    sum = a + b
    print("sum of two numbers is : ",sum)
    return sum
calc_sum(6,7)       #this is function call with argument 6 and 7
calc_sum(9,14)
calc_sum(77,78)
#functions are used to remove redundency in program

#another way
def add(a , b):
    return a + b
sum1 = add(6,7)
print(sum1)


#function to print string
def name():
    print("my name is raja uamr")
name()
name()

#average of three numbers
def avg (a,b,c):
    average = (a +b +c)/3
    print(average)
    return average
avg(3,8,9)
avg(99,7,7,)