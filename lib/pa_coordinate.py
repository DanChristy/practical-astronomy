import math
from . import pa_macro as PM

## @brief Convert an Angle (degrees, minutes, and seconds) to Decimal Degrees
def angle_to_decimal_degrees(degrees, minutes, seconds):
	A = abs(seconds)/60
	B = (abs(minutes)+A)/60
	C = abs(degrees)+B
	D = -(C) if degrees < 0 or minutes < 0 or seconds < 0 else C

	return D

## @brief Convert Decimal Degrees to an Angle (degrees, minutes, and seconds)
## @returns degrees, minutes, seconds
def decimal_degrees_to_angle(decimalDegrees):
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

## @brief Convert Ecliptic Coordinates to Equatorial Coordinates
def ecliptic_coordinate_to_equatorial_coordinate(ecliptic_longitude_degrees,ecliptic_longitude_minutes,ecliptic_longitude_seconds,ecliptic_latitude_degrees,ecliptic_latitude_minutes,ecliptic_latitude_seconds,greenwich_day,greenwich_month,greenwich_year):
	eclon_deg = PM.DMSDD(ecliptic_longitude_degrees,ecliptic_longitude_minutes,ecliptic_longitude_seconds)
	eclat_deg = PM.DMSDD(ecliptic_latitude_degrees,ecliptic_latitude_minutes,ecliptic_latitude_seconds)
	eclon_rad = math.radians(eclon_deg)
	eclat_rad = math.radians(eclat_deg)
	obliq_deg = PM.Obliq(greenwich_day,greenwich_month,greenwich_year)
	obliq_rad = math.radians(obliq_deg)
	sin_dec = math.sin(eclat_rad) * math.cos(obliq_rad) + math.cos(eclat_rad) * math.sin(obliq_rad) * math.sin(eclon_rad)
	dec_rad = math.asin(sin_dec)
	dec_deg = PM.Degrees(dec_rad)
	y = math.sin(eclon_rad) * math.cos(obliq_rad) - math.tan(eclat_rad) * math.sin(obliq_rad)
	x = math.cos(eclon_rad)
	ra_rad = PM.Atan2(x,y)
	ra_deg1 = PM.Degrees(ra_rad)
	ra_deg2 = ra_deg1 - 360 * math.floor(ra_deg1/360)
	ra_hours = PM.DDDH(ra_deg2)

	out_ra_hours = PM.DHHour(ra_hours)
	out_ra_minutes = PM.DHMin(ra_hours)
	out_ra_seconds = PM.DHSec(ra_hours)
	out_dec_degrees = PM.DDDeg(dec_deg)
	out_dec_minutes = PM.DDMin(dec_deg)
	out_dec_seconds = PM.DDSec(dec_deg)

	return out_ra_hours,out_ra_minutes,out_ra_seconds,out_dec_degrees,out_dec_minutes,out_dec_seconds

## @brief Convert Equatorial Coordinates to Ecliptic Coordinates
def equatorial_coordinate_to_ecliptic_coordinate(ra_hours,ra_minutes,ra_seconds,dec_degrees,dec_minutes,dec_seconds,gw_day,gw_month,gw_year):
	ra_deg = PM.DHDD(PM.HMSDH(ra_hours,ra_minutes,ra_seconds))
	dec_deg = PM.DMSDD(dec_degrees,dec_minutes,dec_seconds)
	ra_rad = math.radians(ra_deg)
	dec_rad = math.radians(dec_deg)
	obliq_deg = PM.Obliq(gw_day,gw_month,gw_year)
	obliq_rad = math.radians(obliq_deg)
	sin_ecl_lat = math.sin(dec_rad) * math.cos(obliq_rad) - math.cos(dec_rad) * math.sin(obliq_rad) * math.sin(ra_rad)
	ecl_lat_rad = math.asin(sin_ecl_lat)
	ecl_lat_deg = PM.Degrees(ecl_lat_rad)
	y = math.sin(ra_rad) * math.cos(obliq_rad) + math.tan(dec_rad) * math.sin(obliq_rad)
	x = math.cos(ra_rad)
	ecl_long_rad = PM.Atan2(x,y)
	ecl_long_deg1 = PM.Degrees(ecl_long_rad)
	ecl_long_deg2 = ecl_long_deg1 - 360 * math.floor(ecl_long_deg1/360)

	out_ecl_long_deg = PM.DDDeg(ecl_long_deg2)
	out_ecl_long_min = PM.DDMin(ecl_long_deg2)
	out_ecl_long_sec = PM.DDSec(ecl_long_deg2)
	out_ecl_lat_deg = PM.DDDeg(ecl_lat_deg)
	out_ecl_lat_min = PM.DDMin(ecl_lat_deg)
	out_ecl_lat_sec = PM.DDSec(ecl_lat_deg)

	return out_ecl_long_deg,out_ecl_long_min,out_ecl_long_sec,out_ecl_lat_deg,out_ecl_lat_min,out_ecl_lat_sec

