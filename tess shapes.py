import turtle
wn = turtle.Screen()
wn.title('Hi Tess! (V 1.07)')

tess = turtle.Turtle()
turtle.shape('turtle')

while True:
	turtleColor = input('What color is Tess? ')
	if turtleColor not in ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']:
		print('Invalid color (ROYGBIV only)')
	else:
		break
tess.color(turtleColor)

while True:
	bgcolor = input('What color should the background be? ')
	if bgcolor not in ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']:
		print('Invalid color (ROYGBIV only)')
	else:
		break
wn.bgcolor(bgcolor)

while True:
	try:
		penSize = input('What should Tess\'s pen size be? ')
		penSize = int(penSize)
	except ValueError:
		print('Invalid response')
	else:
		break
tess.pensize(penSize)

while True:
	while True:
		shape = input('What shape should Tess draw? ')
		if shape == 'triangle':
			sides = 3
			break
		elif shape == 'square':
			sides = 4
			break
		elif shape == 'pentagon':
			sides = 5
			break
		elif shape == 'hexagon':
			sides = 6
			break
		elif shape == 'heptagon':
			sides = 7
			break
		elif shape == 'octagon':
			sides = 8
			break
		elif shape == 'circle':
			sides = 360
			break
		else:
			print('Shape invalid or not supported')

	for i in range(sides):
		if shape == 'circle':
			tess.forward(1)
		else:
			tess.forward(50)
		tess.left(360/sides)
	while True:
		drawAgain = input('Have Tess draw another shape? ')
		if drawAgain == 'yes':
			tess.clear()
			break
		elif drawAgain == 'no':
			raise SystemExit
		else:
			print('Invalid response')