def parse_input(user_input):
    """Розбиває введений рядок на команду (у нижньому регістрі) та аргументи."""
    parts = user_input.split()
    if not parts:
        return "", []  # порожній ввід
    cmd, *args = parts
    cmd = cmd.strip().lower()
    return cmd, args


def add_contact(args, contacts):
    """Додає новий контакт (або перезаписує існуючий)."""
    if len(args) != 2:
        return "Invalid format. Use: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return "Contact added."


def change_contact(args, contacts):
    """Змінює номер телефону для існуючого контакту."""
    if len(args) != 2:
        return "Invalid format. Use: change [name] [new phone]"
    name, phone = args
    if name not in contacts:
        return f"Contact '{name}' not found."
    contacts[name] = phone
    return "Contact updated."


def show_phone(args, contacts):
    """Повертає номер телефону для зазначеного контакту."""
    if len(args) != 1:
        return "Invalid format. Use: phone [name]"
    name = args[0]
    if name not in contacts:
        return f"Contact '{name}' not found."
    return contacts[name]


def show_all(contacts):
    """Повертає всі збережені контакти з номерами телефонів."""
    if not contacts:
        return "No contacts saved."
    return "\n".join(f"{name}: {phone}" for name, phone in contacts.items())


def main():
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()