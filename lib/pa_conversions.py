import math
from . import pa_shared

## This class provides conversion functions.
class CConvert(object):
	def __init__(self):
		pass

	## \brief Returns the day number for the date specified.
	def GreenwichDateToDayNumber(self, greenwichDate):
		workingMonth = greenwichDate.month
		workingDay = greenwichDate.day
		workingYear = greenwichDate.year

		if workingMonth <= 2:
			workingMonth = workingMonth - 1
			if pa_shared.IsLeapYear(workingYear):
				workingMonth = workingMonth * 62
			else:
				workingMonth = workingMonth * 62
			workingMonth = workingMonth / 2
			workingMonth = math.floor(workingMonth)
		else:
			workingMonth = workingMonth + 1
			workingMonth = workingMonth * 30.6
			workingMonth = math.floor(workingMonth)
			if pa_shared.IsLeapYear(workingYear):
				workingMonth = workingMonth - 62
			else:
				workingMonth = workingMonth - 63
		
		returnValue = workingMonth + workingDay

		return returnValue

