import turtle
t = turtle.Pen()
def petal():
    t.width(2)
    t.color('yellow', 'red')
    t.begin_fill()
    t.circle(150, 50)
    t.lt(130)
    t.circle(150, 50)
    t.end_fill()
for i in range(5):
    t.lt(60)
    petal()
