# This is a program to Reverse an array.
#           OR
# We can also use (arr.reverse) to reverse an array.


arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

rev =[]
for i in range(n):
    p= arr.pop(n-1-i)
    rev.append(p)
print("Reversed array is:")
print(rev)