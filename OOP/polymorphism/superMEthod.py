class father:
    def __init__(self):
        print("father constructor")

    def show(self):
        print("Father class method")


class son(father):
    def __init__(self):
        super().__init__()
        print("son class constructor")

    def display(self):
        print("Son class method")


s = son()
s.show()