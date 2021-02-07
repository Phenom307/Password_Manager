from models import store_data, find_users, find_password_by_email
import pyperclip
from hashing import password

def menu():
    print('-'*30)
    print(('-'*13) + 'Menu'+ ('-' *13))
    print('1. Create new password')
    print('2. Find all sites and apps connected to an email')
    print('3. Find a password for a site or app')
    print('4. Add a password for a site or app')
    print('Q. Exit')
    print('-'*30)
    return input(': ').upper()

def add():
    print('Provide name of site or app')
    app_name = input().strip()
    print('Provide your username for site or app (if any)')
    user = input()
    print('Provide your email address for site or app')
    email = input()
    print('Provide your password')
    passw = input()
    print('Provide URL for the site')
    url = input()
    print("\n" + 'Your information has been stored succesfully!' + "\n")
    store_data(app_name, passw, user, email, url)

def create():
    print('Please proivide the name of the site or app you want to generate a password for')
    app_name = input()
    print('Please provide a simple password for this site: ')
    plaintext = input()
    passw = password(plaintext, app_name, 12)
    pyperclip.copy(passw)
    # pyperclip.run("pbcopy", universal_newlines=True, input=passw)
    print('-'*30)
    print('')
    print('Your password has now been created and copied to your clipboard')
    print('')
    print('-' *30)
    print('Please provide a user email for this app or site')
    email = input()
    print('Please provide a username for this app or site (if applicable)')
    user = input()
    if user == None:
        user = ''
    print('Please paste the url to the site that you are creating the password for')
    url = input()
    store_data(app_name, passw, user, email, url)

def find_password():
   print('Please proivide the name of the site or app you want to find the password to')
   app_name = input("App name: ")
   find_password_by_email(app_name)

def find_accounts():
   print('Please proivide the email that you want to find accounts for')
   user_email = input("Email id: ") 
   find_users(user_email)
