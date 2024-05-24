"""
define a circle clss to create a circle with radius r using the constructor
define an area() method of the class which claculates the area of the circle
define a perameter() method of the class which allows you to calculate the perimeter of the circle
"""
class Circle:
    def __init__(self,radius):
        self.radius = radius

    def Area(self):
        return (22/7)*self.radius**2

    def perimeter(self):
        return 2*(22/7)*self.radius

c1 = Circle(21)
print(c1.Area())
print(c1.perimeter())

"""
define a employee class with attributes role, department and salary
this clss also have a show details method
Create an Engineer class that inherits properties from Employess and has additional attributes 
name and age
"""
class Employee:
    def __init__(self,role,department,salary):
        self.role = role
        self.department = department
        self.salary = salary

    def showdetails(self):
        print("role = ", self.role)
        print("department = ",self.department)
        print("salary =", self.salary)

class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer", "IT","75,000")  #inherit kia ha

e1 = Engineer("umar", "21")
print("name =",e1.name,"\nage =",e1.age)
e1.showdetails()


"""
create a class order which store item and its price.
use dunder function __gt__() to convey that:
order1> order2 if price of order1 > price of order2
"""
class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price

    def __gt__(self, odr2):  #(self shows odr1, odr2 shows odr2)
        return self.price > odr2.price #this tunder function is used of greater than

odr1 = Order("shampoo",700)
odr2 = Order("Tea",600)
print(odr1.item,"=",odr1.price)
print(odr2.item,"=",odr2.price)

print("price of odr1 > price of odr2 = ",odr1>odr2)
