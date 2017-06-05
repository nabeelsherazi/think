print('Welcome to Seconds2Hours Converter Version 1.03!')
while True:
	inputSeconds = input('How many seconds in total? ')
	try:
		numberOfSeconds = int(inputSeconds)
		if numberOfSeconds < 0:
			raise TypeError
	except ValueError:
		print('That\'s not a number!')
	except TypeError:
		print('You can\'t have negative seconds!')
	else:
		numberOfHours = numberOfSeconds // 3600
		numberOfSecondsRemaining = numberOfSeconds % 3600
		numberOfMinutes = numberOfSecondsRemaining // 60
		numberOfSecondsRemaining = numberOfSecondsRemaining % 60
		print('That\'s', numberOfHours, 'hours,', numberOfMinutes, 'minutes, and', numberOfSecondsRemaining, 'seconds in total!', sep = ' ')
		while True:
			convertAgain = input('Do you want to convert another amount? Type "yes" or "no." ')
			if convertAgain == 'yes':
				break
			elif convertAgain == 'no':
				print('Thanks for using Seconds2Hours Converter! Have a nice day.')
				raise SystemExit
			else:
				print('That doesn\'t answer my question!')
