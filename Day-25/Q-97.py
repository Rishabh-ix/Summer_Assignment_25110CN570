# This is a program to merge two sorted array.

arr1 = []
arr2 = []
n1 = int(input("Enter number of elements in first array: "))
print("Enter elements of first array: ")
for i in range(n1):
    value = int(input("Enter element: "))
    arr1.append(value)

n2 = int(input("Enter number of elements in second array: "))
print("Enter elements of second array: ")
for i in range(n2):
    value = int(input("Enter element: "))
    arr2.append(value)
i=0
j=0
arr3 = []
i = 0
j = 0
arr3 = []

while i < n1 and j < n2:
    if arr1[i] <= arr2[j]:
        arr3.append(arr1[i])
        i += 1
    else:
        arr3.append(arr2[j])
        j += 1

while i < n1:
    arr3.append(arr1[i])
    i += 1

while j < n2:
    arr3.append(arr2[j])
    j += 1
print("Merged array is: ")
print(arr3)
    


