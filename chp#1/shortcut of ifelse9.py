#single line if / ternary operator

"""
food =  input("food: ")
print("sweet") if food == "cake" or food == "jalebi" else print("not sweet")

#cldver if ternary operator
age = int(input("age : "))
vote = ("yes","no")[age < 18]
print(vote)

#salery tax example
sal = float(input("sal : "))
tax = sal*(0.1,0.2)[sal>=50000]
print(tax)"""

#best practice declare the variable with actual name i.e simple interest =  p*r*t/100
# we use p r t instead of a b c

p = float(input("principal amount : "))
r = float(input("rete : "))
t = float(input("time : "))

si = (p*r*t)/100
print("simple interest is : ", si)