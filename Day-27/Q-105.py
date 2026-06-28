# Student Record Management System Program.

students = {}

while True:
    print("\n===== Student Management System =====")
    print("1. Add Student")
    print("2. View Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        roll = int(input("Enter Roll Number: "))

        if roll in students:
            print("Student with this roll number already exists.")
        else:
            name = input("Enter Name: ")
            age = int(input("Enter Age: "))
            marks = float(input("Enter Marks: "))

            students[roll] = {
                "Name": name,
                "Age": age,
                "Marks": marks
            }

            print("Student added successfully!")

    elif choice == 2:
        roll = int(input("Enter Roll Number: "))

        if roll in students:
            print("\nStudent Details")
            print("Roll Number:", roll)
            print("Name:", students[roll]["Name"])
            print("Age:", students[roll]["Age"])
            print("Marks:", students[roll]["Marks"])
        else:
            print("Student not found.")

    elif choice == 3:
        roll = int(input("Enter Roll Number: "))

        if roll in students:
            print("\n1. Update Name")
            print("2. Update Age")
            print("3. Update Marks")

            update = int(input("Enter your choice: "))

            if update == 1:
                students[roll]["Name"] = input("Enter New Name: ")

            elif update == 2:
                students[roll]["Age"] = int(input("Enter New Age: "))

            elif update == 3:
                students[roll]["Marks"] = float(input("Enter New Marks: "))

            else:
                print("Invalid choice.")

            print("Record updated successfully!")

        else:
            print("Student not found.")

    elif choice == 4:
        roll = int(input("Enter Roll Number: "))

        if roll in students:
            del students[roll]
            print("Student record deleted successfully.")
        else:
            print("Student not found.")

    elif choice == 5:
        if len(students) == 0:
            print("No student records available.")
        else:
            print("\n===== All Student Records =====")
            for roll in students:
                print("-----------------------------")
                print("Roll Number:", roll)
                print("Name:", students[roll]["Name"])
                print("Age:", students[roll]["Age"])
                print("Marks:", students[roll]["Marks"])

    elif choice == 6:
        print("Thank you for using the Student Management System!")
        break

    else:
        print("Invalid choice. Please try again.")