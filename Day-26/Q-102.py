# This is a program for checking voting eligibility.


age = int(input("Enter your age: "))
if(age<=0):
    print("Are you high? This is not even a valid age...")
elif(age<18 and age>14):
    print("You are not eligible for voting, just wait for few more years...")
elif(age<14):
    print("Mate! You should be doing your homework rather than checking your eligibility for voting.")
elif(age>=18 and age<24):
    print("You are eligible for voting , but choose your vote wisely in nation's favour...")
else:
    print("Obviously you are eligible , what are you doing until now? Hurry up, the democracy needs you my friend...")