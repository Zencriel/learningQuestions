# program to take 4 inputs and output how many negative numbers and positive numbers there are (class question of turning flowchart into code)
#inputs are (1,-5,2,-8,-7)

def real():
    C=0
    neg=0
    pos=0
    while C < 5:
        N=int(input("Enter your number "))
        if N<0:
            neg=neg+1
        elif N>0:
            pos=pos+1
        C=C+1
    if C >= 5:
        print(f"There are {pos} positive numbers and {neg} negative numbers in your input." )
        print(f"There were a total of {C} inputs.")

real()