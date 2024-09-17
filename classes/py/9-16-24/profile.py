import datetime as dt

class User:
    def __init__(self, identifier: int, name, birth_date, description):
        self.id = identifier
        self.name = name
        self.bd = birth_date
        self.description = description
        self.friends = set()
    
    def __str__(self):
        return f'{self.name}[{self.id}]'

    def __repr__(self):
        return str(self)
 
    @property
    def age(self):
        difference =  dt.date.today() - self.bd
        return int(difference.days / 365)
    
    @property
    def user_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "age": self.age,
            "description": self.description
        }

    def add_friend(self, friend):
        if friend is not self:
            self.friends.add(friend)
        else:
            raise ValueError
    
    def remove_friend(self, friend):
        if friend in self.friends:
            self.friends.remove(friend)
            print(f'your friend {friend} was removed')
        else:
            raise ValueError
    
john123 = User(1, "john123", dt.date(1932, 4, 28), "hi, im dan123")
jirik = User(2, "jirik", dt.date(2001, 12, 5), "hi, im jirik")
dan = User(3, "dan", dt.date(2009, 10, 11), "hi, im dan hello")

dan.add_friend(john123)
dan.add_friend(jirik)
john123.add_friend(jirik)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     
jirik.add_friend(john123)
john123.remove_friend(jirik)

print("john123: ", john123.friends)
print("jirik: ", jirik.friends)
print("dan: ",dan.friends)

print(john123, jirik, dan)