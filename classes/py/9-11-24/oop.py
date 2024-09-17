# oop - Object Oriented Programming
#       class - broad definition - multiple instances in a class
#       instance - it's a concrete 'thing' that you made using a specific class. One of things that are in a certain classw


class Human:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def greeting(self):
        print(f'Hi, im {self.name} and im {self.age} years old, im {self.height}cm tall')

    def am_i_old_enough(self):
        if self.age >= 18:
            return True
        else:
            return False
        
    
Dan = Human("Dan", 20, 178)
Peter = Human("Peter Black", 71, 185)
Dan_f = Human("Daniil Fedotov", 14, 174)

Dan.greeting()
print(Dan.am_i_old_enough())
Peter.greeting()
Peter.am_i_old_enough()
Dan_f.greeting()
Dan_f.am_i_old_enough()