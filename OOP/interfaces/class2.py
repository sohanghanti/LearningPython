from Interface import Implements
# python does not deliberately supports interface,
# as it is already supporting multiple inheritance
# though it has a package 'interface' from which we can achieve the implementation
# in an interface, all the defined methods are abstract
# the subclass implementing inheritance has to implement these abstract classes


class myInterface(Interface):
    def m1(self):
        pass

    def m2(self):
        pass

    def m3(self):
        print("m3")


class myClass(Implements):
    def m1(self):
        print("m1")

    def m2(self):
        print("m2")

    def m3(self):
        print("overridden m3")


m =myClass()
m.m1()
m.m2()
m.m3()




