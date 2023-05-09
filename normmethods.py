class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def point_in_rec(self, lowleft, upright):
        print("I am ordinary")
        if lowleft[0] < self.x < upright[0] and lowleft[1] < self.y < upright[1]:
            return True
        else:
            return False