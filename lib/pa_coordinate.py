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

## @brief Calculate the angle between two celestial objects
def angle_between_two_objects(ra_long_1_hour_deg,ra_long_1_min,ra_long_1_sec,dec_lat_1_deg,dec_lat_1_min,dec_lat_1_sec,ra_long_2_hour_deg,ra_long_2_min,ra_long_2_sec,dec_lat_2_deg,dec_lat_2_min,dec_lat_2_sec,hour_or_degree):
	ra_long_1_decimal = PM.HMSDH(ra_long_1_hour_deg,ra_long_1_min,ra_long_1_sec) if hour_or_degree == "H" else PM.DMSDD(ra_long_1_hour_deg,ra_long_1_min,ra_long_1_sec)
	ra_long_1_deg = PM.DHDD(ra_long_1_decimal) if hour_or_degree == "H" else ra_long_1_decimal
	ra_long_1_rad = math.radians(ra_long_1_deg)
	dec_lat_1_deg1 = PM.DMSDD(dec_lat_1_deg,dec_lat_1_min,dec_lat_1_sec)
	dec_lat_1_rad = math.radians(dec_lat_1_deg1)

	ra_long_2_decimal = PM.HMSDH(ra_long_2_hour_deg,ra_long_2_min,ra_long_2_sec) if hour_or_degree == "H" else PM.DMSDD(ra_long_2_hour_deg,ra_long_2_min,ra_long_2_sec)
	ra_long_2_deg = PM.DHDD(ra_long_2_decimal) if hour_or_degree == "H" else ra_long_2_decimal
	ra_long_2_rad = math.radians(ra_long_2_deg)
	dec_lat_2_deg1 = PM.DMSDD(dec_lat_2_deg,dec_lat_2_min,dec_lat_2_sec)
	dec_lat_2_rad = math.radians(dec_lat_2_deg1)

	cos_d = math.sin(dec_lat_1_rad) * math.sin(dec_lat_2_rad) + math.cos(dec_lat_1_rad) * math.cos(dec_lat_2_rad) * math.cos(ra_long_1_rad - ra_long_2_rad)
	d_rad = math.acos(cos_d)
	d_deg = PM.Degrees(d_rad)

	angle_deg = PM.DDDeg(d_deg)
	angle_min = PM.DDMin(d_deg)
	angle_sec = PM.DDSec(d_deg)

	return angle_deg,angle_min,angle_sec

