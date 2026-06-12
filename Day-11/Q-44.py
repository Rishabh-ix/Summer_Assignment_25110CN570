# This is a program to write function to find factorial.

def factorial(a):
    fact =1
    if(a==0):
       return 1
    if(a<0):
        return "not defined"
    for i in range(1,a+1):
        fact = fact*i
    return fact

 
n = int(input("Enter a number:"))

fact = factorial(n)
print(f"Factorial of {n} is:",fact)