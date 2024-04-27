import turtle
t = turtle.Pen()
d = 90
f = 10
t.speed(0)
t.dot(10)
for i in range(2000):
    t.fd(f)
    t.lt(d)
    f += 5
    d += 0.01
