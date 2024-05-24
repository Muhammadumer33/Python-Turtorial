#list is mutalbe jis ki value change ho skti ha
#tuple is immutable is ki value change nhe ho skti
#list ma square bracket hoty []
#in touple () these brackets are used
tup = (1, 2, 4, 5, 3, 5)
print(type(tup))
print(tup[2])
print(tup[3])
#tup(1) = 3 is not allowed in tuples
tup1 = (1,)
print(type(tup1))
tup2 = (2)      #for this compiler show class int
print(type(tup2))       #compiler conside is integer cause tup2(2) (2  this comma is missing inside",")