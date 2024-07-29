import sys

# Initialize an empty contact list
contact_list = []

print("Welcome to the Contact Management System")

while True:
    print("\nMenu:")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        continue

    if choice == 1:
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact_list.append({"name": name, "phone": phone, "email": email, "address": address})
        print(f"Contact '{name}' added successfully.")

    elif choice == 2:
        if not contact_list:
            print("\nContact list is empty.")
        else:
            print("\nContact List:")
            for idx, contact in enumerate(contact_list, start=1):
                print(f"{idx}. {contact['name']} - {contact['phone']}")

    elif choice == 3:
        query = input("Enter name or phone number to search: ")
        results = [contact for contact in contact_list if query in contact['name'] or query in contact['phone']]
        if results:
            for contact in results:
                print(f"\nName: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
                print(f"Address: {contact['address']}")
        else:
            print("No contact found.")

    elif choice == 4:
        query = input("Enter the name or phone number of the contact to update: ")
        for contact in contact_list:
            if query in contact['name'] or query in contact['phone']:
                print(f"Updating contact '{contact['name']}'")
                new_name = input("Enter new name (leave blank to keep current): ")
                new_phone = input("Enter new phone number (leave blank to keep current): ")
                new_email = input("Enter new email (leave blank to keep current): ")
                new_address = input("Enter new address (leave blank to keep current): ")
                
                if new_name:
                    contact['name'] = new_name
                if new_phone:
                    contact['phone'] = new_phone
                if new_email:
                    contact['email'] = new_email
                if new_address:
                    contact['address'] = new_address

                print(f"Contact '{contact['name']}' updated successfully.")
                break
        else:
            print("No contact found to update.")

    elif choice == 5:
        query = input("Enter the name or phone number of the contact to delete: ")
        for idx, contact in enumerate(contact_list):
            if query in contact['name'] or query in contact['phone']:
                contact_list.pop(idx)
                print(f"Contact '{contact['name']}' deleted successfully.")
                break
        else:
            print("No contact found to delete.")

    elif choice == 6:
        print("Exiting the Contact Management System. Goodbye!")
        break

    else:
        print("Invalid choice. Please enter a number between 1 and 6.")