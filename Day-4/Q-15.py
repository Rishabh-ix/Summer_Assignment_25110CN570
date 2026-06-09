# This is a program to check if n is an armstrong number or not.
n = int(input("Enter the number:"))

sum=0
digits=len(str(n))
temp=n
 
while(temp>0):
    d = temp%10
    sum = sum + pow(d , digits)
    temp = temp//10

if(sum==n):
    print(f"{n} is a armstrong number.")
else:
    print(f"{n} is not a armstrong number.")
    

 
