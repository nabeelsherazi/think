print('Welcome to Time Calculator Version 1.16')
while True:
	while True:
		try:
			currentHour = input('What hour is it on the clock now? ')
			currentHour = int(currentHour)
			if currentHour not in range(1, 13):
				raise ValueError
		except ValueError:
			print('That\'s not an acceptable answer!')
		else:
			break
	while True:
		try:
			hourType = input('Is it AM or PM? ')
			hourType = str.upper(hourType)
			if hourType not in ['AM', 'PM']:
				raise TypeError
		except TypeError:
			print('That\'s not an acceptable answer!')
		else:
			break
	if hourType == 'AM':
		hourType = 'AM.'
		oppositeHourType = 'PM.'
	elif hourType == 'PM':
		hourType = 'PM.'
		oppositeHourType = 'AM.'
	while True:
		try:
			hoursForward = input('How many hours will you wait for? ')
			hoursForward = int(hoursForward)
			if hoursForward < 0:
				raise ValueError
		except ValueError:
			print('That\'s not an acceptable answer!')
		else:
			break
	if currentHour + hoursForward < 12:
		print('When you are done, the time will be', currentHour + hoursForward, hourType, sep = ' ')
	elif currentHour + hoursForward >= 12:
		hoursAfterTwelve = (currentHour + hoursForward) % 12
		if hoursAfterTwelve == 0:
			typeChanges = (currentHour + hoursForward) // 12
			if typeChanges % 2 == 0:
				print('When you are done, the time will be 12', hourType, sep = ' ')
			elif typeChanges % 2 != 0:
				print('When you are done, the time will be 12', oppositeHourType, sep = ' ')
		else:
			typeChanges = (currentHour + hoursForward) // 12
			if typeChanges % 2 == 0:
				print('When you are done, the time will be', hoursAfterTwelve, hourType, sep = ' ')
			elif typeChanges % 2 !=0:
				print('When you are done, the time will be', hoursAfterTwelve, oppositeHourType, sep = ' ')
	while True:
		calculateAgain = input('Would you like to calculate another time? Type "yes" or "no." ')
		if calculateAgain == 'yes':
			break
		elif calculateAgain == 'no':
			raise SystemExit
		else:
			print('That\'s not an acceptable answer!')
