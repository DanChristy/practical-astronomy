import math
from . import pa_shared

## This class provides conversion functions.
class CConvert(object):
	def __init__(self):
		pass

	## \brief Returns the day number for the date specified.
	def CivilDateToDayNumber(self, civilDate):
		workingMonth = civilDate.month
		workingDay = civilDate.day
		workingYear = civilDate.year

		if workingMonth <= 2:
			workingMonth = workingMonth - 1
			workingMonth = workingMonth * 62 if pa_shared.IsLeapYear(workingYear) else workingMonth * 63
			workingMonth = math.floor(workingMonth / 2)
		else:
			workingMonth = math.floor((workingMonth + 1) * 30.6)
			workingMonth = workingMonth - 62 if pa_shared.IsLeapYear(workingYear) else workingMonth - 63
		
		returnValue = workingMonth + workingDay

		return returnValue