## @brief Rising and setting times
# @param ra_hours		Right Ascension, in hours.
# @param ra_minutes		Right Ascension, in minutes.
# @param ra_seconds		Right Ascension, in seconds.
# @param dec_deg		Declination, in degrees.
# @param dec_min		Declination, in minutes.
# @param dec_sec		Declination, in seconds.
# @param gw_date_day	Greenwich Date, day part.
# @param gw_date_month	Greenwich Date, month part.
# @param gw_date_year	Greenwich Date, year part.
# @param geog_long_deg	Geographical Longitude, in degrees.
# @param geog_lat_deg	Geographical Latitude, in degrees.
# @param vert_shift_deg	Vertical Shift, in degrees.
# @return
# @arg @b rise_set_status	"Never Rises", "Circumpolar", or "OK".
# @arg @b ut_rise_hour		Rise time, UT, hour part.
# @arg @b ut_rise_min		Rise time, UT, minute part.
# @arg @b ut_set_hour		Set time, UT, hour part.
# @arg @b ut_set_min		Set time, UT, minute part.
# @arg @b az_rise			Azimuth angle, at rise.
# @arg @b az_set			Azimuth angle, at set.
def rising_and_setting(ra_hours,ra_minutes,ra_seconds,dec_deg,dec_min,dec_sec,gw_date_day,gw_date_month,gw_date_year,geog_long_deg,geog_lat_deg,vert_shift_deg):
	ra_hours1 = PM.HMSDH(ra_hours,ra_minutes,ra_seconds)
	dec_rad = math.radians(PM.DMSDD(dec_deg,dec_min,dec_sec))
	vertical_displ_radians = math.radians(vert_shift_deg)
	geo_lat_radians = math.radians(geog_lat_deg)
	cos_h = -(math.sin(vertical_displ_radians) + math.sin(geo_lat_radians) * math.sin(dec_rad)) / (math.cos(geo_lat_radians) * math.cos(dec_rad))
	h_hours = PM.DDDH(PM.Degrees(math.acos(cos_h)))
	lst_rise_hours = (ra_hours1-h_hours)-24*math.floor((ra_hours1-h_hours)/24)
	lst_set_hours = (ra_hours1+h_hours)-24*math.floor((ra_hours1+h_hours)/24)
	a_deg = PM.Degrees(math.acos((math.sin(dec_rad)+math.sin(vertical_displ_radians)*math.sin(geo_lat_radians))/(math.cos(vertical_displ_radians)*math.cos(geo_lat_radians))))
	az_rise_deg = a_deg - 360 * math.floor(a_deg/360)
	az_set_deg = (360-a_deg)-360*math.floor((360-a_deg)/360)
	ut_rise_hours1 = PM.GSTUT(PM.LSTGST(lst_rise_hours,0,0,geog_long_deg),0,0,gw_date_day,gw_date_month,gw_date_year)
	ut_set_hours1 = PM.GSTUT(PM.LSTGST(lst_set_hours,0,0,geog_long_deg),0,0,gw_date_day,gw_date_month,gw_date_year)
	ut_rise_adjusted_hours = ut_rise_hours1 + 0.008333
	ut_set_adjusted_hours = ut_set_hours1 + 0.008333

	rise_set_status = "never rises" if cos_h > 1 else "circumpolar" if cos_h < -1 else "OK"
	ut_rise_hour = PM.DHHour(ut_rise_adjusted_hours) if rise_set_status == "OK" else None
	ut_rise_min = PM.DHMin(ut_rise_adjusted_hours) if rise_set_status == "OK" else None
	ut_set_hour = PM.DHHour(ut_set_adjusted_hours) if rise_set_status == "OK" else None
	ut_set_min = PM.DHMin(ut_set_adjusted_hours) if rise_set_status == "OK" else None
	az_rise = round(az_rise_deg,2) if rise_set_status == "OK" else None
	az_set = round(az_set_deg,2) if rise_set_status == "OK" else None

	return rise_set_status,ut_rise_hour,ut_rise_min,ut_set_hour,ut_set_min,az_rise,az_set

## @brief Calculate precession (corrected coordinates between two epochs)
# @return corrected RA hour, corrected RA minutes, corrected RA seconds, corrected Declination degrees, corrected Declination minutes, corrected Declination seconds
def correct_for_precession(ra_hour,ra_minutes,ra_seconds,dec_deg,dec_minutes,dec_seconds,epoch1_day,epoch1_month,epoch1_year,epoch2_day,epoch2_month,epoch2_year):
	ra_1_rad = math.radians(PM.DHDD(PM.HMSDH(ra_hour,ra_minutes,ra_seconds)))
	dec_1_rad = math.radians(PM.DMSDD(dec_deg,dec_minutes,dec_seconds))
	t_centuries = (PM.CDJD(epoch1_day,epoch1_month,epoch1_year)-2415020)/36525
	m_sec = 3.07234+(0.00186*t_centuries)
	n_arcsec = 20.0468-(0.0085*t_centuries)
	n_years = (PM.CDJD(epoch2_day,epoch2_month,epoch2_year)-PM.CDJD(epoch1_day,epoch1_month,epoch1_year))/365.25
	s1_hours = ((m_sec+(n_arcsec*math.sin(ra_1_rad)*math.tan(dec_1_rad)/15))*n_years)/3600
	ra_2_hours = PM.HMSDH(ra_hour,ra_minutes,ra_seconds)+s1_hours
	s2_deg = (n_arcsec*math.cos(ra_1_rad)*n_years)/3600
	dec_2_deg = PM.DMSDD(dec_deg,dec_minutes,dec_seconds)+s2_deg

	corrected_ra_hour = PM.DHHour(ra_2_hours)
	corrected_ra_minutes = PM.DHMin(ra_2_hours)
	corrected_ra_seconds = PM.DHSec(ra_2_hours)
	corrected_dec_deg = PM.DDDeg(dec_2_deg)
	corrected_dec_minutes = PM.DDMin(dec_2_deg)
	corrected_dec_seconds = PM.DDSec(dec_2_deg)

	return corrected_ra_hour,corrected_ra_minutes,corrected_ra_seconds,corrected_dec_deg,corrected_dec_minutes,corrected_dec_seconds

