import math

## @brief Convert a Greenwich Date/Civil Date (day,month,year) to Julian Date
def cd_jd(day, month, year):
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
def jdc_day(julianDate):
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
def jdc_month(julianDate):
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
def jdc_year(julianDate):
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
def f_dow(julianDate):
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
def hms_dh(hours,minutes,seconds):
	A = abs(seconds) / 60
	B = (abs(minutes) + A) / 60
	C = abs(hours) + B
	
	return -C if ((hours < 0) or (minutes < 0) or (seconds < 0)) else C

## @brief Return the hour part of a Decimal Hours
def dh_hour(decimalHours):
	A = abs(decimalHours)
	B = A * 3600
	C = round(B - 60 * math.floor(B / 60), 2)
	D = 0 if C == 60 else C
	E = B + 60 if C == 60 else B

	return -(math.floor(E / 3600)) if decimalHours < 0 else math.floor(E / 3600)

## @brief Return the minutes part of a Decimal Hours
def dh_min(decimalHours):
	A = abs(decimalHours)
	B = A * 3600
	C = round(B - 60 * math.floor(B / 60), 2)
	D = 0 if C == 60 else C
	E = B + 60 if C == 60 else B

	return math.floor(E / 60) % 60

## @brief Return the seconds part of a Decimal Hours
def dh_sec(decimalHours):
	A = abs(decimalHours)
	B = A * 3600
	C = round(B - 60 * math.floor(B / 60), 2)
	D = 0 if C == 60 else C

	return D

## @brief Convert Local Civil Time to Universal Time
def lct_ut(lctHours,lctMinutes,lctSeconds,daylightSaving,zoneCorrection,localDay,localMonth,localYear):
	A = hms_dh(lctHours,lctMinutes,lctSeconds)
	B = A - daylightSaving - zoneCorrection
	C = localDay + (B/24)
	D = cd_jd(C, localMonth, localYear)
	E = jdc_day(D)
	E1 = math.floor(E)
	
	return 24 * (E - E1)

## @brief Convert Universal Time to Local Civil Time
def ut_lct(uHours,uMinutes,uSeconds,daylightSaving,zoneCorrection,greenwichDay,greenwichMonth,greenwichYear):
	A = hms_dh(uHours,uMinutes,uSeconds)
	B = A + zoneCorrection
	C = B + daylightSaving
	D = cd_jd(greenwichDay,greenwichMonth,greenwichYear) + (C / 24)
	E = jdc_day(D)
	E1 = math.floor(E)
	
	return 24 * (E - E1)

## @brief Get Local Civil Day for Universal Time
def ut_lc_day(uHours,uMinutes,uSeconds,daylightSaving,zoneCorrection,greenwichDay,greenwichMonth,greenwichYear):
	A = hms_dh(uHours,uMinutes,uSeconds)
	B = A + zoneCorrection
	C = B + daylightSaving
	D = cd_jd(greenwichDay,greenwichMonth,greenwichYear) + (C / 24)
	E = jdc_day(D)
	E1 = math.floor(E)
	
	return E1

## @brief Get Local Civil Month for Universal Time
def ut_lc_month(uHours,uMinutes,uSeconds,daylightSaving,zoneCorrection,greenwichDay,greenwichMonth,greenwichYear):
	A = hms_dh(uHours,uMinutes,uSeconds)
	B = A + zoneCorrection
	C = B + daylightSaving
	D = cd_jd(greenwichDay,greenwichMonth,greenwichYear) + (C / 24)
	
	return jdc_month(D)

## @brief Get Local Civil Year for Universal Time
def ut_lc_year(uHours,uMinutes,uSeconds,daylightSaving,zoneCorrection,greenwichDay,greenwichMonth,greenwichYear):
	A = hms_dh(uHours,uMinutes,uSeconds)
	B = A + zoneCorrection
	C = B + daylightSaving
	D = cd_jd(greenwichYear,greenwichMonth,greenwichYear) + (C / 24)
	
	return jdc_year(D)

## @brief Determine Greenwich Day for Local Time
def lct_gday(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year):
	A = hms_dh(lct_hours,lct_minutes,lct_seconds)
	B = A - daylight_saving - zone_correction
	C = local_day + (B/24)
	D = cd_jd(C,local_month,local_year)
	E = jdc_day(D)
	
	return math.floor(E)

## @brief Determine Greenwich Month for Local Time
def lct_gmonth(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year):
	A = hms_dh(lct_hours,lct_minutes,lct_seconds)
	B = A - daylight_saving - zone_correction
	C = local_day + (B/24)
	D = cd_jd(C,local_month,local_year)
	
	return jdc_month(D)

## @brief Determine Greenwich Year for Local Time
def lct_gyear(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year):
	A = hms_dh(lct_hours,lct_minutes,lct_seconds)
	B = A - daylight_saving - zone_correction
	C = local_day + (B/24)
	D = cd_jd(C,local_month,local_year)
	
	return jdc_year(D)

## @brief Convert Universal Time to Greenwich Sidereal Time
def ut_gst(u_hours,u_minutes,u_seconds,greenwich_day,greenwich_month,greenwich_year):
	A = cd_jd(greenwich_day,greenwich_month,greenwich_year)
	B = A - 2451545
	C = B / 36525
	D = 6.697374558 + (2400.051336 * C) + (0.000025862 * C * C)
	E = D - (24 * math.floor(D / 24))
	F = hms_dh(u_hours,u_minutes,u_seconds)
	G = F * 1.002737909
	H = E + G
	
	return H - (24 * math.floor(H / 24))

## @brief Convert Greenwich Sidereal Time to Local Sidereal Time
def gst_lst(greenwich_hours,greenwich_minutes,greenwich_seconds,geographical_longitude):
	A = hms_dh(greenwich_hours,greenwich_minutes,greenwich_seconds)
	B = geographical_longitude / 15
	C = A + B

	return C - (24 * math.floor(C / 24))

## @brief Convert Local Sidereal Time to Greenwich Sidereal Time
def lst_gst(local_hours,local_minutes,local_seconds,longitude):
	A = hms_dh(local_hours,local_minutes,local_seconds)
	B = longitude / 15
	C = A - B
	
	return C - (24 * math.floor(C / 24))

## @brief Convert Greenwich Sidereal Time to Universal Time
def gst_ut(greenwich_sidereal_hours,greenwich_sidereal_minutes,greenwich_sidereal_seconds,greenwich_day,greenwich_month,greenwich_year):
	A = cd_jd(greenwich_day,greenwich_month,greenwich_year)
	B = A - 2451545
	C = B / 36525
	D = 6.697374558 + (2400.051336 * C) + (0.000025862 * C * C)
	E = D - (24 * math.floor(D / 24))
	F = hms_dh(greenwich_sidereal_hours,greenwich_sidereal_minutes,greenwich_sidereal_seconds)
	G = F - E
	H = G - (24 * math.floor(G / 24))
	
	return H * 0.9972695663

## @brief Status of conversion of Greenwich Sidereal Time to Universal Time.
# Original macro name: eGSTUT
def e_gst_ut(GSH, GSM, GSS, GD, GM, GY):
	A = cd_jd(GD, GM, GY)
	B = A - 2451545
	C = B / 36525
	D = 6.697374558 + (2400.051336 * C) + (0.000025862 * C * C)
	E = D - (24 * math.floor(D / 24))
	F = hms_dh(GSH, GSM, GSS)
	G = F - E
	H = G - (24 * math.floor(G / 24))

	return "Warning" if ((H * 0.9972695663) < (4 / 60)) else "OK"

## @brief Convert Right Ascension to Hour Angle
def ra_ha(ra_hours, ra_minutes, ra_seconds, lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year, geographical_longitude):
	A = lct_ut(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year)
	B = lct_gday(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year)
	C = lct_gmonth(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year)
	D = lct_gyear(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year)
	E = ut_gst(A, 0, 0, B, C, D)
	F = gst_lst(E, 0, 0, geographical_longitude)
	G = hms_dh(ra_hours, ra_minutes, ra_seconds)
	H = F - G
	
	return 24 + H if H < 0 else H

## @brief Convert Hour Angle to Right Ascension
def ha_ra(hour_angle_hours,hour_angle_minutes,hour_angle_seconds,lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year,geographical_longitude):
	A = lct_ut(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year)
	B = lct_gday(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year)
	C = lct_gmonth(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year)
	D = lct_gyear(lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year)
	E = ut_gst(A, 0, 0, B, C, D)
	F = gst_lst(E, 0, 0, geographical_longitude)
	G = hms_dh(hour_angle_hours,hour_angle_minutes,hour_angle_seconds)
	H = F - G

	return 24 + H if H < 0 else H

