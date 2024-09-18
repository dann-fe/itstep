import datetime as dt

with open('C:/Users/adamk/Desktop/programovani/step_fullstack/classes/py/9-16-24/template.html', encoding="utf-8") as file:
    TEMPLATE = file.read()


class User:
    def __init__(self, identifier: int, name, birth_date, description):
        self.id = identifier
        self.name = name
        self.bd = birth_date
        self.description = description
        self.friends = set()
    
    def __str__(self):
        return f'{self.name}[{self.id}]'

    @classmethod
    def shared_friends(cls, person1: "User", person2: "User"):
        return person1.friends & person2.friends

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
    
    def add_more_friends(self, friends_list: list):
        for friend in friends_list:
            self.add_friend(friend)


    def make_html(self):
        html = TEMPLATE
        d = self.bd
        bd = f'{d.day}. {d.month}. {d.year}'
        replace_values = (
            ("{name}", self.name),
            ("{bd}", bd),
            ("{age}", str(self.age)),
            ("{description}", self.description),
            ("{id}", str(self.id)),
            ("{friends}", self.get_html_friends()),
        )

        for key, value in replace_values:
            html = html.replace(key, value)

        with open(f'C:/Users/adamk/Desktop/programovani/step_fullstack/classes/py/9-16-24/html/{self.id}.html', mode="w", encoding="utf-8") as file:
            file.write(html)

    def get_html_friends(self):
        html = ""
        for item in self.friends:
            html += f'<li>{item.name}</li>'

        return html

john123 = User(1, "john123", dt.date(1932, 4, 28), "hi, im john123")
jirik = User(2, "jirik", dt.date(2001, 12, 5), "hi, im jirik")
dan = User(3, "dan", dt.date(2009, 10, 11), "hi, im dan hello")

dan.add_more_friends([john123, jirik])
john123.add_friend(jirik)

print(User.shared_friends(john123, dan))

print("dan: ",dan.friends)

print(john123, jirik, dan)

jirik.make_html()
dan.make_html()
john123.make_html()