#if - elif - else synatax
#traffic light code
light = input("light : ")
if(light == "red"):
    print(stop)
elif(light == "yellow"):
    print("look")
elif(light == "green"):
    print("go")
else:
    print("light is broken")

    

#grades of student
marks = int(input("marks : "))
if(marks >= 90):
    print("A")
elif(marks >= 80 and marks < 90):
    print("B")
elif(marks >= 70 and marks <80):
    print("C")
elif(marks >=50 and marks < 70):
    print("D")
else:
    print("F")