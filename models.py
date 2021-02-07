import pymongo

try:
    uri = "mongodb://127.0.0.1:27017"
    client = pymongo.MongoClient(uri)
    db = client.Passwords
    Passwords = db["Passwords"]
except:
    print("Connection Failed. Try again later!")

def store_data(app_name, passw, user, email, url):    
    Passwords.insert({
        'App_name': app_name,
        'Email': email,
        'Username': user,
        'Password': passw,
        'URL': url
    })

def find_users(user_email):
    email = Passwords.find({
        "Email": user_email
    })
    email1 = Passwords.find({
        "Email": user_email
    }).count()
    
    print("\n" + "There are " + str(email1) + " results")
    for data in email:
        print("\n" + " App name is: " + data['App_name'] + "\n" + " Email id is: " + data['Email'] + "\n" + " Password is: " + data['Password'] + "\n")
    
def find_password_by_email(app_name):
    data = Passwords.find_one({
        "App_name": app_name
    })

    print("Your Password for " + app_name + " is: " + data['Password'])
