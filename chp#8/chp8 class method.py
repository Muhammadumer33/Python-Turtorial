"""
class method:
a class method is bound to the class and receives the class an implicit first argument.
note_ static method can't access or modify class state and generally for utility
i.e @staticmethod
@class_method

there are three type of methods:
static method
classmehtod (cls)
instancethod (self)
"""
class Person:
    name = "raja python"

    @classmethod     #classmethod asy use hota ha or yahe tareeqa best ha it is known as decorator
    def changeName(cls,name):
        cls.name = name
       
"""
    #or ir trha b kr skty
    def changeName(self,name):
        Person.name = name

    def changeName(self, name):
        self.__class__.name = name
"""

p1 = Person()
p1.changeName("raja umer")
print(p1.name)
print(Person.name)


"""
property decorator:
we use @property decorator or any method in the class to use the method in the class to use 
the method as a property
"""
class Student:
    #constructor
    def __init__(self, phy, che, math):
        self.phy = phy
        self.che = che
        self.math = math
        #agr hmy aik percentage wala attribute b add krna ho to
        #ya to hm isi k andr he bna skty hain
        #self.percentage = str((self.phy + self.che + self.math)/3) + "%"


        #hm is trha b percentage update kr skty hain percentage ko call kr k
    #def calculatepercentage(self):
        #self.percentage = str((self.phy + self.che + self.math) / 3) + "%"


    @property
    def percentage(self):
        return str((self.phy + self.che + self.math) / 3) + "%"
    #latest percentage return kry ga


stu1 = Student(98, 97, 89)
print(stu1.percentage)


#for example kl ko teacher ko pta chlta ha k student k phy k marks 98 nhe blky 86 hain

stu1.phy = 86
print(stu1.phy)
#marks to change ho gy mgr percentage nhe change hue to is mamaly ma hm @property ka use kry gy
print(stu1.percentage)


#two more dacorators are
#@getattr()
#@setattr()