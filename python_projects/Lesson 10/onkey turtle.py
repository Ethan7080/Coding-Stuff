import turtle
import random
t = turtle.Pen()
turtle.colormode(255)
t.speed(0)
def up():
    t.setheading(90)
def right():
    t.setheading(0)
def down():
    t.setheading(270)
def left():
    t.setheading(180)

turtle.onkey(up, 'Up')
turtle.onkey(right, 'Right')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.listen()
while True:
    t.fd(5)
