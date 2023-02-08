from array import array

numbers = array('i',[0]*10)

sum = 0
for i in range (10):
    numbers[i]=int(input("Enter your integer "))
for i in range(10):
    sum=sum+numbers[i]
print(sum)
