# This is a program to find string length without strlen() function.


n = input("Enter a string:")
count = 0
for i in n:
    count =  count+1
print(f"The length of string \"{n}\" is:", count)