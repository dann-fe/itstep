
username = input("whats your username?")
age = input("how old are you?")

with open("C:/Users/adamk/Desktop/programovani/step_fullstack/du/python_du/user02.txt", mode="a") as file:
    file.write(f"username: {username}\n"
               f"age: {age}\n")