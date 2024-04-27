import turtle
import time
t = turtle.Pen()



t.color("blue")
t.pu()
t.goto(-200,0)
t.shape("turtle")
t.shapesize(0.1)

for i in range(100):
    t.dot(5)
    t.fd(10)
    time.sleep(1)
