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
