def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_phone(args, contacts):
    name, new_phone = args
    if name in contacts:
        contacts[name] = new_phone
        return "Phone number updated."
    else:
        return "Contact not found."

def show_phone(args, contacts):
    if args:
        name = args[0]
        if name in contacts:
            return f"Phone number for {name}: {contacts[name]}"
        else:
            return "Contact not found."
    else:
        return "Please provide a contact name."

def show_all_contacts(contacts):
    if contacts:
        all_contacts = "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])
        return "All contacts:\n" + all_contacts
    else:
        return "No contacts available."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_phone(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all_contacts(contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
