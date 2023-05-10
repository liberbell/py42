class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, lowleft, upright):
        if lowleft[0] < self.x < upright[0] and lowleft[1] < self.y < upright[1]:
            return True
        else:
            return False
        
point1 = Point(6, 7)
print(point1.falls_in_rectangle((5, 6), (7, 9)))

class Rectangle:
    def __init__(self, rectangle):
        self.rectangle.lowleft = lowleft
        self.rectangle.upright = upright

point = Point(6, 7)
rectanglex = Rectangle(Point(5, 6), Point(7, 9))

print(point.falls_in_rectangle(rectanglex))