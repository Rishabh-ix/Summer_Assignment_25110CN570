

arr = []
n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

sum=0
for i in arr:
    sum = sum +i
print("Sum of elements of array is:",sum)
average = sum/n
print("Average of elements of array is:",average)
