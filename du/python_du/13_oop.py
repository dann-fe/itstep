class Planet:
    def __init__(self, name = str, order = int):
        self.name = name
        self.order = order

    def info(self):
        print(f'Hi, im {self.name} and im on the {self.order}. place in the solar system')


Earth = Planet("Earth", 3)
Earth.info()

Venus = Planet("Venus", 2)
Venus.info()