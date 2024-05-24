"""
constructor:
all clases have a function called __init__() which is always executed awhen the class is being initaiad

creating class                                            creating object
clss Student:                                            s1 = Student("umar")
    def __init__(self, name):                            print(s1.name)
        self.name = name
"""
class Student:
    # default constructor
    def __int__(self):
        pass

    #parametrize constructor
    def __init__(self,name, marks):     #constructor
        self.name = name   #self is used to access variable that belogns to class
        self.marks = marks
        print("adding new student in database..")
#constructor apny app call ho jata ha  agr class ma construtor ma kkuch print krwaya ho to just
#class ko cl kry to print output ma show ho jay ga

s1 =Student("umar", 89)     #constructor call in class
print(s1.name,s1.marks)

s2 = Student("nazakt", 91)
print(s2.name,s2.marks)         #variables used such as name marks are called attributes