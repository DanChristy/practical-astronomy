import math
from . import pa_shared

## This class provides Date-of-Easter functions.
class CDateOfEaster(object):
	def __init__(self):
		pass

	## \brief Gets the date of Easter for the year specified.
	# @param  year  Year for which you'd like the date of Easter.
	# @returns  GreenwichDate, a simple month/day/year structure.
	def GetDateOfEaster(self, year):

		a = year % 19
		b = math.floor(year/100)
		c = year % 100
		d = math.floor(b/4)
		e = b % 4
		f = math.floor((b+8)/25)
		g = math.floor((b-f+1)/3)
		h = ((19*a)+b-d-g+15) % 30
		i = math.floor(c/4)
		k = c % 4
		l = (32 + 2 * (e + i) - h - k) % 7
		m = math.floor((a + (11 * h) + (22 * l)) / 451 )
		n = math.floor((h + l - (7 * m) + 114) / 31)
		p = (h + l - (7 * m) + 114) % 31
		
		returnDay = p + 1
		returnMonth = n
		returnYear = year

		returnValue = pa_shared.GreenwichDate(returnMonth, returnDay, returnYear)

		return returnValue