## @brief Calculate nutation for two values: ecliptic longitude and obliquity, for a Greenwich date.
# @return nutation in ecliptic longitude (degrees), nutation in obliquity (degrees)
def nutation_in_ecliptic_longitude_and_obliquity(greenwich_day, greenwich_month, greenwich_year):
	jd_days = PM.CDJD(greenwich_day,greenwich_month,greenwich_year)
	t_centuries = (jd_days - 2415020) /36525
	a_deg = 100.0021358 * t_centuries
	l_1_deg = 279.6967 + (0.000303 * t_centuries * t_centuries)
	l_deg1 = l_1_deg + 360 * (a_deg - math.floor(a_deg))
	l_deg2 = l_deg1 - 360 * math.floor(l_deg1/360)
	l_rad = math.radians(l_deg2)
	b_deg = 5.372617 * t_centuries
	n_deg1 = 259.1833 - 360 * (b_deg - math.floor(b_deg))
	n_deg2 = n_deg1 - 360 * (math.floor(n_deg1/360))
	n_rad = math.radians(n_deg2)
	nut_in_long_arcsec = -17.2 * math.sin(n_rad) - 1.3 * math.sin(2 * l_rad)
	nut_in_obl_arcsec = 9.2 * math.cos(n_rad) + 0.5 * math.cos(2 * l_rad)

	nut_in_long_deg = nut_in_long_arcsec / 3600
	nut_in_obl_deg = nut_in_obl_arcsec / 3600

	return nut_in_long_deg,nut_in_obl_deg

## @brief Correct ecliptic coordinates for the effects of aberration.
# @return apparent ecliptic longitude (degrees, minutes, seconds), apparent ecliptic latitude (degrees, minutes, seconds)
def correct_for_aberration(ut_hour,ut_minutes,ut_seconds,gw_day,gw_month,gw_year,true_ecl_long_deg,true_ecl_long_min,true_ecl_long_sec,true_ecl_lat_deg,true_ecl_lat_min,true_ecl_lat_sec):
	true_long_deg = PM.DMSDD(true_ecl_long_deg,true_ecl_long_min,true_ecl_long_sec)
	true_lat_deg = PM.DMSDD(true_ecl_lat_deg,true_ecl_lat_min,true_ecl_lat_sec)
	sun_true_long_deg = PM.SunLong(ut_hour,ut_minutes,ut_seconds,0,0,gw_day,gw_month,gw_year)
	dlong_arcsec = -20.5 * math.cos(math.radians(sun_true_long_deg-true_long_deg))/math.cos(math.radians(true_lat_deg))
	dlat_arcsec = -20.5 * math.sin(math.radians(sun_true_long_deg-true_long_deg))*math.sin(math.radians(true_lat_deg))
	apparent_long_deg = true_long_deg + (dlong_arcsec/3600)
	apparent_lat_deg = true_lat_deg + (dlat_arcsec / 3600)

	apparent_ecl_long_deg = PM.DDDeg(apparent_long_deg)
	apparent_ecl_long_min = PM.DDMin(apparent_long_deg)
	apparent_ecl_long_sec = PM.DDSec(apparent_long_deg)
	apparent_ecl_lat_deg = PM.DDDeg(apparent_lat_deg)
	apparent_ecl_lat_min = PM.DDMin(apparent_lat_deg)
	apparent_ecl_lat_sec = PM.DDSec(apparent_lat_deg)

	return apparent_ecl_long_deg,apparent_ecl_long_min,apparent_ecl_long_sec,apparent_ecl_lat_deg,apparent_ecl_lat_min,apparent_ecl_lat_sec

