# variable and method overriding

# two or more methods with same name but doing the things differently
# it means one of the methods overrides other
# if there is a method in superclass and method with the same name in a subclass,
# then by executing the method, the method of corresponding class is executed


class bank:
    a = 10

    def ROI(self):
        return 9.5


class SBI(bank):
    a = 20

    def ROI(self):
        return 8.5


s = SBI()
print(s.ROI())
print(s.a)