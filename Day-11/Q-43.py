# This program is to wrie a function to check prime number.

def prime(a):
   if(a<=1):
            return "This number is not prime"
   for i in range(2,a//2+1):

     if(a%i==0):
            return "This number is not prime"
     
   return "This number is prime"
        
       
n = int(input("Enter a number:"))

check = prime(n)

print(check)