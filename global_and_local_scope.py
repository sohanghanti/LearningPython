spam = 12  # global variable


def eggs():
    spam = 42  # local variable
    print(spam)


eggs()  # local variable is printed  42
print(spam)  # global variable printed  12

print("####################################################")


def box():
    spam = 32
    eggs()
    print(spam)


eggs()  # local variable from eggs() printed
box()  # local variable from box() not printed, because there is a call to eggs() function, local variable from
# eggs() printed first and local variable 'spam' printed after that
print(spam)  # global variable printed
print("####################################################")


#  change value of global variable inside the function


def square():
    global spam
    spam = 15
    print(spam)


def rectangle():
    spam = 19
    square()
    print(spam)


rectangle()
print(spam)

print("##################")


def add():
    spam = 22

    def change():
        global spam
        spam = 23
    print("Before making changing: ", spam)
    print("Making change")
    change()
    print("After making change: ", spam)


add()
print("value of spam", spam)
