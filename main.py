import handler
while True:
    line=input()
    command=line.split(' ')[0].lower()
    if line.lower() in ('good bye','close','exit'):
        print("Good bye!")
        break
    elif line.lower()=='hello':
        print("How can I help you?")
    elif 'add' == command:
        handler.add_number(line)
    elif 'change' == command:
        handler.change_number(line)
    elif 'phone' == command.lower():
        handler.get_phone(line)
    elif 'show all' == line.lower():
        handler.show_all()