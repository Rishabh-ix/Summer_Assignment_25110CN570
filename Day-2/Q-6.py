n = int(input("Enter a number:"))
temp1 = n
temp2 = 0
rev = 0

while(temp1>0):
    temp2 = temp1%10;
    rev = rev*10 + temp2;
    temp1 = temp1//10;

print(f"The reverse of {n} is", rev )

    