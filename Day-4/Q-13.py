# This program is to print fibonacci series upto n terms.

n = int(input("Enter number of terms:"))
 
print("Fibonacci series:")
 
a = 0
b = 1

print( a )
print(b)

for i in range (3 , n+1):
    c = a+b
    print(c)
    a=b
    b=c
