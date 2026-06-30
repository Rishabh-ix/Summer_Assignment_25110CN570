# Library Management System Program.


library={}
while(True):
            print("--Library Management System--")
            print("1. Add Book")
            print("2. Search Book")
            print("3. Update Book")
            print("4. Delete Book")
            print("5. Exit")
        
            choice = int(input("Enter your choice: "))

            if(choice == 1):
                    id = int(input("Enter Book ID: "))
                    if(id in library):
                            print("Book with this id already exists.")
                    else:
                            book_name = input("Enter the name of the book: ")
                            author = input("Enter the name of the author: ")
                            publisher = input("Enter the name of the publisher: ")
                            price = int(input("Enter the price of the book: "))
                            quantity = int(input("Enter the number of books: "))

                            library[id] = {
                                "Book name" : book_name,
                                "Author" : author,
                                "Publisher" : publisher,
                                "Price" : price,
                                "Quantity" : quantity
                            }
                            print("Book added successfully.")
            elif(choice==2):
                    id = int(input("Enter Book ID: "))
                    if id in library:
                            print("\n-Book details-")
                            print("Book id: ", id)
                            print("Book Name: ", library[id]["Book name"])
                            print("Author: ", library[id]["Author"])
                            print("Publisher: ", library[id]["Publisher"])
                            print("Price: ", library[id]["Price"])
                            print("Quantity: ", library[id]["Quantity"])
                    else: 
                            print("Book not found.")
            elif(choice==3):
                    id = int(input("Enter Book ID: "))
                    if id in library:
                            library[id]["Book name"] = input("Update Book name: ")
                            library[id]["Author"] = input("Update Author name: ")
                            library[id]["Publisher"] = input("Update Publisher name: ")
                            library[id]["Price"] = int(input("Update Book price: "))
                            library[id]["Quantity"] = int(input("Update Book Quantity: "))

                            print("Book Updated Successfully.")
                    else:
                            print("Book not found.")

            elif(choice == 4):
                    id = int(input("Enter Book ID: "))
                    if id in library:
                            del library[id]
                            print("Book record deleted successfully.")
                    else:
                            print("Book not found.")
            elif(choice == 5):
                    print("Thank You For Using Library Management System.")
                    break
            else:
                    print("Invalid choice.")


