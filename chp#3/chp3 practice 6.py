#ask user to enter name of their 3 movies and store them in a list
"""
str1 = input("enter 1st movie: ")
str2 = input("enter 2nd movie: ")
str3 = input("enter 3rd movie: ")
list = [str1, str2, str3]
print(list)

#another way
movies = []
movies.append(str1)
movies.append(str2)
movies.append(str3)
print(movies)       #append is used to add element in the last

#another way
film = []
film.append(input("1st film: "))
film.append(input("1st film: "))
film.append(input("1st film: "))
print(film)


#2nd practice question :     if a list contains palindrome of elements
#palindroem is a list jis ko start sy prho tb b same hoti ha or last sy prho tb b same hoti ha
#i.e rececar, [1,2,2,1], [1, "abc", "abc", 1]
#palindrome check krny k lye phly hm copy bnaty list ki phr usko reverse krty age same aa jy to
#palindrome ho ga wrna nhe

list2 = [1,2,2,1]
list3 = [1,2,3,4,5]
copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("palindrome")
else:
    print("not palindromw")

copy_list3 = list3.copy()
copy_list3.reverse()
if(copy_list3 == list3):
    print("palindrome")
else:
    print("not palindrome")

"""
#to count the number of students with "A+" grade in the following touple
tup = ["C", "D", "A", "A", "B", "B", "A", "C", "A", "D"]
student = tup.count("A")
print("student with grade A: ", student)


#sort the values in ascending order
tup1 = ["C", "D", "A", "A", "B", "B", "A", "C", "A", "D"]
tup1.sort()
print(tup1)