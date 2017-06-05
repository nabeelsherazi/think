import turtle
import random

turtleName = input(
'''Name your turtle!

Their name is... ''')

wn = turtle.Screen()
string = turtleName + "'s Playground!"
wn.title(string)
turtle = turtle.Turtle()
turtle.pensize(2)
turtle.speed(10)

print(turtleName, "is going to go crazy!! Are you ready?")
input()
print("AHHHHHHHH!")

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

while True:
	turtle.forward(5)
	if turtle.xcor()**2 + turtle.ycor()**2 >= 10000:
		turtle.left(180 + random.randint(0, 45))
		turtle.color(colors[random.randint(0, 6)])
		turtle.forward(10)