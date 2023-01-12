# Write a program to generate a number from 1-10, user will guess the number. After each guess, the user will be asked to continue the program or not.
# If the user chooses 'Y' it should continue, if not end program.

import random
def myprog():
    a=random.randint(1,10)
    while True:
        b=int(input("Guess number "))
        if a==b:
            print("You Win")
        else:
            print("You lost")
        c = input("Do you want to continue? Y/N ")
        if c.upper() == "Y":
            continue
        else:
            break
myprog()
