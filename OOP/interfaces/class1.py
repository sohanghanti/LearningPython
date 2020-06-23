import zope.interface


class class1(zope.interface.Interface):
    def method1(self):
        pass

    def method2(self):
        pass


@zope.interface.implementer(class1)
class class2():
    def method1(self):
        a = 2*4
        return a



c = class2()
val1 = c.method1()
print(val1)
