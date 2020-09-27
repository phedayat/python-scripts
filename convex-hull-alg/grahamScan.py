import point
import random
import turtle

class GrahamScan:
    def __init__(self, numPoints = 100, lower = 1, upper = 300, pl = [], tu = turtle.Turtle()):
        '''
        Constructor for a GrahamScan object

        @param numPoints The number of points in the pointset. Only used to create a list of
            random points if no list is passed in
        @param lower The lower bound of any random point created for the list
        @param upper The upper bound of any random point created for the list
        @param pl The list of points to find the convex hull of
        @param tu A turtle object for drawing
        '''
        self.N = numPoints
        self.L = lower
        self.U = upper
        self.points = pl
        self.t = tu

        self.t.speed(75)

        if self.points == []:
            self.createPointSet()

    def createPointSet(self):
        for i in range(self.N):
            self.points.append(point.Point(random.randint(self.L, self.U), random.randint(self.L, self.U)))

    def findMinPoint(self, pl):
        '''
        Find the point with the smallest y-value. Ties are resolved by
        smallest x-value

        @param pl The list of points

        @return The point with smallest y-value (and x-value)
        '''
        newPoints = sorted(self.points, key=lambda x: x.getY())
        min = 0

        for i in range(len(newPoints)):
            if newPoints[i].getY() == newPoints[min].getY() and newPoints[i].getX() < newPoints[min].getX():
                min = i

        return newPoints[min]

    def ccw(self, p1, p2, p3):
        '''
        Determine if the points passed in constitute a counterclockwise turn

        @param p1 The first point. The first point of the first edge
        @param p1 The second point. The second point of the first edge
            and first point of the second edge
        @param p1 The third point. The second point of the second edge

        @return 1 if CCW, otherwise 0
        '''
        z = (p2.getX() - p1.getX())*(p3.getY() - p1.getY()) - (p2.getY() - p1.getY())*(p3.getX() - p1.getX())

        if z > 0:
            return 1
        else:
            return 0

    def createHull(self, pl, minP):
        '''
        Create the list of points that make up the hull

        @param pl The list of all points
        @param minP The point with the smallest y-value (and x-value)

        @return A list of points that make up the hull
        '''
        hull = [minP]

        pl = sorted(pl, key=lambda x: point.Point.angleBetween(x, minP))

        # First half of hull
        for i in pl:
            while len(hull) > 1 and self.ccw(hull[1], hull[0], i) == 0:
                hull.pop(0)
            
            hull.insert(0, i)
        
        # Second half of hull
        for i in reversed(pl):
            while len(hull) > 1 and self.ccw(hull[1], hull[0], i) == 0:
                hull.pop(0)
            
            hull.insert(0, i)
        
        return hull

    def grahamScan(self):
        '''
        Find the convex hull of a list of points using a Graham Scan

        @param pl The list of points
        '''
        # Find point with smallest y-value. Ties are resolved by lowest 
        # x-value
        p = self.findMinPoint(self.points)

        # Create the hull
        hull = self.createHull(self.points, p)

        # Draw the points and the hull
        self.drawPoints(self.points)
        self.drawHull(hull)

    def drawPoints(self, pl):
        '''
        Draw the points in the list. First point is always red

        @param pl The list of points to draw
        '''
        self.t.penup()

        for i in range(len(pl)):
            self.t.goto(pl[i].getX(), pl[i].getY())
            self.t.pendown()
            if i == 0:
                self.t.color('red')
                self.t.dot()
            else:
                self.t.color('black')
                self.t.dot()
            self.t.penup()

    def drawHull(self, hl):
        '''
        Draw the edges of the hull

        @param hl The list of points in the hull
        '''
        self.t.pendown()

        for i in range(len(hl)):
            self.t.goto(hl[i].getX(), hl[i].getY())

        self.t.penup()

if __name__ == '__main__':
    g = GrahamScan()
    g.grahamScan()

input('wait')