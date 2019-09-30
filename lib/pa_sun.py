import math
from . import pa_macro as PM

## @brief Calculate approximate position of the sun for a local date and time.
def approximate_position_of_sun(lct_hours, lct_minutes, lct_seconds, local_day, local_month, local_year, is_daylight_saving, zone_correction):
	daylight_saving = 1 if is_daylight_saving == True else 0

	greenwich_date_day = PM.lct_gday(lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year)
	greenwich_date_month = PM.lct_gmonth(lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year)
	greenwich_date_year = PM.lct_gyear(lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year)
	ut_hours = PM.lct_ut(lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year)
	ut_days = ut_hours / 24
	jd_days = PM.cd_jd(greenwich_date_day,greenwich_date_month,greenwich_date_year) + ut_days
	d_days = jd_days - PM.cd_jd(0,1,2010)
	n_deg = 360 * d_days / 365.242191
	m_deg1 = n_deg + PM.sun_e_long(0,1,2010) - PM.sun_peri(0,1,2010)
	m_deg2 = m_deg1 - 360 * math.floor(m_deg1/360)
	e_c_deg = 360 * PM.sun_ecc(0,1,2010) * math.sin(math.radians(m_deg2)) / math.pi
	l_s_deg1 = n_deg + e_c_deg + PM.sun_e_long(0,1,2010)
	l_s_deg2 = l_s_deg1 - 360 * math.floor(l_s_deg1/360)
	ra_deg = PM.ec_ra(l_s_deg2,0,0,0,0,0,greenwich_date_day,greenwich_date_month,greenwich_date_year)
	ra_hours = PM.dd_dh(ra_deg)
	dec_deg = PM.ec_dec(l_s_deg2,0,0,0,0,0,greenwich_date_day,greenwich_date_month,greenwich_date_year)

	sun_ra_hour = PM.dh_hour(ra_hours)
	sun_ra_min = PM.dh_min(ra_hours)
	sun_ra_sec = PM.dh_sec(ra_hours)
	sun_dec_deg = PM.dd_deg(dec_deg)
	sun_dec_min = PM.dd_min(dec_deg)
	sun_dec_sec = PM.dd_sec(dec_deg)

	return sun_ra_hour,sun_ra_min,sun_ra_sec,sun_dec_deg,sun_dec_min,sun_dec_sec

## @brief Calculate precise position of the sun for a local date and time.
def precise_position_of_sun(lct_hours, lct_minutes, lct_seconds, local_day, local_month, local_year, is_daylight_saving, zone_correction):
	daylight_saving = 1 if is_daylight_saving == True else 0

	g_day = PM.lct_gday(lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year)
	g_month = PM.lct_gmonth(lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year)
	g_year = PM.lct_gyear(lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year)
	sun_ecliptic_longitude_deg = PM.sun_long(lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year)
	ra_deg = PM.ec_ra(sun_ecliptic_longitude_deg,0,0,0,0,0,g_day,g_month,g_year)
	ra_hours = PM.dd_dh(ra_deg)
	dec_deg = PM.ec_dec(sun_ecliptic_longitude_deg,0,0,0,0,0,g_day,g_month,g_year)

	sun_ra_hour = PM.dh_hour(ra_hours)
	sun_ra_min = PM.dh_min(ra_hours)
	sun_ra_sec = PM.dh_sec(ra_hours)
	sun_dec_deg = PM.dd_deg(dec_deg)
	sun_dec_min = PM.dd_min(dec_deg)
	sun_dec_sec = PM.dd_sec(dec_deg)

	return sun_ra_hour,sun_ra_min,sun_ra_sec,sun_dec_deg,sun_dec_min,sun_dec_sec

## @brief Calculate distance to the Sun (in km), and angular size.
def sun_distance_and_angular_size(lct_hours, lct_minutes, lct_seconds, local_day, local_month, local_year, is_daylight_saving, zone_correction):
	daylight_saving = 1 if is_daylight_saving == True else 0

	g_day = PM.lct_gday(lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year)
	g_month = PM.lct_gmonth(lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year)
	g_year = PM.lct_gyear(lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year)
	true_anomaly_deg = PM.sun_true_anomaly(lct_hours,lct_minutes,lct_seconds,daylight_saving,zone_correction,local_day,local_month,local_year)
	true_anomaly_rad = math.radians(true_anomaly_deg)
	eccentricity = PM.sun_ecc(g_day,g_month,g_year)
	f = (1 + eccentricity * math.cos(true_anomaly_rad)) / (1 - eccentricity * eccentricity)
	r_km = 149598500 / f
	theta_deg = f * 0.533128

	sun_dist_km = round(r_km,-2)
	sun_ang_size_deg = PM.dd_deg(theta_deg)
	sun_ang_size_min = PM.dd_min(theta_deg)
	sun_ang_size_sec = PM.dd_sec(theta_deg)

	return sun_dist_km,sun_ang_size_deg,sun_ang_size_min,sun_ang_size_sec

