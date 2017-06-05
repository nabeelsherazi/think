import turtle
alex = turtle.Turtle()
wn = turtle.Screen()
alex.color('blue')
wn.bgcolor('light green')


def square(sz):
	alex.forward(sz/2)
	alex.right(90)
	alex.forward(sz/2)
	alex.right(90)
	for i in range(3):
		alex.forward(sz)
		alex.right(90)
	alex.forward(sz/2)
	alex.right(90)
	alex.forward(sz/2)
	alex.right(180)

def draw_and_turn(theta, sz):
	square(sz)
	alex.right(theta)

angle = int(input('theta? '))
size = int(input('size? '))

for i in range(int(360/angle)):
	draw_and_turn(angle, size)

input()
