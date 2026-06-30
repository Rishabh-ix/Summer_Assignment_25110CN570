# Student Record System using Arrays and Strings

roll_no = []
name = []
course = []
marks = []

while True:

    print("\n===== Student Record System =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        roll = int(input("Enter Roll Number: "))

        if roll in roll_no:
            print("Student already exists.")

        else:
            n = input("Enter Name: ")
            c = input("Enter Course: ")
            m = float(input("Enter Marks: "))

            roll_no.append(roll)
            name.append(n)
            course.append(c)
            marks.append(m)

            print("Student added successfully.")

    elif choice == 2:

        roll = int(input("Enter Roll Number: "))

        if roll in roll_no:

            index = roll_no.index(roll)

            print("\n----- Student Details -----")
            print("Roll Number :", roll_no[index])
            print("Name        :", name[index])
            print("Course      :", course[index])
            print("Marks       :", marks[index])

        else:
            print("Student not found.")

    elif choice == 3:

        roll = int(input("Enter Roll Number: "))

        if roll in roll_no:

            index = roll_no.index(roll)

            name[index] = input("Enter New Name: ")
            course[index] = input("Enter New Course: ")
            marks[index] = float(input("Enter New Marks: "))

            print("Student record updated.")

        else:
            print("Student not found.")

    elif choice == 4:

        roll = int(input("Enter Roll Number: "))

        if roll in roll_no:

            index = roll_no.index(roll)

            del roll_no[index]
            del name[index]
            del course[index]
            del marks[index]

            print("Student record deleted.")

        else:
            print("Student not found.")

    elif choice == 5:

        if len(roll_no) == 0:
            print("No student records found.")

        else:

            print("\n===== All Students =====")

            for i in range(len(roll_no)):

                print("-------------------------")
                print("Roll Number :", roll_no[i])
                print("Name        :", name[i])
                print("Course      :", course[i])
                print("Marks       :", marks[i])

    elif choice == 6:

        print("Thank You!")
        break

    else:

        print("Invalid choice.")