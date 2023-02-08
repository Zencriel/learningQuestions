from array import array

numbers = array ('i',[0]*10)

min=0
max=0

for i in range(10):
    numbers[i]=int(input("Enter your integer "))
    if numbers[i]>max:
        max=numbers[i]
    min=numbers[0]
    if numbers[i]<min:
        min=numbers[i]
print(f"Max is: {max}")
print(f"Min is: {min}")