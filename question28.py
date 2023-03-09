# WAP to find the sum of all values in the matrix of the previous question.
# WAP to find sum of third row.
# WAP to find sum of second coloumn.
# WAP to find sum of main diagonal.
# WAP to find no. of even values in the matrix.
# WAP to input a value and search the given value in the matrix.

def all():
    example = [[0] * 3 for i in range(4)]
    sum=0
    for i in range(4):
        for j in range(3):
            example[i][j] = int(input(f"Enter your value at {i},{j} "))
    for i in range(4):
        for j in range(3):
            sum=sum + example[i][j]
    print(f"The sum is {sum}")


def third_row():
    example = [[0] * 3 for i in range(4)]
    sum = 0
    for i in range(4):
        for j in range(3):
            example[i][j] = int(input(f"Enter your value at {i},{j} "))

    for j in range(3):
            sum = sum + example[3][j]
    print(f"The sum of third row is {sum}")

def second_coloumn():
    example = [[0] * 3 for i in range(4)]
    sum = 0
    for i in range(4):
        for j in range(3):
            example[i][j] = int(input(f"Enter your value at {i},{j} "))

    for j in range(3):
        sum = sum + example[j][2]
    print(f"The sum of second coloumn is {sum}")

def main_diagonal():
    example = [[0] * 4 for i in range(4)]
    sum = 0
    for i in range(4):
        for j in range(4):
            example[i][j] = int(input(f"Enter your value at {i},{j} "))
    for i in range(4):
            sum = sum + example[i][i]
    print(f"The sum of main diagonal is {sum}")

def evens():
    example = [[0] * 3 for i in range(4)]
    even = 0
    for i in range(4):
        for j in range(3):
            example[i][j] = int(input(f"Enter your value at {i},{j} "))
    for i in range(4):
        for j in range(3):
            if example[i][j]%2==0 and example[i][j]!=0:
                even+=1
    print(f"There are {even} even numbers.")

def search():
    example = [[0] * 3 for i in range(4)]

    for i in range(4):
        for j in range(3):
            example[i][j] = int(input(f"Enter your value at {i},{j} "))

    check = int(input("Enter a number to check in the array. "))

    for i in range(4):
        for j in range(3):
            if check==example[i][j]:
                print(f"{check} is in the array at {i},{j}")

search()
