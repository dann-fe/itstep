password_input = input("put in your password: ")

def password_long_enough():
    if len(password_input) >= 8:
        print("your password is long enough")
    else:
       print("your password isn't long enough") 

