class Point:
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        print(self)

point1 = Point(3, 4)
point2 = Point(6, 7)

print(point1.x)

class Point2:
    
    def __init__(this_object, x, y):
        this_object.x = x
        this_object.y = y

point3 = Point2(3, 4)

print(point3.x)

class Person:

    def __init__(self, n, a):
        self.name = n
        self.age = a

person1 = Person("John", 30)
print(person1.name)