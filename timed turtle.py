import turtle
import time

turtle.setup(400,500)
wn = turtle.Screen()
wn.title("Using a timer")
wn.bgcolor("lightgreen")

tess = turtle.Turtle()
tess.color("purple")
tess.pensize(3)

def h1():
    tess.forward(10)
    tess.left(round(time.clock(), 1))
    wn.ontimer(h1, 1)

h1()
wn.mainloop()
