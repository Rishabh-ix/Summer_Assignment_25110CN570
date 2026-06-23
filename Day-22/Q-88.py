# This is a program to remove spaces from a string.

s1 = input("Enter a string: ")
s2 = ""
for i in s1:
    if(i != " "):
        s2 = s2+i
print("After spaces are removed , string is:")
print(s2)