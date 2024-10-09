import random

class Iterator:
    def __init__(self, max_count):
        self.max_count = max_count
        self.counter = 0

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.counter < self.max_count:
            self.counter += 1
            return random.randint(1, 100)
        else:
            raise StopIteration
    

iterator = Iterator(10)
print(next(iterator))
    
for item in iterator:
    print(item)