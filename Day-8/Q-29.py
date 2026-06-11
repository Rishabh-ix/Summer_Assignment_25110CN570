# This program prints half pyramid pattern.

n = int(input("Enter number of rows:"))

for i in range(1,n+1):
    for m in range(i):
        print("*",end=" ")

    print()