## @brief Convert Degrees Minutes Seconds to Decimal Degrees
def dms_dd(degrees,minutes,seconds):
	A = abs(seconds) / 60
	B = (abs(minutes) + A) / 60
	C = abs(degrees) + B

	return -C if degrees < 0 or minutes < 0 or seconds < 0 else C

## @brief Return Degrees part of Decimal Degrees
def dd_deg(decimal_degrees):
	A = abs(decimal_degrees)
	B = A * 3600
	C = round(B - 60 * math.floor(B / 60),2)
	D = 0 if C == 60 else C
	E = B = 60 if C == 60 else B

	return -math.floor(E/3600) if decimal_degrees < 0 else math.floor(E/3600)

## @brief Return Minutes part of Decimal Degrees
def dd_min(decimal_degrees):
	A = abs(decimal_degrees)
	B = A * 3600
	C = round(B - 60 * math.floor(B / 60),2)
	D = 0 if C == 60 else C
	E = B + 60 if C == 60 else B

	return math.floor(E/60) % 60

## @brief Return Seconds part of Decimal Degrees
def dd_sec(decimal_degrees):
	A = abs(decimal_degrees)
	B = A * 3600
	C = round(B - 60 * math.floor(B / 60),2)
	D = 0 if C == 60 else C

	return D

## @brief Convert Decimal Degrees to Degree-Hours
def dd_dh(decimal_degrees):
	return decimal_degrees / 15

## @brief Convert Degree-Hours to Decimal Degrees
def dh_dd(degree_hours):
	return degree_hours * 15

## @brief Convert W to Degrees
def degrees(W):
	return W * 57.29577951

## @brief Custom ATAN2 function
def atan2(X, Y):
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
def eq_az(hour_angle_hours,hour_angle_minutes,hour_angle_seconds,declination_degrees,declination_minutes,declination_seconds,geographical_latitude):
	A = hms_dh(hour_angle_hours,hour_angle_minutes,hour_angle_seconds)
	B = A * 15
	C = math.radians(B)
	D = dms_dd(declination_degrees,declination_minutes,declination_seconds)
	E = math.radians(D)
	F = math.radians(geographical_latitude)
	G = math.sin(E) * math.sin(F) + math.cos(E) * math.cos(F) * math.cos(C)
	H = -math.cos(E) * math.cos(F) * math.sin(C)
	I = math.sin(E) - (math.sin(F) * G)
	J = degrees(atan2(I,H))
	
	return J - 360 * math.floor(J / 360)

## @brief Convert Equatorial Coordinates to Altitude (in decimal degrees)
def eq_alt(hour_angle_hours,hour_angle_minutes,hour_angle_seconds,declination_degrees,declination_minutes,declination_seconds,geographical_latitude):
	A = hms_dh(hour_angle_hours,hour_angle_minutes,hour_angle_seconds)
	B = A * 15
	C = math.radians(B)
	D = dms_dd(declination_degrees,declination_minutes,declination_seconds)
	E = math.radians(D)
	F = math.radians(geographical_latitude)
	G = math.sin(E) * math.sin(F) + math.cos(E) * math.cos(F) * math.cos(C)

	return degrees(math.asin(G))

## @brief Convert Horizon Coordinates to Declination (in decimal degrees)
def hor_dec(azimuth_degrees,azimuth_minutes,azimuth_seconds,altitude_degrees,altitude_minutes,altitude_seconds,geographical_latitude):
	A = dms_dd(azimuth_degrees,azimuth_minutes,azimuth_seconds)
	B = dms_dd(altitude_degrees,altitude_minutes,altitude_seconds)
	C = math.radians(A)
	D = math.radians(B)
	E = math.radians(geographical_latitude)
	F = math.sin(D) * math.sin(E) + math.cos(D) * math.cos(E) * math.cos(C)
	
	return degrees(math.asin(F))

## @brief Convert Horizon Coordinates to Hour Angle (in decimal degrees)
def hor_ha(azimuth_degrees,azimuth_minutes,azimuth_seconds,altitude_degrees,altitude_minutes,altitude_seconds,geographical_latitude):
	A = dms_dd(azimuth_degrees,azimuth_minutes,azimuth_seconds)
	B = dms_dd(altitude_degrees,altitude_minutes,altitude_seconds)
	C = math.radians(A)
	D = math.radians(B)
	E = math.radians(geographical_latitude)
	F = math.sin(D) * math.sin(E) + math.cos(D) * math.cos(E) * math.cos(C)
	G = -math.cos(D) * math.cos(E) * math.sin(C)
	H = math.sin(D) - math.sin(E) * F
	I = dd_dh(degrees(atan2(H, G)))
	
	return I - 24 * math.floor(I / 24)

## @brief Nutation of Obliquity
def nutat_obl(greenwich_day,greenwich_month,greenwich_year):
	DJ = cd_jd(greenwich_day,greenwich_month,greenwich_year) - 2415020
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
def obliq(greenwich_day,greenwich_month,greenwich_year):
	A = cd_jd(greenwich_day,greenwich_month,greenwich_year)
	B = A - 2415020
	C = (B / 36525) - 1
	D = C * (46.815 + C * (0.0006 - (C * 0.00181)))
	E = D / 3600
	
	return 23.43929167 - E + nutat_obl(greenwich_day,greenwich_month,greenwich_year)

## @brief Calculate Sun's ecliptic longitude
def sun_long(LCH,LCM,LCS,DS,ZC,LD,LM,LY):
	AA = lct_gday(LCH, LCM, LCS, DS, ZC, LD, LM, LY)
	BB = lct_gmonth(LCH, LCM, LCS, DS, ZC, LD, LM, LY)
	CC = lct_gyear(LCH, LCM, LCS, DS, ZC, LD, LM, LY)
	UT = lct_ut(LCH, LCM, LCS, DS, ZC, LD, LM, LY)
	DJ = cd_jd(AA, BB, CC) - 2415020
	T = (DJ / 36525) + (UT / 876600)
	T2 = T * T
	A = 100.0021359 * T
	B = 360 * (A - math.floor(A))
	
	L = 279.69668 + 0.0003025 * T2 + B
	A = 99.99736042 * T
	B = 360 * (A - math.floor(A))
	
	M1 = 358.47583 - (0.00015 + 0.0000033 * T) * T2 + B
	EC = 0.01675104 - 0.0000418 * T - 0.000000126 * T2

	AM = math.radians(M1)
	AT = true_anomaly(AM, EC)
	AE = eccentric_anomaly(AM, EC)

	A = 62.55209472 * T
	B = 360 * (A - math.floor(A))

	A1 = math.radians(153.23 + B)
	A = 125.1041894 * T
	B = 360 * (A - math.floor(A))

	B1 = math.radians(216.57 + B)
	A = 91.56766028 * T
	B = 360 * (A - math.floor(A))

	C1 = math.radians(312.69 + B)
	A = 1236.853095 * T
	B = 360 * (A - math.floor(A))

	D1 = math.radians(350.74 - 0.00144 * T2 + B)
	E1 = math.radians(231.19 + 20.2 * T)
	A = 183.1353208 * T
	B = 360 * (A - math.floor(A))
	H1 = math.radians(353.4 + B)

	D2 = 0.00134 * math.cos(A1) + 0.00154 * math.cos(B1) + 0.002 * math.cos(C1)
	D2 = D2 + 0.00179 * math.sin(D1) + 0.00178 * math.sin(E1)
	D3 = 0.00000543 * math.sin(A1) + 0.00001575 * math.sin(B1)
	D3 = D3 + 0.00001627 * math.sin(C1) + 0.00003076 * math.cos(D1)
	D3 = D3 + 0.00000927 * math.sin(H1)

	SR = AT + math.radians(L - M1 + D2)
	TP = 6.283185308

	SR = SR - TP * math.floor(SR / TP)

	return degrees(SR)

