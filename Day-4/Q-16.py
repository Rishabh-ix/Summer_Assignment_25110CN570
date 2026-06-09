# This program is to print all the armstrong numbers between the limit l to u.


l = int(input("Enter lower limit:"))
u = int(input("Enter upper limit:"))


for i in range(l,u+1):
    sum = 0
    digit = len(str(i))
    temp = i
    while(temp>0):
        d= temp%10
        sum = sum + pow(d,digit)
        temp= temp//10
    if(sum==i):
      print(i)

  
