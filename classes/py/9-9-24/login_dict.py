
data = {
    "dan": "tree123",
    "suche": "password12345y",
    "john": "abc"
}

def login (user, password):
    if user in data and data[username] == password:
        return True
    
    return False


while True:
    username = str(input("input your username: "))
    password = str(input("input your password: "))
    try:
        if not username:
            raise ValueError("input your username")
        if not password:
            raise ValueError("input your password")

        if " " in username or not username.islower():
            raise ValueError("invalid username")

        result = login(username, password)
        if result:
            print("ok")
            break
        else:
            print("try again")
    except ValueError as e:
        print(e) 


