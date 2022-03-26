import os

f=open('poems.txt','r')
data=f.read()
if 'literature' in data:
    print('find out')
else:
    print("good")
        
print(data)
f.close();

# Problam-->2
def game():
    return 700

score=game()
with open("hiscore.txt") as f:
    hiscore=int(f.read());

if hiscore <score:
    with open('hiscore.txt','w') as f:
        f.write(str(score))

# Problam-->3
for i in range(2,21):
    with open (f"tables/multipliction{i}.txt",'w') as f:
        for j in range(1,11):
            f.write(f"{i}X{j}={i*j}\n")
        

# Problam-->4
with open("greet.txt") as f:
    content=f.read();
content=content.replace("anuj VAGHANI"," ")
with open("greet.txt",'w') as f:
    f.write(content)

# Problam-->6
content=True
i=1
with open("log.txt") as f:
    while content:
        content=f.readline();
        if 'anujvaghani0' in content:
            
            print(content)
            print("Yes follow")
            print(f"{i}")
        i+=1

# Problam-->7
from importlib.metadata import files


with open("greet.txt") as f:
    content=f.read();

with open("copy.txt",'w') as f:
    f.write(content)        

# Problam-->8
# both file are same or not checked

file1="greet.txt"
file2="copy.txt"

with open('greet.txt') as f:
    f1=f.read()
with open('copy.txt') as f:
    f2=f.read()

if f1==f1:
    print("both files are same")
else:
    print("not a both files are same")

# Problam-->9
# rename files
oldname="greet1.txt"
newname="github.txt"

with open(oldname) as f:
    content1=f.read()
with open(newname,'w') as f:
    f.write(content1)

os.remove(oldname)