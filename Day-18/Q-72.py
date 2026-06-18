# This is a program to bubble sorting in descending order



arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

for i in range(n-1):
  for j in range(n-1-i):
    if(arr[j]<arr[j+1]):
        temp = arr[j]
        arr[j] = arr[j+1]
        arr[j+1] = temp
print("Sorted array is:")
print(arr)


        