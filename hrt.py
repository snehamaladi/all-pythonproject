import turtle
pen = turtle.Turtle()
def curve():
    for i in range(200):
        pen.right(1)
        pen.forward(1)

def heart():
    pen.fillcolor('red')
    pen.begin_fill()
    pen.left(140)
    pen.forward(113)
    curve()
    pen.left(120)

    curve()
    pen.forward(112)
    pen.end_fill()

if __name__ == '__main__' :
    heart()
    pen.hideturtle()
    turtle.done()