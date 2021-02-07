from menu import find_password, menu, add, find_accounts, create
from models import db, Passwords

secret = '1'

attempts = 3
print("Remaining Attempts: " + str(attempts))

while(attempts > 0):
    passw = input('Please provide the master password to start using Password Manager: ')

    if passw == secret:
        print('You\'re in')
        break
        
    else:
        print('Wrong Password! Try Again.')   
        attempts = attempts-1
        if attempts == 0:
            print('\n' + 'Pity you!')
            exit()        

choice = menu()
while choice != 'Q':
    if choice == '1':
        create()
    if choice == '2':
        find_accounts()
    if choice == '3':
        find_password()
    if choice == '4':
        add()
    else:
        choice = menu()
exit()


# if __name__ == "__main__":
#     app.run(debug=True)
