# This is a program to merge arrays.


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
for i in arr2:
    arr1.append(i)
print("After merging both arrays , the resultant array is: ")
print(arr1)