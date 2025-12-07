#loops in python


# count = 1 
# while count <= 5 :
#     print("hello",count)
#     count += 1


#Q1 print number of 1 to 100

# i = 1
# while i <= 100:
#     print(i)
#     i += 1

#Q2 print number from 100 to 1 

# i = 100 
# while i >=1: #stoping condition 
#     print(i)
#     i -= 1

#Q3 print the multiplication table of a number n 
# n = int(input("enter number"))
# i = 1 
# while i <= 10:
#     print(n*i)
#     i += 1

#Q4 print the eliment of the following list 

# nums = [1,4,16,25,36,49,64,81,100]

# idx = 0 
# while idx < len(nums):

#     print(nums[idx])
#     idx += 1

#4  search for a number x in this tuple using loop 

# nums = (1,4,16,25,36,49,64,81,100)

# x = 49
# i = 0 
# while i < len(nums): 
#     if(nums[i] == x):
#         print("FOUND at idx",i)
#     else:
#         print("finding..")
#     i += 1


    #brack and continue key word 

#brack keyword

# i = 1
# while i <= 5:
#     print(i)
#     if(i == 3):
#      break 
#     i += 1 

#continue keyword 

# i = 1
# while i <= 5:
#     if(i == 3):
#        i += 1 
#        continue 
#     print(i)
#     i += 1 

#for loop

# nums = [1,2,3,4,5,6]

# for val in nums:
#     print(val)

# veggies = ["potato", "brijal","ladyfinger","bagan"]

# for val in veggies:
#     print(val)

# tup = (1,2,3,4,5,6,)

# for num in tup:
#     print(num)



#using for 
    #Q1 print the eliment of the following listnusing a loop:

# nums = [1,4,9,16,25,36,49,64,81,100] 

# for elemant in nums:
#     print(elemant)

#Q2 search for a number x in this tuple using loop 

# nums = (1,4,9,16,25,36,49,64,81,100)

# x = 49 
# idx = 0
# for el in nums: 
#     if(el == x):  
#        print("number found at idx",idx)
#     idx += 1 

#range()

# seq = range(5)
# for i in seq:
#     print(i)

#same 

# for i in range(10): #range of (stop) 
#     print(i)


# for i in range(2,10): #range of (start , stop)
#       print(i)


# for i in range(2, 10, 2): #range (start, stop , step)
#     print(i)


#even number 
# for i in range(2,101,2):
#     print(i)

#odd number 
# for i in range(1, 101, 2):
#     print(i)


#luets practice 

#using for & range

#Q1 print numbers from 1 to 100

# for i in range(1, 101):
#     print(i)

#Q2 print number from 100 to 1 

# for i in range(100, 0, -1):
#     print(i)

#Q 4 print the number multiplication table of a number n.

# n = int(input("inter number:"))

# for i in range(1, 11):
#     print(n * i)

#Q5 write a program to find the sum of first n numbers.(using while)

# n = 5 
# sum = 0 
# for i in range(1, n+1 ):

#   sum += i
# print(sum) 

#Q6 wap to the factorial of first n numbers. (using for)

n = 5 
fact = 1
i = 1
while i <= n:
    fact *= i
    i +=1

    print("factorial =",fact)


