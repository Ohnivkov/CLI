from collections import UserDict
from datetime import datetime
import pickle
import os
class Field:
    def __init__(self, value):
        self._value = None
        self.value = value

    @property
    def value1(self) -> str:
        return self._value


class Name(Field):
    pass


class Phone(Field):
    @Field.value1.setter
    def value(self, value) -> None:
        if 8 <= len(value) <= 10:
            self._value = value
        else:
            raise ValueError('Wrong phone')


class Birthday(Field):
    @Field.value1.setter
    def value(self, value) -> None:
        try:
            now_time = datetime.now().date()
            new_format_date = datetime.strptime(value, '%Y-%m-%d').date()
            birthday_date = datetime(now_time.year, new_format_date.month, new_format_date.day).date()
            if now_time > birthday_date:
                birthday_date = datetime(now_time.year + 1, new_format_date.month, new_format_date.day).date()
            self._value = birthday_date
        except:
            raise ValueError('Wrong birthday')


class Record:

    def __init__(self, name, phone=None, birthday=None):
        self.name = Name(value=name)
        self.phones = []
        self.birthday_date = None
        if phone:
            self.add_number(phone)
        if birthday:
            self.birthday_date = Birthday(value=birthday)

    def add_number(self, phone):
        phone = Phone(value=phone)
        self.phones.append(phone.value)

    def remove_number(self, phone):
        self.phones = adresbook[self.name.value]
        for number in self.phones:
            if phone == number:
                self.phones.remove(number)

    def days_to_birthday(self):
        now = datetime.now().date()
        if adresbook[self.name.value].birthday_date.value:
            delta = adresbook[self.name.value].birthday_date.value - now
            return delta.days
        else:
            raise ValueError('No information for birthday')


class AdressBook(UserDict):
    def add_record(self, record: Record):
        self.data[record.name.value] = record

    def finder(self, request):
        found_requests = ''
        for name, value in self.data.items():
            if request in name or request in str(value.phones):
                found_requests += f'{name}: {value.phones}\n'
        return found_requests



adresbook = AdressBook()
if os.path.exists('data.bin'):
    with open('data.bin', 'rb') as fh:
        adresbook.data = pickle.load(fh)
class Iterable:
    page_counter = 0

    def __init__(self, n=5):
        self.counter = 1
        self.contacts_for_page = n
        self.info_list = [(key, items) for key, items in adresbook.items()]

    def __next__(self):
        if self.counter <= self.contacts_for_page and len(adresbook) != Iterable.page_counter:
            self.counter += 1
            Iterable.page_counter += 1
            return self.info_list[Iterable.page_counter - 1][0], self.info_list[Iterable.page_counter - 1][1]
        raise StopIteration


class CustomIterator:
    def __init__(self, n):
        self.n = n

    def __iter__(self):
        return Iterable(self.n)


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


page_counter = 0


@input_error
def show_all(n=5):
    global page_counter
    page_counter = n
    contacts = ''
    limit = CustomIterator(int(n))
    for i in limit:
        contacts += f'{i[0]} : {i[1].phones} {i[1].birthday_date.value} \n' if i[
            1].birthday_date else f'{i[0]} : {i[1].phones} \n'
    if Iterable.page_counter == len(adresbook):
        Iterable.page_counter = 0
        return contacts + "that's all"
    else:
        return contacts + 'type "next" if you want see more'


@input_error
def exit_func():
    return 'good bye'


@input_error
def class_processor(command, task):
    if task == 'add':
        if len(parse_command(command)) == 2:
            name, phones = parse_command(command)[0], parse_command(command)[1]
            record = Record(name)
        else:
            name, phones, birthday = parse_command(command)[0], parse_command(command)[1], parse_command(command)[2]
            record = Record(name, birthday=birthday)
        if name not in adresbook:
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
            record = Record(name)
            for phone in phones:
                if phone in adresbook[name]:
                    record.remove_number(phone)
                    adresbook.add_record(record)
                else:
                    raise ValueError('Wrong phone')
        else:
            raise ValueError('Wrong name')
    elif task == 'days_to_birthday':
        name = parse_command(command)
        record = Record(name)
        return record.days_to_birthday()
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
    'search': class_processor,
    'days_to_birthday': class_processor,
    'next': show_all
}


def get_command(input):
    command = ''
    user_input = ''
    for key in Command_dict:
        if input.strip().lower().startswith(key):
            command = key
            user_input = input[len(command):].strip()
            break
    if command in ('add', 'search', 'remove', 'days_to_birthday'):
        return Command_dict[command](user_input, command)
    elif command:
        if user_input:
            return Command_dict[command](user_input)
        else:
            if command == 'next':
                if Iterable.page_counter != 0 and len(adresbook) > int(page_counter):
                    return Command_dict[command](page_counter)
                else:
                    return 'Wrong command'
            else:

                return Command_dict[command]()

    else:
        return 'Wrong command'


def parse_command(command):
    new_command = command.split(' ')
    name = new_command[0]
    if len(new_command) == 1:
        return name
    elif not new_command[-1].isnumeric():
        phones = new_command[1:-1]
        birthday = new_command[-1]
        return name, phones, birthday
    else:
        phones = new_command[1:]
        return name, phones
