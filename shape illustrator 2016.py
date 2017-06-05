import turtle
import math

def draw_box(text, x, y, wd=140, ht=60, fill=True):
    '''draws a box centered at (x, y) with centered text. defaults to width 140
    and height 60 unless specified otherwise. defaults to filling box with fillcolor
    unless specified otherwise '''
    tess_reset(x, y)
    tess.forward(wd/2)
    # x_max = round(tess.xcor(), 1)
    tess.left(90)
    tess.pendown()
    if fill == True:
        tess.begin_fill()
    tess.forward(ht/2)
    tess.left(90)
    # y_max = round(tess.ycor())
    tess.forward(wd)
    tess.left(90)
    # x_min = round(tess.xcor())
    tess.forward(ht)
    tess.left(90)
    # y_min = round(tess.ycor())
    tess.forward(wd)
    tess.left(90)
    tess.forward(ht/2)
    tess.penup()
    if fill == True:
        tess.end_fill()
    tess_reset(x, y)
    tess.right(90)
    tess.forward(ht/4)
    tess.write(text, align="center", font=("Segoe UI", 18, "normal"))
    tess_reset()
    return

def menu_handler(x, y):
    '''handles clicks while in menu state, checking if they correspond to a
    clicked box and, if so, determining which shape needs to be drawn'''
    shape_to_draw = None
    tess.goto(x, y)
    for (shape, x_bounds, y_bounds) in box_cors:
        if x >= x_bounds[0] and x <= x_bounds[1] and y >= y_bounds[0] and y <= y_bounds[1]:
            shape_to_draw = shape
            tess_reset()
            tess.clear()
            draw_shape(shape_to_draw)
            break
    return None

def exit_handler(x, y):
    '''handles clicks while in draw state, checking if they correspond to a
    click at the exit box and, if so, returning screen to menu state'''
    tess.goto(x, y)
    if x >= -570 and x <= -430 and y >= 250 and y <= 310:
        tess.clear()
        tess_reset()
        menu_state()

def draw_shape_choices():
    '''draws all six shape options'''
    tess_reset()
    tess.clear()
    shape_counter = 0
    for row in range(1, 3):
        for column in range(1, 4):
            draw_box(shapes_list[shape_counter], -640 + (320 * column), 360 - (240 * row))
            shape_counter += 1
    return

def tess_reset(x=0, y=0):
    '''moves tess to a location and sets her heading to zero. if no arguments
    are given, moves tess to origin'''
    tess.goto(x, y)
    tess.setheading(0)

def draw_shape(shape):
    '''draws the inputted shape as well as an exit box. binds clicks to exit handler'''
    correct_position(shape)
    tess.setheading(0)
    tess.pendown()
    tess.begin_fill()
    sides = shapes_list.index(shape) + 3
    for i in range(sides):
        tess.forward(200)
        tess.left(360/sides)
    tess.penup()
    tess.end_fill()
    draw_box("Exit", -500, 280)
    wn.onclick(exit_handler)

def correct_position(shape):
    '''moves tess so that inputted shape is drawn in the center of the screen'''
    if shape == "triangle":
        tess.backward(100)
        tess.right(90)
        tess.forward(173/2)
        tess.left(90)
    else:
        angle = 360/(shapes_list.index(shape) + 3)
        center_height = 100/(math.tan(math.radians(angle/2)))
        tess.backward(100)
        tess.right(90)
        tess.forward(center_height)
        tess.left(90)

def menu_state():
    '''main state of program, draws shape choices and title. binds
    clicks to menu handler'''
    draw_shape_choices()
    draw_box("", 0, 260, 700, 100)
    tess.goto(0, 250)
    tess.write("Shape Illustrator 2016", align="center", font=("Courier", 24, "normal"))
    tess.goto(0, 230)
    tess.write("Running on 100% pasteurized love", align="center", font=("Agency FB", 14, "normal"))
    tess_reset()
    wn.onclick(menu_handler)

# box bounds
box_cors = [("triangle", (-390, -250.0), (90, 150)),
("square", (-70, 70.0), (90, 150)),
("pentagon", (270, 370.0), (90, 150)),
("hexagon", (-390, -250.0), (-150, -90)),
("heptagon", (-70, 70.0), (-150, -90)),
("octagon", (270, 370.0), (-150, -90))]

turtle.setup(1280, 720)
wn = turtle.Screen()
wn.title("Shape Illustrator 2016")
wn.bgcolor("orange")
shapes_list = ('triangle', 'square', 'pentagon', 'hexagon', 'heptagon', 'octagon')

#initialize draw
tess = turtle.Turtle()
tess.hideturtle()
tess.penup()
tess.speed(0)
tess.color("gold", "grey")

menu_state()
wn.mainloop()