## @brief Calculate Sun's distance from the Earth in astronomical units
def sun_dist(LCH,LCM,LCS,DS,ZC,LD,LM,LY):
	AA = lct_gday(LCH,LCM,LCS,DS,ZC,LD,LM,LY)
	BB = lct_gmonth(LCH,LCM,LCS,DS,ZC,LD,LM,LY)
	CC = lct_gyear(LCH,LCM,LCS,DS,ZC,LD,LM,LY)
	UT = lct_ut(LCH,LCM,LCS,DS,ZC,LD,LM,LY)
	DJ = cd_jd(AA,BB,CC) - 2415020
	
	T = (DJ / 36525) + (UT / 876600)
	T2 = T * T

	A = 100.0021359 * T
	B = 360 * (A - math.floor(A))
	L = 279.69668 + 0.0003025 * T2 + B
	A = 99.99736042 * T
	B = 360 * (A - math.floor(A))
	M1 = 358.47583 - (0.00015 + 0.0000033 * T) * T2 + B
	EC = 0.01675104 - 0.0000418 * T - 0.000000126 * T2

	AM = math.radians(M1)
	AT = true_anomaly(AM,EC)
	AE = eccentric_anomaly(AM, EC)

	A = 62.55209472 * T
	B = 360 * (A - math.floor(A))
	A1 = math.radians(153.23 + B)
	A = 125.1041894 * T
	B = 360 * (A - math.floor(A))
	B1 = math.radians(216.57 + B)
	A = 91.56766028 * T
	B = 360 * (A - math.floor(A))
	C1 = math.radians(312.69 + B)
	A = 1236.853095 * T
	B = 360 * (A - math.floor(A))
	D1 = math.radians(350.74 - 0.00144 * T2 + B)
	E1 = math.radians(231.19 + 20.2 * T)
	A = 183.1353208 * T
	B = 360 * (A - math.floor(A))
	H1 = math.radians(353.4 + B)

	D2 = 0.00134 * math.cos(A1) + 0.00154 * math.cos(B1) + 0.002 * math.cos(C1)
	D2 = D2 + 0.00179 * math.sin(D1) + 0.00178 * math.sin(E1)
	D3 = 0.00000543 * math.sin(A1) + 0.00001575 * math.sin(B1)
	D3 = D3 + 0.00001627 * math.sin(C1) + 0.00003076 * math.cos(D1)
	D3 = D3 + 0.00000927 * math.sin(H1)

	return 1.0000002 * (1 - EC * math.cos(AE)) + D3

## @brief Calculate Sun's angular diameter in decimal degrees
def sun_dia(LCH,LCM,LCS,DS,ZC,LD,LM,LY):
	A = sun_dist(LCH, LCM, LCS, DS, ZC, LD, LM, LY)
	
	return 0.533128 / A

## @brief Solve Kepler's equation, and return value of the true anomaly in radians
def true_anomaly(AM,EC):
	TP = 6.283185308
	M = AM - TP * math.floor(AM / TP)
	AE = M

	while 1 == 1:
		D = AE - (EC * math.sin(AE)) - M
		if abs(D) < 0.000001:
			break
		D = D / (1 - (EC * math.cos(AE)))
		AE = AE - D

	A = math.sqrt((1 + EC) / (1 - EC)) * math.tan(AE / 2)
	AT = 2 * math.atan(A)

	return AT

## @brief Solve Kepler's equation, and return value of the eccentric anomaly in radians
def eccentric_anomaly(AM,EC):
	TP = 6.283185308
	M = AM - TP * math.floor(AM / TP)
	AE = M

	while 1 == 1:
		D = AE - (EC * math.sin(AE)) - M

		if abs(D) < 0.000001:
			break

		D = D / (1 - (EC * math.cos(AE)))
		AE = AE - D

	return AE

## @brief Calculate effects of refraction
def refract(Y2,SW,PR,TR):
	Y = math.radians(Y2)
	
	D = -1 if SW[0].lower() == "t" else 1

	if D == -1:
		Y3 = Y
		Y1 = Y
		R1 = 0

		while 1 == 1:
			Y = Y1 + R1
			Q = Y
			
			RF = refract_l3035(PR,TR,Y,D)

			if Y < -0.087:
				return 0
			
			R2 = RF

			if (R2 == 0) or (abs(R2 - R1) < 0.000001):
				Q = Y3
				return degrees(Q + RF)

			R1 = R2

	RF = refract_l3035(PR,TR,Y,D)

	if Y < -0.087:
		return 0

	Q = Y

	return degrees(Q + RF)

## @brief Helper function for refract
def refract_l3035(PR,TR,Y,D):
	if Y < 0.2617994:
		if Y < -0.087:
			return 0

		YD = degrees(Y)
		A = ((0.00002 * YD + 0.0196) * YD + 0.1594) * PR
		B = (273 + TR) * ((0.0845 * YD + 0.505) * YD + 1)

		return math.radians(-(A / B) * D)

	return -D * 0.00007888888 * PR / ((273 + TR) * math.tan(Y))

## @brief Calculate corrected hour angle in decimal hours
def parallax_ha(HH,HM,HS,DD,DM,DS,SW,GP,HT,HP):
	A = math.radians(GP)
	C1 = math.cos(A)
	S1 = math.sin(A)

	U = math.atan(0.996647 * S1 / C1)
	
	C2 = math.cos(U)
	S2 = math.sin(U)
	B = HT / 6378160

	RS = (0.996647 * S2) + (B * S1)
	
	RC = C2 + (B * C1)
	TP = 6.283185308

	RP = 1 / math.sin(math.radians(HP))

	X = math.radians(dh_dd(hms_dh(HH, HM, HS)))
	X1 = X

	Y = math.radians(dms_dd(DD, DM, DS))
	Y1 = Y

	D = 1 if SW[0].lower() == "t" else -1

	if D == 1:
		P,Q = parallax_ha_l2870(X,Y,RC,RP,RS,TP)
		return dd_dh(degrees(P))

	P1 = 0
	Q1 = 0
	while 1==1:
		P,Q = parallax_ha_l2870(X,Y,RC,RP,RS,TP)
		
		P2 = P - X
		Q2 = Q - Y

		AA = abs(P2 - P1)
		BB = abs(Q2 - Q1)

		if (AA < 0.000001) and (BB < 0.000001):
			P = X1 - P2
			Q = Y1 - Q2
			X = X1
			Y = Y1
			return dd_dh(degrees(P))
		
		X = X1 - P2
		Y = Y1 - Q2
		P1 = P2
		Q1 = Q2

## @brief Helper function for parallax_ha
def parallax_ha_l2870(X,Y,RC,RP,RS,TP):
	CX = math.cos(X)
	SY = math.sin(Y)
	CY = math.cos(Y)

	AA = (RC * math.sin(X)) / ((RP * CY) - (RC * CX))
	
	DX = math.atan(AA)
	P = X + DX
	CP = math.cos(P)

	P = P - TP * math.floor(P / TP)
	Q = math.atan(CP * (RP * SY - RS) / (RP * CY * CX - RC))

	return P,Q

## @brief Calculate corrected declination in decimal degrees
def parallax_dec(HH,HM,HS,DD,DM,DS,SW,GP,HT,HP):
	A = math.radians(GP)
	C1 = math.cos(A)
	S1 = math.sin(A)

	U = math.atan(0.996647 * S1 / C1)
	
	C2 = math.cos(U)
	S2 = math.sin(U)
	B = HT / 6378160
	RS = (0.996647 * S2) + (B * S1)
	
	RC = C2 + (B * C1)
	TP = 6.283185308

	RP = 1 / math.sin(math.radians(HP))

	X = math.radians(dh_dd(hms_dh(HH, HM, HS)))
	X1 = X

	Y = math.radians(dms_dd(DD, DM, DS))
	Y1 = Y

	D = 1 if SW[0].lower() == "t" else -1

	if D == 1:
		P,Q = parallax_dec_l2870(X,Y,RC,RP,RS,TP)
		return degrees(Q)

	P1 = 0
	Q1 = 0

	while 1 == 1:
		P,Q = parallax_dec_l2870(X,Y,RC,RP,RS,TP)
		
		P2 = P - X
		Q2 = Q - Y

		AA = abs(P2 - P1)
		BB = abs(Q2 - Q1)

		if (AA < 0.000001) and (BB < 0.000001):
			P = X1 - P2
			Q = Y1 - Q2
			X = X1
			Y = Y1
			return degrees(Q)
		
		X = X1 - P2
		Y = Y1 - Q2
		P1 = P2
		Q1 = Q2

## @brief Helper function for parallax_dec
def parallax_dec_l2870(X,Y,RC,RP,RS,TP):
	CX = math.cos(X)
	SY = math.sin(Y)
	CY = math.cos(Y)

	AA = (RC * math.sin(X)) / ((RP * CY) - (RC * CX))
	
	DX = math.atan(AA)
	P = X + DX
	CP = math.cos(P)

	P = P - TP * math.floor(P / TP)
	Q = math.atan(CP * (RP * SY - RS) / (RP * CY * CX - RC))
	
	return P,Q

