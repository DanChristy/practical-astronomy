import math

## @brief Convert a Greenwich Date/Civil Date (day,month,year) to Julian Date
def CDJD(day, month, year):
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

## @brief Returns the day part of a Julian Date
def JDCDay(julianDate):
	I = math.floor(julianDate + 0.5)
	F = julianDate + 0.5 - I
	A = math.floor((I - 1867216.25) / 36524.25)
	B = I + 1 + A - math.floor(A / 4) if I > 2299160 else I
	C = B + 1524
	D = math.floor((C - 122.1) / 365.25)
	E = math.floor(365.25 * D)
	G = math.floor((C - E) / 30.6001)

	return C - E + F - math.floor(30.6001 * G)

## @brief Returns the month part of a Julian Date
def JDCMonth(julianDate):
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

## @brief Returns the year part of a Julian Date
def JDCYear(julianDate):
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

## @brief Convert a Julian Date to Day-of-Week (e.g., Sunday)
def FDOW(julianDate):
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

## @brief Convert a Civil Time (hours,minutes,seconds) to Decimal Hours
def HMSDH(hours,minutes,seconds):
	A = abs(seconds) / 60
	B = (abs(minutes) + A) / 60
	C = abs(hours) + B
	
	return -C if ((hours < 0) or (minutes < 0) or (seconds < 0)) else C

## @brief Return the hour part of a Decimal Hours
def DHHour(decimalHours):
	A = abs(decimalHours)
	B = A * 3600
	C = round(B - 60 * math.floor(B / 60), 2)
	D = 0 if C == 60 else C
	E = B + 60 if C == 60 else B

	return -(math.floor(E / 3600)) if decimalHours < 0 else math.floor(E / 3600)

## @brief Return the minutes part of a Decimal Hours
def DHMin(decimalHours):
	A = abs(decimalHours)
	B = A * 3600
	C = round(B - 60 * math.floor(B / 60), 2)
	D = 0 if C == 60 else C
	E = B + 60 if C == 60 else B

	return math.floor(E / 60) % 60

## @brief Return the seconds part of a Decimal Hours
def DHSec(decimalHours):
	A = abs(decimalHours)
	B = A * 3600
	C = round(B - 60 * math.floor(B / 60), 2)
	D = 0 if C == 60 else C

	return D

## @brief Convert Local Civil Time to Universal Time
def LctUT(lctHours,lctMinutes,lctSeconds,daylightSaving,zoneCorrection,localDay,localMonth,localYear):
	A = HMSDH(lctHours,lctMinutes,lctSeconds)
	B = A - daylightSaving - zoneCorrection
	C = localDay + (B/24)
	D = CDJD(C, localMonth, localYear)
	E = JDCDay(D)
	E1 = math.floor(E)
	
	return 24 * (E - E1)

## @brief Convert Universal Time to Local Civil Time
def UTLct(uHours,uMinutes,uSeconds,daylightSaving,zoneCorrection,greenwichDay,greenwichMonth,greenwichYear):
	A = HMSDH(uHours,uMinutes,uSeconds)
	B = A + zoneCorrection
	C = B + daylightSaving
	D = CDJD(greenwichDay,greenwichMonth,greenwichYear) + (C / 24)
	E = JDCDay(D)
	E1 = math.floor(E)
	
	return 24 * (E - E1)

## @brief Get Local Civil Day for Universal Time
def UTLcDay(uHours,uMinutes,uSeconds,daylightSaving,zoneCorrection,greenwichDay,greenwichMonth,greenwichYear):
	A = HMSDH(uHours,uMinutes,uSeconds)
	B = A + zoneCorrection
	C = B + daylightSaving
	D = CDJD(greenwichDay,greenwichMonth,greenwichYear) + (C / 24)
	E = JDCDay(D)
	E1 = math.floor(E)
	
	return E1

## @brief Get Local Civil Month for Universal Time
def UTLcMonth(uHours,uMinutes,uSeconds,daylightSaving,zoneCorrection,greenwichDay,greenwichMonth,greenwichYear):
	A = HMSDH(uHours,uMinutes,uSeconds)
	B = A + zoneCorrection
	C = B + daylightSaving
	D = CDJD(greenwichDay,greenwichMonth,greenwichYear) + (C / 24)
	
	return JDCMonth(D)

## @brief Get Local Civil Year for Universal Time
def UTLcYear(uHours,uMinutes,uSeconds,daylightSaving,zoneCorrection,greenwichDay,greenwichMonth,greenwichYear):
	A = HMSDH(uHours,uMinutes,uSeconds)
	B = A + zoneCorrection
	C = B + daylightSaving
	D = CDJD(greenwichYear,greenwichMonth,greenwichYear) + (C / 24)
	
	return JDCYear(D)

## @brief Determine Greenwich Day for Local Time
def LctGDay(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year):
	A = HMSDH(lct_hours,lct_minutes,lct_seconds)
	B = A - daylight_saving - zone_correction
	C = local_day + (B/24)
	D = CDJD(C,local_month,local_year)
	E = JDCDay(D)
	
	return math.floor(E)

