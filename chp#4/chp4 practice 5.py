#store the following word meaing in python
"""
dict = {
    "cat" : "a small animal",
    "table" : ["a piece of furniture" , "list of facts and figures"]
}
print(dict)


#how many classrooms are needed by all students
set1 = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print(len(set1))


#to enter marks of 3 subjects from the user an store them in a dictionary  start with an empty dictionary
#and add one by one use subject name as key adn marks as value
student1 = int(input("enter physice marks : "))
student2 = int(input("enter chemistry marks : "))
student3 = int(input("enter bio marks : "))
marks = {}
marks.update({"phy": student1})
marks.update({"che": student2})
marks.update({"bio": student3})
print(marks)
"""


#figure out a way to store 9 and 9.0 as separate value in the set (you can help of built in function)
values = {9, "9.0"}     #one possible solution to store 9 and 9.0
print(values)

value1 = {
    ("float", 9.0),
    ("int", 9),
}
print(value1)