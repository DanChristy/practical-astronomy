import math
from . import pa_models
from . import pa_util

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
			workingMonth = workingMonth * 62 if pa_util.IsLeapYear(workingYear) else workingMonth * 63
			workingMonth = math.floor(workingMonth / 2)
		else:
			workingMonth = math.floor((workingMonth + 1) * 30.6)
			workingMonth = workingMonth - 62 if pa_util.IsLeapYear(workingYear) else workingMonth - 63
		
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
		returnDay = self.JulianDateDay(julianDate)
		returnMonth = self.JulianDateMonth(julianDate)
		returnYear = self.JulianDateYear(julianDate)

		return pa_models.CivilDate(returnMonth, returnDay, returnYear)

	## \brief Convert a Julian Date to Day-of-Week (e.g., Sunday)
	def JulianDateToWeekdayName(self, julianDate):
		J = math.floor(julianDate - 0.5) + 0.5
		N = (J + 1.5) % 7
		
		if N == 0: return "Sunday"
		if N == 1: return "Monday"
		if N == 2: return "Tuesday"
		if N == 3: return "Wednesday"
		if N == 4: return "Thursday"
		if N == 5: return "Friday"
		if N == 6: return "Saturday"

		return "Unknown"

	## \brief Returns the day part of a Julian Date
	def JulianDateDay(self, julianDate):
		I = math.floor(julianDate + 0.5)
		F = julianDate + 0.5 - I
		A = math.floor((I - 1867216.25) / 36524.25)
		B = I + 1 + A - math.floor(A / 4) if I > 2299160 else I
		C = B + 1524
		D = math.floor((C - 122.1) / 365.25)
		E = math.floor(365.25 * D)
		G = math.floor((C - E) / 30.6001)

		return C - E + F - math.floor(30.6001 * G)

	## \brief Returns the month part of a Julian Date
	def JulianDateMonth(self, julianDate):
		I = math.floor(julianDate + 0.5)
		F = julianDate + 0.5 - I
		A = math.floor((I - 1867216.25) / 36524.25)
		B = I + 1 + A - math.floor(A / 4) if I > 2299160 else I
		C = B + 1524
		D = math.floor((C - 122.1) / 365.25)
		E = math.floor(365.25 * D)
		G = math.floor((C - E) / 30.6001)

		returnValue = G - 1 if G < 13.5 else G - 13
		return returnValue

	## \brief Returns the year part of a Julian Date
	def JulianDateYear(self, julianDate):
		I = math.floor(julianDate + 0.5)
		F = julianDate + 0.5 - I
		A = math.floor((I - 1867216.25) / 36524.25)
		B = I + 1 + A - math.floor(A / 4) if I > 2299160 else I
		C = B + 1524
		D = math.floor((C - 122.1) / 365.25)
		E = math.floor(365.25 * D)
		G = math.floor((C - E) / 30.6001)
		H = G - 1 if G < 13.5 else G - 13

		returnValue = D - 4716 if H > 2.5 else D - 4715
		return returnValue

	## \brief Convert a Civil Time to Decimal Hours
	def CivilTimeToDecimalHours(self, civilTime):
		inputHours = civilTime.hours
		inputMinutes = civilTime.minutes
		inputSeconds = civilTime.seconds

		A = abs(inputSeconds) / 60
		B = (abs(inputMinutes) + A) / 60
		C = abs(inputHours) + B
		
		return -C if ((inputHours < 0) or (inputMinutes < 0) or (inputSeconds < 0)) else C

	## \brief Return the hour part of a Decimal Hours
	def DecimalHourHour(self, decimalHours):
		A = abs(decimalHours)
		B = A * 3600
		C = round(B - 60 * math.floor(B / 60), 2)
		D = 0 if C == 60 else C
		E = B + 60 if C == 60 else B

		return -(math.floor(E / 3600)) if decimalHours < 0 else math.floor(E / 3600)

	## \brief Return the minutes part of a Decimal Hours
	def DecimalHourMinutes(self, decimalHours):
		A = abs(decimalHours)
		B = A * 3600
		C = round(B - 60 * math.floor(B / 60), 2)
		D = 0 if C == 60 else C
		E = B + 60 if C == 60 else B

		return math.floor(E / 60) % 60

	## \brief Return the seconds part of a Decimal Hours
	def DecimalHourSeconds(self, decimalHours):
		A = abs(decimalHours)
		B = A * 3600
		C = round(B - 60 * math.floor(B / 60), 2)
		D = 0 if C == 60 else C

		return math.floor(D)

	## \brief Convert Decimal Hours to Civil Time
	def DecimalHoursToCivilTime(self, decimalHours):
		hours = self.DecimalHourHour(decimalHours)
		minutes = self.DecimalHourMinutes(decimalHours)
		seconds = self.DecimalHourSeconds(decimalHours)

		return pa_models.CivilTime(hours, minutes, seconds)

	## \brief Convert local Civil Time to Universal Time
	def LocalCivilTimeToUniversalTime(self, localCivilTime, isDaylightSavings, zoneCorrection, localDate):
		LCT = self.CivilTimeToDecimalHours(localCivilTime)

		daylightSavingsOffset = 1 if isDaylightSavings == True else 0
		UTinterim = LCT - daylightSavingsOffset - zoneCorrection
		GDayInterim = localDate.day + (UTinterim / 24)
		
		greenwichInput = pa_models.CivilDate(localDate.month,GDayInterim,localDate.year)
		JD = self.GreenwichDateToJulianDate(greenwichInput)
		
		GDay = self.JulianDateDay(JD)
		GMonth = self.JulianDateMonth(JD)
		GYear = self.JulianDateYear(JD)
		
		UT = 24 * (GDay - math.floor(GDay))
		
		return pa_models.UniversalTime(self.DecimalHourHour(UT),self.DecimalHourMinutes(UT),self.DecimalHourSeconds(UT),math.floor(GDay),GMonth,GYear)

	## \brief Convert Universal Time to local Civil Time
	def UniversalTimeToLocalCivilTime(self, universalTime, isDayLightSavings, zoneCorrection, greenwichDate):
		UT = self.CivilTimeToDecimalHours(universalTime)
		zoneTime = UT + zoneCorrection
		localTime = zoneTime + (1 if isDayLightSavings == True else 0)
		localJDPlusLocalTime = self.GreenwichDateToJulianDate(greenwichDate) + (localTime / 24)
		localDay = self.JulianDateDay(localJDPlusLocalTime)
		integerDay = math.floor(localDay)
		localMonth = self.JulianDateMonth(localJDPlusLocalTime)
		localYear = self.JulianDateYear(localJDPlusLocalTime)
		LCT = 24 * (localDay - integerDay)

		return pa_models.UniversalTime(self.DecimalHourHour(LCT),self.DecimalHourMinutes(LCT),self.DecimalHourSeconds(LCT),integerDay,localMonth,localYear)