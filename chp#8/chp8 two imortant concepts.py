"""
4 pillars of oop
1)      abstraction: hiding the implementation of a class and only showing the essential features to the user:
abstract mtlb chupa wa jo chz clear nhe ha

2)      Encapsultion: wrapping data and function into a single unit (object)

3)      inheritance

4)      pollimorphism

"""
#abstraction:
"""
class Car:
    def __int__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):        #class k bahir ya show nhe ho rha unnecesery data hide ho gya
        self.clutch = True      #ya hide hua
        self.acc = True     #ya hide hua
        print("car started..")

car1 = Car()
car1.start()
"""

"""
practice question:
create account class with 2 attributes balance and account no.
create method for debit and credit and printing the balance"""
"""
class Account:
    #create constructor
    def __init__(self, bal, acc):
        #make attributes balance and account no
        self.balance = bal
        self.account_no = acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs.",amount,"was debitted")
        print("total balance = ", self.get_balance())

    def credit(self, amount):
        self.balance += amount
        print("Rs.", amount, "was credited")
        print("total balance = ", self.get_balance())
    def get_balance(self):
        return self.balance


acc1 = Account(1000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(20000)
"""

"""del keyword
use to delete object properties of object itself
del s1.name
del s1
"""
"""
class Student:
    def __init__(self,name,marks,surname):
        self.name = name
        self.marks = marks
        self.surname = surname


s1 = Student("umar",98,"azam")
print(s1.name)
print(s1.surname)
print(s1.marks)
del s1.marks
print(s1.marks) #show error cause we delete it

"""
"""
private(like) attribute and method
conceptual implementation in python
private attributes and method are meant to be used onl within the class and are not 
accessible from outside the class.

in other languages we say it public or private i.e in c++
"""
"""
class Account:
    def __init__(self,acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

        here __ before attribute show that the account password is private
 and cant be access outside the class we access it inside the class he we access it in another function
reset_pass
    def reset_pass(self):
        print(self.__acc_pass)


acc1 = Account("12352","2132")
print(acc1.acc_no)
print(acc1.reset_pass())
"""
#priivate function
class Person:
    __name = "umar"

    def __hello(self):
        print("hello person")

    def welcome(self):
        self.__hello()


p1 = Person()
print(p1.welcome())
