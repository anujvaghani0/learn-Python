# print("hello world")

# Open
# use to open a files
f=open('greet.txt','r')
f=open('greet.txt')  #'r' are by defualt used
data=f.read()
data=f.read(6)  #use reange defind
print(data)
f.close()


# Openline
f=open('greet.txt','r')
#how many time to print readline to print one line by line
#read a first line
data=f.readline();
print(data);
#read a secound line
data=f.readline();
print(data);
#read a third line
data=f.readline();
print(data);
# f.close()

# write
f=open('greet1.txt','w')
data=f.write("fllow in github-->")
print(data)

# append mode
f=open('greet1.txt','a')
data=f.write("anujvaghani0")
print(data)
f.close();

# with statment
with open ('greet.txt','r') as f:  #use with do not write a close option
    a=f.read()
with open ('greet1.txt','w') as f:
    a=f.write('anujvaghani0')
print(a)

