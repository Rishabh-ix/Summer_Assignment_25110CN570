# This is a number guessing game program.

import random
n = random.randint(1, 100)
print("Let's start a number guessing game.....")
a = int(input("Guess a number between 1 and 100: "))
count = 0
while(a!=n):
 if(a>n):
    print("Try guessing a lower number")
    count+=1
    a = int(input("Guess another number: "))
 elif(a<n):
    print("Try guessing a higher number")
    count+=1
    a = int(input("Guess another number: "))
 
if(a==n):
    print(f"Hurray! You got it right in {count} tries.")