import turtle
t = turtle.Pen()
t.speed(0)
colors = ["red","green","blue"]
for i in range(10):
    t.color(colors[i%3])
    for j in range(4):
        t.fd(25)
        t.lt(90)
    t.fd(25)
    
