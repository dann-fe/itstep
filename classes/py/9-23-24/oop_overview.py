class Dog:
    MAX_COUNT = 10  
    DOG_LIST = set()

    def __init__(self, name: int, gender: bool, breed: str, age: int):
        """
        1: male
        2: female
        """

        self.name = name
        self.gender = gender
        self.breed = breed
        self.age = age
        
        if len(self.DOG_LIST) < self.MAX_COUNT:
            self.DOG_LIST.add(self)
        else:
            raise ValueError("more dogs than it is allowed")

    def bark(self):
        return "woof woof"
    
    @classmethod
    def info(cls):
        print("classmethod", cls)

    @staticmethod
    def function():
        print("does not need any references (self or cls)")

    @property
    def human_age(self):
        return self.age * 7

my_dog = Dog("dan", 1, "husky", "5")
print(my_dog.bark())

print(Dog.DOG_LIST)