class Human:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def introduce(self):
        print(f'hi, im {self._name} and im {self._age} years old')

class ShyPerson(Human): #took the __init__ from class Human


    def introduce(self):
        print(f'hi, im shy')

john = Human("john", 25)
john.introduce()
dan = ShyPerson("dan", 40)
dan.introduce()