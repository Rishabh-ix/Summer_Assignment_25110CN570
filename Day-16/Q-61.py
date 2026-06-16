# This program finds missing element in an array.


arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

array_sum = 0
total_sum = 0
for i in arr:
    array_sum = array_sum + i
for i in range(1,n+2):
    total_sum = total_sum + i

element = total_sum - array_sum
print("Missing elemnt in array is:", element)