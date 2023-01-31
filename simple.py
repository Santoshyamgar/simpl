# def decor(fun):
#     def inner():
#         print("IF: Before encing function")
#         fun()
#         print("IF: Before Enhancing Function")
#     return inner

# def num():
#     print("we will use thise function")
#     print(" and will enhance this in decorator")

# ressult=decor(num)
# ressult()  

#############################################################################################
# decoretor

# def decor1(num):
#     def inner():
#         b = num()
#         multi = b * 5
#         return multi
#     return inner 

# def decor(num):
#     def inner():
#         a = num()
#         add = a + 5
#         return add
#     return inner
# @decor
# @decor1
# def num():
#     return 10
# num = decor(decor1(num))
# print(num)    


####################################################################################

# def myfun():
#     print("my recorsion function")
#     myfun()

# myfun()    

##################################################################################


# a = [1,2,3,4,5]
# print("before appendin:")
# for i in a:
#     print(i)

# print("after appending:")
# a.append(6)
# print(a)    


####################################################################################


# a = []

# n = int(input("enter the no :"))
# for i in range(n):
#     a.append(int(input("enter the no :")))

# print("list")
# for i in a:
#     print(i)
######################################################################################################

# a = [1,2,3,4,5,1,2,45]
# a.insert(62,'appu')
# for i in a:
#     print(i)
  
###############################################################################################################

# a = [1,2,3,45,6,5,0,4,7]
# b = ['geeky',54]
# a.append(b)
# print(a)

#################################################################################

# a = [10,20,30,40]
# b= a.copy()
# print("A:",a)
# print("b",b)

# print()
# print('modification A')
# a[1]=12

# print("A:",a)
# print("b",b)

# print()
# print('modification A')
# b[1]=12

# print("A:",a)
# print("b",b)

##############################################################################################################

#index

# a = [10,20,30,[50,60]]
# print(a[3][0])

#####################################################################################

# nested for loop

# a = [[10,20,30,40],[60,70]]
# for i in a:
#     for c in i:
#         print(c)

####################################################################################################
#using filter function 
# a = [10,20,30,40,50,60,61,62,66,67,70]
# result=list(filter(lambda n :(n>60), a))
# print(result)

# for i in result:
#     print(i)


##############################################################################################################
# map using 

# a = [10,20,30,40,50]
# def inc(n):
#     return n+2
    
# result = list(map(inc, a))
# print(result)
# for i in result:
#     print(i)

#out put
# [12, 22, 32, 42, 52]
# 12
# 22
# 32
# 42
# 52
#######################################################################################################################
 # reduse function
# from functools import reduce

# a = [10,20,30,40,50]
# reslt = reduce(lambda n,m: n+m, a)
# print(reslt)

#########################################################################################################

# generetor in python

# def disp(a,b):
#     yield a
#     yield b

# result = disp(10,20)
# a = list(result) 
# print(a)   

# def show(a,b):
#     while a<=b:
#         yield a
#         a+=1
# result = show(1,5)
# print(next(result))  
# print(next(result)) 

# for i in result:
#     print(i)


##########################################################################################################################
# tuple using for loop

# a = (10,20,30,20.1,'geekyshow')
# n = len(a)
# for i in range(n):
#     print(a[i])

# using while loop

# a = (10,20,30,20.1,'geekyshow')
# n = len(a)
# i = 0
# while i>0:
#     print(a[i])
#     i+=1

###########################################################################################################################################

# modify the truple using slice

# a = (10,20,30,40,50,'geekyshow')
# print(a)
# c = (101, 102)
# s1 = a[0:1]
# s2 = a[2:]
# tup3 = s1+c+s2
# print(tup3)


#tuple

# a = []
# n = int(input("enter the Number:"))
# for i in range(n):
#     a.append(int(input("enter the number:")))

# print(type(a))
# print(type(a))
# print("tuples:")
# for i in a:
#     print(i)



#repet element
# a = (1,2,3,4)
# print(a)

# result = (a * 3)
# print(result)



####################################################################
    
# how to pass tuple in function

# def show(t):
#     print(t)

#     for i in t:
#         print(i)
# tup = (10,20,30,40,50,"geekyshow") 
# show(tup) 

# passing and Return tuple 

# def show(t):
#     print(t)

