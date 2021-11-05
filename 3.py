import random as rnd
num = rnd.randint(0,100)
inpt = int(input("Please enter an integer"))
while not inpt == num:
    if inpt < num:
        print("increase your number")
        inpt = int(input("Please enter an integer"))
    elif inpt >num:
        print("decrease your number")
        inpt = int(input("Please enter an integer"))
print("you did it!!!")
