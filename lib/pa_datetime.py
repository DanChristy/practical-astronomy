import math
from . import pa_models
from . import pa_util

## This class provides functions for working with dates and times.
class CDateTime(object):
	def __init__(self):
		pass

	## \brief Gets the date of Easter for the year specified.
	# @param  year  Year for which you'd like the date of Easter.
	# @returns  CivilDate, a simple month/day/year structure.
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

		returnValue = pa_models.CivilDate(returnMonth, returnDay, returnYear)

		return returnValue

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

		return D

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

	## \brief Convert Universal Time to Greenwich Sidereal Time
	def UniversalTimeToGreenwichSiderealTime(self, universalTime, greenwichDate):
		JD = self.GreenwichDateToJulianDate(greenwichDate)
		S = JD - 2451545
		T = S / 36525
		T01 = 6.697374558+(2400.051336*T)+(0.000025862*T*T)
		T02 = T01-(24*math.floor(T01/24))
		UT = self.CivilTimeToDecimalHours(universalTime)
		A = UT*1.002737909
		GST1 = T02 + A
		GST2 = GST1 - (24*math.floor(GST1/24))

		gstHours = self.DecimalHourHour(GST2)
		gstMinutes = self.DecimalHourMinutes(GST2)
		gstSeconds = self.DecimalHourSeconds(GST2)
				
		return pa_models.CivilTime(gstHours,gstMinutes,gstSeconds)

	## \brief Convert Greenwich Sidereal Time to Universal Time
	def GreenwichSiderealTimeToUniversalTime(self, siderealTime, greenwichDate):
		JD = self.GreenwichDateToJulianDate(greenwichDate)
		S = JD - 2451545
		T = S / 36525
		T01 = 6.697374558 + (2400.051336*T) + (0.000025862*T*T)
		T02 = T01-(24*math.floor(T01/24))
		gstHours = self.CivilTimeToDecimalHours(siderealTime)
		A = gstHours-T02
		B = A-(24*math.floor(A/24))
		UT = B*0.9972695663	
		
		utHours = self.DecimalHourHour(UT)
		utMinutes = self.DecimalHourMinutes(UT)
		utSeconds = self.DecimalHourSeconds(UT)

		warningFlag = "Warning" if UT < 0.065574 else "OK"  # TODO: Log this somewhere...

		return pa_models.CivilTime(utHours,utMinutes,utSeconds)

	## \brief Convert Greenwich Sidereal Time to Local Sidereal Time
	def GreenwichSiderealTimeToLocalSiderealTime(self, siderealTime, geographicalLongitude):
		GST = self.CivilTimeToDecimalHours(siderealTime)
		offset = geographicalLongitude /15
		lstHours1 = GST + offset
		lstHours2 = lstHours1-(24*math.floor(lstHours1/24))
		
		lstHours = self.DecimalHourHour(lstHours2)
		lstMinutes = self.DecimalHourMinutes(lstHours2)
		lstSeconds = self.DecimalHourSeconds(lstHours2)

		return pa_models.CivilTime(lstHours,lstMinutes,lstSeconds)

	## \brief Convert Local Sidereal Time to Greenwich Sidereal Time
	def LocalSiderealTimeToGreenwichSiderealTime(self, localSiderealTime, geographicalLongitude):
		GST = self.CivilTimeToDecimalHours(localSiderealTime)
		longHours = geographicalLongitude / 15
		GST1 = GST - longHours
		GST2 = GST1 - (24*math.floor(GST1/24))
		
		gstHours = self.DecimalHourHour(GST2)
		gstMinutes = self.DecimalHourMinutes(GST2)
		gstSeconds = self.DecimalHourSeconds(GST2)

		return pa_models.CivilTime(gstHours,gstMinutes,gstSeconds)