"""
dictionaries are used to store data values in key value pairs
they are unordered, mutable(changeable) and dont allow duplicate keys

dict = {
    "name" : "umer",        #in this name is key and umer is value
    "age" : 20,
    "cgpa" : 3.2,
    "marks": [96, 98,83],
    "is_adult" : True,
    "subjects": ["python", "C", "java"],   #we can add list
    "topics" : ("dictionary", "set",),        #we can add tuples
    23 : 97         #we can use name as integer or floar probably strings mostly used
}
print(dict)
print(type(dict))
#we can access individual key
print(dict["cgpa"])
print(dict["subjects"])

dict["name"] = "raja"
dict["surname"]= "umer"     #new key value also add in dictionary here we did it
print(dict)
"""

#Nested dictionaries
#dictionary inside dictionary
student = {
    "name": "umer",
    "age": 20,
    "reg no": 2061,
    "subjects" : {
        "math": 89,
        "phy": 67,
        "isl": 30,
},
}
print(student)      #print full dictionary
print((student["subjects"]))        #print nested dicionary
print(student["subjects"]["math"])      #print nested loop .. key math with value 89