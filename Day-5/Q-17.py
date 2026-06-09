#This program is to check whether n is a perfect number or not.

n = int(input("Enter a number:"))

sum=0
d=n//2
for i in range(1,d+1):
    if(n%i==0):
        sum=sum+i

if(sum==n):
    print(f"{n} is a perfect number.")
else: 
    print(f"{n} is not a perfect number.")