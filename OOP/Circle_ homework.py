class Circle:
    pi = 3.14

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.radius ** self.radius * Circle.pi

    def circumference(self):
        return 2 * Circle.pi * self.radius


c = Circle(6)
print(c.area())
print(c.circumference())
