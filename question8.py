# Write a program which generates a random number from 0-5, user will try to guess the random number, if user guesses right display You Win!

import random
def answer():
    a=(random.randint(0,5))
    b=float(input("Guess the random number between 0 and 5 "))
    if a==b :
        print("Congratulations, you guessed it right!")
    else:
        print(f"You were wrong! The number was {a}")
answer()