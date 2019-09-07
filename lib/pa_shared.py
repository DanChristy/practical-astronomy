## This class holds a simple Civil Date (month, day, and year)
class CivilDate(object):
	def __init__(self, month, day, year):
		self.month = month
		self.day = day
		self.year = year

## Returns True or False indicating if the specified year is a leap year.
def IsLeapYear(year):
	if (year % 4) == 0:
		if (year % 100) == 0:
			if (year % 400) == 0:
				return True
			else:
				return False
		else:
			return True
	else:
		return False
