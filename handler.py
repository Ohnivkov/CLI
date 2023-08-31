phone_numbers_dict={}
def input_error(func):
     def inner(*args, **kwargs):
        try:
            if inner == get_phone:
                print(func(*args, **kwargs))
            else:
                func(*args,**kwargs)
        except KeyError:
            return KeyError
     return inner
@input_error
def add_number(name,phone):
    if is_keyindict(name):
        raise KeyError
    else:
        phone_numbers_dict[name] = phone
@input_error
def change_number(name,phone):

    if is_keyindict(name):
        phone_numbers_dict[name] = phone
    else:
        raise KeyError
@input_error
def get_phone(name):
    if is_keyindict(name):
        result=phone_numbers_dict[name]
        return result
    else:
        raise KeyError
def show_all():
    for i in phone_numbers_dict:
        yield f'{i}: {phone_numbers_dict[i]}'
def is_keyindict(key):
    if key in phone_numbers_dict:
        return True
    else:
        return False