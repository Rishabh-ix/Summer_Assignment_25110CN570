# This program prints number triangle.

n = int(input("Enter number of rows:"))

for i in range(1,n+1):
    for m in range(1,i+1):
        print(m,end=" ")

    print()