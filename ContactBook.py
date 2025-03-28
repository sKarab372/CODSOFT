contact_book = []

def add_contact(name, phone,email,address):
    contact = {
        'name': name,
        'phone': phone,
        'email': email,
        'address': address
    }
    contact_book.append(contact)
    print(f"Contact '{name}' added successfully.") 

def view_contacts():
    if len(contact_book) == 0:
        print("No contacts available.")
    else:
        print("Contacts:")
        for i, contact in enumerate(contact_book):
            print(f"{i + 1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}, Address: {contact['address']}")

def delete_contact(index):
    if 0 <= index < len(contact_book):
        deleted_contact = contact_book.pop(index)
        print(f"Contact '{deleted_contact['name']}' deleted successfully.")
    else:
        print("Invalid contact number.")

def main():
    flag = True
    while flag:
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            name = input("Enter contact name: ")
            phone = input("Enter contact phone number: ")
            email = input("Enter contact email: ")
            address = input("Enter contact address: ")
            add_contact(name, phone, email, address)
        elif choice == 2:
            view_contacts()
        elif choice == 3:
            view_contacts()
            contact_num = int(input("Enter the contact number to delete: ")) - 1
            delete_contact(contact_num)
        elif choice == 4:
            print("Bye, bye!!!")
            flag = False
        else:
            print("Invalid choice. Choose again.")

if __name__ == "__main__":
    main()
# This code implements a simple contact book application that allows users to add, view, and delete contacts.
# It uses a list to store contacts and provides a menu for user interaction.
# The contacts are stored as dictionaries with 'name', 'phone', 'email', and 'address' as keys.
# The application handles user input and provides feedback for successful operations.