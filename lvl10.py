class Thing:
    pass


class Thing2:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f'{self.name} is {self.age}'


class Thing3:
    def __init__(self):
        self.letters = 'xyz'


example = Thing3()
print(example.letters)
i = {'name': 'Alla', 'age': '57'}
persona = Thing2(**i)
print(persona)
