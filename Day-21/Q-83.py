# This is a program to count vowel and consonant in string.


s = input("Enter a string:")
vowel = 0
consonant = 0
for i in s:
    if i.isalpha():
        if i in "aeiouAEIOU":
            vowel += 1
        else:
            consonant +=1

print("Number of vowels in string are:", vowel)
print("Number of consonants in string are:", consonant)