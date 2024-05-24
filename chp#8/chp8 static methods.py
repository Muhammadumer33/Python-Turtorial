"""
static method:
method that dont use the self parameter(work at class level)

class Student:
    @static method  #we use this decorator to make mehod or function at class level
    def college(no self inside bracket):
    print("this is my college")

    @static method this decorator change the behaviour of function and return
"""
class Student:
    @staticmethod
    def college():
        print("this is my college")

s1 = Student()
print(s1.college())
