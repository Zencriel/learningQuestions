# Input 5 names in an array, print all the names which start with "A"

names = [0]*5

for i in range(5):
    names[i]=input("Enter name: ")

for i in range(5):
    if names[i].startswith("A"):
        print(names[i])