## @brief Convert angle in degrees to equivalent angle in the range 0 to 360 degrees.
def unwind(W):
	return W - 6.283185308 * math.floor(W / 6.283185308)

## @brief Calculate geocentric ecliptic longitude for the Moon
def moon_long(LH,LM,LS,DS,ZC,DY,MN,YR):
	UT = lct_ut(LH, LM, LS, DS, ZC, DY, MN, YR)
	GD = lct_gday(LH, LM, LS, DS, ZC, DY, MN, YR)
	GM = lct_gmonth(LH, LM, LS, DS, ZC, DY, MN, YR)
	GY = lct_gyear(LH, LM, LS, DS, ZC, DY, MN, YR)
	T = ((cd_jd(GD, GM, GY) - 2415020) / 36525) + (UT / 876600)
	T2 = T * T

	M1 = 27.32158213
	M2 = 365.2596407
	M3 = 27.55455094
	M4 = 29.53058868
	M5 = 27.21222039
	M6 = 6798.363307
	Q = cd_jd(GD, GM, GY) - 2415020 + (UT / 24)
	M1 = Q / M1
	M2 = Q / M2
	M3 = Q / M3
	M4 = Q / M4
	M5 = Q / M5
	M6 = Q / M6
	M1 = 360 * (M1 - math.floor(M1))
	M2 = 360 * (M2 - math.floor(M2))
	M3 = 360 * (M3 - math.floor(M3))
	M4 = 360 * (M4 - math.floor(M4))
	M5 = 360 * (M5 - math.floor(M5))
	M6 = 360 * (M6 - math.floor(M6))

	ML = 270.434164 + M1 - (0.001133 - 0.0000019 * T) * T2
	MS = 358.475833 + M2 - (0.00015 + 0.0000033 * T) * T2
	MD = 296.104608 + M3 + (0.009192 + 0.0000144 * T) * T2
	ME1 = 350.737486 + M4 - (0.001436 - 0.0000019 * T) * T2
	MF = 11.250889 + M5 - (0.003211 + 0.0000003 * T) * T2
	NA = 259.183275 - M6 + (0.002078 + 0.0000022 * T) * T2
	A = math.radians(51.2 + 20.2 * T)
	S1 = math.sin(A)
	S2 = math.sin(math.radians(NA))
	B = 346.56 + (132.87 - 0.0091731 * T) * T
	S3 = 0.003964 * math.sin(math.radians(B))
	C = math.radians(NA + 275.05 - 2.3 * T)
	S4 = math.sin(C)
	ML = ML + 0.000233 * S1 + S3 + 0.001964 * S2
	MS = MS - 0.001778 * S1
	MD = MD + 0.000817 * S1 + S3 + 0.002541 * S2
	MF = MF + S3 - 0.024691 * S2 - 0.004328 * S4
	ME1 = ME1 + 0.002011 * S1 + S3 + 0.001964 * S2
	E = 1 - (0.002495 + 0.00000752 * T) * T
	E2 = E * E
	ML = math.radians(ML)
	MS = math.radians(MS)
	NA = math.radians(NA)
	ME1 = math.radians(ME1)
	MF = math.radians(MF)
	MD = math.radians(MD)

	L = 6.28875 * math.sin(MD) + 1.274018 * math.sin(2 * ME1 - MD)
	L = L + 0.658309 * math.sin(2 * ME1) + 0.213616 * math.sin(2 * MD)
	L = L - E * 0.185596 * math.sin(MS) - 0.114336 * math.sin(2 * MF)
	L = L + 0.058793 * math.sin(2 * (ME1 - MD))
	L = L + 0.057212 * E * math.sin(2 * ME1 - MS - MD) + 0.05332 * math.sin(2 * ME1 + MD)
	L = L + 0.045874 * E * math.sin(2 * ME1 - MS) + 0.041024 * E * math.sin(MD - MS)
	L = L - 0.034718 * math.sin(ME1) - E * 0.030465 * math.sin(MS + MD)
	L = L + 0.015326 * math.sin(2 * (ME1 - MF)) - 0.012528 * math.sin(2 * MF + MD)
	L = L - 0.01098 * math.sin(2 * MF - MD) + 0.010674 * math.sin(4 * ME1 - MD)
	L = L + 0.010034 * math.sin(3 * MD) + 0.008548 * math.sin(4 * ME1 - 2 * MD)
	L = L - E * 0.00791 * math.sin(MS - MD + 2 * ME1) - E * 0.006783 * math.sin(2 * ME1 + MS)
	L = L + 0.005162 * math.sin(MD - ME1) + E * 0.005 * math.sin(MS + ME1)
	L = L + 0.003862 * math.sin(4 * ME1) + E * 0.004049 * math.sin(MD - MS + 2 * ME1)
	L = L + 0.003996 * math.sin(2 * (MD + ME1)) + 0.003665 * math.sin(2 * ME1 - 3 * MD)
	L = L + E * 0.002695 * math.sin(2 * MD - MS) + 0.002602 * math.sin(MD - 2 * (MF + ME1))
	L = L + E * 0.002396 * math.sin(2 * (ME1 - MD) - MS) - 0.002349 * math.sin(MD + ME1)
	L = L + E2 * 0.002249 * math.sin(2 * (ME1 - MS)) - E * 0.002125 * math.sin(2 * MD + MS)
	L = L - E2 * 0.002079 * math.sin(2 * MS) + E2 * 0.002059 * math.sin(2 * (ME1 - MS) - MD)
	L = L - 0.001773 * math.sin(MD + 2 * (ME1 - MF)) - 0.001595 * math.sin(2 * (MF + ME1))
	L = L + E * 0.00122 * math.sin(4 * ME1 - MS - MD) - 0.00111 * math.sin(2 * (MD + MF))
	L = L + 0.000892 * math.sin(MD - 3 * ME1) - E * 0.000811 * math.sin(MS + MD + 2 * ME1)
	L = L + E * 0.000761 * math.sin(4 * ME1 - MS - 2 * MD)
	L = L + E2 * 0.000704 * math.sin(MD - 2 * (MS + ME1))
	L = L + E * 0.000693 * math.sin(MS - 2 * (MD - ME1))
	L = L + E * 0.000598 * math.sin(2 * (ME1 - MF) - MS)
	L = L + 0.00055 * math.sin(MD + 4 * ME1) + 0.000538 * math.sin(4 * MD)
	L = L + E * 0.000521 * math.sin(4 * ME1 - MS) + 0.000486 * math.sin(2 * MD - ME1)
	L = L + E2 * 0.000717 * math.sin(MD - 2 * MS)
	MM = unwind(ML + math.radians(L))

	return degrees(MM)

