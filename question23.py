# Input 10 values in an Integer array, then print only the values that are even.

from array import array

numbers = array('i',[0]*10)

for i in range(10):
    numbers[i]=int(input("What is your integer? "))
for i in range(10):
    if numbers[i]%2==0:
        print(numbers[i], end=' ')