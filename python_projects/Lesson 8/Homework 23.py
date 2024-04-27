import turtle
from shapes import *
t = turtle.Pen()
a = 150
t.shape('pixal1.gif')
t.pd()
def star(size):
    for i in range(5):
        t.forward(size)
        t.left(144)
for i in range(12):
    t.pu()
    t.color('yellow')
    t.speed(0)
    t.goto(0,-200)
    t.circle(200,360/10 * i)
    t.begin_fill()
    star((a - (a // (i + 1))))
    t.end_fill()
    a -= 10
