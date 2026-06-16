# This is a program which finds maximum frequency element in an array using dictionary concept.

arr = []

n = int(input("Enter number of elements: "))

for i in range(n):
    value = int(input("Enter element: "))
    arr.append(value)

freq_dict = {}

for i in arr:
    if i in freq_dict:
        freq_dict[i] += 1
    else:
        freq_dict[i] = 1

max_freq = max(freq_dict.values())

print("Elements with maximum frequency are:")

for key in freq_dict:
    if freq_dict[key] == max_freq:
        print(key)

print("Frequency is:", max_freq)