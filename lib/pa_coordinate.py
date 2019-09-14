import math
from . import pa_macro as PM

## @brief Convert an Angle (degrees, minutes, and seconds) to Decimal Degrees
def AngleToDecimalDegrees(degrees, minutes, seconds):
	A = abs(seconds)/60
	B = (abs(minutes)+A)/60
	C = abs(degrees)+B
	D = -(C) if degrees < 0 or minutes < 0 or seconds < 0 else C

	return D

## @brief Convert Decimal Degrees to an Angle (degrees, minutes, and seconds)
## @returns degrees, minutes, seconds
def DecimalDegreesToAngle(decimalDegrees):
	unsignedDecimal = abs(decimalDegrees)
	totalSeconds = unsignedDecimal * 3600
	seconds2dp = round(totalSeconds % 60, 2)
	correctedSeconds = 0 if seconds2dp == 60 else seconds2dp
	correctedRemainder = totalSeconds + 60 if seconds2dp == 60 else totalSeconds
	minutes = math.floor(correctedRemainder/60) % 60
	unsignedDegrees = math.floor(correctedRemainder / 3600)
	signedDegrees = -1 * unsignedDegrees if decimalDegrees < 0 else unsignedDegrees

	return signedDegrees,minutes,math.floor(correctedSeconds)

## @brief Convert Right Ascension to Hour Angle
def right_ascension_to_hour_angle(ra_hours, ra_minutes, ra_seconds, lct_hours, lct_minutes, lct_seconds, is_daylight_saving, zone_correction, local_day, local_month, local_year, geographical_longitude):
	daylight_saving = 1 if is_daylight_saving == True else 0

	hour_angle = PM.RAHA(ra_hours, ra_minutes, ra_seconds, lct_hours, lct_minutes, lct_seconds, daylight_saving, zone_correction, local_day, local_month, local_year, geographical_longitude)

	hour_angle_hours = PM.DHHour(hour_angle)
	hour_angle_minutes = PM.DHMin(hour_angle)
	hour_angle_seconds = PM.DHSec(hour_angle)

	return hour_angle_hours,hour_angle_minutes,hour_angle_seconds

## @brief Convert Hour Angle to Right Ascension
def hour_angle_to_right_ascension(hour_angle_hours,hour_angle_minutes,hour_angle_seconds,lct_hours,lct_minutes,lct_seconds,is_daylight_saving,zone_correction,local_day,local_month,local_year,geographical_longitude):
	daylight_saving = 1 if is_daylight_saving == True else 0

	right_ascension = PM.HARA(hour_angle_hours,hour_angle_minutes,hour_angle_seconds,lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year,geographical_longitude)

	right_ascension_hours = PM.DHHour(right_ascension)
	right_ascension_minutes = PM.DHMin(right_ascension)
	right_ascension_seconds = PM.DHSec(right_ascension)

	return right_ascension_hours,right_ascension_minutes,right_ascension_seconds
