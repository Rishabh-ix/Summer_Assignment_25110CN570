# Program to develop complete mini project using arrays , strings and functions.

student_id = []
name = []
course = []
marks = []

def add_student():

    sid = int(input("Enter Student ID: "))

    if sid in student_id:
        print("Student already exists.")
    else:
        n = input("Enter Name: ")
        c = input("Enter Course: ")
        m = float(input("Enter Marks: "))

        student_id.append(sid)
        name.append(n)
        course.append(c)
        marks.append(m)

        print("Student added successfully.")


def search_student():

    sid = int(input("Enter Student ID: "))

    if sid in student_id:

        index = student_id.index(sid)

        print("\nStudent ID :", student_id[index])
        print("Name       :", name[index])
        print("Course     :", course[index])
        print("Marks      :", marks[index])

    else:
        print("Student not found.")


def update_student():

    sid = int(input("Enter Student ID: "))

    if sid in student_id:

        index = student_id.index(sid)

        name[index] = input("Enter New Name: ")
        course[index] = input("Enter New Course: ")
        marks[index] = float(input("Enter New Marks: "))

        print("Student updated.")

    else:
        print("Student not found.")


def delete_student():

    sid = int(input("Enter Student ID: "))

    if sid in student_id:

        index = student_id.index(sid)

        del student_id[index]
        del name[index]
        del course[index]
        del marks[index]

        print("Student deleted.")

    else:
        print("Student not found.")


def display_students():

    if len(student_id) == 0:
        print("No records found.")

    else:

        for i in range(len(student_id)):

            print("------------------")
            print("Student ID :", student_id[i])
            print("Name       :", name[i])
            print("Course     :", course[i])
            print("Marks      :", marks[i])


while True:

    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. Search Student")
    print("3. Update Student")
    print("4. Delete Student")
    print("5. Display All Students")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        search_student()

    elif choice == 3:
        update_student()

    elif choice == 4:
        delete_student()

    elif choice == 5:
        display_students()

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Choice.")