l = int(input("Enter Lower range:"))
u = int(input("Enter upper range:"))
print(f"Prime numbers in the range {l} to {u} are:")
for i in range(l,u+1):
    if(i>1):
     for m in range(2 , i//2+1):
        if(i%m==0):
         break
     else:
        print(i)
