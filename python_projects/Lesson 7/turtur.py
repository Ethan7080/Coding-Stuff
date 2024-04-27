import turtle
t = turtle.Pen()
t.speed(0)
y = 0
x = 0
a = int(input())
b = int(input())
for k in range(a):
    for i in range(b):
        for j in range(4):
            t.fd(25)
            t.lt(90)
        t.fd(25)
    t.pu()
    y -= 25
    t.goto(x, y)
    t.pd()
t.hideturtle()