## @brief Calculate corrected RA/Dec, accounting for atmospheric refraction.
# NOTE: Valid values for coordinate_type are "TRUE" and "APPARENT".
# @return corrected RA hours,minutes,seconds and corrected Declination degrees,minutes,seconds
def atmospheric_refraction(true_ra_hour,true_ra_min,true_ra_sec,true_dec_deg,true_dec_min,true_dec_sec,coordinate_type,geog_long_deg,geog_lat_deg,daylight_saving_hours,timezone_hours,lcd_day,lcd_month,lcd_year,lct_hour,lct_min,lct_sec,atmospheric_pressure_mbar,atmospheric_temperature_celsius):
	ha_hour = PM.RAHA(true_ra_hour,true_ra_min,true_ra_sec,lct_hour,lct_min,lct_sec,daylight_saving_hours,timezone_hours,lcd_day,lcd_month,lcd_year,geog_long_deg)

	azimuth_deg = PM.EQAz(ha_hour,0,0,true_dec_deg,true_dec_min,true_dec_sec,geog_lat_deg)

	altitude_deg = PM.EQAlt(ha_hour,0,0,true_dec_deg,true_dec_min,true_dec_sec,geog_lat_deg)
	
	corrected_altitude_deg = PM.Refract(altitude_deg,coordinate_type,atmospheric_pressure_mbar,atmospheric_temperature_celsius)

	corrected_ha_hour = PM.HORHa(azimuth_deg,0,0,corrected_altitude_deg,0,0,geog_lat_deg)
	corrected_ra_hour1 = PM.HARA(corrected_ha_hour,0,0,lct_hour,lct_min,lct_sec,daylight_saving_hours,timezone_hours,lcd_day,lcd_month,lcd_year,geog_long_deg)
	corrected_dec_deg1 = PM.HORDec(azimuth_deg,0,0,corrected_altitude_deg,0,0,geog_lat_deg)

	corrected_ra_hour = PM.DHHour(corrected_ra_hour1)
	corrected_ra_min = PM.DHMin(corrected_ra_hour1)
	corrected_ra_sec = PM.DHSec(corrected_ra_hour1)
	corrected_dec_deg = PM.DDDeg(corrected_dec_deg1)
	corrected_dec_min = PM.DDMin(corrected_dec_deg1)
	corrected_dec_sec = PM.DDSec(corrected_dec_deg1)

	return corrected_ra_hour,corrected_ra_min,corrected_ra_sec,corrected_dec_deg,corrected_dec_min,corrected_dec_sec

