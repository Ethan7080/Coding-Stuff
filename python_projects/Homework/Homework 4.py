import turtle
t = turtle.Pen()
f = turtle.Pen()
t.speed(100)
t.width(3)
t.goto(-300, 0)
for i in range(20):
    t.dot(5)
    t.fd(30)

t.up()
t.goto(-300, 10)
a = -10
for i in range(20):
    t.write(str(a),font=("",10))
    t.fd(30)
    a += 1

t.goto(303, 0)


f.goto(0, -300)
f.lt(90)
f.width(3)
for i in range(20):
    f.dot(5)
    f.fd(30)
f.up()
f.goto(10, -305)
b = -10
for i in range(20):
    f.write(str(b),font=("",10))
    f.fd(30)
    b += 1


f.goto(0, 300)






