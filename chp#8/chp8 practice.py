"""
create a student class that takes name and marks of three subjects as arguments in constructor then create
a method to print average
"""
class Student:
    def __init__(self,name, marks):
        self.name = name
        self.marks = marks

    def average(self):      #these are method that use in class
        sum = 0
        for val in self.marks:
            sum+= val
        print("hi",self.name,"your avergae marks is:", sum/3)


s1 = Student("umar",[99,98,97])
print(s1.name,s1.marks)
s1.average()