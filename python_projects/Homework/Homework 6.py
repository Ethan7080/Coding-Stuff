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

    
for i in range(11):
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    dig_wait = random.randint(3, 5) #define time for digging
    dig_prob = random.randint(1,100)
    pos = x, y
    if dig_prob <= 10:
        t.goto(pos)
        time.sleep(dig_wait)
        t.write('X',font=('',20),align='center')
        
        
    else:
        t.goto(pos)
        time.sleep(dig_wait)
        t.dot(20)
        


    
