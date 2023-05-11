class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft.x < self.x < rectangle.upright.x and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False
        
point1 = Point(6, 7)
# print(point1.falls_in_rectangle((5, 6), (7, 9)))

class Rectangle:
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

point = Point(6, 7)
rectanglex = Rectangle(Point(5, 6), Point(7, 9))

print(point.falls_in_rectangle(rectanglex))