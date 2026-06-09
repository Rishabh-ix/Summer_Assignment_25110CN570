# This program converts binary to decimal.


binary = int(input("Enter binary number: "))
temp=binary
digit = len(str(binary))
sum=0
power=0
while(temp>0):
    d = temp%10
    sum = sum + (d*pow(2,power))
    temp=temp//10
    power=power+1
 
print(f"The decimal conversion of {binary} is:" , sum)
