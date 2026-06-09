# This program is to check whether n is a strong number or not.

n = int(input("Enter a number:"))

temp=n
sum=0
while(temp>0):
    fact=1
    d=temp%10
    tomp=d
    while(tomp>0):
        fact=fact*tomp
        tomp=tomp-1

    sum = sum + fact
    temp=temp//10

if(sum==n):
    print(f"{n} is a strong number.")
else:
    print(f"{n} is not a strong number.")