import datetime as dt
"""

product - iphone16, macbook pro
- price
- name 

product item:
- id
- product


iphone16:
- price: 20 000kc
- items = {}

item iphone 16 
- serial number 209712498
- product - iphone 16

order:
- all items
- date and time of the order



order 104104:
date and time: 24. 1. 2025
all items = [
    iphone 16 124214
    iphone 16 124215
    iphone 16 124216
]

"""

class Product:
    def __init__(self, name: str, price: int):
        self.name = name
        self.price = price
        self.items = {} 
    
    def __str__(self):
        return f'<{self.__class__.__name__}> self.name'
    
    def add(self, identificator: int):
        self.items[identificator] = ProductItem(identificator, self)

    def get(self):
        # first_key = next(iter(self.items))
        # return self.items.pop()
        first_id = tuple(self.items)[0]
        return self.items.pop(first_id)


class ProductItem:
    def __init__(self, identificator: int, product: Product):
        self.product = product
        self.identificator = identificator                                                                       

    def __str__(self):
        return f'{self.product.name}: {str(self.identificator)}'

class Order:
    def __init__(self):
        self.date = dt.datetime.now()
        self.items = []


p1 = Product("IPhone 16", 20_000)
p2 = Product("LG TV", 18_000)

p1.add(235326)
p1.add(987147)
p1.add(701641)

next_iphone = p1.get()
print(next_iphone)
print("------------------------------")


for key, value in p1.items.items():
    print(key, value)