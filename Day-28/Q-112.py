# Contact Management System Program.

contact_id = []
name = []
phone = []
email = []
address = []

while True:

    print("\n===== Contact Management System =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Display All Contacts")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        cid = int(input("Enter Contact ID: "))

        if cid in contact_id:
            print("Contact ID already exists.")

        else:
            n = input("Enter Name: ")
            p = input("Enter Phone Number: ")
            e = input("Enter Email: ")
            a = input("Enter Address: ")

            contact_id.append(cid)
            name.append(n)
            phone.append(p)
            email.append(e)
            address.append(a)

            print("Contact added successfully.")

    elif choice == 2:

        cid = int(input("Enter Contact ID: "))

        if cid in contact_id:

            index = contact_id.index(cid)

            print("\n----- Contact Details -----")
            print("Contact ID :", contact_id[index])
            print("Name       :", name[index])
            print("Phone      :", phone[index])
            print("Email      :", email[index])
            print("Address    :", address[index])

        else:
            print("Contact not found.")

    elif choice == 3:

        cid = int(input("Enter Contact ID: "))

        if cid in contact_id:

            index = contact_id.index(cid)

            name[index] = input("Enter New Name: ")
            phone[index] = input("Enter New Phone Number: ")
            email[index] = input("Enter New Email: ")
            address[index] = input("Enter New Address: ")

            print("Contact updated successfully.")

        else:
            print("Contact not found.")

    elif choice == 4:

        cid = int(input("Enter Contact ID: "))

        if cid in contact_id:

            index = contact_id.index(cid)

            del contact_id[index]
            del name[index]
            del phone[index]
            del email[index]
            del address[index]

            print("Contact deleted successfully.")

        else:
            print("Contact not found.")

    elif choice == 5:

        if len(contact_id) == 0:
            print("No contacts available.")

        else:

            print("\n===== All Contacts =====")

            for i in range(len(contact_id)):
                print("---------------------------")
                print("Contact ID :", contact_id[i])
                print("Name       :", name[i])
                print("Phone      :", phone[i])
                print("Email      :", email[i])
                print("Address    :", address[i])

    elif choice == 6:

        print("Thank you!")
        break

    else:
        print("Invalid choice.")