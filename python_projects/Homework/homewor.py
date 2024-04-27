import turtle
t = turtle.Pen()
b = 0
size = 2
colors = ["red", "orange", "yellow", "green", "blue", "black", "white"]
while True:
    a = input()
    if a == "1":
        t.fd(100)
    elif a == "2":
        t.lt(90)
    elif a == "3":
        t.rt(90)
    elif a == "4":
        t.color(colors[b%7])
        b += 1
    elif a == "5":
        for i in range(4):
            t.fd(100)
            t.lt(90)
    elif a == "6":
        size += 1
    elif a == "7":
        size -= 1
    elif a == "0":
        quit()
    elif size <= 0:
        size = 1
    t.shapesize(size%5)
    
        
