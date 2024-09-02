people = {
    "John": 180,
    "Peter": 170,
    "Kevin": 200,
    1: 1000000000,
    True: False,
}

# print(people)
# print(list(people))
# print(ple.values())
# print(list(people.values()))eop

print(people.items())

for key, value in people.items():
    print(key, value)