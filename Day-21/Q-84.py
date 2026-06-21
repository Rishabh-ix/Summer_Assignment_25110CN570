# This is a program to convert lowercase to uppercase.

s = input("Enter a string: ")

result = ""
for i in s:
    if("a"<=i<="z"):
        result += chr(ord(i) - 32)
    else:
        result += i
        

print("String in uppercase is:", result)