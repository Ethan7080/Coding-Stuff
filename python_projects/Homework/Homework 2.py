import turtle

t = turtle.Pen()
d = 90
f = 50
w = 10
c = "green"
r = 4

t.color(c)
t.width(w)
t.up()
t.left(d+d)
t.forward(f+f+f)
t.right(d+d)
t.down()
for i in range(r):
    t.forward(f)
    t.left(d)
    t.forward(f)
    t.right(d)
    t.forward(f)
    t.right(d)
    t.forward(f)
    t.left(d)
