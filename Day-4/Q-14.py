# This program is to print the nth term of fibonacci series

n = int(input("Enter the term:"))

a=0
b=1
# Considering the first and second term of fibonacci series 0 and 1.
for i in range(3,n+1):
    c = a+b
    a=b
    b=c

print(f"Enter {n}th term of fibonacci series is {c}")