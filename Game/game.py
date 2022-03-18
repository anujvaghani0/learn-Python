import random

def game(comp,you):
    if comp == you:
        return None

    # Check for all possibilities when computer chose s
    elif comp == 's':
        if you=='w':
            return False
        elif you=='g':
            return True
    
    # Check for all possibilities when computer chose w
    elif comp == 'w':
        if you=='g':
            return False
        elif you=='s':
            return True
    
    # Check for all possibilities when computer chose g
    elif comp == 'g':
        if you=='s':
            return False
        elif you=='w':
            return True

print("computer Turn: Snake(s) Water(w) or Gun(g)");
randno=random.randint(1,3);
if randno==1:
    comp="s"
elif randno==2:
    comp="w";
else:
    comp="g";
    
you=input("Player 2 Turn: Snake(s) Water(w) or Gun(g)");
a=game(comp,you)
print(f"computer chose{comp}")
print(f"you chose{you}")

if a==None:
    print("match is a tie")
elif a:
    print("You Win!")
else:
    print("You Lose!")