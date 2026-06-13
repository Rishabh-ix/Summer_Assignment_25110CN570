# This program finds largest and smallest elemnet in an array


arr = []
n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

largest = arr[1]
smallest = arr[1]
for i in arr:
    if(i>largest):
        largest=i
print("Largest element in array is:",largest)
for i in  arr:
    if(i<smallest):
        smallest=i
print("Smallest element in array is:",smallest)
