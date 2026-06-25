# This is a program to sort names alpabetically.

names = []

n = int(input("Enter number of names: "))

for i in range(n):
    name = input(f"Enter name {i+1}: ")
    names.append(name)

for i in range(n - 1):
    for j in range(n - 1 - i):
        if(names[j] > names[j + 1]):
            temp = names[j]
            names[j] = names[j + 1]
            names[j + 1] = temp

print("Names in alphabetical order:")
for name in names:
    print(name)