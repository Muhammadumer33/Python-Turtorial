"""
4 types of oop
abstraction
encapsulation
inheritance
polymorphism: operator overloading ; aik chz ko alg alg tareeeqy  sy use kia ja sky
when the same operator is allowed to have different meaning according to the context

operator and dunder functions:
a  +  b              addition                   a.__add__(b)
a  - b               Subtraction                a.__sub__(b)
a  *  b              multiplication             a.__mul__(b)
a  /  b              division                   a.__truediv__(b)
a  %  b              modulus                    a.__mod__(b)
"""

#implicit overloading
print(1+2) #3 ... integer ma addition ka alg mtlb 2 num ko add krta ha
print(type(1))

print("raja"+"umer") #rajaumer.... concatenation ,,string ma add sign 2 string ko jorta ha
print(type("raja"))

print([1,2,3]+[4,5,6]) #merge ...list ma add sign 2 list ko aik bna deta [1,2,3,4,5,6]
print(type([1,2,3]))

"""
python k andar complex number ko create krny k lye koi class ha e ni
hum khud ki class bny gy
asi class jo complex num ko create kr sky
integer string or list ko python ma create kr skty mgr complex ko nhe kr skty
"""

class Complex:
    def __init__(self,real,imag):
        self.real =  real
        self.imag = imag

    def ShowNumber(self):
        print(self.real,"i+",self.imag,"j")

    def __add__(self,num2):     #self num1 or num2 num2 ko show kr rha ha...or ma isy dunder function bnatata
        #hu ta k mjy just num3 = num1 + num2 likhna pary
        newReal = self.real + num2.real
        newImag = self.imag + num2.imag
        return Complex(newReal,newImag) #ya function 2 num ko add kr rha ha

num1 = Complex(1,3)
num1.ShowNumber()

num2 = Complex(4,5)
num2.ShowNumber()

#num3 = num1.add(num2) idr many function call kia ha
# ya function k bijay ma chahta hu mjy likhna pary num3 = num1 + num2
#is k lye ma dunder function use kru ga jo + operator ko mri class ma define kr dy gy
num3 = num1 + num2
print(num3.ShowNumber())
#isi trha bqi dunder function b use hoty hain __init__ is also dunder fucntion