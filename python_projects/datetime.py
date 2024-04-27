import turtle, datetime
timepen = turtle.Pen()
datepen = turtle.Pen()
datepen.pu()
timepen.pu
datepen.hideturtle()
timepen.hideturtle()
datepen.goto(0,-100)
while True:
    turtle.tracer(False)
    datepen.clear()
    timepen.clear()
    date = datetime.datetime.now().strftime("%Y-%m-%d")
    datepen.write(date,font=("",90),align="center")
    time = datetime.datetime.now().strftime("%H:%M:%S")
    timepen.write(time,font=("",100),align="center")
    turtle.tracer(True)
    
    
