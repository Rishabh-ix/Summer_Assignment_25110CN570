# Mini Library System

book_id = []
book_name = []
author = []
quantity = []

while True:

    print("\n===== Mini Library System =====")
    print("1. Add Book")
    print("2. Search Book")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Display All Books")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        bid = int(input("Enter Book ID: "))

        if bid in book_id:
            print("Book already exists.")

        else:
            name = input("Enter Book Name: ")
            auth = input("Enter Author Name: ")
            qty = int(input("Enter Quantity: "))

            book_id.append(bid)
            book_name.append(name)
            author.append(auth)
            quantity.append(qty)

            print("Book added successfully.")

    elif choice == 2:

        bid = int(input("Enter Book ID: "))

        if bid in book_id:

            index = book_id.index(bid)

            print("\n----- Book Details -----")
            print("Book ID   :", book_id[index])
            print("Book Name :", book_name[index])
            print("Author    :", author[index])
            print("Quantity  :", quantity[index])

        else:
            print("Book not found.")

    elif choice == 3:

        bid = int(input("Enter Book ID: "))

        if bid in book_id:

            index = book_id.index(bid)

            if quantity[index] > 0:
                quantity[index] -= 1
                print("Book issued successfully.")
            else:
                print("Book is not available.")

        else:
            print("Book not found.")

    elif choice == 4:

        bid = int(input("Enter Book ID: "))

        if bid in book_id:

            index = book_id.index(bid)

            quantity[index] += 1
            print("Book returned successfully.")

        else:
            print("Book not found.")

    elif choice == 5:

        if len(book_id) == 0:
            print("Library is empty.")

        else:

            print("\n===== All Books =====")

            for i in range(len(book_id)):

                print("------------------------")
                print("Book ID   :", book_id[i])
                print("Book Name :", book_name[i])
                print("Author    :", author[i])
                print("Quantity  :", quantity[i])

    elif choice == 6:

        print("Thank you!")
        break

    else:

        print("Invalid choice.")