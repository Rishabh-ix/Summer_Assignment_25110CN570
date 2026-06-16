# This progrm finds pair with given sum in an array.


arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

target = int(input("Enter target sum:"))
for i in range(n):
    for j in range(i+1,n):
        if(arr[i]+arr[j]==target):
            print(f"{arr[i]} + {arr[j]} =", target)
            