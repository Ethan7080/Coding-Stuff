import turtle
from shapes import *
t = turtle.Pen()
t.speed(0)
size = 50
t.shape('ironman.gif')
##for i in range(5):
##    for j in range(4):
##        t.fd(25)
##        t.lt(90)
##    t.fd(25)
##    for k in range(3):
##        t.fd(25)
##        t.lt(120)
##    t.fd(25)t
for k in range(5):
    for i in [4, 3 ,6, 4]:
        for j in range(i):
            t.fd(size)
            t.lt(360/i)
        t.fd(size)
        
 
