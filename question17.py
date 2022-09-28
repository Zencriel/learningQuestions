#empty list

def myprog():
    a = []
    b = 0
    for i in range(5):
        c = int(input("Enter your number "))
        a.append(c)
    print(a[1])
    print(a[3])
    for i in range(5):
        b=b+a[i]
    print(f"The sum is {b}")
myprog()