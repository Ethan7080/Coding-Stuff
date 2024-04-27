import turtle
import time
turtles = []
a = int(input())
turtle.tracer(False)
for i in range(1000000000000):
    t = turtle.Pen()
    t.speed(0)
    turtles.append(t)
    t.lt(360/a*i)
all_shapes = ("turtle","arrow","square","triangle","classic","circle")
for i in range(10):
    for x in all_shapes:
        turtle.tracer(False)
        for o in turtles:
            o.shape(x)
            o.shapesize(i+1)
            o.fd(10)

