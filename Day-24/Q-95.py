# This is a program to find the longest word in a sentence.

s = input("Enter a string: ")

longest = ""
i = 0
while(i<len(s)):
  word = ""
  while(i<len(s) and s[i] != " "):
    word += s[i]
    i +=1
    
  if(len(word)>len(longest)):
    longest = word
  i += 1
print("Longest word in this string is:", longest)
   