#     for i in t:
#         print(i)
#     return i    
# tup = (10,20,30,40,50,"geekyshow") 
# newtup= show(tup) 
# print(newtup)

#####################################################################################################

# sets

# a = [10,20,30,40,'geekyshow']
# a.sort()
# print(a)

# a = [10,20,30,40,'geekyshow']
# b= a[::-1]
# print(b)

# a = {10,20,30,"geekyshow"}
# a.add('python')
# print(a)

#####################################################################################################

# Dicitionary in python


# a = {1:'santosh',2:'samadhan'}
# a[3]="geekyshow"
# print(a)


# a = {1:'santosh',2:'samadhan', 3:'geekyshow'}
# b=a[3]
# print(b)


# a = {1:'santosh',2:'samadhan',3:'geekyshow'}
# b=a['geekyshow']
# print(b)


# a = {1:'santosh',2:'samadhan'}
# print(a.get(1))


# a = [1,2,3,4,5]
# a.pop(1)
# print(a)


# a = {}
# n = int(input("Enter the Elements: "))
# for i in range(n):
#     k = input("Enter key: ")
#     v = input("Enter the value: ")
#     a.update({k:v})

# print(a) 
# 
#    



##################################################################################

# print(r"santosh yamgar\\samadhan")
# print("line A \\n Line B") 
# print("\U0001F602")
# print("\U0001F618")

################################################################################

# a = input("enter the name :")
# print("hello" + a)

# number=input("enter the number")
# number1 = input("enter the number")
# total = number+number1
# print("tpotal is" + total)

# num = str(4)
# num = float("4")
# print(num)

# name , age = "santosh", "25"
# print("hello "  + name + " ypor age is"+age)
# name, age = input("enter yor name and age").split()
# print(name)
# print(age)


# name= "sam"
# age = 20
# print(f"hello {name} yor age {age}".format(name,age))

# num1 = input("enter the first no :")
# num2 = input("enter the second no :")
# num3 = input("enter the third no :")
# print(f"avragew")

#################################################################################################################
#string

# a = 'santosh'
# print(a[5::-1])


# a = input("enter the string :")
# print(a[::-1])

# a = "    santosh      "
# print(a.lstrip())



# name = ""
# if name:
#     print("string is not empty")

# else:
#     print("string is empty")    


#############################################################################

# total = 0
# for i in range(1,20):
#     total += i
# print(total)    

# class A:
#     def add():
#         a =12
#         b= 10
#         c=a+b
#         print(c)
# obj=A
# obj.add()      
###############################################################################  


# class Mobile:
#     def __init__(self):
#         self.model='Realme'

#     def show_model(self,p):
#         self.price=p
#         print("model:",self.model, "price:", self.price)

# obj=Mobile()
# obj.show_model(100)        

##############################################################################################

# class Mobile:
#     def __init__(self):
#         self.model = "realme X"

#     def show_model(self):
#         return self.model

# obj = Mobile()
# a = obj.show_model()
# print(a)      
# 
# 
# ##################################################################################################
      

# class method


# class Mobile:
#     fp = 'Yes'

#     @staticmethod
#     def show_model(cls,r):
#         cls.ram = r
#         print("Fingerprint :" ,cls.fp)
#         print("RAM",cls.ram)
# realme=Mobile()
# Mobile.show_model('4GB')



################################################################################################################

#static Method

# class Student:
#     def __init__(self,n,r):
#         self.name = n
#         self.roll = r

#     def disp(self):
#         print("student name:", self .name)
#         print("student roll no :", self.roll)    

# class User:
#     @staticmethod
#     def show(s):
#         print("user name :",s.name) 
#         print("user roll no :",s.roll)
#         s.disp()

# stu = Student('Rahul',101)
# User.show(stu)   
# 
################################################################################################################################################

# inheritance 


# class father:

#     money = 1000

#     def show(self):
#         print("present class insdtance method")

#     @classmethod
#     def showmoney(cls):
#         print("present class class method:",cls.money)

# class son(father):
#     def disp(self):
#         print("child class instance method")

# s = son() 
# s.disp()   
# s.show()   
# s.showmoney() 

#####################################################################################################################################

# class Sam:
#     def __init__(self):
#         self.name = 'santosh'

#     def san(self):
#         print(self.name)
# s = Sam()
# s.san()
       






