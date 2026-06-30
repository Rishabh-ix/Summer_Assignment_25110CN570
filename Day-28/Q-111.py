# Ticket Booking System Program.

ticket_id = []
name = []
age = []
destination = []
date = []
while True:
    print("\n\n--Welcome to the Ticket Booking System--")
    print("1. Book Ticket")
    print("2. View Ticket")
    print("3. Cancel Ticket")
    print("4. Display All Ticket")
    print("5. Exit")
    choice = int(input("Enter your choice: "))
    if(choice==1):
        id=int(input("Enter ticket id: "))
        if id in ticket_id:
            print("Ticket with this id already exist")
        else:
            n = input("Enter Your Name: ")
            a = int(input("Enter Your Age: "))
            d = input("Enter Your Destination: ")
            da = input("Enter the Departure Date: ")
            ticket_id.append(id)
            name.append(n)
            age.append(a)
            destination.append(d)
            date.append(da)
            print("\nTICKET BOOKED SUCCESSFULLY.")
    elif(choice==2):
        id = int(input("Enter ticket id: "))
        if id in ticket_id:
            index = ticket_id.index(id)
            print("\n---Ticket Found---")
            print("Ticket ID: ", id)
            print("Name: ", name[index])
            print("Age: ", age[index])
            print("Destination: ", destination[index])
            print("Date: ", date[index])
        else:
            print("TICKET NOT FOUND")
    elif(choice==3):
        id = int(input("Enter ticket id: "))
        if id in ticket_id:
            index = ticket_id.index(id)
            del ticket_id[index]
            del name[index]
            del age[index]
            del destination[index]
            del date[index]
            print("\n TICKET CANCELLED SUCCESSFULLY.")
    elif(choice==4):
        if (len(ticket_id)==0):
            print("\nNo Ticket Found")
        else:
            print("\n===ALL TICKETS===")
            print("\n")
            for i in range(len(ticket_id)):
               print("----------------------")
               print("Ticket ID  :", ticket_id[i])
               print("Name       :", name[i])
               print("Age        :", age[i])
               print("Destination:", destination[i])
               print("Date       :", date[i])
    elif(choice==5):
        print("\nThank You For Visiting Us.")
        break
    else:
        print("\nInvalid Choice.")




