# This program counts words in a sentence.

s = input("Enter a sentence: ")

words = 0
in_word = False
for i in s:
    if(i != " " and in_word == False):
        words +=1
        in_word = True
    elif(i == " "):
        in_word = False
print("The number of words in this sentence is:", words)