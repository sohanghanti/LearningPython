from abc import ABC, abstractmethod


# classes contain one or more abstract methods
# abstract methods do not have implementation in abstract class,
# they have only definition of abstract method
# we cannot create object for abstract class
# subclasses implement the abstract methods
# we have to create object for the subclass

# subclass should implement all the abstract methods, else object cannot be created for subclass

# we can also create a constructor in abstract class

class class1(ABC):
    @abstractmethod
    def method1(self, b, c):
        pass

    def normal_method(self, b, c):
        pass


class class2(class1):
    def method1(self, b, c):
        a = b/c
        return a

    def method2(self, b, c):
        a = b*c
        return a


c = class2()
val1 = c.method1(2, 4)
val2 = c.method2(2, 4)

print(val1)
print(val2)