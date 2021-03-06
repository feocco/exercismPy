import calendar
import datetime

def meetup_day(year, month, day, param):
	weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
	numOfDays = calendar.monthrange(year, month)
	mydict = {}
	tempList = []
	meetupday = 0

	#Creates dictionary with days of month & what weekday it is. ( 0 = Monday, 6 = Sunday)
	for x in range(1, numOfDays[1] + 1):
		mydict[x] = datetime.date(year, month, x).weekday()

	#Creates list with all days of the month of a certain weekday
	for x in mydict:
		if datetime.date(year, month, x).weekday() == weekdays.index(day):
			tempList.append(x)
	
	#Flow control for parameter and return value
	if param == 'last':
		return datetime.date(year, month, tempList[-1])
	elif param == 'teenth':
		for x in tempList:
			if x >= 13 and x <= 19:
				return datetime.date(year, month, x)
	else:
		meetupday = tempList[int(param[0])-1]
		return datetime.date(year, month, meetupday)
