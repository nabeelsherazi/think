dayList = ['Sunday','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
while True:
	try:
		dayNumber = int(input('What number day is it? '))
	except:
		print('Not valid')
	else:
		if dayNumber not in range(1, 8):
			print('Not valid')
		else:
			print(dayList[dayNumber -1])