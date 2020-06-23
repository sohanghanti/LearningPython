class Dog:

    def __init__(self, name):
        self.name = name

    def speaks(self):
        return self.name + ' says woof'


class Cat:

    def __init__(self, name):
        self.name = name

    def speaks(self):
        return self.name + ' says meow'


dog = Dog('Sammy')
cat = Cat('Catty')


# speaks method in both the classes show different output
print(dog.speaks())
print(cat.speaks())

for pet in [dog, cat]:
    print(pet.speaks())


def pet_speak(p):
    print(p.speaks())


pet_speak(dog)
pet_speak(cat)

