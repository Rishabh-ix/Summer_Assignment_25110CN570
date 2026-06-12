# This is a program write function for fibonacci.

def fibonacci(a):
    x=0
    y=1
    if(a==1):
        print(x)
    elif(a>=2):
     print(x)
     print(y)
     for i in range(3,a+1):
        z=x+y
        print(z)
        x=y
        y=z
        
        

n = int(input("Enter number of terms:"))

print("Fibpnacci series:")
fibonacci(n)
