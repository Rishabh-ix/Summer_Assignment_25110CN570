# This is a program to find maximum occuring character.

s = input("Enter a string: ")
max_freq = 0
max_element = ""
if(len(s)==0):
    print("String is empty")
else:
    for i in s:
     freq = 0
     for j in s:
        if(i == j):
            freq+=1
     if(freq>max_freq):
        max_freq = freq
        max_element = i
    print(f"Maximum frequency element is -{max_element}- and its frequency is: ",max_freq)