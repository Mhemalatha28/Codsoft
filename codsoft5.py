# Contact Management System

contacts = {}

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    print(f"\n✅ Contact '{name}' added successfully!")

def view_contacts():
    if not contacts:
        print("\n📭 No contacts found.")
        return
    print("\n📖 Contact List:")
    print("-" * 40)
    for name, details in contacts.items():
        print(f"Name: {name}")
        print(f"Phone: {details['Phone']}")
        print(f"Email: {details['Email']}")
        print(f"Address: {details['Address']}")
        print("-" * 40)

def search_contact():
    search = input("🔍 Enter name or phone number to search: ")
    found = False
    for name, details in contacts.items():
        if search.lower() in name.lower() or search == details['Phone']:
            print("\n✅ Contact Found:")
            print(f"Name: {name}")
            print(f"Phone: {details['Phone']}")
            print(f"Email: {details['Email']}")
            print(f"Address: {details['Address']}")
            found = True
            break
    if not found:
        print("\n❌ Contact not found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        print("\nEnter new details (leave blank to keep current value):")
        phone = input(f"New Phone [{contacts[name]['Phone']}]: ") or contacts[name]['Phone']
        email = input(f"New Email [{contacts[name]['Email']}]: ") or contacts[name]['Email']
        address = input(f"New Address [{contacts[name]['Address']}]: ") or contacts[name]['Address']
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        print(f"\n🔄 Contact '{name}' updated successfully!")
    else:
        print("\n❌ Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"\n🗑️ Contact '{name}' deleted successfully!")
    else:
        print("\n❌ Contact not found.")

def main_menu():
    while True:
        print("\n------ CONTACT MANAGEMENT SYSTEM ------")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("\n👋 Thank you for using the Contact Management System!")
            break
        else:
            print("\n⚠️ Invalid choice! Please try again.")

main_menu()
