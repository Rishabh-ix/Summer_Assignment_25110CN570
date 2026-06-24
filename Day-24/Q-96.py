# This is a program to remove duplicate characters from a string.


s1 = input("Enter a string: ")

s2 = ""

for i in s1:
    if i not in s2:
        s2 += i
print("After removing duplicate characters from string , it becomes:", s2)