import turtle

def draw_bar(t, height):
	'''Makes turtle t draw a bar of height'''
	t.pendown()
	t.left(90)
	if height <= 255:
		for i in range(height):
			t.color(i, 0, 100)
			t.forward(1)
	else:
		for i in range(255):
			t.color(i, 0, 100)
			t.forward(1)
		t.forward(height - 255)
	t.right(90)
	t.forward(10)
	t.write(height)
	t.forward(30)
	t.right(90)
	if height <= 255:
		xs = list(range(height))
		xs.reverse()
		for i in xs:
			t.color(i, 0, 100)
			t.forward(1)
	else:
		t.forward(height - 255)
		xs = list(range(255))
		xs.reverse()
		for i in xs:
			t.color(i, 0, 100)
			t.forward(1)
	t.left(90)
	t.penup()
	t.forward(10)
	
def get_data():
	'''gets data points and converts into list of strings, returns list'''
	print("Enter your data points separated by spaces. Numbers only please!")
	RawDataSet = input()
	RawDataSet = RawDataSet.split()
	return RawDataSet

def check_list(inputList):
	'''checks if list is composed of numbers, and, if so, returns a new list of purely integers'''
	VerifiedDataSet = []
	for i in inputList:
		try:
			VerifiedDataSet.append(int(i))
		except:
			print("Value in", inputList.index(i) + 1, "position isn't a number!")
			return ("not approved",)
	return ("approved", VerifiedDataSet)

print("This program will make your data set into a color coded bar graph!")

listStatus = "not approved"

while listStatus == "not approved": #should continue to loop of check_list returns "not approved"
	dataSet = get_data()
	result = check_list(dataSet)
	listStatus = result[0]
	if listStatus == 'approved':
		dataSet = result[1]
	else:
		pass

alex = turtle.Turtle()
wn = turtle.Screen()
wn.colormode(255)

for pt in dataSet:
	draw_bar(alex, pt)
alex.left(180)
alex.color('blue')
alex.pendown()
alex.forward(len(dataSet)*50)

wn.mainloop()