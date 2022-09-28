# write a program to add 100 integer values in a list. Display how many even and odd numbers are in the list.

import random
def myprog():
    a=[]
    even=0
    odd=0
    for i in range(100):
        b = random.randint(0,20)
        a.append(b)
    for n in range(100):
        if a[n]%2==0:
            even=even+1
        else:
            odd=odd+1
    print(a)
    print(f"There are {even} even numbers.")
    print(f"There are {odd} odd even numbers.")
myprog()
