# This is a program for binary search in a sorted array.


arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)
arr.sort()
a = int(input("Enter element to be searched:"))
low = 0
high = n-1
found = False
while(low<=high):
    mid= (high+low)//2
    if(arr[mid]<a):
        low = mid+1
    elif(arr[mid]==a):
        print(f"Element found at index {mid}")
        found = True
        break
    else:
        high = mid-1

if not found:
    print("Element not found in array")
