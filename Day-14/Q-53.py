# This is a program for linear searching in an array.

arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

a = int(input("Enter element to be searched:"))

flag=0
for j in range(n):
    if(arr[j]==a):
       flag = flag+1
       location = j
       break
if(flag==1):
    print("Element found at index",location)
else:
    print("Element not found in array")

   


