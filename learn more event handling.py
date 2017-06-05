import turtle

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("How to handle mouse clicks on the window!")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("purple")
tess.pensize(3)
tess.shape("circle")

def h1(x, y):
    wn.title("Got a click at {0}, {1}".format(x, y))
    tess.goto(x, y)
    print(x, y)

tess.ondrag(turtle.goto)  # Wire up a click on the window.
wn.mainloop()
