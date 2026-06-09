# This program is to find x^n without pow.

x= int(input("Enter x:"))
n= int(input("Enter n:"))

ans=x
for i in range(2,n+1):
    ans=ans*x

print(f"{x}^{n} is",ans)

