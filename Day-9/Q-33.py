# This program prints reverse star pattern.

n = int(input("Enter number of rows:"))

for i in range(1,n+1):
    for m in range(n+1-i):
        print("*",end=" ")
        

    print()