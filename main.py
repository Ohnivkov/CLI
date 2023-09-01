import handler
def main():
    while True:
        user_input = input('Enter command for bot: ')
        result = handler.get_command(user_input)
        print(result,end='\n')
        if result == 'good bye':
            break

if __name__ == '__main__':
    main()