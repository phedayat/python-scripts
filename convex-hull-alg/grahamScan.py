import point
import math
import random
import turtle
from functools import reduce

N = 100
L = 1
U = 200
points = []

t = turtle.Turtle()
t.speed(75)

def ccw(p1, p2, p3):
    z = (p2.getX() - p1.getX())*(p3.getY() - p1.getY()) - (p2.getY() - p1.getY())*(p3.getX() - p1.getX())

    if z > 0:
        return 1
    else:
        return 0

def drawPoints(pl):
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
    t.pendown()

    for i in range(len(hl)):
        t.goto(hl[i].getX(), hl[i].getY())
    t.penup()

# Create points
for i in range(N):
    points.append(point.Point(random.randint(L, U), random.randint(L, U)))

def grahamScanParsia():
    global points
    newPoints = sorted(points, key=lambda x: x.getY())

    min = 0
    for i in range(len(newPoints)):
        if newPoints[i].getX() < newPoints[min].getX() and newPoints[i].getY() == newPoints[min].getY():
            min = i

    p = newPoints[min]

    hull = [p]

    points = sorted(points, key=lambda x: point.Point.angleBetween(x, p))
    

    for i in points:
        while len(hull) > 1 and ccw(hull[1], hull[0], i) == 0:
            hull.pop(0)
        
        hull.insert(0, i)

    # for i in hull:
    #     print(i.getValue())

    points = sorted(points, key=lambda x: point.Point.angleBetween(x, p), )
    for i in reversed(points):
        while len(hull) > 1 and ccw(hull[1], hull[0], i) == 0:
            hull.pop(0)
        
        hull.insert(0, i)

    drawPoints(points)
    drawHull(hull)

#####################################################

def turn(p1, p2, p3):
    z = (p2.getX() - p1.getX())*(p3.getY() - p1.getY()) - (p3.getX() - p1.getX())*(p2.getY() - p1.getY())
    return cmp(z, 0)

def _keep_left(pl, r):
    while len(pl) > 1 and turn(pl[-2], pl[-1], r) <= 0:
        pl.pop()
    if not len(pl) or pl[-1] != r:
        pl.append(r)
    
    return pl

def grahamScanTix(pl):
    l = reduce(_keep_left, pl, [])
    u = reduce(_keep_left, reversed(pl), [])
    return l.extend(u[i] for i in range(1, len(u) - 1)) or l

if __name__=='__main__':
    grahamScanParsia()

input('wait')