## @brief Calculate geocentric ecliptic latitude for the Moon
def moon_lat(LH,LM,LS,DS,ZC,DY,MN,YR):
	UT = lct_ut(LH, LM, LS, DS, ZC, DY, MN, YR)
	GD = lct_gday(LH, LM, LS, DS, ZC, DY, MN, YR)
	GM = lct_gmonth(LH, LM, LS, DS, ZC, DY, MN, YR)
	GY = lct_gyear(LH, LM, LS, DS, ZC, DY, MN, YR)
	T = ((cd_jd(GD, GM, GY) - 2415020) / 36525) + (UT / 876600)
	T2 = T * T

	M1 = 27.32158213
	M2 = 365.2596407
	M3 = 27.55455094
	M4 = 29.53058868
	M5 = 27.21222039
	M6 = 6798.363307
	Q = cd_jd(GD, GM, GY) - 2415020 + (UT / 24)
	M1 = Q / M1
	M2 = Q / M2
	M3 = Q / M3
	M4 = Q / M4
	M5 = Q / M5
	M6 = Q / M6
	M1 = 360 * (M1 - math.floor(M1))
	M2 = 360 * (M2 - math.floor(M2))
	M3 = 360 * (M3 - math.floor(M3))
	M4 = 360 * (M4 - math.floor(M4))
	M5 = 360 * (M5 - math.floor(M5))
	M6 = 360 * (M6 - math.floor(M6))

	ML = 270.434164 + M1 - (0.001133 - 0.0000019 * T) * T2
	MS = 358.475833 + M2 - (0.00015 + 0.0000033 * T) * T2
	MD = 296.104608 + M3 + (0.009192 + 0.0000144 * T) * T2
	ME1 = 350.737486 + M4 - (0.001436 - 0.0000019 * T) * T2
	MF = 11.250889 + M5 - (0.003211 + 0.0000003 * T) * T2
	NA = 259.183275 - M6 + (0.002078 + 0.0000022 * T) * T2
	A = math.radians(51.2 + 20.2 * T)
	S1 = math.sin(A)
	S2 = math.sin(math.radians(NA))
	B = 346.56 + (132.87 - 0.0091731 * T) * T
	S3 = 0.003964 * math.sin(math.radians(B))
	C = math.radians(NA + 275.05 - 2.3 * T)
	S4 = math.sin(C)
	ML = ML + 0.000233 * S1 + S3 + 0.001964 * S2
	MS = MS - 0.001778 * S1
	MD = MD + 0.000817 * S1 + S3 + 0.002541 * S2
	MF = MF + S3 - 0.024691 * S2 - 0.004328 * S4
	ME1 = ME1 + 0.002011 * S1 + S3 + 0.001964 * S2
	E = 1 - (0.002495 + 0.00000752 * T) * T
	E2 = E * E
	ML = math.radians(ML)
	MS = math.radians(MS)
	NA = math.radians(NA)
	ME1 = math.radians(ME1)
	MF = math.radians(MF)
	MD = math.radians(MD)

	G = 5.128189 * math.sin(MF) + 0.280606 * math.sin(MD + MF)
	G = G + 0.277693 * math.sin(MD - MF) + 0.173238 * math.sin(2 * ME1 - MF)
	G = G + 0.055413 * math.sin(2 * ME1 + MF - MD) + 0.046272 * math.sin(2 * ME1 - MF - MD)
	G = G + 0.032573 * math.sin(2 * ME1 + MF) + 0.017198 * math.sin(2 * MD + MF)
	G = G + 0.009267 * math.sin(2 * ME1 + MD - MF) + 0.008823 * math.sin(2 * MD - MF)
	G = G + E * 0.008247 * math.sin(2 * ME1 - MS - MF) + 0.004323 * math.sin(2 * (ME1 - MD) - MF)
	G = G + 0.0042 * math.sin(2 * ME1 + MF + MD) + E * 0.003372 * math.sin(MF - MS - 2 * ME1)
	G = G + E * 0.002472 * math.sin(2 * ME1 + MF - MS - MD)
	G = G + E * 0.002222 * math.sin(2 * ME1 + MF - MS)
	G = G + E * 0.002072 * math.sin(2 * ME1 - MF - MS - MD)
	G = G + E * 0.001877 * math.sin(MF - MS + MD) + 0.001828 * math.sin(4 * ME1 - MF - MD)
	G = G - E * 0.001803 * math.sin(MF + MS) - 0.00175 * math.sin(3 * MF)
	G = G + E * 0.00157 * math.sin(MD - MS - MF) - 0.001487 * math.sin(MF + ME1)
	G = G - E * 0.001481 * math.sin(MF + MS + MD) + E * 0.001417 * math.sin(MF - MS - MD)
	G = G + E * 0.00135 * math.sin(MF - MS) + 0.00133 * math.sin(MF - ME1)
	G = G + 0.001106 * math.sin(MF + 3 * MD) + 0.00102 * math.sin(4 * ME1 - MF)
	G = G + 0.000833 * math.sin(MF + 4 * ME1 - MD) + 0.000781 * math.sin(MD - 3 * MF)
	G = G + 0.00067 * math.sin(MF + 4 * ME1 - 2 * MD) + 0.000606 * math.sin(2 * ME1 - 3 * MF)
	G = G + 0.000597 * math.sin(2 * (ME1 + MD) - MF)
	G = G + E * 0.000492 * math.sin(2 * ME1 + MD - MS - MF) + 0.00045 * math.sin(2 * (MD - ME1) - MF)
	G = G + 0.000439 * math.sin(3 * MD - MF) + 0.000423 * math.sin(MF + 2 * (ME1 + MD))
	G = G + 0.000422 * math.sin(2 * ME1 - MF - 3 * MD) - E * 0.000367 * math.sin(MS + MF + 2 * ME1 - MD)
	G = G - E * 0.000353 * math.sin(MS + MF + 2 * ME1) + 0.000331 * math.sin(MF + 4 * ME1)
	G = G + E * 0.000317 * math.sin(2 * ME1 + MF - MS + MD)
	G = G + E2 * 0.000306 * math.sin(2 * (ME1 - MS) - MF) - 0.000283 * math.sin(MD + 3 * MF)
	W1 = 0.0004664 * math.cos(NA)
	W2 = 0.0000754 * math.cos(C)
	BM = math.radians(G) * (1 - W1 - W2)

	return degrees(BM)

## @brief Calculate horizontal parallax for the Moon
def moon_hp(LH,LM,LS,DS,ZC,DY,MN,YR):
	UT = lct_ut(LH, LM, LS, DS, ZC, DY, MN, YR)
	GD = lct_gday(LH, LM, LS, DS, ZC, DY, MN, YR)
	GM = lct_gmonth(LH, LM, LS, DS, ZC, DY, MN, YR)
	GY = lct_gyear(LH, LM, LS, DS, ZC, DY, MN, YR)
	T = ((cd_jd(GD, GM, GY) - 2415020) / 36525) + (UT / 876600)
	T2 = T * T

	M1 = 27.32158213
	M2 = 365.2596407
	M3 = 27.55455094
	M4 = 29.53058868
	M5 = 27.21222039
	M6 = 6798.363307
	Q = cd_jd(GD, GM, GY) - 2415020 + (UT / 24)
	M1 = Q / M1
	M2 = Q / M2
	M3 = Q / M3
	M4 = Q / M4
	M5 = Q / M5
	M6 = Q / M6
	M1 = 360 * (M1 - math.floor(M1))
	M2 = 360 * (M2 - math.floor(M2))
	M3 = 360 * (M3 - math.floor(M3))
	M4 = 360 * (M4 - math.floor(M4))
	M5 = 360 * (M5 - math.floor(M5))
	M6 = 360 * (M6 - math.floor(M6))

	ML = 270.434164 + M1 - (0.001133 - 0.0000019 * T) * T2
	MS = 358.475833 + M2 - (0.00015 + 0.0000033 * T) * T2
	MD = 296.104608 + M3 + (0.009192 + 0.0000144 * T) * T2
	ME1 = 350.737486 + M4 - (0.001436 - 0.0000019 * T) * T2
	MF = 11.250889 + M5 - (0.003211 + 0.0000003 * T) * T2
	NA = 259.183275 - M6 + (0.002078 + 0.0000022 * T) * T2
	A = math.radians(51.2 + 20.2 * T)
	S1 = math.sin(A)
	S2 = math.sin(math.radians(NA))
	B = 346.56 + (132.87 - 0.0091731 * T) * T
	S3 = 0.003964 * math.sin(math.radians(B))
	C = math.radians(NA + 275.05 - 2.3 * T)
	S4 = math.sin(C)
	ML = ML + 0.000233 * S1 + S3 + 0.001964 * S2
	MS = MS - 0.001778 * S1
	MD = MD + 0.000817 * S1 + S3 + 0.002541 * S2
	MF = MF + S3 - 0.024691 * S2 - 0.004328 * S4
	ME1 = ME1 + 0.002011 * S1 + S3 + 0.001964 * S2
	E = 1 - (0.002495 + 0.00000752 * T) * T
	E2 = E * E
	ML = math.radians(ML)
	MS = math.radians(MS)
	NA = math.radians(NA)
	ME1 = math.radians(ME1)
	MF = math.radians(MF)
	MD = math.radians(MD)

	PM = 0.950724 + 0.051818 * math.cos(MD) + 0.009531 * math.cos(2 * ME1 - MD)
	PM = PM + 0.007843 * math.cos(2 * ME1) + 0.002824 * math.cos(2 * MD)
	PM = PM + 0.000857 * math.cos(2 * ME1 + MD) + E * 0.000533 * math.cos(2 * ME1 - MS)
	PM = PM + E * 0.000401 * math.cos(2 * ME1 - MD - MS)
	PM = PM + E * 0.00032 * math.cos(MD - MS) - 0.000271 * math.cos(ME1)
	PM = PM - E * 0.000264 * math.cos(MS + MD) - 0.000198 * math.cos(2 * MF - MD)
	PM = PM + 0.000173 * math.cos(3 * MD) + 0.000167 * math.cos(4 * ME1 - MD)
	PM = PM - E * 0.000111 * math.cos(MS) + 0.000103 * math.cos(4 * ME1 - 2 * MD)
	PM = PM - 0.000084 * math.cos(2 * MD - 2 * ME1) - E * 0.000083 * math.cos(2 * ME1 + MS)
	PM = PM + 0.000079 * math.cos(2 * ME1 + 2 * MD) + 0.000072 * math.cos(4 * ME1)
	PM = PM + E * 0.000064 * math.cos(2 * ME1 - MS + MD) - E * 0.000063 * math.cos(2 * ME1 + MS - MD)
	PM = PM + E * 0.000041 * math.cos(MS + ME1) + E * 0.000035 * math.cos(2 * MD - MS)
	PM = PM - 0.000033 * math.cos(3 * MD - 2 * ME1) - 0.00003 * math.cos(MD + ME1)
	PM = PM - 0.000029 * math.cos(2 * (MF - ME1)) - E * 0.000029 * math.cos(2 * MD + MS)
	PM = PM + E2 * 0.000026 * math.cos(2 * (ME1 - MS)) - 0.000023 * math.cos(2 * (MF - ME1) + MD)
	PM = PM + E * 0.000019 * math.cos(4 * ME1 - MS - MD)

	return PM

