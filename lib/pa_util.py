def is_leap_year(year):
	""" Returns True or False indicating if the specified year is a leap year. """
	if (year % 4) == 0:
		if (year % 100) == 0:
			return True if (year % 400) == 0 else False
		else:
			return True
	else:
		return False
