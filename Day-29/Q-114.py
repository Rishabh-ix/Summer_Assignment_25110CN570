# Menu Driven Array Operations System

arr = []

while True:

    print("\n===== ARRAY OPERATIONS =====")
    print("1. Insert Element")
    print("2. Display Array")
    print("3. Search Element")
    print("4. Update Element")
    print("5. Delete Element")
    print("6. Sort Array")
    print("7. Find Maximum")
    print("8. Find Minimum")
    print("9. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        value = int(input("Enter element: "))
        arr.append(value)
        print("Element inserted successfully.")

    elif choice == 2:

        if len(arr) == 0:
            print("Array is empty.")
        else:
            print("Array =", arr)

    elif choice == 3:

        if len(arr) == 0:
            print("Array is empty.")
        else:
            value = int(input("Enter element to search: "))

            if value in arr:
                print("Element found at index", arr.index(value))
            else:
                print("Element not found.")

    elif choice == 4:

        if len(arr) == 0:
            print("Array is empty.")
        else:
            old = int(input("Enter element to update: "))

            if old in arr:
                index = arr.index(old)
                new = int(input("Enter new element: "))
                arr[index] = new
                print("Element updated successfully.")
            else:
                print("Element not found.")

    elif choice == 5:

        if len(arr) == 0:
            print("Array is empty.")
        else:
            value = int(input("Enter element to delete: "))

            if value in arr:
                arr.remove(value)
                print("Element deleted successfully.")
            else:
                print("Element not found.")

    elif choice == 6:

        if len(arr) == 0:
            print("Array is empty.")
        else:
            arr.sort()
            print("Sorted Array =", arr)

    elif choice == 7:

        if len(arr) == 0:
            print("Array is empty.")
        else:
            print("Maximum Element =", max(arr))

    elif choice == 8:

        if len(arr) == 0:
            print("Array is empty.")
        else:
            print("Minimum Element =", min(arr))

    elif choice == 9:

        print("Thank you!")
        break

    else:
        print("Invalid choice.")