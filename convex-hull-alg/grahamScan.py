import point
import math
import random
import turtle

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

for i in hull:
    print(i.getValue())

drawPoints(points)
drawHull(hull)
# angularList = sorted(points, key=lambda x: x)

input('wait')