## @brief Calculate local sunrise and sunset.
def sunrise_and_sunset(local_day, local_month, local_year, is_daylight_saving, zone_correction, geographical_long_deg, geographical_lat_deg):
	daylight_saving = 1 if is_daylight_saving == True else 0

	local_sunrise_hours = PM.sunrise_lct(local_day, local_month, local_year, daylight_saving, zone_correction, geographical_long_deg, geographical_lat_deg)

	local_sunset_hours = PM.sunset_lct(local_day, local_month, local_year, daylight_saving, zone_correction, geographical_long_deg, geographical_lat_deg)

	sun_rise_set_status = PM.e_sun_rs(local_day, local_month, local_year, daylight_saving, zone_correction, geographical_long_deg, geographical_lat_deg)

	adjusted_sunrise_hours = local_sunrise_hours + 0.008333
	adjusted_sunset_hours = local_sunset_hours + 0.008333
	azimuth_of_sunrise_deg1 = PM.sunrise_az(local_day, local_month, local_year, daylight_saving, zone_correction, geographical_long_deg, geographical_lat_deg)
	azimuth_of_sunset_deg1 = PM.sunset_az(local_day, local_month, local_year, daylight_saving, zone_correction, geographical_long_deg, geographical_lat_deg)

	local_sunrise_hour = PM.dh_hour(adjusted_sunrise_hours) if sun_rise_set_status == "OK" else None
	local_sunrise_minute = PM.dh_min(adjusted_sunrise_hours) if sun_rise_set_status == "OK" else None
	local_sunset_hour = PM.dh_hour(adjusted_sunset_hours) if sun_rise_set_status == "OK" else None
	local_sunset_minute = PM.dh_min(adjusted_sunset_hours) if sun_rise_set_status == "OK" else None
	azimuth_of_sunrise_deg = round(azimuth_of_sunrise_deg1,2) if sun_rise_set_status == "OK" else None
	azimuth_of_sunset_deg = round(azimuth_of_sunset_deg1,2) if sun_rise_set_status == "OK" else None
	status = sun_rise_set_status

	return local_sunrise_hour,local_sunrise_minute,local_sunset_hour,local_sunset_minute,azimuth_of_sunrise_deg,azimuth_of_sunset_deg,status

## @brief Calculate times of morning and evening twilight.
# @param twilight_type	"C" (civil), "N" (nautical), or "A" (astronomical)
def morning_and_evening_twilight(local_day, local_month, local_year, is_daylight_saving, zone_correction, geographical_long_deg, geographical_lat_deg, twilight_type):
	daylight_saving = 1 if is_daylight_saving == True else 0

	start_of_am_twilight_hours = PM.twilight_am_lct(local_day, local_month, local_year, daylight_saving, zone_correction, geographical_long_deg, geographical_lat_deg, twilight_type)

	end_of_pm_twilight_hours = PM.twilight_pm_lct(local_day, local_month, local_year, daylight_saving, zone_correction, geographical_long_deg, geographical_lat_deg, twilight_type)

	twilight_status = PM.e_twilight(local_day, local_month, local_year, daylight_saving, zone_correction, geographical_long_deg, geographical_lat_deg, twilight_type)

	adjusted_am_start_time = start_of_am_twilight_hours + 0.008333
	adjusted_pm_start_time = end_of_pm_twilight_hours + 0.008333

	am_twilight_begins_hour = PM.dh_hour(adjusted_am_start_time) if twilight_status == "OK" else None
	am_twilight_begins_min = PM.dh_min(adjusted_am_start_time) if twilight_status == "OK" else None
	pm_twilight_ends_hour = PM.dh_hour(adjusted_pm_start_time) if twilight_status == "OK" else None
	pm_twilight_ends_min = PM.dh_min(adjusted_pm_start_time) if twilight_status == "OK" else None
	status = twilight_status

	return am_twilight_begins_hour,am_twilight_begins_min,pm_twilight_ends_hour,pm_twilight_ends_min,status