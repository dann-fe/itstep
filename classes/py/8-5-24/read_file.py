# file = open("classes/py/5-8-24/read_file.txt")

# print(file.read())

# file.close()

direction = "classes/py/5-8-24/read_file.txt"

with open(direction, mode="a") as file:
    file.write("test_12345678")