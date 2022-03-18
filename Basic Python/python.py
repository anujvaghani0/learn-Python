# from math import factorial
import os
import this

# from unicodedata import name
# from playsound import playsound


# playsound('C:/Users/anujv/Downloads/tic tac toe/tic tac toe#/gameover.mp3')
# print("hello world");
# print(3+6)
# print(os.listdir())

# a=30
# b="anuj"
# a="40"
# b=30
# b+=52
# print("anuj vaghani")
# print(b)
# print(type(b))


# a="26"
# a=int(a);
# b=25
# print(type(a))
# print(a+b)

# a=input("enter the number")
# a=int(a);
# print(type(a));

# a="anuj"
# b="vaghani anuj rohit sharma"
# print(a[-1])
# print(a[0:3])
# print(b[0:3:2])
# print(len(b))
# print(a.endswith("anuj"))
# print(b.count("a"))
# print(b.capitalize())
# print(b.find("vaghani"))
# print(b.replace("rohit","hit-man"))

# st="hello my name is \n anuj\t \\ vaghani"
# print(st);

# name1=input("Enter your name:")
# print("good afternoon,"+name1)
    
# letter='''Dear <|NAME|>,
# You are selected!
# Date:<|Date|
# '''

# name=input("enter the your name")
# date=input("Enter the date")
# letter=letter.replace("<|NAME|>",name);
# letter=letter.replace("<|Date|",date)
# print(letter)

#list 
# a=[10,20,30,40,50]
# print(a[1])

#list are string as well inclued
# a=["anuj","vaghani",16,56,"hello"]
# print(a[0])
# print(a[0:4])

# a=[10,60,58,64,25,78]
# a.sort()
# a.reverse()
# a.append(45)  #last of list
# a.insert(2,5)
# a.pop(2)
# a.remove(64)
# print(a)

# Tuple
# t=(1,2,4,5,6,1,2,1,21,1,1,1,25,1)
# print(sum(t))
# t1=()  #Empty tuple
# t2=(1,)
# prin
# t(t[0])
# t[0]=45  #throws a error
# print(t.count(1))
# print(t.index(5))
  
#   Dictionary

# myDict={
#     "fast":"In a quicker manner",
#      "anuj":"i hv guniuse",
#      "dic":{
#          "rohit":597,
#          "virat":569
#      },
# }
# print(type(myDict.keys()))
# print(list(myDict.keys()))
# print([myDict["anuj"]])
# print(myDict["dic"]["rohit"])

# update_mydict={
#     "anuj2":"vaghani"
# }
# myDict.update(update_mydict)
# print(myDict)
# print(myDict.get("nuja"))

# Sets
# a={1,5,6,5,6,8,10}
# print(type(a))
# print(a)

# Empty set created
# a=set();
# print(type(a))
# a.add(45);
# a.add(56)
# a.add(70)
# a.add((4,5,6))

# a.remove(56)  #remove a set element
# print(a)

# length of set element
# print(len(a))

# Practicas question-6
# favlang={}
# a=input("enter the fav lang")
# b=input("enter the fav lang")
# c=input("enter the fav lang")
# d=input("enter the fav lang")
# favlang["anuj"]=a
# favlang["jay"]=b
# favlang["aashurt"]=c
# favlang["dharmik"]=d
# print(favlang)

# s={25,"anuj",8,7,12,[12,25]};   #do not store a set in list element
# print(s)
# print(s)           
  

# A=input("enter the numbere")
# A=int(A)
# print(A)

# if(A>45):
#     print("more 45")
# else:
#     print("more ")
    
# age=45
# if age<45 and age>45:
#     print("hello")
# else:
#     print("hello 2")

# IS
# a=None;
# if (a is None): #is as compresson to a equle to none or not
#     print("yes")
# else:
#     print("no");

# IN
# a=[456,256,36] #Element are present in list or not that are show in
# print(256 in a)

# a=int(input("Enter the number"))
# b=int(input("Enter the number"))
# c=int(input("Enter the number"))
# d=int(input("Enter the number"))

# if (a>b):
#     if (a>c):
#         if (a>d):
#             print("a is large")
#         else:
#             print("d is large")
#             elif (b>c):
#                 if (b>d):
#                     print("b is large")

# a=input("enter the name")
# b=True
# a=a.upper();
# print(a)  

# loop
# a=0
# while a<10:
#     print("yes " + str(a))
#     a=a+1

# crickter=["rohit","virat","smith","iyer","mayank","hanuma"]
# i=0
# while i<len(crickter):
#     print(crickter[i]);
#     i=i+1;

# crickter=["rohit","virat","smith","iyer","mayank","hanuma"]
# for item in crickter:
#     print(item)

# for i in range(2,8,2):
#     print(i)

# For else together
# for i in range(10):
#     print(i);
# else:
#     print("done")
        
# for i in range(10):
#     print(i)
#     if i==5:
#      break;
# else:
#     print("done")

# Continue    
# for i in range(10):
#     if i==5:
#      continue;
#     print(i)
# else:
#     print("done")

# pass to use to no activity are further do
# i=0;
# if i==0:
#     pass
    
# num= input("enter")
# num=int(num);
# for i in range(1,11):
    # print(str(num)+ " X" + str(i)+ " = "+ str(num*i))
    # print(f"{num}X{i}={num*i}")

# crickter=["rohit","virat","smith","iyer","mayank","hanuma"]
# for item in crickter:
#     if item.startswith("s"):
#         print("hello " + item)

# num= input("enter")
# num=int(num);
# prime=True
# for i in range(2,num):
#     if (num%i==0):
#         prime=False
        
# if prime:
#     print("given num are prime")
# else:
#     print("given num are not prime")
        
# num= input("enter")
# num=int(num);
# f=1
# for i in range(1,num+1):
#     f=f*i
# print(f"the number are {f}")

# n=4
# for i in range(4):
#     print("* "*(i+1))

# n=3
# for i in range(3):
#     print(" " * (n-i-1),end="")
#     print("*" * (2*i+1),end="")
#     print(" " * (n-i-1))

# Function


# marks=[10,20,30,47,70]
# p1=(sum(marks)/4)*100;
# marks2=[10,20,30,47,70]
# p2=(sum(marks)/4)*100;
# print(p1,p2);

# def persent(marks):
#     return ((marks[0]+marks[1]+marks[2]+marks[3]+marks[4])/500)*100;

# marks1=[100,200,300,400,500]
# p1=persent(marks1);
# print(p1)

# def greet(name):
#     print("Hello! good Morning "+name);

# greet("anuj");

# factorial
# p=1
# n=5
# for item in range(n):
#     p=p*(item+1);
#     print(p)
    
    # Function use to factorial
# def Fectorial(n):
#     p=1
#     n=5;
#     for item in range(n):
#         p=p*item+1;
#     return p;

# print(factorial(5))


# Function Recursion use to find a factorial
# def Fectorial_R(n):
#     if n==1 or n==0:
#       return 1;
#     else:
#         return n*Fectorial_R(n-1);
       

# print(Fectorial_R(5))

# problem-1
# def max(a,b,c):
#     if a>b:
#         if a>c:
#           return a;
#         else:
#            return c;
#     else:
#         if b>c:
#             return b;
#         else:
#             return c;

# print(max(5,600,58))
            
# n=6
# for item in range(n):
#     print("* "*(n-item))
    
# this="   anuj vaghani   "
# print(this)
# print(this.strip())

def rms(string,word):
    newstring=string.replace(word,"");
    return newstring
this="anuj vaghani anuj anuj vaghani"
print(this)
n=rms(this, "anuj")
print(n);