#read programe

# f = open(r"C:\Users\Hp\OneDrive\Documents\tushar.tech\Python\demo.text" ,"r")
# data = f.read()
# print(data)
# print(type(data))
# f.close()

#write programe

# f = open(r"C:\Users\Hp\OneDrive\Documents\tushar.tech\Python\demo.text" ,"w")

# f.write("i am learn java script ")

# f.close()

#aappend add karna 

# f = open(r"C:\Users\Hp\OneDrive\Documents\tushar.tech\Python\demo.text" ,"a")

# f.write("\n frome youtube")

# f.close()

#r+

# f = open(r"C:\Users\Hp\OneDrive\Documents\tushar.tech\Python\demo.text" ,"r+")

# f.write("i am ")

# f.close()

#deleting a file 

# import os 


# os.remove(r"")


#Q1 creat a new file practice.txt using python. add the following data 

# with open("practice.txt","w") as f: 
#     f.write("hi everyone \nwe are learning file I?0\n")
#     f.write("using java.\nI like programing in java.")

#Q2 waf that replace all occurrences of "java" with "python" in above file 

# with open("practice.txt","r") as f:
#     data = f.read()  

# new_data = data.replace("java", "python")
# print(new_data)

# with open("practice.txt","w") as f:
#     f.write(new_data)

#Q 3search if the word "learning" exists in the file or not.

with open(practice.txt, "r") as f:
    data = f.read()

