# Write a program to input 3 numbers, display sum and average

def answer():
    a = float(input("enter first number "))
    b = float(input("enter second number "))
    c = float(input("enter third number "))
    sum= a+b+c
    average=sum/3
    print(f"sum is {sum}")
    print(f"the average is {average}")
answer()