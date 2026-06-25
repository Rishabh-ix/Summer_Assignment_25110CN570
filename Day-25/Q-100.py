# This is a program to sort words by length.

words = []

n = int(input("Enter number of words: "))

for i in range(n):
    word = input(f"Enter word {i+1}: ")
    words.append(word)

for i in range(n-1):
    for j in range(n-1-i):
        if(len(words[j])>len(words[j+1])):
            temp = words[j]
            words[j] = words[j+1]
            words[j+1] = temp

print("Words sorted by length: ")
for i in words:
    print(i)