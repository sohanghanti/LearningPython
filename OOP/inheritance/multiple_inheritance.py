
class A:
    a = 10


class B:
    a = 20
    b = 30


class C(A, B): # sequence matters
    pass


c = C()
print(c.a)   # 'a' from class A is called
