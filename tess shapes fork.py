import turtle
wn = turtle.Screen()
wn.title('Hi Tess! (V 2.11)')

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
	shapeFill = input('What color should Tess fill the shape with? ')
	if shapeFill not in ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']:
		print('Invalid color (ROYGBIV only)')
	else:
		break
tess.color(turtleColor, shapeFill)

shapesList = ['triangle', 'square', 'pentagon', 'hexagon', 'heptagon', 'octagon']

while True:
	while True:
		shape = input('What shape should Tess draw? ')
		if shape == 'circle':
			sides = 360
			break
		else:
			try:
				sides = shapesList.index(shape) + 3
				break
			except ValueError:
				print('Shape invalid or not supported')
	while True:
		try:
			shapeSize = input('How big should Tess draw the shape? ')
			shapeSize = int(shapeSize)
		except ValueError:
			print('Invalid response')
		else:
			break

	tess.begin_fill()	
	for i in range(sides):
		if shape == 'circle':
			tess.forward(1)
		else:
			tess.forward(shapeSize)
		tess.left(360/sides)
	tess.end_fill()
	while True:
		drawAgain = input('Have Tess draw another shape? ')
		if drawAgain == 'yes':
			tess.clear()
			break
		elif drawAgain == 'no':
			raise SystemExit
		else:
			print('Invalid response')