import turtle
import random
t = turtle.Pen()
turtle.colormode(255)
def click(x, y):
    t.color(random.randint(0,255),random.randint(0,255),random.randint(0,255))
    t.goto(x,y)
    t.dot(random.randint(0,50))
turtle.onscreenclick(click,1)
