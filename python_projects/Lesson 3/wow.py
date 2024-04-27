import turtle
import random
t = turtle.Pen()
t.speed(100)
while True:
    a = random.randint(0,100)
    b = random.randint(0,10)
    t.color(random.randint(0,255),random.randint(0.255),random.randint(0,255))
    t.width(b)
    t.fd(a)
    t.lt(90)
    
