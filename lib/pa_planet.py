import math
from . import pa_macro as PM

PlanetData = {
	"Mercury": {
		"Tp": 0.24085,
		"Long": 75.5671,
		"Peri": 77.612,
		"Ecc": 0.205627,
		"Axis": 0.387098,
		"Incl": 7.0051,
		"Node": 48.449
	},
	"Venus": {
		"Tp": 0.615207,
		"Long": 272.30044,
		"Peri": 131.54,
		"Ecc": 0.006812,
		"Axis": 0.723329,
		"Incl": 3.3947,
		"Node": 76.769
	},
	"Earth": {
		"Tp": 0.999996,
		"Long": 99.556772,
		"Peri": 103.2055,
		"Ecc": 0.016671,
		"Axis": 0.999985,
		"Incl": None,
		"Node": None
	},
	"Mars": {
		"Tp": 1.880765,
		"Long": 109.09646,
		"Peri": 336.217,
		"Ecc": 0.093348,
		"Axis": 1.523689,
		"Incl": 1.8497,
		"Node": 49.632
	},
	"Jupiter": {
		"Tp": 11.857911,
		"Long": 337.917132,
		"Peri": 14.6633,
		"Ecc": 0.048907,
		"Axis": 5.20278,
		"Incl": 1.3035,
		"Node": 100.595
	},
	"Saturn": {
		"Tp": 29.310579,
		"Long": 172.398316,
		"Peri": 89.567,
		"Ecc": 0.053853,
		"Axis": 9.51134,
		"Incl": 2.4873,
		"Node": 113.752
	},
	"Uranus": {
		"Tp": 84.039492,
		"Long": 271.063148,
		"Peri": 172.884833,
		"Ecc": 0.046321,
		"Axis": 19.21814,
		"Incl": 0.773059,
		"Node": 73.926961
	},
	"Neptune": {
		"Tp": 165.845392,
		"Long": 326.895127,
		"Peri": 23.07,
		"Ecc": 0.010483,
		"Axis": 30.1985,
		"Incl": 1.7673,
		"Node": 131.879
	}
}

