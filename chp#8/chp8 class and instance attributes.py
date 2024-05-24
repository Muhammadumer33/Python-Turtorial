"""
class Student:
    college = "prime college"
    name = "ali"  #class atrr

    def __init__(self,name, marks):
        self.name = name  #object attr > class attr here self.name name is attr
        self.marks = marks
        print("adding new student in database")

s1 = Student("umar", 90)  #function k data ko access krny k lye initailize krna parta ha
print(s1.name,s1.marks)

s2 = Student("arjun", 98)
print(s2.name,s2.marks)

print(Student.college)   #class k data ko access krny k lye initialize nhe krna prta
"""
#class is collection of two things data and methods ,, data means attributes

"""
Mehtos....
methods are functions that belong to object 
"""
class Student:
    college = "prime college"

    def __init__(self,name, marks):
        self.name = name
        self.marks = marks
    def welcomee(self):
        print("welcome student",self.name)

    def getmarks(self):
        return self.marks

s1 = Student("umar", 90)
s1.welcomee()
print("your marks",s1.getmarks())


