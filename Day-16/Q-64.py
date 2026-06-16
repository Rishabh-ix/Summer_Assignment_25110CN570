# This program removes duplicate elements from an array.

arr=[]
n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)
dupli = []
for i in arr:
    if i not in dupli:
        dupli.append(i)
print("After removing duplicate elements , new array is:")
print(dupli)