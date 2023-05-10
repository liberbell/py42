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
        
    def distance_from_point(self, point):
        return ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
    
point1 = Point(1, 1)
point2 = Point(2, 2)
# print(point1.distance_from_point(3, 3))
print(point1.distance_from_point(point2))