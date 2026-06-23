# This is a program to find character frequency.

s = input("Enter a string:")
n = input("Enter a charcter you need to find frequency of:")
freq = 0
if(len(n)!=1):
    print("Please , enter only one character")
else:
  for i in s:
    if(i == n):
        freq += 1

  print(f"Frequency of character {n} is:", freq)
