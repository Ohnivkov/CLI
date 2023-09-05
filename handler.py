from collections import UserDict


class Field:
    def __init__(self, value):
        self.value = value


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:

    def __init__(self, name, phone=None):
        self.name = Name(value=name)
        self.phones = []
        if phone:
            self.add_number(phone)

    def add_number(self, phone):
        phone =Phone(value=phone)
        self.phones.append(phone.value)

    def remove_number(self, phone):
        self.phones=adresbook[self.name.value]
        for number in self.phones:
            if phone==number:
                self.phones.remove(number)


class AdressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record.phones
    def finder(self, request):
        found_requests = ''
        for name, phone in self.data.items():
            if request in name or request in str(phone):
                found_requests += f'{name}: {phone}\n'
        return found_requests


adresbook = AdressBook()


def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except TypeError:
            return 'wrong command'
        except IndexError:
            return 'print: name and number'
        except KeyError:
            return 'Wrong name'
        except ValueError as e:
            return e.args[0]

    return inner


@input_error
def hello_func():
    return 'How can i help you'


@input_error
def change_number(data):
    name, phone = parse_command(data)
    if name in adresbook:
        adresbook[name] = phone
        return 'You changed number'
    else:
        raise ValueError('this contact does not exist')


@input_error
def show_all():
    contacts = ''
    for key, value in adresbook.items():
        contacts += f'{key} : {value} \n'
    return contacts[0:-2]


@input_error
def exit_func():
    return 'good bye'


@input_error
def class_processor(command, task):
    if task == 'add':
        name, phones = parse_command(command)[0], parse_command(command)[1]
        if name not in adresbook:
            record = Record(name)
            for phone in phones:
                if not phone.isnumeric():
                    raise ValueError('Wrong phone.')
                record.add_number(phone)
            adresbook.add_record(record)
            return 'Number added'
        else:
            raise ValueError('The contact is in adressbook')
    elif task == 'remove':
        name, phones = parse_command(command)[0], parse_command(command)[1]
        if name in adresbook:
            record=Record(name)
            for phone in phones:
                if phone in adresbook[name]:
                    record.remove_number(phone)
                    adresbook.add_record(record)
                else:
                    raise ValueError('Wrong phone')
        else:
            raise ValueError('Wrong name')
    else:
        request = command
        if adresbook.finder(request):
            return adresbook.finder(request)
        else:
            return 'no results'


Command_dict = {
    'hello': hello_func,
    'exit': exit_func,
    'close': exit_func,
    'good bye': exit_func,
    'change': change_number,
    'show all': show_all,
    'add': class_processor,
    'remove': class_processor,
    'search': class_processor
}


def get_command(input):
    command = ''
    user_input = ''
    for key in Command_dict:
        if input.strip().lower().startswith(key):
            command = key
            user_input = input[len(command):].strip()
            break
    if command in ('add', 'search', 'remove'):
        return Command_dict[command](user_input, command)
    elif command:
        if user_input:
            return Command_dict[command](user_input)
        else:
            return Command_dict[command]()
    else:
        return 'Wrong command'


def parse_command(command):
    new_command = command.split(" ")
    name = new_command[0]
    phone = new_command[1:]
    if name.isnumeric():
        raise ValueError('Wrong name.')

    return name, phone

