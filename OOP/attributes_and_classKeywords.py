def bark():
    print('woof')


class Dog:
    # CLASS OBJECT ATTRIBUTE
    # SAME FOR EVERY INSTANCE  OF A CLASS
    # not connected to any particular instance
    # it's value is same to every instance of a class, i.e. 'mammal', hence self keyword is not used
    # mentioned above init() method

    species = 'mammal'

    def __init__(self, breed, name):
        # init() method is called upon automatically every time we create an instance of a class
        # it always starts with 'self' keyword, which connects this method to the instance of a class
        # and allows us to refer to itself
        # 'breed' is any attribute the we define

        # init() is the constructor of a class, and it gets called automatically when you create an instance of a class
        # 'self' keyword represents the instance of the object itself
        # 'breed' is the parameter/argument that gets assigned to the attribute of init() i.e. self.breed
        # by convention the argument and attribute (breed and self.breed are named similar, but not necessary
        # when we will create an object of Dog(), self.breed will receive the value assigned in breed argument
        # like my_dog = Dog('Lab')
        # 'Lab' is the a value passed to argument breed, and attribute self.breed gets assigned to this value
        # by self.breed = breed
        # my_dog will show up the the value passed in the attribute self.breed
        # we can have more than one parameters and attributes, like, we added 'name' attribute and parameter
        # these are user defined attributes.
        # not every attribute mentioned inside init() need to be have passed as parameter, e.g. self.age
        # it does not require to be passed through parameters as we have kept its value 2
        self.breed = breed
        self.name = name
        self.age = 2

    # Methods:
    # Operations/Actions
    # inside of the class
    # will use the attributes of the class
    # 'self' keyword will actually connect method to the actual object or to instance of a class
    # 'self' keyword enable to access attributes of a class, both Class Object Attributes and attributes inside init()
    # method
    def bark(self):
        print('woof')
        print('Dog name is {}'.format(self.name))

    # method can have there own parameters to be passed like 'distance' in below 'run' method
    def run(self, distance):
        print('my {} dog {} of breed {} can run {} kms'.format(Dog.species, self.name, self.breed, distance))


my_dog = Dog('Lab', 'Sunny')

print(type(my_dog))
print(my_dog.breed)
print(my_dog.species)
my_dog.bark()
my_dog.run(10)
