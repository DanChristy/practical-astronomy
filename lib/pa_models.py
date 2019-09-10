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

## This class holds a Universal Time object (month, day, year and hours, minutes, seconds)
class UniversalTime(object):
	def __init__(self, utHours, utMinutes, utSeconds, gwDay, gwMonth, gwYear):
		self.utHours = utHours
		self.utMinutes = utMinutes
		self.utSeconds = utSeconds
		self.gwDay = gwDay
		self.gwMonth = gwMonth
		self.gwYear = gwYear

## This class holds an Angle object (degrees, minutes, seconds)
class Angle(object):
	def __init__(self, degrees, minutes, seconds):
		self.degrees = degrees
		self.minutes = minutes
		self.seconds = seconds
