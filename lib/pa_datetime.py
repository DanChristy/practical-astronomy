import math
from . import pa_util as PU
from . import pa_datetime_macro as PDM

## @brief Gets the date of Easter for the year specified.
# @param  year  Year for which you'd like the date of Easter.
# @returns  month, day, and year.
def GetDateOfEaster(year):

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
	
	day = p + 1
	month = n

	return month,day,year

## \brief Returns the day number for the date specified.
def CivilDateToDayNumber(month, day, year):
	if month <= 2:
		month = month - 1
		month = month * 62 if PU.IsLeapYear(year) else month * 63
		month = math.floor(month / 2)
	else:
		month = math.floor((month + 1) * 30.6)
		month = month - 62 if PU.IsLeapYear(year) else month - 63
	
	return month + day

## @brief Convert a Greenwich Date/Civil Date (day,month,year) to Julian Date
def GreenwichDateToJulianDate(day, month, year):
	return PDM.CDJD(day,month,year)

## @brief Convert a Julian Date to Greenwich Date/Civil Date (day,month,year)
def JulianDateToGreenwichDate(julianDate):
	returnDay = JulianDateDay(julianDate)
	returnMonth = JulianDateMonth(julianDate)
	returnYear = JulianDateYear(julianDate)

	return returnDay,returnMonth,returnYear

## @brief Returns the day part of a Julian Date
def JulianDateDay(julianDate):
	return PDM.JDCDay(julianDate)

## @brief Returns the month part of a Julian Date
def JulianDateMonth(julianDate):
	return PDM.JDCMonth(julianDate)

## @brief Returns the year part of a Julian Date
def JulianDateYear(julianDate):
	return PDM.JDCYear(julianDate)

## @brief Convert a Julian Date to Day-of-Week (e.g., Sunday)
def JulianDateToWeekdayName(julianDate):
	return PDM.FDOW(julianDate)

## @brief Convert a Civil Time (hours,minutes,seconds) to Decimal Hours
def CivilTimeToDecimalHours(hours,minutes,seconds):
	return PDM.HMSDH(hours,minutes,seconds)

## @brief Return the hour part of a Decimal Hours
def DecimalHourHour(decimalHours):
	return PDM.DHHour(decimalHours)

## @brief Return the minutes part of a Decimal Hours
def DecimalHourMinutes(decimalHours):
	return PDM.DHMin(decimalHours)

## @brief Return the seconds part of a Decimal Hours
def DecimalHourSeconds(decimalHours):
	return PDM.DHSec(decimalHours)

## @brief Convert Decimal Hours to Civil Time
def DecimalHoursToCivilTime(decimalHours):
	hours = PDM.DHHour(decimalHours)
	minutes = PDM.DHMin(decimalHours)
	seconds = PDM.DHSec(decimalHours)

	return hours,minutes,seconds

## @brief Convert local Civil Time to Universal Time
## @returns UT hours, UT mins, UT secs, GW day, GW month, GW year
def LocalCivilTimeToUniversalTime(lctHours,lctMinutes,lctSeconds,isDaylightSavings, zoneCorrection, localDay,localMonth,localYear):
	LCT = CivilTimeToDecimalHours(lctHours,lctMinutes,lctSeconds)
	
	daylightSavingsOffset = 1 if isDaylightSavings == True else 0
	UTinterim = LCT - daylightSavingsOffset - zoneCorrection
	GDayInterim = localDay + (UTinterim / 24)

	JD = PDM.CDJD(GDayInterim,localMonth,localYear)
	
	GDay = JulianDateDay(JD)
	GMonth = JulianDateMonth(JD)
	GYear = JulianDateYear(JD)
	
	UT = 24 * (GDay - math.floor(GDay))
	
	return DecimalHourHour(UT),DecimalHourMinutes(UT),DecimalHourSeconds(UT),math.floor(GDay),GMonth,GYear

