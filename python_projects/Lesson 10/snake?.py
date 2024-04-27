import turtle, random
dots = []
size = 0.5
scores = 0
poisons = []
eater = turtle.Pen()
score = turtle.Pen()
score.pu()
score.hideturtle()
score.speed(0)
for i in range(5):
    dot = turtle.Pen()
    dot.shape('circle')
    dot.speed(0)
    dot.pu()
    dot.color('red')
    dot.goto(random.randint(-300,300),random.randint(-300,300))
    dots.append(dot)
eater.speed(0)
eater.pu()
def up():
    eater.setheading(90)
def right():
    eater.setheading(0)
def down():
    eater.setheading(270)
def left():
    eater.setheading(180)
turtle.onkey(up, 'Up')
turtle.onkey(right, 'Right')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.listen()
while True:
    turtle.tracer(False)
    score.undo()
    score.goto(-350,285)
    score.write('Score: ' + str(scores),font=("",50))
    eater.shapesize(size)
    pos = eater.pos()
    if pos[0] == 350 or pos[1] == 350 or pos[0] == -350 or pos[1] == -350:
        eater.goto(0,0)
        eater.write('Game Over!',font=("",100),align='center')
        break
    if size < 0.5:
        eater.goto(0,0)
        eater.write('Game Over!',font=("",100),align='center')
        break
    for i in dots:
        if eater.distance(i) <= size*2+15:      
            i.goto(random.randint(-300,300),random.randint(-300,300))
            size += 0.1
            scores += 1
            if random.randint(1,5) == 1:
                poison = turtle.Pen()
                poison.shape('circle')
                poison.speed(0)
                poison.pu()
                poison.color('black')
                poison.goto(random.randint(-300,300),random.randint(-300,300))
                poisons.append(poison)
    for i in range(len(poisons)):
        if eater.distance(poisons[i]) <= size*2+15:      
            poisons[i].goto(random.randint(-300,300),random.randint(-300,300))
            size -= 0.5
            scores -= 5
            poisons[i].hideturtle()
            poisons.pop(i)
            break
    turtle.tracer(True)
    eater.fd(5)
