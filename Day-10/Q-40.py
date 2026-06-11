# This program prints character pyramid.


n = int(input("Enter the number of rows:"))

for i in range(n):
    for j in range(n-1-i):
        print(" ",end=" ")

    for k in range(i+1):
        print(chr(65+k),end=" ")
        
    for l in range(i):
        print(chr(64+i-l),end=" ")
        



    print()