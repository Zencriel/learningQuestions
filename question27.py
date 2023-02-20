# WAP to initialise a matrix with 4 rows and 3 coloumns. Input and print values.

example = [[0]*3 for i in range(4)]

for i in range(4):
    for j in range(3):
        example[i][j]=int(input(f"Enter your value at {i},{j} "))
for i in range(4):
    for j in range(3):
        print(example[i][j], end=' ')
    print()