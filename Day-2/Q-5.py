n = int(input("Enter the number:"))
temp1 = 0
temp2 = n 
sum = 0
while(temp2>0):
    temp1 = temp2%10;
    sum = sum + temp1;
    temp2 = temp2//10;

print(f"Sum of digits of {n} is",sum)

