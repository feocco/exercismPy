import calendar
import datetime

def meetup_day(year, month, day, param):
	weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
	numOfDays = calendar.monthrange(year, month)
	mydict = {}
	tempList = []
	meetupday = 0

	#Creates dictionary with days of month & what weekday it is. ( 0 = Monday, 6 = Sunday)
	for x in range(1, numOfDays[1]):
		mydict[x] = datetime.date(year, month, x).weekday()

	#Creates list with all days of the month of a certain weekday
	for x in mydict:
		if datetime.date(year, month, x).weekday() == weekdays.index(day):
			tempList.append(x)
	
	#Returns meetup day based on param and list
	meetupday = tempList[int(param[0])-1]
	return datetime.date(year, month, meetupday)

	#Troubleshooting:
	print('Temp List' + str(tempList))
	print("Meet up day " + str(meetupday))
	print("Correct Output: date(2013, 4, 8)")
	print("Actual Output: date({0}, {1}, {2})".format(year, month, meetupday))

meetup_day(2013, 4, 'Monday', '2nd')
