from turtle import *

speed(-10000000)
width(3)

# how to draw a centered circle
def circle(radius):
    penup()
    forward(radius)
    pendown()
    left(90)
    for i in range(60):
        forward(3.14*radius/30)
        left(6)
    right(90)
    penup()
    back(radius)
    
# how to draw an eye
def eye():
    color('black', 'white')
    begin_fill()
    circle(80)
    end_fill()
    forward(25)
    # pupil
    color('black', 'black')
    begin_fill()
    circle(40)
    end_fill()
    back(25)

def right_arc(radius, angle):
    for i in range(angle):
        forward(2*3.14*radius/360)
        right(1)

def centered_arc(radius, angle):
    penup()
    left(angle/2)
    forward(radius)
    right(90)
    pendown()
    right_arc(radius, angle)
    penup()
    left(90)
    back(radius)
    left(angle/2)

def rotate_left():
  left(90)
    
def rotate_right():
  right(90)





def draw():
  # drawing the head
  color('black', 'yellow')
  begin_fill()
  circle(300)
  end_fill()

  # drawing the left eye
  rotate_left()
  forward(150)
  rotate_left()
  forward(100)
  right(270)
  eye()

  # drawing the right eye
  rotate_left()
  forward(200)
  rotate_right()
  eye()

  # move back into the middle
  right(90)
  forward(100)
  left(90)

  # drawing the mouth
  width(15)
  forward(200)
  left(180)
  color('red')
  centered_arc(-150, 180)

  #drawing the glasses
  width(5)
  color('black')
  forward(200)
  right(90)
  forward(105)
  circle(100)
  left(180)
  forward(205)
  circle(100)
  forward(100)
  pendown()
  forward(65)
  penup()
  left(180)
  forward(270)
  pendown()
  forward(1)
  penup()
  forward(199)
  pendown()
  forward(60)
  penup()

  #drawing eyebrow
  left(90)
  forward(150)
  left(90)
  forward(260)
  left(90)
  forward(100)
  left(90)
  forward(100)
  right(90)
  forward(30)
  left(180)
  centered_arc(100, 100)
  left(90)
  forward(200)
  right(90)
  centered_arc(100, 100)

  #drawing hair
  right(90)
  forward(100)
  right(90)
  forward(160)
  left(180)

  for i in range(5):
    forward(0.000000000000000000000000001)
    centered_arc(300, 200)
  

  #drawing ears
  forward(10)
  left(90)
  forward(270)
  right(7)
  color('black', 'yellow')
  begin_fill()
  centered_arc(100, 170)
  end_fill()
  left(187)
  forward(542)
  begin_fill()
  left(7)
  centered_arc(100, 170)
  end_fill()


  # drawing the head
  right(187)
  forward(270)
  left(90)
  forward(20)
  right(90)
  forward(8)

  color('black')
  circle(300)


  #DRAWING THE NOSE
  left(90)
  forward(50)
  right(90)
  forward(50)
  right(120)
  color('black', 'orange')
  begin_fill()
  pendown()
  forward(110)
  right(110)
  forward(120)
  right(130)
  forward(130)
  end_fill()

  #drawing hat
for i in range(100):
  left(180)
  draw()
  forward(20)
draw()

#hideturtle()
bye()	