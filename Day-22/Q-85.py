# This program checks whether a string is palindrome or not.

s = input("Enter a string: ")

rev = ""

for i in s:
    rev = i + rev

if(s == rev):
    print("String is palindrome")
else:
    print("String is not palindrome")