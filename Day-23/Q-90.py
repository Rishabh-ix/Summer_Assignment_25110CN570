# This program finds first repeating character in a string.


s = input("Enter a string: ")
found = False
for i in s:
    freq = 0
    for j in s:
        if(j==i):
            freq +=1
    if(freq>1):
        print(f"{i} is the first repeating character in string")
        found = True
        break
if(found == False):
    print("There is no repeating character in this string")