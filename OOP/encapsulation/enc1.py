
class myClass:
    __a = 10

    def __disp1(self):
        print("display 1")

    def disp2(self):
        self.__disp1()
        print(self.__a)
        print("display 2")


mc = myClass()

print(mc.disp2())
# error is shown, as '__a' is private variable, cannot be accessed outside the class

