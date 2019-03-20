import turtle
colors=["red","blue","purple","green","yellow","orange"]
t = turtle.Pen()
t.speed(0)
turtle.bgcolor("black")
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100+1)
    t.forward(x)
    t.left(75)

    t.left(64)
    t.left(75)
    t.left(90)
    t.left(150)
turtle.done()