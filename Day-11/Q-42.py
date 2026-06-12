# This is a program to write funtion to find maximum.

def maxnum(a,b):
    if(a>b):
        return a
    else:
        return b
    
x = int(input("Enter first number:"))
y = int(input("Enter first number:"))

max = maxnum(x,y)

print(f"Maximum of {x} and {y} is:",max)