# This is a program for ATM simulation.

print("--Welcome to the ATM--")
balance = 10000
pin = 1234
print("1 = Balance Enquiry")
print("2 = Withdraw Cash")
print("3 = Deposit Money")
print("4 = Exit")
op = int(input("Please enter the operation you want to perform: "))
if(op == 1):
    x = int(input("Enter the security pin: "))
    if(x == pin):
        print("Correct pin")
        print(f"Current balance = ${balance}")
    else:
        print("Incorrect pin")
    
elif(op == 2):
    x = int(input("Enter the security pin: "))
    if(x==pin):
         print("Correct pin.")
         y = int(input("Enter the amount you want to withdraw: "))
         if(y<=balance):
          balance = balance - y
          print(f"Remaining balance = ${balance}")
         else:
          print("Insufficient balance.")
    else:
        print("Incorrect pin.")

elif(op == 3):
    z = int(input("Enter the amount to deposit:"))
    x = int(input("Enter the security pin: "))
    if(x == pin):
        print("Correct pin")
        balance = balance + z
        print(f"${z} deposited successfully.")
        print(f"Current balance: ${balance}")
    else:
        print("Incorrect pin")
elif(op == 4):
    print("Thanks for banking with us, come again.")
else:
    print("Invalid operation.")