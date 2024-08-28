import random

random_num = random.randint(0, 10)

while True:
    users_num = input("Pick a number between 0 and 10: ")
    if len(users_num) > 0:
        print(f'your number is {users_num}')
    else:
        print("error, put in a number")
    
    if int(users_num) == random_num:
        print(f'the number i was thinking of was {random_num}, you won!')
        break
    else:
        print(f'{users_num} was not the number i was thinking of, choose another one')