## @brief Mean ecliptic longitude of the Sun at the epoch
def sun_e_long(GD,GM,GY):
	T = (cd_jd(GD,GM,GY) - 2415020) / 36525
	T2 = T * T
	X = 279.6966778 + 36000.76892 * T + 0.0003025 * T2
	
	return X - 360 * math.floor(X / 360)

## @brief Longitude of the Sun at perigee
def sun_peri(GD,GM,GY):
	T = (cd_jd(GD,GM,GY) - 2415020) / 36525
	T2 = T * T
	X = 281.2208444 + 1.719175 * T + 0.000452778 * T2
	
	return X - 360 * math.floor(X / 360)

## @brief Eccentricity of the Sun-Earth orbit
def sun_ecc(GD,GM,GY):
	T = (cd_jd(GD,GM,GY) - 2415020) / 36525
	T2 = T * T
	
	return 0.01675104 - 0.0000418 * T - 0.000000126 * T2

## @brief Ecliptic - Declination (degrees)
def ec_dec(ELD,ELM,ELS,BD,BM,BS,GD,GM,GY):
	A = math.radians(dms_dd(ELD, ELM, ELS))
	B = math.radians(dms_dd(BD, BM, BS))
	C = math.radians(obliq(GD, GM, GY))
	D = math.sin(B) * math.cos(C) + math.cos(B) * math.sin(C) * math.sin(A)
	
	return degrees(math.asin(D))

## @brief Ecliptic - Right Ascension (degrees)
def ec_ra(ELD,ELM,ELS,BD,BM,BS,GD,GM,GY):
	A = math.radians(dms_dd(ELD, ELM, ELS))
	B = math.radians(dms_dd(BD, BM, BS))
	C = math.radians(obliq(GD, GM, GY))
	D = math.sin(A) * math.cos(C) - math.tan(B) * math.sin(C)
	E = math.cos(A)
	F = degrees(atan2(E, D))
	
	return F - 360 * math.floor(F / 360)

## @brief Calculate Sun's true anomaly, i.e., how much its orbit deviates from a true circle to an ellipse.
def sun_true_anomaly(LCH, LCM, LCS, DS, ZC, LD, LM, LY):
	AA = lct_gday(LCH, LCM, LCS, DS, ZC, LD, LM, LY)
	BB = lct_gmonth(LCH, LCM, LCS, DS, ZC, LD, LM, LY)
	CC = lct_gyear(LCH, LCM, LCS, DS, ZC, LD, LM, LY)
	UT = lct_ut(LCH, LCM, LCS, DS, ZC, LD, LM, LY)
	DJ = cd_jd(AA, BB, CC) - 2415020
	
	T = (DJ / 36525) + (UT / 876600)
	T2 = T * T
	
	A = 100.0021359 * T
	B = 360 * (A - math.floor(A))

	L = 279.69668 + 0.0003025 * T2 + B
	
	A = 99.99736042 * T
	B = 360 * (A - math.floor(A))

	M1 = 358.47583 - (0.00015 + 0.0000033 * T) * T2 + B
	EC = 0.01675104 - 0.0000418 * T - 0.000000126 * T2

	AM = math.radians(M1)

	return degrees(true_anomaly(AM, EC))

## @brief Calculate local civil time of sunrise.
# Original macro name: SunriseLCT
def sunrise_lct(LD, LM, LY, DS, ZC, GL, GP):
	DI = 0.8333333
	GD = lct_gday(12, 0, 0, DS, ZC, LD, LM, LY)
	GM = lct_gmonth(12, 0, 0, DS, ZC, LD, LM, LY)
	GY = lct_gyear(12, 0, 0, DS, ZC, LD, LM, LY)
	SR = sun_long(12, 0, 0, DS, ZC, LD, LM, LY)
	
	A,X,Y,LA,S = sunrise_lct_l3710(GD,GM,GY,SR,DI,GP)

	if S != "OK":
		XX = -99
	else:
		X = lst_gst(LA, 0, 0, GL)
		UT = gst_ut(X, 0, 0, GD, GM, GY)

		if e_gst_ut(X, 0, 0, GD, GM, GY) != "OK":
			XX = -99
		else:
			SR = sun_long(UT, 0, 0, 0, 0, GD, GM, GY)
			A,X,Y,LA,S = sunrise_lct_l3710(GD,GM,GY,SR,DI,GP)

			if S != "OK":
				XX = -99
			else:
				X = lst_gst(LA, 0, 0, GL)
				UT = gst_ut(X, 0, 0, GD, GM, GY)
				XX = ut_lct(UT, 0, 0, DS, ZC, GD, GM, GY)

	return XX

## @brief Helper function for sunrise_lct().
def sunrise_lct_l3710(GD, GM, GY, SR, DI, GP):
	A = SR + nutat_long(GD, GM, GY) - 0.005694
	X = ec_ra(A, 0, 0, 0, 0, 0, GD, GM, GY)
	Y = ec_dec(A, 0, 0, 0, 0, 0, GD, GM, GY)
	LA = rise_set_local_sidereal_time_rise(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)
	S = e_rs(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)

	return A,X,Y,LA,S

## @brief Calculate azimuth of sunrise.
# Original macro name: SunriseAz
def sunrise_az(LD, LM, LY, DS, ZC, GL, GP):
	DI = 0.8333333
	GD = lct_gday(12, 0, 0, DS, ZC, LD, LM, LY)
	GM = lct_gmonth(12, 0, 0, DS, ZC, LD, LM, LY)
	GY = lct_gyear(12, 0, 0, DS, ZC, LD, LM, LY)
	SR = sun_long(12, 0, 0, DS, ZC, LD, LM, LY)

	A,X,Y,LA,S = sunrise_az_l3710(GD, GM, GY, SR, DI, GP)
        
	if S != "OK":
		return -99

	X = lst_gst(LA, 0, 0, GL)
	UT = gst_ut(X, 0, 0, GD, GM, GY)

	if e_gst_ut(X, 0, 0, GD, GM, GY) != "OK":
		return -99

	SR = sun_long(UT, 0, 0, 0, 0, GD, GM, GY)
	A,X,Y,LA,S = sunrise_az_l3710(GD, GM, GY, SR, DI, GP)

	if S != "OK":
		return -99

	return rise_set_azimuth_rise(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)
        
## @brief Helper function for sunrise_az().
def sunrise_az_l3710(GD, GM, GY, SR, DI, GP):
	A = SR + nutat_long(GD, GM, GY) - 0.005694
	X = ec_ra(A, 0, 0, 0, 0, 0, GD, GM, GY)
	Y = ec_dec(A, 0, 0, 0, 0, 0, GD, GM, GY)
	LA = rise_set_local_sidereal_time_rise(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)
	S = e_rs(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)

	return A,X,Y,LA,S