## @brief Calculate corrected RA/Dec, accounting for geocentric parallax.
# NOTE: Valid values for coordinate_type are "TRUE" and "APPARENT".
# @return corrected RA hours,minutes,seconds and corrected Declination degrees,minutes,seconds
def corrections_for_geocentric_parallax(ra_hour,ra_min,ra_sec,dec_deg,dec_min,dec_sec,coordinate_type,equatorial_hor_parallax_deg,geog_long_deg,geog_lat_deg,height_m,daylight_saving,timezone_hours,lcd_day,lcd_month,lcd_year,lct_hour,lct_min,lct_sec):
	ha_hours = PM.RAHA(ra_hour,ra_min,ra_sec,lct_hour,lct_min,lct_sec,daylight_saving,timezone_hours,lcd_day,lcd_month,lcd_year,geog_long_deg)

	corrected_ha_hours = PM.ParallaxHA(ha_hours,0,0,dec_deg,dec_min,dec_sec,coordinate_type,geog_lat_deg,height_m,equatorial_hor_parallax_deg)

	corrected_ra_hours = PM.HARA(corrected_ha_hours,0,0,lct_hour,lct_min,lct_sec,daylight_saving,timezone_hours,lcd_day,lcd_month,lcd_year,geog_long_deg)

	corrected_dec_deg1 = PM.ParallaxDec(ha_hours,0,0,dec_deg,dec_min,dec_sec,coordinate_type,geog_lat_deg,height_m,equatorial_hor_parallax_deg)

	corrected_ra_hour = PM.DHHour(corrected_ra_hours)
	corrected_ra_min = PM.DHMin(corrected_ra_hours)
	corrected_ra_sec = PM.DHSec(corrected_ra_hours)
	corrected_dec_deg = PM.DDDeg(corrected_dec_deg1)
	corrected_dec_min = PM.DDMin(corrected_dec_deg1)
	corrected_dec_sec = PM.DDSec(corrected_dec_deg1)

	return corrected_ra_hour,corrected_ra_min,corrected_ra_sec,corrected_dec_deg,corrected_dec_min,corrected_dec_sec

## @brief Calculate heliographic coordinates for a given Greenwich date, with a given heliographic position angle and heliographic displacement in arc minutes.
# @return heliographic longitude and heliographic latitude, in degrees
def heliographic_coordinates(helio_position_angle_deg,helio_displacement_arcmin,gwdate_day,gwdate_month,gwdate_year):
	julian_date_days = PM.CDJD(gwdate_day,gwdate_month,gwdate_year)
	t_centuries = (julian_date_days-2415020)/36525
	long_asc_node_deg = PM.DMSDD(74,22,0)+(84*t_centuries/60)
	sun_long_deg = PM.SunLong(0,0,0,0,0,gwdate_day,gwdate_month,gwdate_year)
	y = math.sin(math.radians(long_asc_node_deg-sun_long_deg))*math.cos(math.radians(PM.DMSDD(7,15,0)))
	x = -math.cos(math.radians(long_asc_node_deg-sun_long_deg))
	a_deg = PM.Degrees(PM.Atan2(x,y))
	m_deg1 = 360-(360*(julian_date_days-2398220)/25.38)
	m_deg2 = m_deg1-360*math.floor(m_deg1/360)
	l0_deg1 = m_deg2 + a_deg
	l0_deg2 = l0_deg1-360*math.floor(l0_deg1/360)
	b0_rad = math.asin(math.sin(math.radians(sun_long_deg-long_asc_node_deg))*math.sin(math.radians(PM.DMSDD(7,15,0))))
	theta1_rad = math.atan(-math.cos(math.radians(sun_long_deg))*math.tan(math.radians(PM.Obliq(gwdate_day,gwdate_month,gwdate_year))))
	theta2_rad = math.atan(-math.cos(math.radians(long_asc_node_deg-sun_long_deg))*math.tan(math.radians(PM.DMSDD(7,15,0))))
	p_deg = PM.Degrees(theta1_rad+theta2_rad)
	rho1_deg = helio_displacement_arcmin/60
	rho_rad = math.asin(2*rho1_deg/PM.SunDia(0,0,0,0,0,gwdate_day,gwdate_month,gwdate_year))-math.radians(rho1_deg)
	b_rad = math.asin(math.sin(b0_rad)*math.cos(rho_rad)+math.cos(b0_rad)*math.sin(rho_rad)*math.cos(math.radians(p_deg-helio_position_angle_deg)))
	b_deg = PM.Degrees(b_rad)
	l_deg1 = PM.Degrees(math.asin(math.sin(rho_rad)*math.sin(math.radians(p_deg-helio_position_angle_deg))/math.cos(b_rad)))+l0_deg1
	l_deg2 = l_deg1-360*math.floor(l_deg1/360)

	helio_long_deg = round(l_deg2,2)
	helio_lat_deg = round(b_deg,2)

	return helio_long_deg,helio_lat_deg
