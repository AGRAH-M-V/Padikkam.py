import random
a=0
print("Guess a number within 1 and 100")
print("You have only 3 chances")
x = random.randrange(1,100)
while(a<3):
    n = int(input("Enter your selection: "))

    if n==x:
        print("You Won")
        break
    else:
        a+=1
        print(x)
        print("You Failed")
        print("You have only ",3-a," attempts left")
        
if a==3:
        print("GAME OVER")       
