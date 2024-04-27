import turtle
import time
t = turtle.Pen()
f = turtle.Pen()
t.hideturtle()
t.speed(0)

while True:
    t.fd(100)
    t.goto(0,0)
    time.sleep(1)
    t.undo()
    t.undo()
    t.rt(6)
    f.fd(100)
    f.goto(0,0)
    time.sleep(60)
    f.undo()
    f.undo()
    f.rt(6)
    
