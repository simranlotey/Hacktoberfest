contacts = {}

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email: ")
    contacts[name] = {'phone': phone, 'email': email}
    print(f"{name} has been added to your contacts.")

def retrieve_contact():
    name = input("Enter the name of the contact you want to retrieve: ")
    contact = contacts.get(name)
    if contact:
        print(f"Name: {name}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
    else:
        print(f"{name} is not in your contacts.")

def main():
    while True:
        print("\nContact Manager")
        print("1. Add a contact")
        print("2. Retrieve a contact")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            retrieve_contact()
        elif choice == "3":
            print("Exiting contact manager.")
            break
        else:
            print("Invalid choice. Please choose 1, 2, or 3.")

if __name__ == "__main__":
    main()
