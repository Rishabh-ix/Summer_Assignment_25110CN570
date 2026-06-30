# Menu Driven Calculator

while True:

    print("\n===== MENU DRIVEN CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Floor Division")
    print("7. Exponent")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 8:
        print("Thank you for using the calculator.")
        break

    if choice >= 1 and choice <= 7:

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            print("Result =", num1 + num2)

        elif choice == 2:
            print("Result =", num1 - num2)

        elif choice == 3:
            print("Result =", num1 * num2)

        elif choice == 4:
            if num2 != 0:
                print("Result =", num1 / num2)
            else:
                print("Division by zero is not possible.")

        elif choice == 5:
            if num2 != 0:
                print("Result =", num1 % num2)
            else:
                print("Division by zero is not possible.")

        elif choice == 6:
            if num2 != 0:
                print("Result =", num1 // num2)
            else:
                print("Division by zero is not possible.")

        elif choice == 7:
            print("Result =", num1 ** num2)

    else:
        print("Invalid choice.")