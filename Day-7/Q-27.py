# This program prints the sum of digits of a number using recursive function.


def SOD(n):
    if(n==0):
        return 0
    else:
        return (n%10)+SOD(n//10)
    
n = int(input("Enter a number:"))

sum = SOD(n)

print(f"sum of digits of {n} is:",sum)

 

