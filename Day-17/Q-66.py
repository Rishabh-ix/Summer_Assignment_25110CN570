# This program finds union of arrays.


arr1=[]
arr2=[]
n1 = int(input("Enter number of elements in first array: "))
n2 = int(input("Enter number of elements in second array: "))
print("Enter elements of first array:")
for i in range(n1):
    value = int(input("Enter element: "))
    arr1.append(value)
print("Enter elements of second array:")
for i in range(n2):
    value = int(input("Enter element: "))
    arr2.append(value)
arr3=[]
for i in range(n1):
    arr3.append(arr1[i])

for i in range(n2):
    if(arr2[i] not in arr3):
        arr3.append(arr2[i])
print("Union of these arrays is:")
print(arr3)