## @brief Calculate azimuth of sunset.
# Original macro name: SunsetAz
def sunset_az(LD, LM, LY, DS, ZC, GL, GP):
	DI = 0.8333333
	GD = lct_gday(12, 0, 0, DS, ZC, LD, LM, LY)
	GM = lct_gmonth(12, 0, 0, DS, ZC, LD, LM, LY)
	GY = lct_gyear(12, 0, 0, DS, ZC, LD, LM, LY)
	SR = sun_long(12, 0, 0, DS, ZC, LD, LM, LY)
	
	A,X,Y,LA,S = sunset_az_l3710(GD, GM, GY, SR, DI, GP)

	if S != "OK":
		return -99
		
	X = lst_gst(LA, 0, 0, GL)
	UT = gst_ut(X, 0, 0, GD, GM, GY)
	
	if e_gst_ut(X, 0, 0, GD, GM, GY) != "OK":
		return -99
		
	SR = sun_long(UT, 0, 0, 0, 0, GD, GM, GY)
	
	A,X,Y,LA,S = sunset_az_l3710(GD, GM, GY, SR, DI, GP)
	
	if S != "OK":
		return -99
	
	return rise_set_azimuth_set(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)
        
## @brief Helper function for sunset_az().
def sunset_az_l3710(GD, GM, GY, SR, DI, GP):
	A = SR + nutat_long(GD, GM, GY) - 0.005694
	X = ec_ra(A, 0, 0, 0, 0, 0, GD, GM, GY)
	Y = ec_dec(A, 0, 0, 0, 0, 0, GD, GM, GY)
	LA = rise_set_local_sidereal_time_set(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)
	S = e_rs(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)

	return A,X,Y,LA,S

## @brief Calculate local civil time of sunset.
# Original macro name: SunsetLCT
def sunset_lct(LD, LM, LY, DS, ZC, GL, GP):
	DI = 0.8333333
	GD = lct_gday(12, 0, 0, DS, ZC, LD, LM, LY)
	GM = lct_gmonth(12, 0, 0, DS, ZC, LD, LM, LY)
	GY = lct_gyear(12, 0, 0, DS, ZC, LD, LM, LY)
	SR = sun_long(12, 0, 0, DS, ZC, LD, LM, LY)

	A,X,Y,LA,S = sunset_lct_l3710(GD,GM,GY,SR,DI,GP)

	if S != "OK":
		XX = -99
	else:
		X = lst_gst(LA, 0, 0, GL)
		UT = gst_ut(X, 0, 0, GD, GM, GY)

		if e_gst_ut(X, 0, 0, GD, GM, GY) != "OK":
			XX = -99
		else:
			SR = sun_long(UT, 0, 0, 0, 0, GD, GM, GY)
			A,X,Y,LA,S = sunset_lct_l3710(GD,GM,GY,SR,DI,GP)

			if S != "OK":
				XX = -99
			else:
				X = lst_gst(LA, 0, 0, GL)
				UT = gst_ut(X, 0, 0, GD, GM, GY)
				XX = ut_lct(UT, 0, 0, DS, ZC, GD, GM, GY)
	
	return XX

## @brief Helper function for sunset_lct().
def sunset_lct_l3710(GD, GM, GY, SR, DI, GP):
	A = SR + nutat_long(GD, GM, GY) - 0.005694
	X = ec_ra(A, 0, 0, 0, 0, 0, GD, GM, GY)
	Y = ec_dec(A, 0, 0, 0, 0, 0, GD, GM, GY)
	LA = rise_set_local_sidereal_time_set(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)
	S = e_rs(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)
	
	return A,X,Y,LA,S

## @brief Sunrise/Sunset calculation status.
# Original macro name: eSunRS
def e_sun_rs(LD, LM, LY, DS, ZC, GL, GP):
	S = ""
	DI = 0.8333333
	GD = lct_gday(12, 0, 0, DS, ZC, LD, LM, LY)
	GM = lct_gmonth(12, 0, 0, DS, ZC, LD, LM, LY)
	GY = lct_gyear(12, 0, 0, DS, ZC, LD, LM, LY)
	SR = sun_long(12, 0, 0, DS, ZC, LD, LM, LY)
	
	A,X,Y,LA,S = e_sun_rs_l3710(GD, GM, GY, SR, DI, GP)

	if S != "OK":
		return S
	else:
		X = lst_gst(LA, 0, 0, GL)
		UT = gst_ut(X, 0, 0, GD, GM, GY)
		SR = sun_long(UT, 0, 0, 0, 0, GD, GM, GY)
		A,X,Y,LA,S = e_sun_rs_l3710(GD, GM, GY, SR, DI, GP)
		if S != "OK":
			return S
		else:
			X = lst_gst(LA, 0, 0, GL)
			UT = gst_ut(X, 0, 0, GD, GM, GY)

			if e_gst_ut(X, 0, 0, GD, GM, GY) != "OK":
				S = S + " GST to UT conversion warning"
				return S
			
			return S

## @brief Helper function for e_sun_rs().
def e_sun_rs_l3710(GD, GM, GY, SR, DI, GP):
	A = SR + nutat_long(GD, GM, GY) - 0.005694
	X = ec_ra(A, 0, 0, 0, 0, 0, GD, GM, GY)
	Y = ec_dec(A, 0, 0, 0, 0, 0, GD, GM, GY)
	LA = rise_set_local_sidereal_time_rise(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)
	S = e_rs(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)

	return A,X,Y,LA,S

## @brief TODO: Needs documentation.  (Currently unused.)
def angle(XX1, XM1, XS1, DD1, DM1, DS1, XX2, XM2, XS2, DD2, DM2, DS2, S):
	A = dh_dd(hms_dh(XX1, XM1, XS1)) if (S in ["H","h"]) else dms_dd(XX1, XM1, XD1)
	B = math.radians(A)
	C = dms_dd(DD1, DM1, DS1)
	D = math.radians(C)
	E = dh_dd(hms_dh(XX2, XM2, XS2)) if (S in ["H","h"]) else dms_dd(XX2, XM2, XD2)
	F = math.radians(E)
	G = dms_dd(DD2, DM2, DS2)
	H = math.radians(G)
	I = math.acos(math.sin(D) * math.sin(H) + math.cos(D) * math.cos(H) * math.cos(B - F))

	return degrees(I)

## @brief Local sidereal time of rise, in hours.
# Original macro name: RSLSTR
def rise_set_local_sidereal_time_rise(RAH, RAM, RAS, DD, DM, DS, VD, G):
	A = hms_dh(RAH, RAM, RAS)
	B = math.radians(dh_dd(A))
	C = math.radians(dms_dd(DD, DM, DS))
	D = math.radians(VD)
	E = math.radians(G)
	F = -(math.sin(D) + math.sin(E) * math.sin(C)) / (math.cos(E) * math.cos(C))
	H = math.acos(F) if (abs(F) < 1) else 0
	I = dd_dh(degrees(B - H))

	return I - 24 * math.floor(I / 24)

## @brief Rise/Set status
# <para>Possible values: "OK", "** never rises", "** circumpolar"</para>
# <para>Original macro name: eRS</para>
def e_rs(RAH, RAM, RAS, DD, DM, DS, VD, G):
	A = hms_dh(RAH, RAM, RAS)
	B = math.radians(dh_dd(A))
	C = math.radians(dms_dd(DD, DM, DS))
	D = math.radians(VD)
	E = math.radians(G)
	F = -(math.sin(D) + math.sin(E) * math.sin(C)) / (math.cos(E) * math.cos(C))

	returnValue = "OK"
	if (F >= 1):
		returnValue = "** never rises"
	if (F <= -1):
		returnValue = "** circumpolar"

	return returnValue

## @brief Local sidereal time of setting, in hours.
# Original macro name: RSLSTS
def rise_set_local_sidereal_time_set(RAH, RAM, RAS, DD, DM, DS, VD, G):
	A = hms_dh(RAH, RAM, RAS)
	B = math.radians(dh_dd(A))
	C = math.radians(dms_dd(DD, DM, DS))
	D = math.radians(VD)
	E = math.radians(G)
	F = -(math.sin(D) + math.sin(E) * math.sin(C)) / (math.cos(E) * math.cos(C))
	H = math.acos(F) if (abs(F) < 1) else 0
	I = dd_dh(degrees(B + H))

	return I - 24 * math.floor(I / 24)

## @brief Azimuth of rising, in degrees.
# Original macro name: RSAZR
def rise_set_azimuth_rise(RAH, RAM, RAS, DD, DM, DS, VD, G):
	A = hms_dh(RAH, RAM, RAS)
	B = math.radians(dh_dd(A))
	C = math.radians(dms_dd(DD, DM, DS))
	D = math.radians(VD)
	E = math.radians(G)
	F = (math.sin(C) + math.sin(D) * math.sin(E)) / (math.cos(D) * math.cos(E))
	H = math.acos(F) if e_rs(RAH, RAM, RAS, DD, DM, DS, VD, G) == "OK" else 0
	I = degrees(H)

	return I - 360 * math.floor(I / 360)

