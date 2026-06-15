# This program rotates array left by r position.

arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

r = int(input("Enter by how many position the array should be rotated left:"))

for i in range(r):
    p = arr.pop(0)
    arr.append(p)
print(f"Array rotated left by {r} position:")
print(arr)