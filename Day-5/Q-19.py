
n = int(input("Enter a number:"))
print(f"Factors of {n} are:")
for i in range(1,int(n*0.5)):
    if(n%i==0):
        print(i)

