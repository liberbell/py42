class Point:
    def __init__(self, x, y):
        print("Hi! I am __init__!no")
        self.x = x
        self.y = y

    def point_in_rec(self, lowleft, upright):
        print("I am ordinary")
        if lowleft[0] < self.x < upright[0] and lowleft[1] < self.y < upright[1]:
            return True
        else:
            return False

point1 = Point(3, 5)

print(point1.point_in_rec((1, 3), (8, 9)))