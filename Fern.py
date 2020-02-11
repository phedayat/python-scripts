import numpy as np
import turtle
import random

f = turtle.Turtle()
turtle.colormode(255)
f.speed(1000)
f.color('green')
f.penup()

x = 0
y = 0

for i in range(100000):
    f.goto(85*x, 57*y-257)
    f.pendown()
    f.dot()
    f.penup()
    xn = x
    yn = y
    r = random.random() * 100
    if r < 3:
        x = 0
        y = .16 * yn
    elif r < 85:
        x = .85*xn + .04*yn
        y = -.04*xn + .85*yn+1.6
    elif r < 92:
        x = .2*xn - .26*yn
        y = .23*xn + .22*yn + 1.6
    else:
        x = -.15*xn + .28*yn
        y = .26*xn + .24*yn + .44

input("EXIT")
