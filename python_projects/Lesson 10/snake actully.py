import turtle, random
dots = []
scores = 0
snake = turtle.Pen()
bodies = []
pos = []
score = turtle.Pen()
score.pu()
score.hideturtle()
score.speed(0)
turtle.tracer(False)
for i in range(5):
    dot = turtle.Pen()
    dot.shape('circle')
    dot.speed(0)
    dot.pu()
    dot.color('red')
    dot.goto(random.randint(-300,300),random.randint(-300,300))
    dots.append(dot)
snake.shape('circle')
snake.color('darkgreen')
snake.speed(0)
snake.pu()
def up():
    snake.setheading(90)
def right():
    snake.setheading(0)
def down():
    snake.setheading(270)
def left():
    snake.setheading(180)
turtle.onkey(up, 'Up')
turtle.onkey(right, 'Right')
turtle.onkey(down, 'Down')
turtle.onkey(left, 'Left')
turtle.listen()
turtle.tracer(True)
while True:
    pos.insert(0, snake.pos())
    turtle.tracer(False)
    score.undo()
    score.goto(-350,285)
    score.write('Score: ' + str(scores),font=("",50))
    for i in range(len(bodies)):
        bodies[i].goto(pos[i])
    if snake.pos()[0] == 350 or snake.pos()[1] == 350 or snake.pos()[0] == -350 or snake.pos()[1] == -350:
        snake.goto(0,0)
        snake.write('Game Over!',font=("",100),align='center')
        break
    for i in dots:
        if snake.distance(i) <= 15:      
            i.goto(random.randint(-300,300),random.randint(-300,300))
            body = turtle.Pen()
            body.pu()
            body.shape('circle')
            body.color('darkgreen')
            bodies.append(body)
            scores += 1
    turtle.tracer(True)
    snake.fd(1)
