phone_numbers_dict={}
def input_error(func):
     def inner(*args, **kwargs):
        try:
            return func(*args,**kwargs)
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
def add_number(data):
    name,phone=parse_command(data)
    if name in phone_numbers_dict:
        raise ValueError('This contact already exist.')
    else:
        phone_numbers_dict[name] = phone
        return 'You added number'

@input_error
def change_number(data):
    name,phone=parse_command(data)
    if name in phone_numbers_dict:
        phone_numbers_dict[name] = phone
        return 'You changed number'
    else:
        raise ValueError('this contact does not exist')

@input_error
def get_phone(name):
    if name in phone_numbers_dict:
        result=phone_numbers_dict[name]
        return result
    else:
        raise ValueError('this contact does not exist')

@input_error
def show_all():
    contacts=''
    for key,value in phone_numbers_dict.items():
        contacts+=f'{key} : {value} \n'
    return contacts[0:-2]

@input_error
def exit_func():
    return 'good bye'

Command_dict={
    'hello':hello_func,
    'exit':exit_func,
    'close':exit_func,
    'good bye':exit_func,
    'add':add_number,
    'change':change_number,
    'show all':show_all,
    'phone':get_phone
}

def get_command(input):
    command = input
    user_input = ''
    for key in Command_dict:
        if input.strip().lower().startswith(key):
            command = key
            user_input = input[len(command):].strip()
            break
    if command:
        if user_input:
            return Command_dict[command](user_input)
        else:
            return Command_dict[command]()
    return 'Wrong input'
def parse_command(command):
    new_command = command.split(" ")
    name = new_command[0]
    phone = new_command[1]
    if name.isnumeric():
        raise ValueError('Wrong name.')
    if not phone.isnumeric():
        raise ValueError('Wrong phone.')
    return name, phone