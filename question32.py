# Sequential Search

N = [2,9,5,6,7,8]
X = 7

def inefficient():
    count = 0
    found = False
    for i in range (0,6):
        if N[count]==X:
            found = True
            print(f"Value found at index {count}.")
        count = count + 1
    if found == False:
        print(f"{X} not found.")

def efficient():
    count = 0
    found = False
    while (found==False) and (count<len(N)):
        for i in range (0,6):
            if N[count]==X:
                found = True
                print(f"Value found at index {count}.")
            count = count + 1
        if found == False:
            print(f"{X} not found.")
efficient()