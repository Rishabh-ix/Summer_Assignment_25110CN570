# This is a program to write function for armstrong.

def armstrong(a):
    temp=a
    sum=0
    digit = len(str(a))
    while(temp>0):
        d = temp%10
        sum = sum + pow(d,digit)
        temp=temp//10
    if(sum==a):
        return "This is a armstrong number"
    return "This is not a armstrong number"

n = int(input("Enter a number:"))

check = armstrong(n)
print(check)