
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

point1 = Point(10, 20)
point2 = Point(11, 21)
point3 = Point(12, 22)
point4 = Point(13, 23)

number1 = int("2")

print(type(point1))
print(type(number1))

from Geometry import Point
point5 = Point(100, 200)
print(type(point5))

import ipaddress
myip = ipaddress.IPv4Address("1.1.1.1")
print(myip)
print(type(myip))