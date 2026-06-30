# Menu Driven String Operation System

s = input("Enter a string: ")

while True:

    print("\n===== STRING OPERATIONS =====")
    print("1. Display String")
    print("2. Find Length")
    print("3. Convert to Uppercase")
    print("4. Convert to Lowercase")
    print("5. Reverse String")
    print("6. Check Palindrome")
    print("7. Count Vowels")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        print("String:", s)

    elif choice == 2:

        count = 0
        for i in s:
            count += 1

        print("Length =", count)

    elif choice == 3:

        result = ""

        for ch in s:
            if 'a' <= ch <= 'z':
                result += chr(ord(ch) - 32)
            else:
                result += ch

        print("Uppercase:", result)

    elif choice == 4:

        result = ""

        for ch in s:
            if 'A' <= ch <= 'Z':
                result += chr(ord(ch) + 32)
            else:
                result += ch

        print("Lowercase:", result)

    elif choice == 5:

        rev = ""

        for i in s:
            rev = i + rev

        print("Reversed String:", rev)

    elif choice == 6:

        rev = ""

        for i in s:
            rev = i + rev

        if s == rev:
            print("Palindrome")
        else:
            print("Not a Palindrome")

    elif choice == 7:

        vowels = 0

        for ch in s:
            if ch in "AEIOUaeiou":
                vowels += 1

        print("Number of vowels =", vowels)

    elif choice == 8:

        print("Thank you!")
        break

    else:

        print("Invalid choice.")