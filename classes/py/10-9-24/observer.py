class Channel:
    def __init__(self):
        self.subscribers = set()

    def add_sub(self, user):
        self.subscribers.add(user)
        print(f'User {user} subscribed')

    def remove_sub(self, user):
        self.subscribers.remove(user)
        print(f'User {user} unsubscribed')

    def notify(self, text):
        for user in self.subscribers:
            user.update(text)

class User:
    def __init__(self, name):
        self.name = name

    def update(self, text):
        print(f'Notification for {self.name}: {text}')


ch1 = Channel()
u1 = User("john")
u2 = User("dan")
u3 = User("peter")

ch1.add_sub(u1)
ch1.add_sub(u3)
ch1.notify("new video")