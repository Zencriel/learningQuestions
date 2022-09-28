# Write a program to input name and age, if age >=18 display you are eligible, else display you are not

import time
def answer():
    name=input("Enter your name ")
    age=float(input("Enter your age "))
    print(f"Hello {name}! Thanks for your application.")
    time.sleep(0.75)
    if age>=18:
        print(f"{name} you are eligible!")
    else:
        print(f"Sorry {name}! You are not eligible.")
answer()