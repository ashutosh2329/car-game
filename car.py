print("Please enter help to start")
user_choice= ""
is_started = False
while True:
        user_choice=input('>').upper()
        if user_choice == 'START':
            if is_started:
                print('car is already started')
            else:
                is_started = True
                print('Car started...Ready to go!')
        elif user_choice == 'STOP':
            if not is_started:
                print('car is already stopped')
            else:
                is_started = False
                print('Car stopped.')
        elif user_choice== 'HELP':
            print('''
start - to start the car
stop - to stop the car
quit - to exit''')
        elif user_choice == "QUIT":
            break
        else:
            print("sorry,I don't understand that ")









