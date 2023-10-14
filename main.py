import handler
import pickle
def main():
    while True:
        user_input = input('Enter command for bot: ')
        result = handler.get_command(user_input)
        print(result,end='\n')
        if result == 'good bye':
            break
    with open('data.bin','wb') as fh:
        pickle.dump(handler.adresbook.data, fh)
if __name__ == '__main__':
    main()
#bbbbbbbbb