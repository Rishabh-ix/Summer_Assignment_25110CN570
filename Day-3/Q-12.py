a = int(input("Enter first number:"))
b = int(input("Enter second number:"))
 
temp = max(a,b)

while (True):
    if(temp%a==0 and temp%b==0):
        print(f"LCM of {a} and {b} is {temp}")
        break
    temp = temp + 1 