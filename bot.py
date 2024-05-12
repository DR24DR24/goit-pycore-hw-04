def parse_input(user_input):
    try:
        cmd, *args = user_input.split()
        cmd = cmd.strip().lower()
        return cmd, *args
    except:
        print("cann't parse")
        return "",""

def add_contact(args, contacts):
    try:
        name, phone = args
        if  (name in contacts):
            raise IndexError
        contacts[name] = phone
        return "Contact added."
    except IndexError : 
        return "user exists"
    except:
        return "cann't add"

def change_contact(args, contacts):
    try:
        name, phone = args
        if not (name in contacts):
            raise IndexError
        contacts[name] = phone
        return "Contact changed"
    except IndexError : 
        return "no such user"
    except: 
        return "cann't change"

def phone_contact(args, contacts):
    try:
        name = args[0]
        print(contacts[name])
        return "Print contact."
    except:
        return "cann't find contact"

def all_contact(args, contacts):
    try:
        for user, phone in contacts.items():
            print(f"user: {user} phone: {phone}")
        return "that is аll contacts."
    except:
        print("cann't print all contacts")


def main():
    try:
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
                print(change_contact(args, contacts))
            elif command == "phone":
                print(phone_contact(args, contacts)) 
            elif command == "all":
                print(all_contact(args, contacts)) 
          
    
            else:
                print("Invalid command.")
    except:
        print("unknown error")

if __name__ == "__main__":
    main()
