# This program finds frequency of an element in an array.

arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

a = int(input("Enter element whose frequency to be found:"))

count=0
for i in arr:
    if(i==a):
        count = count+1

print(f"Element occurs {count} times in array")