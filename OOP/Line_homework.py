class Line:

    def __init__(self, coordinate1, coordinate2):
        self.coordinate1 = coordinate1
        self.coordinate2 = coordinate2

    def distance(self):
        x1, y1 = self.coordinate1
        x2, y2 = self.coordinate1
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


myLine = Line((1, 2), (3, 4))
print(myLine.distance())
