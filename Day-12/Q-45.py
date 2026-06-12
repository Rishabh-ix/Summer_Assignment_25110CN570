# This is a program to write a function for palindrome.
  
def palindrome(a):
    temp=a
    rev=0
    while(temp>0):
      d=temp%10
      rev=rev*10+d
      temp=temp//10
    if(rev==a):
       return "This number is palindrome"
    return "This number is not palindrome"

n = int(input("Enter a number:"))
check = palindrome(n)
print(check)