## @brief Determine Greenwich Month for Local Time
def LctGMonth(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year):
	A = HMSDH(lct_hours,lct_minutes,lct_seconds)
	B = A - daylight_saving - zone_correction
	C = local_day + (B/24)
	D = CDJD(C,local_month,local_year)
	
	return JDCMonth(D)

## @brief Determine Greenwich Year for Local Time
def LctGYear(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year):
	A = HMSDH(lct_hours,lct_minutes,lct_seconds)
	B = A - daylight_saving - zone_correction
	C = local_day + (B/24)
	D = CDJD(C,local_month,local_year)
	
	return JDCYear(D)

## @brief Convert Universal Time to Greenwich Sidereal Time
def UTGST(u_hours,u_minutes,u_seconds,greenwich_day,greenwich_month,greenwich_year):
	A = CDJD(greenwich_day,greenwich_month,greenwich_year)
	B = A - 2451545
	C = B / 36525
	D = 6.697374558 + (2400.051336 * C) + (0.000025862 * C * C)
	E = D - (24 * math.floor(D / 24))
	F = HMSDH(u_hours,u_minutes,u_seconds)
	G = F * 1.002737909
	H = E + G
	
	return H - (24 * math.floor(H / 24))

## @brief Convert Greenwich Sidereal Time to Local Sidereal Time
def GSTLST(greenwich_hours,greenwich_minutes,greenwich_seconds,geographical_longitude):
	A = HMSDH(greenwich_hours,greenwich_minutes,greenwich_seconds)
	B = geographical_longitude / 15
	C = A + B

	return C - (24 * math.floor(C / 24))

## @brief Convert Right Ascension to Hour Angle
def RAHA(ra_hours, ra_minutes, ra_seconds, lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year, geographical_longitude):
	A = LctUT(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year)
	B = LctGDay(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year)
	C = LctGMonth(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year)
	D = LctGYear(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year)
	E = UTGST(A, 0, 0, B, C, D)
	F = GSTLST(E, 0, 0, geographical_longitude)
	G = HMSDH(ra_hours, ra_minutes, ra_seconds)
	H = F - G
	
	return 24 + H if H < 0 else H

## @brief Convert Hour Angle to Right Ascension
def HARA(hour_angle_hours,hour_angle_minutes,hour_angle_seconds,lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year,geographical_longitude):
	A = LctUT(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year)
	B = LctGDay(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year)
	C = LctGMonth(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year)
	D = LctGYear(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year)
	E = UTGST(A, 0, 0, B, C, D)
	F = GSTLST(E, 0, 0, geographical_longitude)
	G = HMSDH(hour_angle_hours,hour_angle_minutes,hour_angle_seconds)
	H = F - G

	return 24 + H if H < 0 else H

## @brief Convert Degrees Minutes Seconds to Decimal Degrees
def DMSDD(degrees,minutes,seconds):
	A = abs(seconds) / 60
	B = (abs(minutes) + A) / 60
	C = abs(degrees) + B

	return -C if degrees < 0 or minutes < 0 or seconds < 0 else C

## @brief Return Degrees part of Decimal Degrees
def DDDeg(decimal_degrees):
	A = abs(decimal_degrees)
	B = A * 3600
	C = round(B - 60 * math.floor(B / 60),2)
	D = 0 if C == 60 else C
	E = B = 60 if C == 60 else B

	return -math.floor(E/3600) if decimal_degrees < 0 else math.floor(E/3600)

## @brief Return Minutes part of Decimal Degrees
def DDMin(decimal_degrees):
	A = abs(decimal_degrees)
	B = A * 3600
	C = round(B - 60 * math.floor(B / 60),2)
	D = 0 if C == 60 else C
	E = B = 60 if C == 60 else B

	return math.floor(E/60) % 60

## @brief Return Seconds part of Decimal Degrees
def DDSec(decimal_degrees):
	A = abs(decimal_degrees)
	B = A * 3600
	C = round(B - 60 * math.floor(B / 60),2)
	D = 0 if C == 60 else C

	return D

## @brief Convert Decimal Degrees to Degree-Hours
def DDDH(decimal_degrees):
	return decimal_degrees / 15

## @brief Convert Degree-Hours to Decimal Degrees
def DHDD(degree_hours):
	return degree_hours * 15

## @brief Convert W to Degrees
def Degrees(W):
	return W * 57.29577951

## @brief Custom ATAN2 function
def Atan2(X, Y):
	B = 3.1415926535
	if abs(X) < 1e-20:
		if Y < 0:
			A = -B / 2
		else:
			A = B / 2
	else:
		A = math.atan(Y/X)

	if X < 0:
		A = B + A
	
	if A < 0:
		A = A + 2 * B

	return A

