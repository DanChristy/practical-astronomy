import math
from . import pa_macro as PM

def approximate_position_of_moon(lct_hour, lct_min, lct_sec, is_daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year):
	"""
	Calculate approximate position of the Moon.

	Arguments:
		lct_hour -- Local civil time, in hours.
		lct_min -- Local civil time, in minutes.
		lct_sec -- Local civil time, in seconds.
		is_daylight_saving -- Is daylight savings in effect?
		zone_correction_hours -- Time zone correction, in hours.
		local_date_day -- Local date, day part.
		local_date_month -- Local date, month part.
		local_date_year -- Local date, year part.

	Returns:
		moon_ra_hour -- Right ascension of Moon (hour part)
		moon_ra_min -- Right ascension of Moon (minutes part)
		moon_ra_sec -- Right ascension of Moon (seconds part)
		moon_dec_deg -- Declination of Moon (degrees part)
		moon_dec_min -- Declination of Moon (minutes part)
		moon_dec_sec -- Declination of Moon (seconds part)
	"""
	daylight_saving = 1 if is_daylight_saving == True else 0

	l0 = 91.9293359879052
	p0 = 130.143076320618
	n0 = 291.682546643194
	i = 5.145396

	gdate_day = PM.lct_gday(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	gdate_month = PM.lct_gmonth(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	gdate_year = PM.lct_gyear(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)

	ut_hours = PM.lct_ut(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	d_days = PM.cd_jd(gdate_day,gdate_month,gdate_year)-PM.cd_jd(0,1,2010)+ut_hours/24
	sun_long_deg = PM.sun_long(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	sun_mean_anomaly_rad = PM.sun_mean_anomaly(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	lm_deg = PM.unwind_deg(13.1763966*d_days+l0)
	mm_deg = PM.unwind_deg(lm_deg-0.1114041*d_days-p0)
	n_deg = PM.unwind_deg(n0-(0.0529539*d_days))
	ev_deg = 1.2739*math.sin(math.radians(2*(lm_deg-sun_long_deg)-mm_deg))
	ae_deg = 0.1858*math.sin(sun_mean_anomaly_rad)
	a3_deg = 0.37*math.sin(sun_mean_anomaly_rad)
	mmd_deg = mm_deg+ev_deg-ae_deg-a3_deg
	ec_deg = 6.2886*math.sin(math.radians(mmd_deg))
	a4_deg = 0.214*math.sin(2*math.radians(mmd_deg))
	ld_deg = lm_deg+ev_deg+ec_deg-ae_deg+a4_deg
	v_deg = 0.6583*math.sin(2*math.radians(ld_deg-sun_long_deg))
	ldd_deg = ld_deg + v_deg
	nd_deg = n_deg-0.16*math.sin(sun_mean_anomaly_rad)
	y = math.sin(math.radians(ldd_deg-nd_deg))*math.cos(math.radians(i))
	x = math.cos(math.radians(ldd_deg-nd_deg))

	moon_long_deg = PM.unwind_deg(PM.degrees(PM.atan2(x,y))+nd_deg)
	moon_lat_deg = PM.degrees(math.asin(math.sin(math.radians(ldd_deg-nd_deg))*math.sin(math.radians(i))))
	moon_ra_hours1 = PM.dd_dh(PM.ec_ra(moon_long_deg,0,0,moon_lat_deg,0,0,gdate_day,gdate_month,gdate_year))
	moon_dec_deg1 = PM.ec_dec(moon_long_deg,0,0,moon_lat_deg,0,0,gdate_day,gdate_month,gdate_year)

	moon_ra_hour = PM.dh_hour(moon_ra_hours1)
	moon_ra_min = PM.dh_min(moon_ra_hours1)
	moon_ra_sec = PM.dh_sec(moon_ra_hours1)
	moon_dec_deg = PM.dd_deg(moon_dec_deg1)
	moon_dec_min = PM.dd_min(moon_dec_deg1)
	moon_dec_sec = PM.dd_sec(moon_dec_deg1)

	return moon_ra_hour, moon_ra_min, moon_ra_sec, moon_dec_deg, moon_dec_min, moon_dec_sec

def precise_position_of_moon(lct_hour, lct_min, lct_sec, is_daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year):
	"""
	Calculate approximate position of the Moon.

	Arguments:
		lct_hour -- Local civil time, in hours.
		lct_min -- Local civil time, in minutes.
		lct_sec -- Local civil time, in seconds.
		is_daylight_saving -- Is daylight savings in effect?
		zone_correction_hours -- Time zone correction, in hours.
		local_date_day -- Local date, day part.
		local_date_month -- Local date, month part.
		local_date_year -- Local date, year part.

	Returns:
		moon_ra_hour -- Right ascension of Moon (hour part)
		moon_ra_min -- Right ascension of Moon (minutes part)
		moon_ra_sec -- Right ascension of Moon (seconds part)
		moon_dec_deg -- Declination of Moon (degrees part)
		moon_dec_min -- Declination of Moon (minutes part)
		moon_dec_sec -- Declination of Moon (seconds part)
		earth_moon_dist_km -- Distance from Earth to Moon (km)
		moon_hor_parallax_deg -- Horizontal parallax of Moon (degrees)
	"""
	daylight_saving = 1 if is_daylight_saving == True else 0

	gdate_day = PM.lct_gday(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	gdate_month = PM.lct_gmonth(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	gdate_year = PM.lct_gyear(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)

	ut_hours = PM.lct_ut(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)

	moon_ecliptic_longitude_deg, moon_ecliptic_latitude_deg, moon_horizontal_parallax_deg = PM.moon_long_lat_hp(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)

	nutation_in_longitude_deg = PM.nutat_long(gdate_day,gdate_month,gdate_year)
	corrected_long_deg = moon_ecliptic_longitude_deg + nutation_in_longitude_deg
	earth_moon_distance_km = 6378.14/math.sin(math.radians(moon_horizontal_parallax_deg))
	moon_ra_hours_1 = PM.dd_dh(PM.ec_ra(corrected_long_deg,0,0,moon_ecliptic_latitude_deg,0,0,gdate_day,gdate_month,gdate_year))
	moon_dec_deg1 = PM.ec_dec(corrected_long_deg,0,0,moon_ecliptic_latitude_deg,0,0,gdate_day,gdate_month,gdate_year)

	moon_ra_hour = PM.dh_hour(moon_ra_hours_1)
	moon_ra_min = PM.dh_min(moon_ra_hours_1)
	moon_ra_sec = PM.dh_sec(moon_ra_hours_1)
	moon_dec_deg = PM.dd_deg(moon_dec_deg1)
	moon_dec_min = PM.dd_min(moon_dec_deg1)
	moon_dec_sec = PM.dd_sec(moon_dec_deg1)
	earth_moon_dist_km = round(earth_moon_distance_km,0)
	moon_hor_parallax_deg = round(moon_horizontal_parallax_deg,6)

	return moon_ra_hour, moon_ra_min, moon_ra_sec, moon_dec_deg, moon_dec_min, moon_dec_sec, earth_moon_dist_km, moon_hor_parallax_deg