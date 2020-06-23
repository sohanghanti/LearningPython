#   *args   **kwargs
#   *args stands for arguments
#   **kwargs stands for keyword arguments

#  when we mention *args as an argument to a function,
#  it means that we can pass as many arguments as we want
#  it returns a tuple of the values passed


def myfunc(*args):
    print(sum(args))


myfunc(2, 3, 4, 6, 7, )


#   **kwargs: it stand for keyword arguments, and it will return a dictionary in the key-value pair format


def sample(**kwargs):
    print(kwargs)


sample(fruit='apple', veggie='spinach', flower='rose', )


def is_even(*args):
    for num in range(0, len(args)):
        if (num > 0 and num % 2 == 0):
            print(num)


is_even(2, 3, 4, 5, 6, 7, 8, 9)


def alternateCapital(myString):
    newString = ''
    for pos in range(0, len(myString)):
        if (pos % 2) != 0:
            capLetter = myString[pos].upper()
        else:
            capLetter = myString[pos]

        newString = newString + capLetter
    return newString


newString = alternateCapital('sohansuhasghanti')
print(newString)