
def main():
    contacts = {}

    print("How can I help you?")

    while True:
        user_input = input("Enter a command: ").strip().lower()

        if user_input == "close" or user_input == "exit":
            print("Good bye!")
            break
        else:
            command, *args = parse_input(user_input)
            if command == "hello":
                hello()
            elif command == "add":
                add_contact(contacts, *args)
            elif command == "change":
                change_contact(contacts, *args)
            elif command == "phone":
                show_phone(contacts, *args)
            elif command == "all":
                show_all(contacts)
            else:
                print("Invalid command.")

def parse_input(user_input):
    return user_input.split()

def hello():
    print("How can I help you?")

def add_contact(contacts, name, phone_number):
    contacts[name] = phone_number
    print("Contact added.")

def change_contact(contacts, name, new_phone_number):
    if name in contacts:
        contacts[name] = new_phone_number
        print("Contact updated.")
    else:
        print("Contact not found.")

def show_phone(contacts, name):
    if name in contacts:
        print(contacts[name])
    else:
        print("Contact not found.")

def show_all(contacts):
    if contacts:
        for name, phone_number in contacts.items():
            print(f"{name}: {phone_number}")
    else:
        print("No contacts.")

if __name__ == "__main__":
    main()
