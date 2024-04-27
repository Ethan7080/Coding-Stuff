import turtle
import random
t = turtle.Pen()
turtle.bgcolor("black")
##def draw_square(size,x,y,color,thick,pen,fill):
##    pen.pu()
##    pen.goto(x,y)
##    pen.pd()
##    pen.width(thick)
##    pen.color(color)
##    if fill:
##        pen.begin_fill()
##    for i in range(4):
##        pen.fd(size)
##        pen.lt(90)
##    if fill:
##        pen.begin_fill()
def draw_star(size,x,y,color,thick,pen,fill):
    pen.pu()
    pen.goto(x,y)
    pen.pd()
    pen.width(thick)
    t.color(color)
    pen.begin_fill()
    for i in range(5):
        pen.fd(size)
        pen.lt(144)
        pen.fd(size)
        pen.rt(72)
    pen.end_fill()
turtle.tracer(False)
for i in range(100000):
    draw_star(random.randint(10,25),random.randint(-300,300),random.randint(-300,300),"yellow",2,t,True)
turtle.tracer(True)
