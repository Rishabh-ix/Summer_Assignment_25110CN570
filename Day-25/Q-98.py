# This is a program to find common characters in strings.

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
s3 = ""
for i in s1:
    if i not in s3:
        for j in s2:
            if(i==j):
                s3 += i

print("Common characters in strings are: ")
for i in s3:
    print(i)