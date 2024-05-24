"""
inheritance:
when one class(child/ derived) derives the properties and methods of another class(parent/ based)
clss Car:
    ....



class ToyotaCar(Car):

"""

# singlel inheritance
"""
class Car:

    color = "black"
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name

car1 = ToyotaCar("fotuner")
car2 = ToyotaCar("prius")

print(car1.name,car1.start(),car1.color)
print(car2.name,car2.stop(),car2.color)
"""



"""
   inheritance types:
   
1   single inheritance
2   multi_level inheritance
3   multiple inheritance
"""
# multi level inheritance:
# class inherit more than one class is called multi inheritance
"""
class Car:
    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self,brand):
        self.brand = brand

class Fortuner(ToyotaCar):
    def __init__(self,type):
        self.type = type


car1 = Fortuner("diesel")
car_1_brand = ToyotaCar("Fortuner")
print(car1.type)
print(car_1_brand.brand)
car1.start()

car2 = Fortuner("petrol")
car_2_brand = ToyotaCar("prius")
print(car2.type,car_2_brand.brand,car2.stop())
"""


"""
multiple inheritance:
    multiple inheritance means one class inherit two different class 
    multi level ma hm aik class ki sub classes bnaty hain 
    mtlb multilevel grandfather phr parent or phr child ata ha mgr multiple ma asa nhe hota"""



"""
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"

class C(A,B):
    varC = "welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varB)
print(c1.varA)
"""

"""
Super method:
    super() method is used to access methods of the parent class
"""
class Car:
    def __init__(self,type):
        self.type = type

    @staticmethod
    def start():
        print("car started")

    @staticmethod
    def stop():
        print("car stopped")

class ToyotaCar(Car):
    def __init__(self,name,type): #perent class ma jo type ha us ko inherit kia ha super k through
        super().__init__(type)
        self.name = name
        super().start()

car1 = ToyotaCar("prius", "electric")
print(car1.type)