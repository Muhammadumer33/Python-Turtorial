#punctuatora -=, +=,/=, *=,||=,= etc
#expressions execution
#strings and numeric can operate with *
A,B = 2,3
txt = "@"
print(2*txt*3)
#output @@@@@@

#string and string can operate with +
A,B = "2",3
txt = "@"
print((A+txt)*B)
#output 2@2@2@

#numeric values can operate with all arithematic operators
A,B = 2,3
C=4
print(A+B*C)

#arithmatic expression with integer and float will result in float
A,B = 10,5.7
C=A*B
print(C)

#result of division opearator awith two integers will be float
A,B = 2,3
C=A/B
print(C)

#integer division with float and int will give float velue
A,B = 2.3,3
C=A//B
print(C, A/B)

#integer division round off the answer floor // will round of but simple division / does not
A,B = 12,5
C = A//B
print(C)

#simple division
A,B = 12,5
C = A/B
print(C)

#modulus
#ans will be positive because denominator is positive
A,B = -12,5
C = A%B
print(C)

#ans will be negative because denomirator is negative
A,B = 12,-5
C = A%B
print(C)

#ans will be positive in both same signs for numerator and denormirator
A,B = 12,5
C = A%B
print(C)

#multiple line code """    """ ecample
"""" hi i am umar
my name is rj
my father name is azam 
we are five brothers"""
