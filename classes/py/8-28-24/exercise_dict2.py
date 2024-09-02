people = {
    "John": 180,
    "Peter": 170,
    "Kevin": 200,
    1: 1000000000,
    True: False,
}

people2 = {
    "Jacob": 160,
    "Peter": 190,
}

people.update(people2)

print(people)

print(people.get("Peter"))
print(people["Dan"])