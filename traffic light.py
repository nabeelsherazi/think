import turtle           # Tess becomes a traffic light.

turtle.setup(1280, 720)
wn = turtle.Screen()
wn.title("Tess becomes a traffic light!")
wn.bgcolor("lightgreen")
tess = turtle.Turtle()
green_guy = turtle.Turtle()
yellow_guy = turtle.Turtle()
red_guy = turtle.Turtle()
guys = (red_guy, yellow_guy, green_guy)


def draw_housing(turtle):
    """ Draw a nice housing to hold the traffic lights """
    turtle.pensize(3)
    turtle.color("black", "darkgrey")
    turtle.begin_fill()
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(200)
    turtle.circle(40, 180)
    turtle.forward(200)
    turtle.left(90)
    turtle.end_fill()

def setup_guys(guy):
    guy.penup()
    guy.backward(180)

guy_forward = 50
def setup_guys_2(guy):
    guy.forward(40)
    guy.left(90)
    guy.forward(guy_forward)
    guy.shape("circle")
    guy.shapesize(3)

for guy in guys:
    setup_guys(guy)

red_guy.pendown()
draw_housing(red_guy)
red_guy.penup()

draw_housing(tess)
tess.penup()
# Position tess onto the place where the green light should be
tess.forward(40)
tess.left(90)
tess.forward(50)

for guy in guys:
    setup_guys_2(guy)
    guy_forward += 70
red_guy.fillcolor("red")
yellow_guy.fillcolor("gold")
green_guy.fillcolor("dark green")
# Turn tess into a big green circle
tess.shape("circle")
tess.shapesize(3)
tess.fillcolor("red")

# A traffic light is a kind of state machine with three states,
# Green, Orange, Red.  We number these states  0, 1, 2
# When the machine changes state, we change tess' position and
# her fillcolor.

# This variable holds the current state of the machine
state_num = 0


def advance_state_machine():
    global state_num
    if state_num == 0:       # Transition from state 0 to state 1
        tess.forward(140)
        tess.fillcolor("green")
        red_guy.fillcolor("dark red")
        green_guy.fillcolor("green")
        state_num = 1
    elif state_num == 1:     # Transition from state 1 to state 2
        tess.backward(70)
        tess.fillcolor("yellow")
        green_guy.fillcolor("dark green")
        yellow_guy.fillcolor("yellow")
        state_num = 2
    else:                    # Transition from state 2 to state 0
        tess.backward(70)
        tess.fillcolor("red")
        yellow_guy.fillcolor("gold")
        red_guy.fillcolor("red")
        state_num = 0
    wn.ontimer(advance_state_machine, 2000)

# Bind the event handler to the space key.
wn.ontimer(advance_state_machine, 2000)

wn.listen()                      # Listen for events
wn.mainloop()
