#return all keys
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
"""
print("total keys = ", student.keys())  #nested keys does not return
#you want to print list
print("keys in list form = ",list(student.keys()))
#print length of keys
print("length of dictionary = ",len( student.keys()))


#return all values
print("the values of dictioanry = ",student.values())
#we also print it in list form
print("the values of dictioanry in list from = ",list(student.values()))


#return all (key , value) pairs as tuples
print(student.items())
#if you want to access specific pair of tuple
pairs = list(student.items())
print("pair at index 1 is = ", pairs[1])


#return the key according to value
print(student["name"])
print(student.get(("name")))
#print(student["name2"])        name2 key is not present it will give us erroe
#print(student.get(("name2")))  in this case we use get and it will return none as output
#hm get use krty taa k error ay to program kam krna na chory wrna error k bd program ouput show nhe krta
#agr next line code sai he q na ho
"""


#insert the specified item to the dictionary
student.update({"sports" : "cricket"})
print(student)
#another way
newdictionary = {"hobby": "snooker"}
student.update(newdictionary)
print(student)