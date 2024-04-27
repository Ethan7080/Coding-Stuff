import turtle
t = turtle.Pen()
t.speed(0)
f = 10
l = 90
n = 1
while True:
    if n % 4 == 2:
        t.color('gold')
    t.fd(f)
    t.lt(l)
    f += 5
    n += 1
    t.color('black')
    
