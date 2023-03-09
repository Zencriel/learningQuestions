# Write a program to create a 5*6 matrix called 'A'. Create another array and find the average of its values like in array5 worksheet.

A = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15], [16, 17, 18, 19, 20], [21, 22, 23, 24, 25]]

averagedarray = [[0] * 5 for i in range(5)]

for i in range(1,4):
    for j in range (1,4):
        averagedarray[i][j]= (A[i][j]+A[i-1][j]+A[i+1][j]+A[i][j-1]+A[i][j+1])
        averagedarray[i][j] = averagedarray[i][j]/5
for i in range (5):
    for j in range(5):
        print(averagedarray[i][j], end=" ")
    print()

