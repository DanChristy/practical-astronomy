#!/usr/bin/python3

import lib.pa_moon as PMO
import unittest as UT

class test_moon_position(UT.TestCase):
	def setUp(self):
		self.lct_hour = 0 
		self.lct_min = 0 
		self.lct_sec = 0 
		self.is_daylight_saving = False 
		self.zone_correction_hours = 0 
		self.local_date_day = 1 
		self.local_date_month = 9 
		self.local_date_year = 2003 

	def test_approximate_position_of_moon(self):
		moon_ra_hour, moon_ra_min, moon_ra_sec, moon_dec_deg, moon_dec_min, moon_dec_sec = PMO.approximate_position_of_moon(self.lct_hour, self.lct_min, self.lct_sec, self.is_daylight_saving, self.zone_correction_hours, self.local_date_day, self.local_date_month, self.local_date_year)

		print(f"Approximate position of Moon: [Local Time] {self.lct_hour}:{self.lct_min}:{self.lct_sec} [DST?] {self.is_daylight_saving} [Zone Correction] {self.zone_correction_hours} [Local Date] {self.local_date_month}/{self.local_date_day}/{self.local_date_year} = [Right Ascension] {moon_ra_hour}h {moon_ra_min}m {moon_ra_sec}s [Declination] {moon_dec_deg}d {moon_dec_min}m {moon_dec_sec}s")

		self.assertEqual(moon_ra_hour,14,"Moon RA (hour)")
		self.assertEqual(moon_ra_min,12,"Moon RA (minutes)")
		self.assertEqual(moon_ra_sec,42.31,"Moon RA (seconds)")
		self.assertEqual(moon_dec_deg,-11, "Moon Declination (degrees)")
		self.assertEqual(moon_dec_min,31,"Moon Declination (minutes)")
		self.assertEqual(moon_dec_sec,38.27,"Moon Declination (seconds)")

	def test_precise_position_of_moon(self):
		moon_ra_hour, moon_ra_min, moon_ra_sec, moon_dec_deg, moon_dec_min, moon_dec_sec, earth_moon_dist_km, moon_hor_parallax_deg = PMO.precise_position_of_moon(self.lct_hour, self.lct_min, self.lct_sec, self.is_daylight_saving, self.zone_correction_hours, self.local_date_day, self.local_date_month, self.local_date_year)

		print(f"Precise position of Moon: [Local Time] {self.lct_hour}:{self.lct_min}:{self.lct_sec} [DST?] {self.is_daylight_saving} [Zone Correction] {self.zone_correction_hours} [Local Date] {self.local_date_month}/{self.local_date_day}/{self.local_date_year} = [Right Ascension] {moon_ra_hour}h {moon_ra_min}m {moon_ra_sec}s [Declination] {moon_dec_deg}d {moon_dec_min}m {moon_dec_sec}s [Earth-Moon distance] {earth_moon_dist_km} km [Horizontal Parallax] {moon_hor_parallax_deg} degrees")

		self.assertEqual(moon_ra_hour,14,"Moon RA (hour)")
		self.assertEqual(moon_ra_min,12,"Moon RA (minutes)")
		self.assertEqual(moon_ra_sec,10.21,"Moon RA (seconds)")
		self.assertEqual(moon_dec_deg,-11, "Moon Declination (degrees)")
		self.assertEqual(moon_dec_min,34,"Moon Declination (minutes)")
		self.assertEqual(moon_dec_sec,57.83,"Moon Declination (seconds)")
		self.assertEqual(earth_moon_dist_km,367964,"Earth-Moon distance (km)")
		self.assertEqual(moon_hor_parallax_deg,0.993191,"Moon Horizontal Parallax (degrees)")

	def test_moon_phase(self):
		moon_phase, pa_bright_limb_deg = PMO.moon_phase(self.lct_hour, self.lct_min, self.lct_sec, self.is_daylight_saving, self.zone_correction_hours, self.local_date_day, self.local_date_month, self.local_date_year)

		print(f"Moon phase: [Local Time] {self.lct_hour}:{self.lct_min}:{self.lct_sec} [DST?] {self.is_daylight_saving} [Zone Correction] {self.zone_correction_hours} [Local Date] {self.local_date_month}/{self.local_date_day}/{self.local_date_year} = [Phase] {moon_phase} [Position Angle of Bright Limb] {pa_bright_limb_deg}")

		self.assertEqual(moon_phase,0.22,"Moon Phase")
		self.assertEqual(pa_bright_limb_deg,-71.58,"Position Angle of Bright Limb")


if __name__ == '__main__':
	UT.main()
