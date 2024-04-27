import turtle
import time
t = turtle.Pen()
all_shapes = ["turtle", "circle", "square", "triangle", "arrow", "classic"]
all_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_size = list(range(1,7))
while True:
    for i in range(6):
        time.sleep(1)
        t.shape(all_shapes[i])
        t.shapesize(all_size[i])
        t.color(all_colors[i])
        t.shapetransform("turtle")

