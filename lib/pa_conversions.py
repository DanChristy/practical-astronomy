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

	## \brief Convert a Greenwich Date (civil date with no timezone info) to Julian Date
	def GreenwichDateToJulianDate(self, greenwichDate):
		month = greenwichDate.month
		day = greenwichDate.day
		year = greenwichDate.year

		Y = year - 1 if month < 3 else year
		M = month + 12 if month < 3 else month

		if year > 1582:
			A = math.floor(Y / 100)
			B = 2 - A + math.floor(A / 4)
		else:
			if year == 1582 and month > 10:
				A = math.floor(Y / 100)
				B = 2 - A + math.floor(A / 4)
			else:
				if year == 1582 and month == 10 and day >= 15:
					A = math.floor(Y / 100)
					B = 2 - A + math.floor(A / 4)
				else:
					B = 0
		
		C = math.floor((365.25 * Y) - 0.75) if Y < 0 else math.floor(365.25 * Y)

		D = math.floor(30.6001 * (M + 1))

		return B + C + D + day + 1720994.5

	## \brief Convert a Julian Date to Greenwich Date (civil date with no timezone info)
	def JulianDateToGreenwichDate(self, julianDate):
		I = math.floor(julianDate + 0.5)
		F = julianDate + 0.5 - I
		A = math.floor((I - 1867216.25) / 36524.25)
		B = I + 1 + A - math.floor(A / 4) if I > 2299160 else I
		C = B + 1524
		D = math.floor((C - 122.1) / 365.25)
		E = math.floor(365.25 * D)
		G = math.floor((C - E) / 30.6001)

		returnDay = C - E + F - math.floor(30.6001 * G)
		returnMonth = G - 1 if G < 13.5 else G - 13
		returnYear = D - 4716 if returnMonth > 2.5 else D - 4715

		return pa_shared.CivilDate(returnMonth, returnDay, returnYear)
