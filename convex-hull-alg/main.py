import point
import random
import turtle

N = 10 # number of points
L = 1 # lower limit
U = 400 # upper limit

points = []
hull = []

for i in range(N):
    # points.append(point.Point(random.randint(L, U), random.randint(L, U)).getValue()[0])
    points.append(point.Point(random.randint(L, U), random.randint(L, U)))

for indPoint in points:
    print("OGX: ", indPoint.getX())
    print("OGV: ", indPoint.getValue())

def returnMinPointIdx(pointList):
    minXIdx = 0
    minX = pointList[0].getX()

    for i in range(len(pointList)):
        if pointList[i].getX() < minX:
            minX = pointList[i].getX()
            minXIdx = i
    
    return [minXIdx, minX]

def returnPointX(pointX):
    '''
    Returns the x-coordinate of the point passed in. Used for getting
    leftmost point
    '''
    return pointX.getX()

# p = min(points, key = returnPointX) # get point with minimum x, i.e. leftmost point
p = returnMinPointIdx(points)

print("Min X: ", p)

def orientation(p1, p2, p3):
    val = (p2.getY() - p1.getY())*(p3.getX() - p2.getX()) - (p2.getX() - p1.getX())*(p3.getY() - p2.getY())

    if val > 0:
        return 1 # clockwise
    elif val < 0:
        return 2 # counterclockwise
    else:
        return 0 # collinear

print("Orientation test: ", orientation(points[0], points[1], points[2]))

def convexHull():
    hull = []
    r = 1
    q = 0
    while True:
        hull.append(r);

        q = (r+1) % N

        for i in range(N):
            if orientation(points[r], points[i], points[q]) == 2:
                q = i
        
        r = q

        if r == 1:
            return hull

results = convexHull()
print(results)

for i in results:
    print("Point of hull: ", points[i].getValue())

results = convexHull()
t = turtle.Turtle()
t.penup()
t.speed(25)

for i in points:
    t.goto(i.getX(), i.getY())
    t.pendown()
    t.dot()
    t.penup()

t.pendown()
for i in results:
    t.goto(points[i].getX(), points[i].getY())

t.goto(points[p[0]].getX(), points[p[0]].getY())
input('Wait')