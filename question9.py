# The computer will generate a random number from 1 to 5, user will then make a guess, then cpu will make a guess, display who wins

import random
import time
def answer():
    a = (random.randint(1, 5))
    b = int(input("Guess the random number between 1 and 5 "))
    c = (random.randint(1,5))
    time.sleep(0.65)
    print(f"The computer has guessed {c}")
    time.sleep(0.5)
    if a==b==c:
        print("The CPU and user win!")
    elif (a==b) and (a!=c):
        print(f"The User wins!!! The CPU loses! The number was {a}")
    elif (a!=b) and (a==c):
        print(f"The user loses, but the CPU wins!!! The number was {a}")
    elif (a!=b) and (a!=c):
        print(f"Both the CPU and the User have lost! The number was {a}")
answer()