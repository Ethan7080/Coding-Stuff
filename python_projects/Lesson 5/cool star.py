import turtle
t = turtle.Pen()
t.speed(0)
l = 144
n = 1
colors = ["gold", "lightblue", "green", "red", "purple"]
for i in range(200):
    t.color(colors[i%5])
    t.fd(i*2)
    t.lt(l)
    n += 1
    
