class Animal:

    def __init__(self):
        print('Animal created')

    def who_am_i(self):
        print('I am an animal')

    def eats(self):
        print('I am eating')


myAnimal = Animal()
myAnimal.eats()
myAnimal.who_am_i()


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print('Dog created')

    # method overriding
    def who_am_i(self):
        print('I am a dog')

    # method of child class
    def bark(self):
        print('woof')


dog = Dog()


dog.who_am_i()
dog.eats()
dog.bark()
