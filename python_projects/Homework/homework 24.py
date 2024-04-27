import turtle
t = turtle.Pen()
colors = ['red','orange','yellow','green','skyblue','darkblue','purple']
size = 30
n = 10
t.speed(0)
turtle.tracer(False)
for i in range(n):
    t.pu()
    t.goto(-size * 4, size * (4  - i))
    t.pd()
    for j in range(n):
        t.color(colors[(j+i)%7])
        t.begin_fill()
        for k in range(4):
            t.fd(size)
            t.lt(90)
        t.end_fill()
        t.fd(size)
        t.color(colors[(j+i)%7])
turtle.tracer(True)
        
