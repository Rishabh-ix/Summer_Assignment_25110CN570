# This program prints number pyramid.


n = int(input("Enter the number of rows:"))

for i in range(n):
    for j in range(n-1-i):
        print(" ",end=" ")

    for k in range(i+1):
        print(k+1,end=" ")
        
    for l in range(i):
        print(i-l,end=" ")
        



    print()