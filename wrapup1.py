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