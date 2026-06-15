# This program shifts array right by r position.

arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

r = int(input("Enter by how many position the array should be rotated right:"))

for i in range(r):
    p = arr.pop()
    arr.insert(0,p)

print(f"Array rotated right by {r} position:")
print(arr)