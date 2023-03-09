# Write a program to fill values in a 5*5 matrix to make a magic square

magicmatrix = [[0 for x in range(5)] for y in range(5)]

i = 2
j = 4

values = 1
while values <= (5 * 5):
    if i == -1 and j == 5:
        j = 3
        i = 0
    else:
        if j == 5:
            j = 0
        if i < 0:
            i = 4
    if magicmatrix[int(i)][int(j)]:
        j = j - 2
        i = i + 1
        continue
    else:
        magicmatrix[int(i)][int(j)] = values
        values = values + 1
    j = j + 1
    i = i - 1

for i in range (5):
    for j in range(5):
        print(magicmatrix[i][j], end=" ")
    print()