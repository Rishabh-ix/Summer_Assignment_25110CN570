# This is a program to check anagram strings.

s1 = input("Enter first string: ")
s2 = input("Enter second string: ")

flag = True

if(len(s1) == len(s2)):
    for i in s1:
        freq1 = 0
        freq2 = 0

        for j in s1:
            if(j == i):
                freq1 += 1

        for j in s2:
            if(j == i):
                freq2 += 1

        if(freq1 != freq2):
            flag = False
            break

    if(flag == True):
        print("These are anagram strings")
    else:
        print("These are not anagram strings")
else:
    print("These are not anagram strings")