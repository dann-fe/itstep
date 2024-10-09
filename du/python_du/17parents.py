class Person:
    def __init__(self: str, name, father = None, mother = None):
        self.name = name
        self.father = father
        self.mother = mother

    def return_parents(self):
        return (self.father, self.mother)


john = Person("John", "Daniel")
print(john.return_parents())