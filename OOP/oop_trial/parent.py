class GrandFather:

    def __init__(self):
        pass

    def method1(self):
        print("method1 from ParentClass")

    def method2(self):
        print("method2 from ParentClass")


class Father1(GrandFather):

    def __init__(self):
        super().__init__()

    def method3(self):
        print('Method3 from Father 1')


class Mother1(GrandFather):

    def __init__(self):
        super().__init__()

    def method4(self):
        print('Method4 from Mother 1')


class Child1(Father1, Mother1):
    def __init__(self):
        Mother1.__init__(self)

    def method5(self):
        print('Method 5 from Child1')


g = GrandFather()
f = Father1()
m = Mother1()
c = Child1()