## @brief Azimuth of setting, in degrees.
# Original macro name: RSAZS
def rise_set_azimuth_set(RAH, RAM, RAS, DD, DM, DS, VD, G):
	A = hms_dh(RAH, RAM, RAS)
	B = math.radians(dh_dd(A))
	C = math.radians(dms_dd(DD, DM, DS))
	D = math.radians(VD)
	E = math.radians(G)
	F = (math.sin(C) + math.sin(D) * math.sin(E)) / (math.cos(D) * math.cos(E))
	H = math.acos(F) if e_rs(RAH, RAM, RAS, DD, DM, DS, VD, G) == "OK" else 0
	I = 360 - degrees(H)

	return I - 360 * math.floor(I / 360)

## @brief Nutation amount to be added in ecliptic longitude, in degrees.
# Original macro name: NutatLong
def nutat_long(GD, GM, GY):
	DJ = cd_jd(GD, GM, GY) - 2415020
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

	DP = (-17.2327 - 0.01737 * T) * math.sin(N1)
	DP = DP + (-1.2729 - 0.00013 * T) * math.sin(l2) + 0.2088 * math.sin(N2)
	DP = DP - 0.2037 * math.sin(D2) + (0.1261 - 0.00031 * T) * math.sin(M1)
	DP = DP + 0.0675 * math.sin(M2) - (0.0497 - 0.00012 * T) * math.sin(l2 + M1)
	DP = DP - 0.0342 * math.sin(D2 - N1) - 0.0261 * math.sin(D2 + M2)
	DP = DP + 0.0214 * math.sin(l2 - M1) - 0.0149 * math.sin(l2 - D2 + M2)
	DP = DP + 0.0124 * math.sin(l2 - N1) + 0.0114 * math.sin(D2 - M2)

	return DP / 3600

## @brief Calculate morning twilight start, in local time.
# Original macro name: TwilightAMLCT
# @param TT		Twilight type: "C" (civil), "N" (nautical), or "A" (astronomical)
def twilight_am_lct(LD, LM, LY, DS, ZC, GL, GP, TT):
	DI = 18
	if TT in ["C","c"]:
		DI = 6
	if TT in ["N","n"]:
		DI = 12

	GD = lct_gday(12, 0, 0, DS, ZC, LD, LM, LY)
	GM = lct_gmonth(12, 0, 0, DS, ZC, LD, LM, LY)
	GY = lct_gyear(12, 0, 0, DS, ZC, LD, LM, LY)
	SR = sun_long(12, 0, 0, DS, ZC, LD, LM, LY)
	
	A,X,Y,LA,S = twilight_am_lct_l3710(GD, GM, GY, SR, DI, GP)

	if S != "OK":
		return -99

	X = lst_gst(LA, 0, 0, GL)
	UT = gst_ut(X, 0, 0, GD, GM, GY)

	if e_gst_ut(X, 0, 0, GD, GM, GY) != "OK":
		return -99

	SR = sun_long(UT, 0, 0, 0, 0, GD, GM, GY)
	
	A,X,Y,LA,S = twilight_am_lct_l3710(GD, GM, GY, SR, DI, GP)

	if S != "OK":
		return -99

	X = lst_gst(LA, 0, 0, GL)
	UT = gst_ut(X, 0, 0, GD, GM, GY)

	XX = ut_lct(UT, 0, 0, DS, ZC, GD, GM, GY)

	return XX

## @brief Helper function for twilight_am_lct().
def twilight_am_lct_l3710(GD, GM, GY, SR, DI, GP):
	A = SR + nutat_long(GD, GM, GY) - 0.005694
	X = ec_ra(A, 0, 0, 0, 0, 0, GD, GM, GY)
	Y = ec_dec(A, 0, 0, 0, 0, 0, GD, GM, GY)
	LA = rise_set_local_sidereal_time_rise(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)
	S = e_rs(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)

	return A,X,Y,LA,S

## @brief Calculate evening twilight end, in local time.
# Original macro name: TwilightPMLCT
# @param TT		Twilight type: "C" (civil), "N" (nautical), or "A" (astronomical)
def twilight_pm_lct(LD, LM, LY, DS, ZC, GL, GP, TT):
	DI = 18
	if TT in ["C","c"]:
		DI = 6
	if TT in ["N","n"]:
		DI = 12

	GD = lct_gday(12, 0, 0, DS, ZC, LD, LM, LY)
	GM = lct_gmonth(12, 0, 0, DS, ZC, LD, LM, LY)
	GY = lct_gyear(12, 0, 0, DS, ZC, LD, LM, LY)
	SR = sun_long(12, 0, 0, DS, ZC, LD, LM, LY)

	A,X,Y,LA,S = twilight_pm_lct_l3710(GD, GM, GY, SR, DI, GP)

	if S != "OK":
		return 0

	X = lst_gst(LA, 0, 0, GL)
	UT = gst_ut(X, 0, 0, GD, GM, GY)

	if e_gst_ut(X, 0, 0, GD, GM, GY) != "OK":
		return 0

	SR = sun_long(UT, 0, 0, 0, 0, GD, GM, GY)
	
	A,X,Y,LA,S = twilight_pm_lct_l3710(GD, GM, GY, SR, DI, GP)

	if S != "OK":
		return 0

	X = lst_gst(LA, 0, 0, GL)
	UT = gst_ut(X, 0, 0, GD, GM, GY)

	return ut_lct(UT, 0, 0, DS, ZC, GD, GM, GY)
        
## @brief Helper function for twilight_pm_lct().
def twilight_pm_lct_l3710(GD, GM, GY, SR, DI, GP):
	A = SR + nutat_long(GD, GM, GY) - 0.005694
	X = ec_ra(A, 0, 0, 0, 0, 0, GD, GM, GY)
	Y = ec_dec(A, 0, 0, 0, 0, 0, GD, GM, GY)
	LA = rise_set_local_sidereal_time_set(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)
	S = e_rs(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)

	return A,X,Y,LA,S

## @brief Twilight calculation status.
# Original macro name: eTwilight
# @param TT		Twilight type: "C" (civil), "N" (nautical), or "A" (astronomical)
# @return One of: "OK", "** lasts all night", or "** Sun too far below horizon"
def e_twilight(LD, LM, LY, DS, ZC, GL, GP, TT):
	S = ""

	DI = 18
	if TT in ["C","c"]:
		DI = 6
	if TT in ["N","n"]:
		DI = 12

	GD = lct_gday(12, 0, 0, DS, ZC, LD, LM, LY)
	GM = lct_gmonth(12, 0, 0, DS, ZC, LD, LM, LY)
	GY = lct_gyear(12, 0, 0, DS, ZC, LD, LM, LY)
	SR = sun_long(12, 0, 0, DS, ZC, LD, LM, LY)

	A,X,Y,LA,S = e_twilight_l3710(GD, GM, GY, SR, DI, GP)

	if S != "OK":
		return S

	X = lst_gst(LA, 0, 0, GL)
	UT = gst_ut(X, 0, 0, GD, GM, GY)
	SR = sun_long(UT, 0, 0, 0, 0, GD, GM, GY)
	
	A,X,Y,LA,S = e_twilight_l3710(GD, GM, GY, SR, DI, GP)

	if S != "OK":
		return S

	X = lst_gst(LA, 0, 0, GL)
	UT = gst_ut(X, 0, 0, GD, GM, GY)

	if e_gst_ut(X, 0, 0, GD, GM, GY) != "OK":
		S = S + " GST to UT conversion warning"
		return S

	return S
        
## @brief Helper function for e_twilight().
def e_twilight_l3710(GD, GM, GY, SR, DI, GP):
	A = SR + nutat_long(GD, GM, GY) - 0.005694
	X = ec_ra(A, 0, 0, 0, 0, 0, GD, GM, GY)
	Y = ec_dec(A, 0, 0, 0, 0, 0, GD, GM, GY)
	LA = rise_set_local_sidereal_time_rise(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)
	S = e_rs(dd_dh(X), 0, 0, Y, 0, 0, DI, GP)

	if S.startswith("** c"):
		S = "** lasts all night"
	else:
		if S.startswith("** n"):
			S = "** Sun too far below horizon"
	
	return A,X,Y,LA,S
