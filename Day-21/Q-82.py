# This is a program to reverse a string.

s = input("Enter a string:")
count = len(s)
n = []
for i in range(count):
    n.append(s[count-1-i])
n = "".join(n)
print("Reversed string is:", n)
