import point
import random
import turtle

N = 100
L = 1
U = 200
points = []

t = turtle.Turtle()
t.speed(75)

####### Functions #######

def findMinPoint(pl):
    '''
    Find the point with the smallest y-value. Ties are resolved by
    smallest x-value

    @param pl The list of points

    @return The point with smallest y-value (and x-value)
    '''
    newPoints = sorted(points, key=lambda x: x.getY())
    min = 0

    for i in range(len(newPoints)):
        if newPoints[i].getY() == newPoints[min].getY() and newPoints[i].getX() < newPoints[min].getX():
            min = i

    return newPoints[min]

def ccw(p1, p2, p3):
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

def createHull(pl, minP):
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
        while len(hull) > 1 and ccw(hull[1], hull[0], i) == 0:
            hull.pop(0)
        
        hull.insert(0, i)
    
    # Second half of hull
    for i in reversed(pl):
        while len(hull) > 1 and ccw(hull[1], hull[0], i) == 0:
            hull.pop(0)
        
        hull.insert(0, i)
    
    return hull

def grahamScan(pl):
    '''
    Find the convex hull of a list of points using a Graham Scan

    @param pl The list of points
    '''
    # Find point with smallest y-value. Ties are resolved by lowest 
    # x-value
    p = findMinPoint(pl)

    # Create the hull
    hull = createHull(pl, p)

    # Draw the points and the hull
    drawPoints(pl)
    drawHull(hull)

def drawPoints(pl):
    '''
    Draw the points in the list. First point is always red

    @param pl The list of points to draw
    '''
    t.penup()

    for i in range(len(pl)):
        t.goto(pl[i].getX(), pl[i].getY())
        t.pendown()
        if i == 0:
            t.color('red')
            t.dot()
        else:
            t.color('black')
            t.dot()
        t.penup()

def drawHull(hl):
    '''
    Draw the edges of the hull

    @param hl The list of points in the hull
    '''
    t.pendown()

    for i in range(len(hl)):
        t.goto(hl[i].getX(), hl[i].getY())
    t.penup()

####### End Functions #######

# Create points
for i in range(N):
    points.append(point.Point(random.randint(L, U), random.randint(L, U)))

if __name__ == '__main__':
    grahamScan(points)

input('wait')