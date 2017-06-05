import turtle

wn = turtle.Screen()
wn.bgcolor('light green')

tess = turtle.Turtle()
tess.shape('turtle')
tess.color('blue')
tess.pensize(3)
tess.penup()

tess.stamp()

for i in range(12):
	tess.right(360 / 12)
	tess.forward(100)
	tess.pendown()
	tess.forward(20)
	tess.penup()
	tess.forward(20)
	tess.stamp()
	tess.backward(140)
	
wn.mainloop()