import random

def guess_number(num1):
    num=random.randrange(1,50)
    if num==num1:
        print("WINNER")
    else:
        print("TRY AGAIN")
        start()

print("Welcome to Number Guessing Game")       

def start():
    number=int(input("enter a number btn 1 and 50: "))
    guess_number(number)

start()
