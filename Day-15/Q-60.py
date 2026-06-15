# This program moves all zeros in an array to the end.

arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)
zero=[]
for i in range(n):
    if(arr[i]!=0):
        zero.append(arr[i])
for i in range(n):
    if(arr[i]==0):
        zero.append(arr[i])

print("After all zeros moved to the end , Your resultant array is:")
print(zero)