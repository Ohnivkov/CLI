import handler

while True:
    line = input()
    command = line.split(' ')[0].lower()
    if line.lower() in ('good bye', 'close', 'exit'):
        print("Good bye!")
        break
    elif line.lower() == 'hello':
        print("How can I help you?")
    elif command == 'add':
        try:
            name = line.split(' ')[1]
            phone = line.split(' ')[2]
            if handler.add_number(name, phone) == KeyError:
                print('this name already exists in the phone book')
        except:
            print("Give me name and phone please")
    elif command == 'change':
        try:
            name = line.split(' ')[1]
            phone = line.split(' ')[2]
            if handler.change_number(name, phone) == KeyError:
                print('there is no such name in the phone book')
        except:
            print("Give me name and phone please")

    elif command.lower() == 'phone':
        try:
            name = line.split(' ')[1]
            if handler.get_phone(name)==KeyError:
                print('there is no such name in the phone book')
        except:
            print("Enter name")
    elif line.lower() == 'show all':
        for i in handler.show_all():
            print(i)