## @brief Convert Universal Time to local Civil Time
## @returns LCT hours, LCT minutes, LCT seconds, day, month, year
def UniversalTimeToLocalCivilTime(utHours,utMinutes,utSeconds,isDayLightSavings, zoneCorrection,gwDay,gwMonth,gwYear):
	UT = CivilTimeToDecimalHours(utHours,utMinutes,utSeconds)
	zoneTime = UT + zoneCorrection
	localTime = zoneTime + (1 if isDayLightSavings == True else 0)
	localJDPlusLocalTime = GreenwichDateToJulianDate(gwDay,gwMonth,gwYear) + (localTime/24)
	localDay = JulianDateDay(localJDPlusLocalTime)
	integerDay = math.floor(localDay)
	localMonth = JulianDateMonth(localJDPlusLocalTime)
	localYear = JulianDateYear(localJDPlusLocalTime)
	LCT = 24 * (localDay - integerDay)

	return DecimalHourHour(LCT),DecimalHourMinutes(LCT),DecimalHourSeconds(LCT),integerDay,localMonth,localYear

## @brief Convert Universal Time to Greenwich Sidereal Time
## @returns GST hours, GST minutes, GST seconds
def UniversalTimeToGreenwichSiderealTime(utHours,utMinutes,utSeconds,gwDay,gwMonth,gwYear):
	JD = GreenwichDateToJulianDate(gwDay,gwMonth,gwYear)
	S = JD - 2451545
	T = S / 36525
	T01 = 6.697374558+(2400.051336*T)+(0.000025862*T*T)
	T02 = T01-(24*math.floor(T01/24))
	UT = CivilTimeToDecimalHours(utHours,utMinutes,utSeconds)
	A = UT*1.002737909
	GST1 = T02 + A
	GST2 = GST1 - (24*math.floor(GST1/24))

	gstHours = DecimalHourHour(GST2)
	gstMinutes = DecimalHourMinutes(GST2)
	gstSeconds = DecimalHourSeconds(GST2)
			
	return gstHours,gstMinutes,gstSeconds

## @brief Convert Greenwich Sidereal Time to Universal Time
## @returns UT hours, UT minutes, UT seconds, Warning Flag
def GreenwichSiderealTimeToUniversalTime(gstHours,gstMinutes,gstSeconds,gwDay,gwMonth,gwYear):
	JD = GreenwichDateToJulianDate(gwDay,gwMonth,gwYear)
	S = JD - 2451545
	T = S / 36525
	T01 = 6.697374558 + (2400.051336*T) + (0.000025862*T*T)
	T02 = T01-(24*math.floor(T01/24))
	gstHours = CivilTimeToDecimalHours(gstHours,gstMinutes,gstSeconds)
	A = gstHours-T02
	B = A-(24*math.floor(A/24))
	UT = B*0.9972695663	
	
	utHours = DecimalHourHour(UT)
	utMinutes = DecimalHourMinutes(UT)
	utSeconds = DecimalHourSeconds(UT)
	warningFlag = "Warning" if UT < 0.065574 else "OK"  # TODO: Log this somewhere...

	return utHours,utMinutes,utSeconds,warningFlag

## @brief Convert Greenwich Sidereal Time to Local Sidereal Time
## @returns LST hours, LST minutes, LST seconds
def GreenwichSiderealTimeToLocalSiderealTime(gstHours,gstMinutes,gstSeconds,geographicalLongitude):
	GST = CivilTimeToDecimalHours(gstHours,gstMinutes,gstSeconds)
	offset = geographicalLongitude / 15
	lstHours1 = GST + offset
	lstHours2 = lstHours1-(24*math.floor(lstHours1/24))
	
	lstHours = DecimalHourHour(lstHours2)
	lstMinutes = DecimalHourMinutes(lstHours2)
	lstSeconds = DecimalHourSeconds(lstHours2)

	return lstHours,lstMinutes,lstSeconds

## @brief Convert Local Sidereal Time to Greenwich Sidereal Time
## @returns GST hours, GST minutes, GST seconds
def LocalSiderealTimeToGreenwichSiderealTime(lstHours,lstMinutes,lstSeconds,geographicalLongitude):
	GST = CivilTimeToDecimalHours(lstHours,lstMinutes,lstSeconds)
	longHours = geographicalLongitude / 15
	GST1 = GST - longHours
	GST2 = GST1 - (24*math.floor(GST1/24))
	
	gstHours = DecimalHourHour(GST2)
	gstMinutes = DecimalHourMinutes(GST2)
	gstSeconds = DecimalHourSeconds(GST2)

	return gstHours,gstMinutes,gstSeconds
