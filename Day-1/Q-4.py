n = int(input("Enter the number:"))

count = 0
temp = n
while (temp>0):
 
    temp = temp//10;
    count =  count +1;
  

print (f"The number of digits in {n} are ",count)