def approximate_position_of_planet(lct_hour, lct_min, lct_sec, is_daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year, planet_name):
	"""
	Calculate approximate position of a planet.

	Parameters:
		lct_hour:				Local civil time, in hours.
		lct_min:				Local civil time, in minutes.
		lct_sec:				Local civil time, in seconds.
		is_daylight_saving:		Is daylight savings in effect?
		zone_correction_hours:	Time zone correction, in hours.
		local_date_day:			Local date, day part.
		local_date_month:		Local date, month part.
		local_date_year:		Local date, year part.
		planet_name				Name of planet, e.g., "Jupiter"

	Returns:
		planet_ra_hour:		Right ascension of planet (hour part)
		planet_ra_min:		Right ascension of planet (minutes part)
		planet_ra_sec:		Right ascension of planet (seconds part)
		planet_dec_deg:		Declination of planet (degrees part)
		planet_dec_min:		Declination of planet (minutes part)
		planet_dec_sec:		Declination of planet (seconds part)
	"""
	daylight_saving = 1 if is_daylight_saving == True else 0

	planet_tp_from_table = PlanetData.get(planet_name)['Tp']
	planet_long_from_table = PlanetData.get(planet_name)['Long']
	planet_peri_from_table = PlanetData.get(planet_name)['Peri']
	planet_ecc_from_table = PlanetData.get(planet_name)['Ecc']
	planet_axis_from_table = PlanetData.get(planet_name)['Axis']
	planet_incl_from_table = PlanetData.get(planet_name)['Incl']
	planet_node_from_table = PlanetData.get(planet_name)['Node']

	gdate_day = PM.lct_gday(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	gdate_month = PM.lct_gmonth(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	gdate_year = PM.lct_gyear(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)

	ut_hours = PM.lct_ut(lct_hour, lct_min, lct_sec, daylight_saving, zone_correction_hours, local_date_day, local_date_month, local_date_year)
	d_days = PM.cd_jd(gdate_day+(ut_hours/24),gdate_month,gdate_year) - PM.cd_jd(0,1,2010)
	np_deg1 = 360 * d_days / (365.242191 * planet_tp_from_table)
	np_deg2 = np_deg1 - 360 * math.floor(np_deg1/360)
	mp_deg = np_deg2 + planet_long_from_table - planet_peri_from_table
	lp_deg1 = np_deg2 + (360 * planet_ecc_from_table * math.sin(math.radians(mp_deg)) / math.pi) + planet_long_from_table
	lp_deg2 = lp_deg1 - 360 * math.floor(lp_deg1/360)
	planet_true_anomaly_deg = lp_deg2 - planet_peri_from_table
	r_au = planet_axis_from_table * (1 - (planet_ecc_from_table)**2) / (1 + planet_ecc_from_table * math.cos(math.radians(planet_true_anomaly_deg)))

	earth_tp_from_table = PlanetData.get("Earth")['Tp']
	earth_long_from_table = PlanetData.get("Earth")['Long']
	earth_peri_from_table = PlanetData.get("Earth")['Peri']
	earth_ecc_from_table = PlanetData.get("Earth")['Ecc']
	earth_axis_from_table = PlanetData.get("Earth")['Axis']
	
	ne_deg1 = 360*d_days/(365.242191*earth_tp_from_table)
	ne_deg2 = ne_deg1-360*math.floor(ne_deg1/360)
	me_deg = ne_deg2+earth_long_from_table-earth_peri_from_table
	le_deg1 = ne_deg2+earth_long_from_table+360*earth_ecc_from_table*math.sin(math.radians(me_deg))/math.pi
	le_deg2 = le_deg1-360*math.floor(le_deg1/360)
	earth_true_anomaly_deg = le_deg2-earth_peri_from_table
	r_au2 = earth_axis_from_table*(1-(earth_ecc_from_table)**2)/(1+earth_ecc_from_table*math.cos(math.radians(earth_true_anomaly_deg)))
	lp_node_rad = math.radians(lp_deg2-planet_node_from_table)
	psi_rad = math.asin(math.sin(lp_node_rad)*math.sin(math.radians(planet_incl_from_table)))
	y = math.sin(lp_node_rad)*math.cos(math.radians(planet_incl_from_table))
	x = math.cos(lp_node_rad)
	ld_deg = PM.degrees(PM.atan2(x,y))+planet_node_from_table
	rd_au = r_au*math.cos(psi_rad)
	le_ld_rad = math.radians(le_deg2-ld_deg)
	atan2_type_1 = PM.atan2(r_au2-rd_au*math.cos(le_ld_rad),rd_au*math.sin(le_ld_rad))
	atan2_type_2 = PM.atan2(rd_au-r_au2*math.cos(le_ld_rad),r_au2*math.sin(-le_ld_rad))
	a_rad = atan2_type_1 if rd_au < 1 else atan2_type_2 
	lamda_deg1 =  180 + le_deg2 + PM.degrees(a_rad) if rd_au < 1 else PM.degrees(a_rad) + ld_deg
	lamda_deg2 = lamda_deg1-360*math.floor(lamda_deg1/360)
	beta_deg = PM.degrees(math.atan(rd_au*math.tan(psi_rad)*math.sin(math.radians(lamda_deg2-ld_deg))/(r_au2*math.sin(-le_ld_rad))))
	ra_hours = PM.dd_dh(PM.ec_ra(lamda_deg2,0,0,beta_deg,0,0,gdate_day,gdate_month,gdate_year))
	dec_deg = PM.ec_dec(lamda_deg2,0,0,beta_deg,0,0,gdate_day,gdate_month,gdate_year)

	planet_ra_hour = PM.dh_hour(ra_hours)
	planet_ra_min = PM.dh_min(ra_hours)
	planet_ra_sec = PM.dh_sec(ra_hours)
	planet_dec_deg = PM.dd_deg(dec_deg)
	planet_dec_min = PM.dd_min(dec_deg)
	planet_dec_sec = PM.dd_sec(dec_deg)

	return planet_ra_hour, planet_ra_min, planet_ra_sec, planet_dec_deg, planet_dec_min, planet_dec_sec
