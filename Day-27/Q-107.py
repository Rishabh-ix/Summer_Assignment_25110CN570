# Salary Management System Program

employees = {}

while True:
    print("\n===== Salary Management System =====")
    print("1. Add Employee")
    print("2. View Salary")
    print("3. Update Salary")
    print("4. Delete Employee")
    print("5. Display All Employees")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        emp_id = int(input("Enter Employee ID: "))

        if emp_id in employees:
            print("Employee ID already exists.")

        else:
            name = input("Enter Employee Name: ")
            salary = float(input("Enter Salary: "))

            employees[emp_id] = {
                "Name": name,
                "Salary": salary
            }

            print("Employee added successfully.")

    elif choice == 2:
        emp_id = int(input("Enter Employee ID: "))

        if emp_id in employees:
            print("\nEmployee Details")
            print("Employee ID :", emp_id)
            print("Name :", employees[emp_id]["Name"])
            print("Salary :", employees[emp_id]["Salary"])

        else:
            print("Employee not found.")

    elif choice == 3:
        emp_id = int(input("Enter Employee ID: "))

        if emp_id in employees:
            employees[emp_id]["Salary"] = float(input("Enter New Salary: "))
            print("Salary updated successfully.")

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
            print("No employee records found.")

        else:
            print("\n===== Employee Salary Records =====")

            for emp_id, data in employees.items():
                print("----------------------------")
                print("Employee ID :", emp_id)
                print("Name :", data["Name"])
                print("Salary :", data["Salary"])

    elif choice == 6:
        print("Thank you!")
        break

    else:
        print("Invalid choice.")