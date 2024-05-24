# add one element at the end
umer = [2, 1, 3, 5, 9, 7]
umer.append(4)      #list.append add number at the end of list
print(umer)

#sort is asceending order
umer.sort()
print(umer)

#in reverse order / desecnding order
fruits = ["apple", "banana", "mango", "orange", "kahrbooz"]
fruits.sort(reverse= True)        #this works ascending or desecing in string to chaech first letter or word
print(fruits)
#strings in ascending in the form of first letter in abc.. apple phly aya q k phla word a ha
fruits.sort()
print(fruits)


#in revers order
ali = [2,4,3,2,3,4,12,5,7,42,45]
ali.sort()
print(ali)
ali.reverse()
print(ali)


#insert element in specific index
rj = [3,5,2,6]
rj.insert(1,4)
print(rj)


#remove method
you = [1,2,3,2,3,4,5]
you.remove(3)       #remove ma 3 ha to phla 3 jo list ma mily ga wo remove ho jay ga at any location
print(you)
you.pop(2)      #pop specific index ko remove krta ha
print(you)