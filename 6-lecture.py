#function in python 

# a = 5 
# b = 10 

# sum = a + b 
# print(sum)

# #more lines of code 

# a = 2 
# b = 10 

# sum = a + b 
# print(sum)

#right code #redanddency kam karna 

# def calc_sum(a, b):
#     sum = a + b
#     print(sum) 
#     return sum 

# calc_sum(2, 5)

# calc_sum(4, 6)

# def calc_sum(a, b): #parameters
#     return a + b

# sum = calc_sum(2, 4) #function call; arguments
# print(sum)


#avrage of 3 numbers 

# def calc_avg(a, b, c):
#     sum = a + b + c 
#     avg = sum / 3 
#     print(avg)
#     return avg

# calc_avg(98, 97, 95) 

#built-in fungtion  

# print("sage university","tushar") #sage university 
                                     #tushar

# print("sage university",end=" ") # #sage university tushar
# print("tushar")


# len()
# range()
# type()


#user defind fungtion 


#default parameters 

# def calc_prod(b, a=5):
#     print(a * b)
#     return a * b
# calc_prod()

#Q1 wap to print the length of a list. (list is the parameter)

# cities = [ "delhi","gurgaon","noida","pune","mumbai","channai"]

# def print_len(list):
#     print(len(list))

# print_len(cities)

#Q2 w a factriol 

# def calc_fact(n):
#     fact = 1 
#     for i in range(1, n+1):
#         fact *= i
#         print(fact)

#     calc_fact(5)


    #Q3 


# def converter(usd_val):
#         inr_val = usd_val * 83
#         print(usd_val, "usd = ",inr_val, "inr"),
# converter(77)

#Recursion  jo kud ko bar bar call karta he 

# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n-1)

# show(5)

def fact(n):
    if(n == 0 or n == 1):
        return 1 
    return fact(n-1) * n

print(fact(4))