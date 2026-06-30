# Mini Employee Management System

emp_id = []
emp_name = []
department = []
salary = []

while True:

    print("\n===== Mini Employee Management System =====")
    print("1. Add Employee")
    print("2. Search Employee")
    print("3. Update Employee")
    print("4. Display All Employees")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        eid = int(input("Enter Employee ID: "))

        if eid in emp_id:
            print("Employee ID already exists.")

        else:
            name = input("Enter Employee Name: ")
            dept = input("Enter Department: ")
            sal = float(input("Enter Salary: "))

            emp_id.append(eid)
            emp_name.append(name)
            department.append(dept)
            salary.append(sal)

            print("Employee added successfully.")

    elif choice == 2:

        eid = int(input("Enter Employee ID: "))

        if eid in emp_id:

            index = emp_id.index(eid)

            print("\n----- Employee Details -----")
            print("Employee ID :", emp_id[index])
            print("Name        :", emp_name[index])
            print("Department  :", department[index])
            print("Salary      :", salary[index])

        else:
            print("Employee not found.")

    elif choice == 3:

        eid = int(input("Enter Employee ID: "))

        if eid in emp_id:

            index = emp_id.index(eid)

            emp_name[index] = input("Enter New Name: ")
            department[index] = input("Enter New Department: ")
            salary[index] = float(input("Enter New Salary: "))

            print("Employee updated successfully.")

        else:
            print("Employee not found.")

    elif choice == 4:

        if len(emp_id) == 0:

            print("No employee records found.")

        else:

            print("\n===== All Employees =====")

            for i in range(len(emp_id)):

                print("---------------------------")
                print("Employee ID :", emp_id[i])
                print("Name        :", emp_name[i])
                print("Department  :", department[i])
                print("Salary      :", salary[i])

    elif choice == 5:

        print("Thank You!")
        break

    else:

        print("Invalid choice.")