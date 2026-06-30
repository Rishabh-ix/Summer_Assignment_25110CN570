# Inventory Management System

product_id = []
product_name = []
price = []
quantity = []

while True:

    print("\n===== Inventory Management System =====")
    print("1. Add Product")
    print("2. Search Product")
    print("3. Update Product")
    print("4. Delete Product")
    print("5. Display All Products")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:

        pid = int(input("Enter Product ID: "))

        if pid in product_id:
            print("Product ID already exists.")

        else:
            name = input("Enter Product Name: ")
            p = float(input("Enter Product Price: "))
            q = int(input("Enter Product Quantity: "))

            product_id.append(pid)
            product_name.append(name)
            price.append(p)
            quantity.append(q)

            print("Product added successfully.")

    elif choice == 2:

        pid = int(input("Enter Product ID: "))

        if pid in product_id:

            index = product_id.index(pid)

            print("\n----- Product Details -----")
            print("Product ID   :", product_id[index])
            print("Product Name :", product_name[index])
            print("Price        :", price[index])
            print("Quantity     :", quantity[index])

        else:
            print("Product not found.")

    elif choice == 3:

        pid = int(input("Enter Product ID: "))

        if pid in product_id:

            index = product_id.index(pid)

            product_name[index] = input("Enter New Product Name: ")
            price[index] = float(input("Enter New Price: "))
            quantity[index] = int(input("Enter New Quantity: "))

            print("Product updated successfully.")

        else:
            print("Product not found.")

    elif choice == 4:

        pid = int(input("Enter Product ID: "))

        if pid in product_id:

            index = product_id.index(pid)

            del product_id[index]
            del product_name[index]
            del price[index]
            del quantity[index]

            print("Product deleted successfully.")

        else:
            print("Product not found.")

    elif choice == 5:

        if len(product_id) == 0:
            print("No products available.")

        else:

            print("\n===== All Products =====")

            for i in range(len(product_id)):

                print("---------------------------")
                print("Product ID   :", product_id[i])
                print("Product Name :", product_name[i])
                print("Price        :", price[i])
                print("Quantity     :", quantity[i])

    elif choice == 6:

        print("Thank you for using the Inventory Management System.")
        break

    else:

        print("Invalid choice.")