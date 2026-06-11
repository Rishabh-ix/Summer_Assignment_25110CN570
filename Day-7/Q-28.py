# This program reverses a number using recursive function.


def reverse(n , rev=0):
    if(n==0):
        return rev
    digit = n%10
    rev = rev*10+digit
    
    return reverse(n//10 , rev)

n = int(input("Enter a number:"))

Rev = reverse(n)

print(f"The reverse of {n} is:",Rev)