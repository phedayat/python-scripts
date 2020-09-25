import math

class Point:
    def __init__(self, xVal = 0, yVal = 0):
        self.x = xVal
        self.y = yVal
        self.value = {xVal, yVal}
        self.length = math.sqrt(self.x**2 + self.y**2)

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y
    
    def getValue(self):
        return self.value
    
    def getLength(self):
        return self.length

    @staticmethod
    def dot(p1, p2):
        return (p1.getX() * p2.getX()) + (p1.getY() * p2.getY())

    @staticmethod
    def angleBetween(p1, p2):
        return math.acos(Point.dot(p1, p2) / float(p1.getLength() * p2.getLength()))

    @staticmethod
    def vectorBetween(p1, p2):
        return Point(p1.getX() - p2.getX(), p1.getY() - p2.getY())

    @staticmethod
    def distance(p1, p2):
        return math.sqrt((p2.getX() - p1.getX())**2 + (p2.getY() - p1.getY())**2)

    @staticmethod
    def edgeAngleBetween(p1, p2, p3):
        a = Point.distance(p1, p2)
        b = Point.distance(p2, p3)
        c = Point.distance(p1, p3)

        # a = Point.vectorBetween(p1, p2).getLength()
        # b = Point.vectorBetween(p2, p3).getLength()
        # c = Point.vectorBetween(p1, p3).getLength()

        return math.acos((b**2-a**2-c**2) / (-2 * a * c))