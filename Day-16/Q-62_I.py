# This program finds maximum frequency element in an array and also finds its frequency.


arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

max_freq=0
max_element=arr[0]
for i in arr:
    freq=0
    for j in arr:
        if(i==j):
            freq=freq+1
    if(freq>max_freq):
        max_freq=freq
        max_element=i
print(f"The maximum frequency element is {max_element} and it occurs {max_freq} times in array")


        