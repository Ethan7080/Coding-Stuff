import time
import turtle
import random
t = turtle.Pen()
all_shapes = ["classic", "turtle", "square", "circle", "arrow", "triangle"]
for i in range(len(all_shapes)):
    t.shape(all_shapes[i%6])
    time.sleep(1)
for i in range(len(all_shapes)):
    t.shape(random.choice(all_shapes))
    time.sleep(1)

    
