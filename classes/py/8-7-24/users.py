import os

def get_user_info():
    username = input("enter your username: ")
    password = input("enter your password: ")
    return [username, password]

def user_verification_process():
    file_in_users = os.path.join("C:/Users/adamk/Desktop/programovani/step_fullstack/classes/py/8-7-24/users" + "/" + username + ".txt")
    user_exists = os.path.isfile(file_in_users)
    success = False
    return [file_in_users, user_exists, success]

def password_verification_process(file_in_users, password):
    with open(file_in_users) as file:
            content = file.read() 
            if content == password: 
               success = True
               return success

def new_password_creation(file_in_users, password):
    with open(file_in_users, "w") as file:
            file.write(password)
    print("signup successful")
    
print(os.path.isdir("C:/Users/adamk/Desktop/programovani/step_fullstack/classes/py/8-7-24/users"))
signup_login = input("if you want to login into the system, type 1, if you want to sign up, type 2: ")

if signup_login == "1":
    username, password = get_user_info()

    file_in_users, user_exists, success = user_verification_process()
    if user_exists:
        success = password_verification_process(file_in_users, password)
    if success:
        print("login successful")
        success = True
    else:
        print("login unsuccessful")


elif signup_login == "2":
    username, password = get_user_info()

    file_in_users, user_exists, success = user_verification_process()
    if user_exists:
        print("username taken, please restart the program and choose a different one")
    elif user_exists == False:
        new_password_creation(file_in_users, password)
    else:
        print("invalid input")