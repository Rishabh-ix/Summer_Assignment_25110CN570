# This program count set bits in a number.

n=int(input("Enter a number:"))
binary = " "
temp=n
while temp > 0:
    rem = temp % 2
    binary = str(rem) + binary
    temp = temp // 2

binary=int(binary)
count=0
while(binary>0):
    d=binary%10
    if(d==1):
        count=count+1
    binary=binary//10

print(f"Number of set bits in {n} is:",count)