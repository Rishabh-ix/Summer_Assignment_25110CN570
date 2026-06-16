# This program finds intersection of arrays.


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
for i in arr1:
        if(i not in arr3 and i in arr2):
            arr3.append(i)
print("Intersection of these two arrays is:")
print(arr3)
