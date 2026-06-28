# Employee Management System Program.

employees = {}

while True:
    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employee")
    print("3. Update Employee")
    print("4. Delete Employee")
    print("5. Display All Employees")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        emp_id = int(input("Enter Employee ID: "))

        if emp_id in employees:
            print("Employee with this ID already exists.")
        else:
            name = input("Enter Employee Name: ")
            department = input("Enter Department: ")
            salary = float(input("Enter Salary: "))

            employees[emp_id] = {
                "Name": name,
                "Department": department,
                "Salary": salary
            }

            print("Employee added successfully!")

    elif choice == 2:
        emp_id = int(input("Enter Employee ID: "))

        if emp_id in employees:
            print("\nEmployee Details")
            print("Employee ID :", emp_id)
            print("Name        :", employees[emp_id]["Name"])
            print("Department  :", employees[emp_id]["Department"])
            print("Salary      :", employees[emp_id]["Salary"])
        else:
            print("Employee not found.")

    elif choice == 3:
        emp_id = int(input("Enter Employee ID: "))

        if emp_id in employees:

            print("\n1. Update Name")
            print("2. Update Department")
            print("3. Update Salary")

            update = int(input("Enter your choice: "))

            if update == 1:
                employees[emp_id]["Name"] = input("Enter New Name: ")

            elif update == 2:
                employees[emp_id]["Department"] = input("Enter New Department: ")

            elif update == 3:
                employees[emp_id]["Salary"] = float(input("Enter New Salary: "))

            else:
                print("Invalid choice.")

            print("Employee record updated successfully!")

        else:
            print("Employee not found.")

    elif choice == 4:
        emp_id = int(input("Enter Employee ID: "))

        if emp_id in employees:
            del employees[emp_id]
            print("Employee deleted successfully.")
        else:
            print("Employee not found.")

    elif choice == 5:

        if len(employees) == 0:
            print("No employee records available.")

        else:
            print("\n===== Employee Records =====")

            for emp_id, data in employees.items():
                print("----------------------------")
                print("Employee ID :", emp_id)
                print("Name        :", data["Name"])
                print("Department  :", data["Department"])
                print("Salary      :", data["Salary"])

    elif choice == 6:
        print("Thank you for using the Employee Management System.")
        break

    else:
        print("Invalid choice.")