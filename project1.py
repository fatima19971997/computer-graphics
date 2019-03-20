import turtle
b = turtle.Turtle()
co = ["red","blue","yellow","pink"]
for i in co:
    b.color(i)
    b.right(90)
    b.backward(90)
b.left(45)
b.forward(125)
b.penup()
b.left(135)
b.forward(87)
b.pendown()
b.left(135)
b.forward(130)
turtle.done()