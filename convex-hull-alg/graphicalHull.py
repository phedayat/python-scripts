import point
import random
import math
import turtle

turtle.colormode(255)

L = 1
U = 450
N = 100
points = []

# add random points to the list
for i in range(N):
    points.append(point.Point(random.randint(L, U), random.randint(L, U)))

def findLeftmostPoint(pointList):
    minIdx = 0
    # pointList = sorted(pointList, key= lambda x: x.getX())
    
    for i in range(len(pointList)):
        # if pointList[i].getX() < pointList[minIdx].getX():
        #     minIdx = i
        if pointList[i].getY() < pointList[minIdx].getY():
            minIdx = i
        elif pointList[i].getY() == pointList[minIdx].getY():
            if pointList[i].getX() < pointList[minIdx].getX():
                minIdx = i
    
    return minIdx

p = findLeftmostPoint(points) # index of our starting point, the leftmost one

# print(point.Point.angleBetween(point.Point(1, 0), point.Point(0, 1)))
# print(point.Point.angleBetween(point.Point.vectorBetween(point.Point(1, 0), point.Point(0, 1)), point.Point(1, 0)))

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

# angularHull = [[i, point.Point.angleBetween(points[i], points[p])] for i in range(len(points))]
# angularHull = sorted(angularHull, key=lambda x: x[1])

def checkEdgeSlopes(p1, p2, p3):
    '''
    Checking to see if p2 belongs in the hull

    @param p1 A point already on the hull. Is the first point of the
    first edge

    @param p2 The point being checked to see if it's in the hull. Is 
    the second point of the first edge, and the first point of the
    second edge

    @param p3 The next point to check. Is the second point of the second edge

    @return {0, 1} 1 if edge slopes create an angle < 180 degrees (or
    pi radians)
    '''
    # sE1 = point.Point.slope(p1, p2)
    # sE2 = point.Point.slope(p2, p3)

    # if (sE1 > 0 and sE2 > 0) or (sE1 < 0 and sE2 < 0):
    #     if sE1 < sE2:
    #         return 1
    #     else:
    #         return 0
    # elif sE1 < 0 and sE2 > 0:
    #     return 1
    # else:
    #     return 0
    
    z = (p2.getX() - p1.getX())*(p3.getY() - p1.getY()) - (p2.getY() - p1.getY())*(p3.getX() - p1.getX())

    if z > 0 or z == 0:
        return 1
    else:
        return 0

# hull = sorted(points, key=lambda x: point.Point.angleBetween(x, points[p]))

hull = points.copy()
del hull[p]

# hull = sorted(hull, key=lambda x: point.Point.slope(points[p], x))
# hull = sorted(hull, key=lambda x: point.Point.distance(points[p], x))
hull = sorted(hull, key=lambda x: point.Point.angleBetween(points[p], x))

# t = turtle.Turtle()
# t.penup()
# t.speed(25)

# for i in range(len(hull) + 1):
#     if i == 0:
#         t.goto(points[p].getX(), points[p].getY())
#         t.pendown()
#         t.color('red')
#         t.dot()
#     else:
#         t.goto(hull[i-1].getX(), hull[i-1].getY())
#         t.pendown()
#         t.color('black')
#         t.dot()
    
#     t.penup()

# t.goto(points[p].getX(), points[p].getY())
# for i in range(len(hull) - 2):
#     t.pendown()
#     if i == 0:
#         print(f"p: {points[p].getValue()}")
#         print(f"i: {hull[i].getValue()}")
#         print(f"i+1: {hull[i+1].getValue()}")
#         if checkEdgeSlopes(points[p], hull[i], hull[i+1]) == 1:
#             t.goto(hull[i].getX(), hull[i].getY())
#         else:
#             t.goto(hull[i+1].getX(), hull[i+1].getY())
#     else:
#         print(f"i: {hull[i].getValue()}")
#         print(f"i+1: {hull[i+1].getValue()}")
#         print(f"i+2: {hull[i+2].getValue()}")
#         if checkEdgeSlopes(hull[i], hull[i+1], hull[i+2]) == 1:
#             t.goto(hull[i+1].getX(), hull[i+1].getY())
#         else:
#             t.goto(hull[i+2].getX(), hull[i+2].getY())


# print("Angle between e1 and e2: ", point.Point.edgeAngleBetween(hull[0], hull[1], hull[2]))

cHull = []
cHull.append(points[p])

lastAdded = 1
for i in range(len(hull) - 2):
    if i == 0:
        if checkEdgeSlopes(points[p], hull[i], hull[i+1]) == 1:
            cHull.append(hull[i])
    else:
        if checkEdgeSlopes(hull[i], hull[i+1], hull[i+2]) == 1:
            cHull.append(hull[i+1])
            # lastAdded += 1
        else:
            # del cHull[lastAdded:i+2]
            cHull.append(hull[i+2])

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
        t.color('red')
        t.dot()
    else:
        t.color(0, 50 + 2 * i, 0)
        t.dot()
    t.color('black')

    t.penup()

t.pendown()
for i in cHull:
    t.goto(i.getX(), i.getY())

t.goto(cHull[0].getX(), cHull[0].getY())
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