#list and tuple

marks = [94.4,87.5,95.2,77.7,88.8]
print(marks)
print(type(marks))
print(marks[0])
print(marks[1])
print(len(marks))


#list-mutable and inmutebal

student = ["tushar",97.8,12,"bhopal"]
print(student) 
student[0] = "arjun" 
print(student)


#list slicing

marks = [85,94,76,63,48]
print(marks[2:4]) 

#list methods

list = [1,2,3,4]
list.append(5) 
print(list)

#list.sort

list = [4,5,2,1,3]
print(list.sort())
print(list)

#list.sort(reverse=True )

list = [4,5,2,1,3]
print(list.sort(reverse=True ))
print(list)

#list.reverse

list = ['a','c','b',]
list.reverse()
print(list)

#list.insert

list = [1,2,3,4,5]
list.insert(1,6)
print(list)

#list.remove

list = [1,2,3,4,5]
list.remove(5)
print(list)

#list.pop

list = [1,2,3,4,5]
list.pop(2)
print(list)


#tuple methods

tup = (1,2,3,4,5,)
print(tup)
print(type(tup))

#tup.index
tup = (1,2,3,4,5,)
print(tup.index(2))

#tup.count()

tup = (1,2,3,4,5,)
print(tup.count(2))

##list muteble vs tuple inmuteble

#Q1 creat a list [10,20,30] and add 40 to it 

list = [10,20,30,]
list.append(40)
print(list)

# #Q2 creat a tuple (1,2,3) and try to add 4 in it 
# ##*** tuple is inmutable 

#Q3 replace the first element of list [5,6,7] with 99.

list = [5, 6, 7]
list[0] = 99 
print(list)

#Q4 try to change the second elemant of tuple(11,22,33)

tup = (11,22,33)
##tuple can not be modifide 

## list slicing 

#Q5 from list [1,2,3,4,5,6] get elements from 2nd to 4th 
list = [1,2,3,4,5,6]
print(list[1:4]) 

#Q6 from list [10,20,30,40,50] get last 3 elemant 
list = [10,20,30,40,50]
print(list[-3:])

#Q7 reverse the list [7,8,9,10,11] using slicing
list = [7,8,9,10,11]
print(list[::-1])

#Q8 prove that list is mutable 

list =[10, 20, 30]
list[0] = 90
print(list)

#Q9 prove that tuple is inmuteble 
tup = (10,20,30)
#tup[0] = 99
print(tup)

#Q10 replace 3rd element in a list 
data = ["A", "b", "c","d"]
data[2] = "z"
print(data)

#Q11 try to change tuple element 
x =(5,10,15)
##x[0] = 99
print(x)

## list slicing

#Q12 print the middle three elements of the list [10,20,30,40,50]
list = [10,20,30,40,50]
print(list[1:4])

#Q.13 print the list[1,2,3,4,5] in reverse order 
list = [1,2,3,4,5]
print(list[::-1])

#Q12 print the alternate every element of the list 
list = [10,20,30,40,50,60,]
print(list[::2])

#Q.13 print the first three element of [1,2,3,4,5,]
list = [1,2,3,4,5]
print(list[:3])

##list method 

#Q.14 add "eraser" to the list ["pen","pencil",]
list = ["pen","pencil"]
list.append("eraser")
print(list)

#Q.15 insert "pencile" at index 1 in the list 
list = ["pen","eraser"]
list.insert(1,"pencile")

#Q.16 remove element 30 from [10,20,30,40,50,]
list = [10,20,30,40,50,]
list.remove(30)
print(list)

#Q.17 remove element in index 2 from [1,2,3,4] using pop()
list = [1,2,3,4]
list.pop(2)
print(list) 

## short and reverse 

#Q18 short the list [5,3,1,4,2]
list = [5,3,1,4,2]
list.sort()
print(list)

#Q.19 short the list[5,3,1,4,2] in descending order 
list = [5,3,1,4,2]
list.sort(reverse=True)
print(list)

#Q.20 reverse the list [1,2,3,4 ] using reverse() 
list = [1,2,3,4]
list.reverse()
print(list)

