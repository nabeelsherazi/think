import time
print("This program will tell you how long you have waited for after pressing enter.")
input()
print("When you are ready to wait, press enter. When you want to stop waiting, press enter again.")
input()
startTime = time.clock()
input()
endTime = time.clock()
numberOfSeconds = endTime - startTime

numberOfHours = numberOfSeconds // 3600
numberOfSecondsRemaining = numberOfSeconds % 3600
numberOfMinutes = numberOfSecondsRemaining // 60
numberOfSecondsRemaining = numberOfSecondsRemaining % 60
print('You waited for', numberOfHours, 'hours,', numberOfMinutes, 'minutes, and', numberOfSecondsRemaining, 'seconds in total!', sep = ' ')
input()