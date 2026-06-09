n = int(input("Enter a number:"))
temp1 = n
temp2 = 0
product = 1

while(temp1>0):
    temp2 = temp1%10;
    product = product*temp2;
    temp1 = temp1//10;

print(f"The product of digits of {n} is", product )