class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if rectangle.lowleft < self.x < rectangle.upright.x \
        and rectangle.lowleft.y < self.y < rectangle.upright.y:
            return True
        else:
            return False
        
class Rectangle:

    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright

from random import randint
randint(0, 9)

rectangle = Rectangle(
    Point(randint(0, 9), randint(0, 9)), Point(randint(10, 19), randint(10, 19))
)

print("Rectangle cordinates: ",
      rectangle.lowleft.x, " ",
      rectangle.lowleft.y, "and",
      rectangle.upright.x, " ",
      rectangle.upright.y)