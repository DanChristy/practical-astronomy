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

## @brief Convert Equatorial Coordinates to Horizon Coordinates
def equatorial_coordinates_to_horizon_coordinates(hour_angle_hours,hour_angle_minutes,hour_angle_seconds,declination_degrees,declination_minutes,declination_seconds,geographical_latitude):
	azimuth_in_decimal_degrees = PM.EQAz(hour_angle_hours,hour_angle_minutes,hour_angle_seconds,declination_degrees,declination_minutes,declination_seconds,geographical_latitude)

	altitude_in_decimal_degrees = PM.EQAlt(hour_angle_hours,hour_angle_minutes,hour_angle_seconds,declination_degrees,declination_minutes,declination_seconds,geographical_latitude)

	azimuth_degrees = PM.DDDeg(azimuth_in_decimal_degrees)
	azimuth_minutes = PM.DDMin(azimuth_in_decimal_degrees)
	azimuth_seconds = PM.DDSec(azimuth_in_decimal_degrees)

	altitude_degrees = PM.DDDeg(altitude_in_decimal_degrees)
	altitude_minutes = PM.DDMin(altitude_in_decimal_degrees)
	altitude_seconds = PM.DDSec(altitude_in_decimal_degrees)

	return azimuth_degrees,azimuth_minutes,azimuth_seconds,altitude_degrees,altitude_minutes,altitude_seconds

## @brief Convert Horizon Coordinates to Equatorial Coordinates
def horizon_coordinates_to_equatorial_coordinates(azimuth_degrees,azimuth_minutes,azimuth_seconds,altitude_degrees,altitude_minutes,altitude_seconds,geographical_latitude):
	hour_angle_in_decimal_degrees = PM.HORHa(azimuth_degrees,azimuth_minutes,azimuth_seconds,altitude_degrees,altitude_minutes,altitude_seconds,geographical_latitude)

	declination_in_decimal_degrees = PM.HORDec(azimuth_degrees,azimuth_minutes,azimuth_seconds,altitude_degrees,altitude_minutes,altitude_seconds,geographical_latitude)

	hour_angle_hours = PM.DHHour(hour_angle_in_decimal_degrees)
	hour_angle_minutes = PM.DHMin(hour_angle_in_decimal_degrees)
	hour_angle_seconds = PM.DHSec(hour_angle_in_decimal_degrees)

	declination_degrees = PM.DDDeg(declination_in_decimal_degrees)
	declination_minutes = PM.DDMin(declination_in_decimal_degrees)
	declination_seconds = PM.DDSec(declination_in_decimal_degrees)

	return hour_angle_hours,hour_angle_minutes,hour_angle_seconds,declination_degrees,declination_minutes,declination_seconds

## @brief Calculate Mean Obliquity of the Ecliptic for a Greenwich Date
def mean_obliquity_of_the_ecliptic(greenwich_day,greenwich_month,greenwich_year):
	JD = PM.CDJD(greenwich_day,greenwich_month,greenwich_year)
	MJD = JD - 2451545
	T = MJD / 36525
	DE1 = T * (46.815 + T * (0.0006 - (T * 0.00181)))
	DE2 = DE1 / 3600

	return 23.439292 - DE2