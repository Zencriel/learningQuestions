# Write a program to input marks in 3 subjects, if total >= 180 display Excellent, if total < 180 and total>= 150 display very good, else display work hard

import time
def answer():
    a=float(input("Enter score for first subject "))
    b=float(input("Enter score for second subject "))
    c=float(input("Enter score for third subject "))

    time.sleep(0.65)
    total= a+b+c
    if total>= 180:
        print("Excellent!")
    elif (total<180) and (total>=150):
        print("Very Good!")
    else:
        print("Work harder!")
answer()