# This is a program to write a function for perfect number.

def perfectno(a):
    sum=0
    for i in range(1,a):
        if(a%i==0):
            sum = sum +i
    if(sum==a):
        print("This is a perfect number")
    else:
     print("This is not a perfect number")

n = int(input("Enter a number:"))

perfectno(n)