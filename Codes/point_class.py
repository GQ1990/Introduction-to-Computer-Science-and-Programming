import math


class cartesianPoint():
    pass


class polarPoint():
    pass


class cPoint():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = math.sqrt(self.x * self.x + self.y * self.y)
        self.angle = math.atan2(self.y, self.x)

    def cartesian(self):
        return (self.x, self.y)

    def polar(self):
        return (self.radius, self.angle)

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def __gt__(self, other):
        return (self.x > other.x) and (self.y > other.y)

    def __add__(self, other):
        return cPoint(self.x + other.x, self.y + other.y)


class pPoint:
    def __init__(self, r, a):
        self.radius = r
        self.angle = a
        self.x = r * math.cos(a)
        self.y = r * math.sin(a)

    def cartesian(self):
        return (self.x, self.y)

    def polar(self):
        return (self.radius, self.angle)

    def __str__(self):
        return '(' + str(self.x) + ',' + str(self.y) + ')'

    def __gt__(self, other):
        return (self.x > other.x) and (self.y > other.y)


class Segment:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def length(self):
        return math.sqrt((self.start.x - self.end.x) * (self.start.x - self.end.x)
                         + (self.start.y - self.end.y) * (self.start.y - self.end.y))


if __name__ == '__main__':
    p1 = cPoint(3., 4.)
    p2 = cPoint(5., 7.)
    s1 = Segment(p1, p2)
    print(s1.length())
