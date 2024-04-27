import turtle,time
from shapes import *
t = turtle.Pen()
colors = ['red','orange','yellow','green','skyblue','darkblue','purple']
size = 30
n = 10
count = 0
t.speed(0)
t.shape('logo31.gif')
while True:
    turtle.tracer(False)
    t.clear()
    for i in range(n):
        t.pu()
        t.goto(-size * 4, size * (4  - i))
        t.pd()
        for j in range(n):
            t.color(colors[(j+i+count)%7])
            t.begin_fill()
            for k in range(4):
                t.fd(size)
                t.lt(90)
            t.end_fill()
            t.fd(size)
            t.color(colors[(j+i)%7])
    turtle.tracer(True)
    time.sleep(0.05)
    count += 1
