# opp in python 
#crating class
# class Student: 
#     name = "tushar"
      
# s1 = Student()
# print(s1.name)

# s2 = Student()
# print(s2.name)


# class Car:
#     color = "red"
#     brand = "maruti"

# car1 = Car()
# print(car1.color)
# print(car1.brand)

# __init__ fungtion 

#creating object 

#default constructors

#..................................................................................................................

#class Student: 
    # def __init__(self, name, marks):
    #     pass
#parameterized constructors 
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
# s1 = Student("karan","97")
# print(s1.name,s1.marks)
 
# s2 = Student("arjun","88")
# print(s2.name,s2.marks)

#class & instance attributes ( attribute matlb data)
 #class
# class Student: 
#    collage_name = "SAGE BHOPAL"
#    def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#    def wellcome(self):
#        print("wellcome student", self.name)
# #objeccet
# s1 = Student("karan","97")
# print(s1.name,s1.marks)
 
# s2 = Student("arjun","88")
# print(s2.name,s2.marks)

# print(s2.collage_name)
# s2.wellcome()  

#Q1 creat student class that takes name & marks of 3 subject as arguments in construuctor 

# class student:
 
#     def __init__(self, name, marks):  #constructor
#         self.name = name 
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val 
#         print("hi",self.name,"your avg score is:",sum/3)

# s1 = student("tushar",[99, 98, 97])
# s1.get_avg()

# s1.name = "poonam"
# s1.get_avg()


#static methods #methods that don't use the self parameter (works at class level)

# class student:
#     @staticmethod #decoratore 
#     def hello():
#         print("hello") 
        
# student.hello()

#important 

#Abstraction 

#hiding the implementation details of a class and only showing the essential features to the user 

# class car:
#     def __init__(self):
#         self.acc = False
#         self.clutch = False
#         self.brack = False

#     def start(self):
#         self.clutch = True
#         self.brack = False
#         print("car started..")
# car1 =car()
# car1.start()

#Encapsulation 

#wrapping data and fungtions into a single unit (object).

#class attribut object all 





#Q4 creat account class with 2 attributes - balance & account me 

# class account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc 

#     #dabit method 
#     def debit(self, amount ):
#         self.balance -= amount 
#         print("Rs", amount, "was debited")
#         print("total balance = ", self.get_balance())

#     #credit method 
#     def credit(self, amount ):
#         self.balance += amount 
#         print("Rs", amount, "was credited")
#         print("total balance = ", self.get_balance())


#     def get_balance(self):
#         return self.balance
    

# acc1 = account(10000, 12345)
# acc1.debit(1000)
# acc1.credit(500)
# acc1.credit(40000)
# acc1.debit(1000000)


# oops part 2 


#del keyword 
#used to delete object properties or object itself 

# class student:
#     def __init__(self, name ):
#         self.name = name 
    
# s1 = student("poonam")
# print(s1.name)
# del s1.name
# print(s1.name)

#privat(like)attributes & methods 

# class account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.acc_pass = acc_pass 

# acc1 = account("12345", "abcde")

# print(acc1.acc_no)
# print(acc1.acc_pass)

#privet attribute 

# class account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass 

# acc1 = account("12345", "abcde")

# print(acc1.acc_no)
# print(acc1.__acc_pass)

#only class ke ander acces

# class account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.acc_pass = acc_pass 

#     def reset_pass(self):
#         print(self.__acc_pass)


# acc1 = account("12345", "abcde")

# print(acc1.acc_no)
# print(acc1.reset_pass)


# class person:
#     __name = "anonymous"

#     def __hello(self):
#         print("hello person")
 
#     def wellcome(self):
#         self.__hello()

# p1 = person()

# print(p1.wellcome()) 


#inheritance
# when one class(child/derived) dderives the properties & methods of another class (prent/base)

# class car:
#     color = "blue"
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped.")

# class toyotacar(car):
#     def __init__(self, name):
#         self.name = name


# car1 = toyotacar("fortuner")
# car2 = toyotacar("inova")

# print(car1.color)

# inheritance type 
#. singel inheritance 
#. multi-level inheritance 
#. multiple inheritance 



#single inheritance 

# class car:
#     color = "blue"
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped.")

# class toyotacar(car):
#     def __init__(self, name):
#         self.name = name


# multi level inheritance

# class car:
#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped.")

# class toyotacar(car):
#     def __init__(self, brand):
#         self.name = brand

# class fortuner(toyotacar):
#     def __init__(self, type):
#        self.type = type 

# car1 = fortuner("diesel")
# car1.start()


# class A:
#     varA = "wellcome to class A"

# class B:
#     varB = "wellcome to class B"

# class C(A, B):
#     varC = "wellcome to class C"

# c1 = C()

# print(c1.varC)
# print(c1.varB)
# print(c1.varA)


#super method 


# class car:
#     def __init__(self, type):
#         self.type = type

#     @staticmethod
#     def start():
#         print("car started..")

#     @staticmethod
#     def stop():
#         print("car stopped.")

# class toyotacar(car):
#     def __init__(self, name, type):
#         self.name = name
#         super().__init__(type)
#         super().start()

# car1 = toyotacar("inova","electric")
# print(car1.type)

#class method 

#note - static method can't access or modify class state & generally for utility 

# class person:
#     name = "anonymous"

#     def changename(self, name):
#         #self.name = name
#         #person.name = name
#         self.__class__.name = "tushar"
# p1 = person()
# p1.changename("tushr singour")
# print(p1.name)
# print(person.name)



# class person:
#     name = "poonam"

#     @classmethod
#     def changename(cls, name):
#         cls.name = name 

# p1 = person()
# p1.changename("tushar")
# print(p1.name)




class student:
    def __init__(self, phy, che, math):
        self.phy = phy
        self.che = che
        self.math = math
        self.percentage = str(self.phy + self.che + self.math /3) + "%"


    #def calcpercentage(self):
        #self.percentage = str(self.phy + self.che + self.math /3) + "%"

        @property
        def percentage(self):
            return str(self.phy + self.che + self.math /3) + "%"
 
stu1 = student(98, 88, 77)
print(stu1.percentage)

stu1.phy = 86
print(stu1.percentage)