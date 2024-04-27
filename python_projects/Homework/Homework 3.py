import turtle
import time
t = turtle.Pen()
t.hideturtle()
t.color('green')
a = 5
b = 20
for i in range(5):
    t.write(str(a),font=("",str(b)),align="center")
    a -= 1
    b += 30
    time.sleep(1)
    t.undo()

for i in range(100):
    t.write("BOOM",font=("",str(b)),align="center")
    b += 25
    t.undo()
    time.sleep(1)
    
