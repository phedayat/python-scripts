import point
import random
import math
import turtle

turtle.colormode(255)

L = 1
U = 300
N = 100
points = []

# add random points to the list
for i in range(N):
    points.append(point.Point(random.randint(L, U), random.randint(L, U)))

def findLeftmostPoint(pointList):
    minIdx = 0
    # pointList = sorted(pointList, key= lambda x: x.getX())
    
    for i in range(len(pointList)):
        if pointList[i].getX() < pointList[minIdx].getX():
            minIdx = i
    
    return minIdx

p = findLeftmostPoint(points) # index of our starting point, the leftmost one

print(point.Point.angleBetween(point.Point(1, 0), point.Point(0, 1)))
print(point.Point.angleBetween(point.Point.vectorBetween(point.Point(1, 0), point.Point(0, 1)), point.Point(1, 0)))

# print(point.Point.angleBetween(points[p], points[p+1]))

'''
Determine hull points
'''

# r = p
# q = 0
# l = 0
# hullIdx = []

# while True:
#     hullIdx.append(r)

#     q = (r+1) % N
#     l = (r+2) % N

#     if point.Point.angleBetween(point.Point.vectorBetween(points[r], points[q]), point.Point.vectorBetween(points[q], points[l])) < math.pi:
#         r = q
    
#     if r == p:
#         break

hull = sorted(points, key=lambda x: point.Point.angleBetween(x, points[p]))

print(hull)

print("Angle between e1 and e2: ", point.Point.edgeAngleBetween(hull[0], hull[1], hull[2]))
cHull = []
cHull.append(hull[0])

for i in range(len(hull) - 2):
    if point.Point.edgeAngleBetween(hull[i], hull[i+1], hull[i+2]) < math.pi - 1:
        print("EDGE ANGLE BETWEEN: ", point.Point.edgeAngleBetween(hull[i], hull[i+1], hull[i+2]))
        cHull.append(hull[i+1])

print("Dist: ", point.Point.distance(point.Point(1, 0), point.Point(0, 1)))

'''
Draw points and hull
'''

t = turtle.Turtle()
t.penup()
t.speed(25)

# t.pendown()
# c = 0
# for i in cHull:
#     if c < 3:
#         t.color('green')
#         c += 1

#     t.goto(i.getX(), i.getY())

#     if i.getX() == points[p].getX() and i.getY() == points[p].getY():
#         t.color(255, 0, 0)
#         t.dot()
#     else:
#         t.color('black')
#         t.dot()

for i in range(len(hull)):
    t.goto(hull[i].getX(), hull[i].getY())
    t.pendown()
    
    if i == 0:
        t.color(255, 0, 0)
        t.dot()
    else:
        t.color('black')
        t.dot()

    t.penup()

t.pendown()
for i in cHull:
    t.goto(i.getX(), i.getY())

t.goto(hull[0].getX(), hull[0].getY())
t.penup()
# for i in hullIdx:
#     t.goto(points[i].getX(), points[i].getY())
#     t.pendown()

#     if i == p:
#         t.color(255, 0, 0)
#         t.dot()
#     else:
#         t.color('black')
#         t.dot()
    
#     t.penup()

# t.goto(points[p].getX(), points[p].getY())
# hull = [points[i] for i in hullIdx]

# for pnt in hull:
#     t.pencolor(random.randint(1, 250), random.randint(1, 250), random.randint(1, 250))
#     t.pendown()
#     t.goto(pnt.getX(), pnt.getY())
#     t.penup() 

input('Wait')