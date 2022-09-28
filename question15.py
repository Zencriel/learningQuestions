# write a program to generate a number from 1 to 10, user will then try to guess the random number 3 times, then display how many times user guessed it right or wrong

import time
import random
import sys
def answer():
    a = (random.randint(1, 10))
    print("Guess a number 1 through 10 with 3 tries!")
    time.sleep(0.5)
    b=int(input("Enter your first number "))
    if a == b:
        print("Congratulations! You got it right on the first try!")
        sys.exit()
    else:
        print("That was wrong! Try again.")
    c=int(input("Enter your second number "))
    if a == c:
        print("Congratulations! You got it right on the second try!")
        sys.exit()
    else:
        print("That was wrong! Try again!")
    d=int(input("Enter your third and final guess "))
    if a == d:
        print("You got it right on the Final try!")
        sys.exit()
    else:
        print(f"That was wrong! You are out of guesses. The number was {a}")
answer()

