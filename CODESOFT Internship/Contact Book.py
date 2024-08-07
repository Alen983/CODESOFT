contacts = {}

def add_contact():
    name = input("Enter contact Name ").strip()
    phone_number = int(input("Enter the phone number "))[:10].strip()
    email = input("Enter contact email ").strip()
    address = input("Enter contact address ").strip()

    if phone_number in contacts:
        print("contact already exists")
    else:
        contacts[name]={"phone_number":phone_number,"email":email,"address":address}
        print("Contact created successfully")

def view_contact():
    if not contacts:
        print("No contacts found")
    else:
        print("Contact Book")
        print("-" * 120)
        print("Name\t\tPhone Number\t\tEmail\t\t\t\tAddress")
        print("-" * 120)
        for name,info in contacts.items():
            print(f"{name}\t\t{info['phone_number']}\t\t{info['email']}\t\t\t{info['address']}")
            
           # print(f"Name: {name}, Phone_number: {info['phone_number']}, email: {info['email']}, address: {info['address']}")
         

def search_contact():
    name = input("Enter contact name ").strip()
    if name in contacts:
        info = contacts[name]
        print(f"Name: {name}\tphone_number: {info['phone_number']}\t email: {info['email']}\t address: {info['address']}\t")
    else:
        print("Contact does not exist")

def update_contact():
    name = input("enter contact to be updated ")
    if name not in contacts:
        print("Contact does not exist")
    else:
        phone_number = input("Enter new phone number ")
        email = input("Enter new email ")
        address = input("Enter new address ")

        if phone_number:
            contacts[name]["phone_number"] = phone_number
        if email:
            contacts[name]["email"] = email
        if address:
            contacts[name]["address"] = address
        
        print("Contact updated successfully")

def del_contact():
    name = input("Enter name of contact to be deleted ").strip()
    if name not in contacts:
        print("Contact does not exist")
    else:
        del contacts[name]
        print("Successfully deleted contact")

def contact_book():
    while True:
        print("Contact book")
        print("Choose an option")
        print("1. Add Contacts")
        print("2. View Contacts")
        print("3. Search Contacts")
        print("4. Update Contacts")
        print("5. Delete Contact")
        print("6. Exit")

        choice = int(input("Enter your choice "))

        if choice == 1:
            add_contact()
        elif choice == 2:
            view_contact()
        elif choice == 3:
            search_contact()
        elif choice == 4:
            update_contact()
        elif choice == 5:
            del_contact()
        elif choice == 6:
            print("Thank You")
            break
        else:
            print("invaluid choice")
        
contact_book()
