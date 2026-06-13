# This program counts even and odd elements in array.


arr = []
n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)
even = 0
odd = 0
for i in arr:
    if(i%2==0):
        even= even+1
    else:
        odd=odd+1

print("Number of odd element in array is:",odd)
print("Number of even element in array is:",even)

