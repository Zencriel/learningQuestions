# Check if a inputted 3*3 matrix is a magic square

example = [[0] * 3 for i in range(3)]

for i in range(3):
    for j in range(3):
        example[i][j] = int(input(f"Enter your value at {i},{j} "))

maindiagonal = 0
seconddiagonal = 0


for i in range(3):
    maindiagonal = maindiagonal + example[i][i]
    seconddiagonal = seconddiagonal + example[i][3-i-1]


for i in range(3):
    rowsum = 0
    colsum = 0
    for j in range(3):
        rowsum = rowsum + example[i][j]
        colsum = colsum + example[j][i]

if (maindiagonal==rowsum==colsum):
    print("The inputted matrix is a magic square.")
else:
    print("The inputted matrix is not a magic square.")
