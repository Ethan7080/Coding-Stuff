import turtle
import time
from shapes import *
turtles = []
shape = turtle.getshapes()
turtle.colormode(255)
print(len(shape))
print(turtle.getshapes())
for i in range(len(shape)):
    t = turtle.Pen()
    t.shape(shape[i])
    t.pu()
    t.color(25*i%255, 255 - 25*i%255,255%255)
    t.shapesize(1)
    t.speed(0)
    t.goto(0,-200)
    t.circle(200,360/10 // (i + 1))
    turtles.append(t)
while True:
    turtle.tracer(False)
    for i in turtles:
        i.circle(200,1)
    turtle.tracer(True)

