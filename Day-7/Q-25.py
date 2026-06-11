# This program prints the factorial of a number using recursive function.

def factorial(n):
    if(n==1):
        return 1
    if(n==0):
        return 1
    else:
        return n*factorial(n-1)
    
n = int(input("Enter a number:"))

fact = factorial(n)

print(f"Factorial of {n} is:",fact)