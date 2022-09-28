# Write a program to  input 100 values into a list, square all the values in the list and copy those values in another list. Display the new list.

def myprog():
    a=[]
    c=[]
    for i in range(100):
        b=int(input("Enter your number "))
        a.append(b)
    for n in range(100):
        d=(a[n]*a[n])
        c.append(d)
    print(c)
myprog()
