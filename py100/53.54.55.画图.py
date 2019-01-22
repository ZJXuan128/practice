import turtle
def line():
    t.up()
    t.goto(-250,250)
    t.down()
    t.goto(500,-500)
def circle():
    turtle.circle(100)
def rectangle():
    t.up()
    t.goto(-100,100)
    t.down()
    t.goto(100,100)
    t.goto(100,-100)
    t.goto(-100,-100)
    t.goto(-100,100)
turtle.setup(width=500,height=500)
t=turtle.Pen()
line()
circle()
rectangle()
turtle.done()
