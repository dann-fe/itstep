class Human:
    def __init__(self, name, age):
        self.name = name
        self._age = age # '_' in something = private information

    def __len__(self):
        return 10

john = Human("John", 23)

print(john.name)
print(john._age)

print(len(john))