## @brief Convert Equatorial Coordinates to Galactic Coordinates
def equatorial_coordinate_to_galactic_coordinate(ra_hours,ra_minutes,ra_seconds,dec_degrees,dec_minutes,dec_seconds):
	ra_deg = PM.DHDD(PM.HMSDH(ra_hours,ra_minutes,ra_seconds))
	dec_deg = PM.DMSDD(dec_degrees,dec_minutes,dec_seconds)
	ra_rad = math.radians(ra_deg)
	dec_rad = math.radians(dec_deg)
	sin_b = math.cos(dec_rad) * math.cos(math.radians(27.4)) * math.cos(ra_rad - math.radians(192.25)) + math.sin(dec_rad) * math.sin(math.radians(27.4))
	b_radians = math.asin(sin_b)
	b_deg = PM.Degrees(b_radians)
	y = math.sin(dec_rad) - sin_b * math.sin(math.radians(27.4))
	x = math.cos(dec_rad) * math.sin(ra_rad - math.radians(192.25)) * math.cos(math.radians(27.4))
	long_deg1 = PM.Degrees(PM.Atan2(x,y)) + 33
	long_deg2 = long_deg1 - 360 * math.floor(long_deg1/360)

	gal_long_deg = PM.DDDeg(long_deg2)
	gal_long_min = PM.DDMin(long_deg2)
	gal_long_sec = PM.DDSec(long_deg2)
	gal_lat_deg = PM.DDDeg(b_deg)
	gal_lat_min = PM.DDMin(b_deg)
	gal_lat_sec = PM.DDSec(b_deg)

	return gal_long_deg,gal_long_min,gal_long_sec,gal_lat_deg,gal_lat_min,gal_lat_sec

## @brief Convert Galactic Coordinates to Equatorial Coordinates
def galactic_coordinate_to_equatorial_coordinate(gal_long_deg,gal_long_min,gal_long_sec,gal_lat_deg,gal_lat_min,gal_lat_sec):
	glong_deg = PM.DMSDD(gal_long_deg,gal_long_min,gal_long_sec)
	glat_deg = PM.DMSDD(gal_lat_deg,gal_lat_min,gal_lat_sec)
	glong_rad = math.radians(glong_deg)
	glat_rad = math.radians(glat_deg)
	sin_dec = math.cos(glat_rad) * math.cos(math.radians(27.4)) * math.sin(glong_rad - math.radians(33)) + math.sin(glat_rad) * math.sin(math.radians(27.4))
	dec_radians = math.asin(sin_dec)
	dec_deg = PM.Degrees(dec_radians)
	y = math.cos(glat_rad) *math.cos(glong_rad - math.radians(33))
	x = math.sin(glat_rad) * math.cos(math.radians(27.4)) - math.cos(glat_rad) * math.sin(math.radians(27.4)) * math.sin(glong_rad - math.radians(33))
	
	ra_deg1 = PM.Degrees(PM.Atan2(x,y)) + 192.25
	ra_deg2 = ra_deg1 - 360 * math.floor(ra_deg1/360)
	ra_hours1 = PM.DDDH(ra_deg2)

	ra_hours = PM.DHHour(ra_hours1)
	ra_minutes = PM.DHMin(ra_hours1)
	ra_seconds = PM.DHSec(ra_hours1)
	dec_degrees = PM.DDDeg(dec_deg)
	dec_minutes = PM.DDMin(dec_deg)
	dec_seconds = PM.DDSec(dec_deg)

	return ra_hours,ra_minutes,ra_seconds,dec_degrees,dec_minutes,dec_seconds