## @brief Convert Equatorial Coordinates to Azimuth (in decimal degrees)
def EQAz(hour_angle_hours,hour_angle_minutes,hour_angle_seconds,declination_degrees,declination_minutes,declination_seconds,geographical_latitude):
	A = HMSDH(hour_angle_hours,hour_angle_minutes,hour_angle_seconds)
	B = A * 15
	C = math.radians(B)
	D = DMSDD(declination_degrees,declination_minutes,declination_seconds)
	E = math.radians(D)
	F = math.radians(geographical_latitude)
	G = math.sin(E) * math.sin(F) + math.cos(E) * math.cos(F) * math.cos(C)
	H = -math.cos(E) * math.cos(F) * math.sin(C)
	I = math.sin(E) - (math.sin(F) * G)
	J = Degrees(Atan2(I,H))
	
	return J - 360 * math.floor(J / 360)

## @brief Convert Equatorial Coordinates to Altitude (in decimal degrees)
def EQAlt(hour_angle_hours,hour_angle_minutes,hour_angle_seconds,declination_degrees,declination_minutes,declination_seconds,geographical_latitude):
	A = HMSDH(hour_angle_hours,hour_angle_minutes,hour_angle_seconds)
	B = A * 15
	C = math.radians(B)
	D = DMSDD(declination_degrees,declination_minutes,declination_seconds)
	E = math.radians(D)
	F = math.radians(geographical_latitude)
	G = math.sin(E) * math.sin(F) + math.cos(E) * math.cos(F) * math.cos(C)

	return Degrees(math.asin(G))

## @brief Convert Horizon Coordinates to Declination (in decimal degrees)
def HORDec(azimuth_degrees,azimuth_minutes,azimuth_seconds,altitude_degrees,altitude_minutes,altitude_seconds,geographical_latitude):
	A = DMSDD(azimuth_degrees,azimuth_minutes,azimuth_seconds)
	B = DMSDD(altitude_degrees,altitude_minutes,altitude_seconds)
	C = math.radians(A)
	D = math.radians(B)
	E = math.radians(geographical_latitude)
	F = math.sin(D) * math.sin(E) + math.cos(D) * math.cos(E) * math.cos(C)
	
	return Degrees(math.asin(F))

## @brief Convert Horizon Coordinates to Hour Angle (in decimal degrees)
def HORHa(azimuth_degrees,azimuth_minutes,azimuth_seconds,altitude_degrees,altitude_minutes,altitude_seconds,geographical_latitude):
	A = DMSDD(azimuth_degrees,azimuth_minutes,azimuth_seconds)
	B = DMSDD(altitude_degrees,altitude_minutes,altitude_seconds)
	C = math.radians(A)
	D = math.radians(B)
	E = math.radians(geographical_latitude)
	F = math.sin(D) * math.sin(E) + math.cos(D) * math.cos(E) * math.cos(C)
	G = -math.cos(D) * math.cos(E) * math.sin(C)
	H = math.sin(D) - math.sin(E) * F
	I = DDDH(Degrees(Atan2(H, G)))
	
	return I - 24 * math.floor(I / 24)

## @brief Nutation of Obliquity
def NutatObl(greenwich_day,greenwich_month,greenwich_year):
	DJ = CDJD(greenwich_day,greenwich_month,greenwich_year) - 2415020
	T = DJ / 36525
	T2 = T * T

	A = 100.0021358 * T
	B = 360 * (A - math.floor(A))

	L1 = 279.6967 + 0.000303 * T2 + B
	l2 = 2 * math.radians(L1)

	A = 1336.855231 * T
	B = 360 * (A - math.floor(A))

	D1 = 270.4342 - 0.001133 * T2 + B
	D2 = 2 * math.radians(D1)

	A = 99.99736056 * T
	B = 360 * (A - math.floor(A))

	M1 = 358.4758 - 0.00015 * T2 + B
	M1 = math.radians(M1)

	A = 1325.552359 * T
	B = 360 * (A - math.floor(A))

	M2 = 296.1046 + 0.009192 * T2 + B
	M2 = math.radians(M2)

	A = 5.372616667 * T
	B = 360 * (A - math.floor(A))

	N1 = 259.1833 + 0.002078 * T2 - B
	N1 = math.radians(N1)

	N2 = 2 * N1

	DDO = (9.21 + 0.00091 * T) * math.cos(N1)
	DDO = DDO + (0.5522 - 0.00029 * T) * math.cos(l2) - 0.0904 * math.cos(N2)
	DDO = DDO + 0.0884 * math.cos(D2) + 0.0216 * math.cos(l2 + M1)
	DDO = DDO + 0.0183 * math.cos(D2 - N1) + 0.0113 * math.cos(D2 + M2)
	DDO = DDO - 0.0093 * math.cos(l2 - M1) - 0.0066 * math.cos(l2 - N1)

	return DDO / 3600

## @brief Obliquity of the Ecliptic for a Greenwich Date
def Obliq(greenwich_day,greenwich_month,greenwich_year):
	A = CDJD(greenwich_day,greenwich_month,greenwich_year)
	B = A - 2415020
	C = (B / 36525) - 1
	D = C * (46.815 + C * (0.0006 - (C * 0.00181)))
	E = D / 3600
	
	return 23.43929167 - E + NutatObl(greenwich_day,greenwich_month,greenwich_year)
