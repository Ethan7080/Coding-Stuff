import random
import turtle
import time
t = turtle.Pen()
t.up()  
t.shape('turtle')
t.shapesize(2)
sc = turtle.Screen()
sc.setup(500, 500)
sc.bgcolor("yellow")
t_tummy = 0
t.speed(20)
for i in range(50):
    weight = random.randint(10, 100)
    x = random.randint(-500, 500)
    y = random.randint(-300, 300)
    t.goto(x, y)
    time.sleep(0.3)
    if weight >= 55:
        t.dot(10, 'red')
        t.write(weight, font=('', 20), align='left')
        t_tummy += weight
    else:
        t.dot(10, 'gray')
        t.write(weight, font=('', 20), align='left')
    if t_tummy >= 1000:
        t.goto(0, 0)
        t.write('I\'m full', font=('', 100), align='center')
        break
t.goto(0, -50)
t.write('I ate ' + str(t_tummy) + ' kg', font=('', 50), align='center')
    
