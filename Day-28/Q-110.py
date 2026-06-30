# Bank Account Management System Program.

account_no = []
name = []
balance = []

while True:

    print("\n===== BANK ACCOUNT SYSTEM =====")
    print("1. Create Account")
    print("2. View Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. Delete Account")
    print("6. Display All Accounts")
    print("7. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        acc = int(input("Enter Account Number: "))

        if acc in account_no:
            print("Account already exists.")

        else:
            n = input("Enter Account Holder Name: ")
            b = float(input("Enter Initial Balance: "))

            account_no.append(acc)
            name.append(n)
            balance.append(b)

            print("Account created successfully.")

    elif choice == 2:

        acc = int(input("Enter Account Number: "))

        if acc in account_no:

            index = account_no.index(acc)

            print("\nAccount Details")
            print("Account Number :", account_no[index])
            print("Name           :", name[index])
            print("Balance        :", balance[index])

        else:
            print("Account not found.")

    elif choice == 3:

        acc = int(input("Enter Account Number: "))

        if acc in account_no:

            index = account_no.index(acc)

            amount = float(input("Enter amount to deposit: "))

            balance[index] += amount

            print("Money deposited successfully.")
            print("Current Balance =", balance[index])

        else:
            print("Account not found.")

    elif choice == 4:

        acc = int(input("Enter Account Number: "))

        if acc in account_no:

            index = account_no.index(acc)

            amount = float(input("Enter amount to withdraw: "))

            if amount <= balance[index]:
                balance[index] -= amount
                print("Withdrawal successful.")
                print("Remaining Balance =", balance[index])

            else:
                print("Insufficient Balance.")

        else:
            print("Account not found.")

    elif choice == 5:

        acc = int(input("Enter Account Number: "))

        if acc in account_no:

            index = account_no.index(acc)

            del account_no[index]
            del name[index]
            del balance[index]

            print("Account deleted successfully.")

        else:
            print("Account not found.")

    elif choice == 6:

        if len(account_no) == 0:
            print("No accounts available.")

        else:
            print("\n===== ALL ACCOUNTS =====")

            for i in range(len(account_no)):
                print("-----------------------")
                print("Account Number :", account_no[i])
                print("Name           :", name[i])
                print("Balance        :", balance[i])

    elif choice == 7:

        print("Thank you for banking with us.")
        break

    else:
        print("Invalid choice.")