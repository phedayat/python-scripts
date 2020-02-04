import turtle
import random
turtle.colormode(255)
print(turtle.screensize())

n = input("Enter the number of points: ")
n = int(n)

t = turtle.Turtle()
t.speed(75)
t.penup()

for i in range(13):
  r = random.randint(0, 255)
  g = random.randint(0, 255)
  b = random.randint(0, 255)
  t.color(r, g, b)

  x = 100 # random.randint(-200, 200)
  y = 100 # random.randint(-200, 200)
  t.goto(x + 2 * -i, y + 2 * -i)
  t.pendown()

  sidelength = 100
  angle = 180 - (((n-2)*180) / n)

  '''
  Do angle = 289 and angle /= 2 when % 4
  '''
  for j in range(2 * n):
    t.forward(sidelength)

    if j % 2 == 0:
        t.left(angle)
    else:
        t.right(2 * angle)
  
  t.penup()

input("wait")