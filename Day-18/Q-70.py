# This is a program for selection sorting.



arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)


for i in range(n-1):
    smallest = i
    for j in range(i+1 , n):
        if(arr[j]<arr[smallest]):
            smallest = j
    temp = arr[i]
    arr[i] = arr[smallest]
    arr[smallest] = temp 
print("Sorted array is:")
print(arr)
