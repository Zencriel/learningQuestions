# WAP to input values in 3*2 Matrix and print all values.

from array import *

example = [[0 for j in range(2)]for i in range(3)]

for i in range(0,3):
    for j in range(0,2):
        example[i][j]=int(input(f"Enter your value at {i},{j} "))
for i in range(0,3):
    for j in range(0,2):
        print(example[i][j])