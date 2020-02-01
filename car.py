
print('Please enter help to start the game!')
user_option=input('>')
if user_option.upper() == 'HELP':
    print('''start - to start the car
stop - to stop the car
quit - to exit''')
    user_choice=input('>')
    while user_choice.upper() != 'QUIT':
        if user_choice.upper() == 'START':
            print('Car started...Ready to go!')
            user_choice=input('>')
        elif user_choice.upper() == 'STOP':
            print('Car stopped.')
            user_choice=input('>')
        else:
            print("I don't understand that...")
            user_choice=input('>')







