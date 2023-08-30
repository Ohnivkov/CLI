phone_numbers_dict={}
def input_error(func):
    def inner(*args,**kwargs):
        try:
            func(*args,**kwargs)
        except IndexError:
            if inner in (add_number,change_number):
                print("Give me name and phone please")
            elif inner == get_phone:
                print("Enter user name")
        except KeyError:
            if inner == change_number:
                print('there is no such name in the phone book')
            elif inner == add_number:
                print('this name already exists in the phone book')
    return inner

@input_error
def add_number(command):
    command = command.split(' ')
    if is_keyindict(command[1]):
        raise KeyError
    else:
        phone_numbers_dict[command[1]] = command[2]
@input_error
def change_number(command):
    command = command.split(' ')
    if is_keyindict(command[1]):
        phone_numbers_dict[command[1]] = command[2]
    else:
        raise KeyError
@input_error
def get_phone(command):
    command = command.split(' ')
    print(phone_numbers_dict[command[0]])
@input_error
def show_all():
    for i in phone_numbers_dict:
        print(f'{i}: {phone_numbers_dict[i]}')
def is_keyindict(key):
    if key in phone_numbers_dict:
        return True
    else:
        return False