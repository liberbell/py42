
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

point1 = Point(10, 20)
print(type(point1))

number1 = int("2")
print(type(number1))

class House:
    def __init__(self, wall_area):
        self.wall_area = wall_area