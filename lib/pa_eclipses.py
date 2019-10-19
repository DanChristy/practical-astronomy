import math
from . import pa_macro as PM

def lunar_eclipse_occurrence(local_date_day,local_date_month,local_date_year,is_daylight_saving,zone_correction_hours):
	"""
	Determine if a lunar eclipse is likely to occur.

	Arguments:
		local_date_day -- Local date, day part.
		local_date_month -- Local date, month part.
		local_date_year -- Local date, year part.
		is_daylight_saving -- Is daylight savings in effect?
		zone_correction_hours -- Time zone correction, in hours.

	Returns:
		status -- One of "Lunar eclipse certain", "Lunar eclipse possible", or "No lunar eclipse".
		event_date_day -- Date of eclipse event (day).
		event_date_month -- Date of eclipse event (month).
		event_date_year -- Date of eclipse event (year).
	"""
	daylight_saving = 1 if is_daylight_saving == True else 0

	julian_date_of_full_moon = PM.full_moon(daylight_saving,zone_correction_hours,local_date_day,local_date_month,local_date_year)
	g_date_of_full_moon_day = PM.jdc_day(julian_date_of_full_moon)
	integer_day = math.floor(g_date_of_full_moon_day)
	g_date_of_full_moon_month = PM.jdc_month(julian_date_of_full_moon)
	g_date_of_full_moon_year = PM.jdc_year(julian_date_of_full_moon)
	ut_of_full_moon_hours = g_date_of_full_moon_day - integer_day
	local_civil_time_hours = PM.ut_lct(ut_of_full_moon_hours,0,0,daylight_saving,zone_correction_hours,integer_day,g_date_of_full_moon_month,g_date_of_full_moon_year)
	local_civil_date_day = PM.ut_lc_day(ut_of_full_moon_hours,0,0,daylight_saving,zone_correction_hours,integer_day,g_date_of_full_moon_month,g_date_of_full_moon_year)
	local_civil_date_month = PM.ut_lc_month(ut_of_full_moon_hours,0,0,daylight_saving,zone_correction_hours,integer_day,g_date_of_full_moon_month,g_date_of_full_moon_year)
	local_civil_date_year = PM.ut_lc_year(ut_of_full_moon_hours,0,0,daylight_saving,zone_correction_hours,integer_day,g_date_of_full_moon_month,g_date_of_full_moon_year)
	eclipse_occurrence = PM.lunar_eclipse_occurrence(daylight_saving,zone_correction_hours,local_date_day,local_date_month,local_date_year)

	status = eclipse_occurrence
	event_date_day = local_civil_date_day
	event_date_month = local_civil_date_month
	event_date_year = local_civil_date_year

	return status,event_date_day,event_date_month,event_date_year
