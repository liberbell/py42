# class Point:

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

point1 = Point(7, 8)
print(point1.x, point1.y)

print("john".count("j"))
print("john".capitalize())

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, lowleft, upright):
        if lowleft[0] < self.x < upright[0] 