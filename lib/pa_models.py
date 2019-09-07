## This class holds a simple Civil Date (month, day, and year)
class CivilDate(object):
	def __init__(self, month, day, year):
		self.month = month
		self.day = day
		self.year = year

## This class holds a simple Civil Time (hours, minutes, and seconds)
class CivilTime(object):
	def __init__(self, hours, minutes, seconds):
		self.hours = hours
		self.minutes = minutes
		self.seconds = seconds