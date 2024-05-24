#set is mutable but elements not set ma kuch add ho skta ha mgr element ko change nhe kia ja skta
"""
#add element
collection = set()
collection.add(1)
collection.add(2)
collection.add((2,3,4,5,6))       #we can add tuple
collection.add("rj")        #we can add string
print(collection)           #unhashable means jin ki hashing value different aa jy bd ma ja k i.e dictionary
#list, sets q k in tenu ma add or remove ho skta

#remove element
collection.remove(2)
print(collection)


#set ko khali krna ho to ya clear krna ho
print(len(collection))
collection.clear()
print(len(collection))


#remove any random value
student = {"umar", "college", "uet", "cse", "peshawar"}
print(student.pop())
print(student)
"""

#union method combine both set value and return new one
#union and intersecion in sets
set1 = {1,2,3,4}
set2 = {2,4,5,6}
print(set1.union(set2))
print(set1.intersection(set2))