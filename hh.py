import turtle
b = turtle.Turtle()
turtle.bgcolor("pink")

def rr(x,y,z):

  b.left(x)
  b.forward(y)
  b.right(90)
  b.color(z)
  b.circle(50)
  b.pencolor("black")
  b.home()
b.begin_fill()
rr(120,50,"red")
b.end_fill()
b.begin_fill()
rr(70,50,"green")
b.end_fill()
b.begin_fill()
rr(80,160,"yellow")
b.end_fill()
b.begin_fill()
rr(105,210,"blue")
b.end_fill()
turtle.done()