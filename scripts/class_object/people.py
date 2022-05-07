# model test class People

class People:
    def __init__(self, name):
        self.Name = name

    def welcome(self):
        print(f'Hello no welcome: {self.Name}')


new_people = People('Dieisson Martins')
new_people.welcome()
