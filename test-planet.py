#!/usr/bin/python3

import lib.pa_planet as PP
import unittest as UT

class test_approximate_position_of_planet(UT.TestCase):
	def setUp(self):
		self.lct_hour = 0 
		self.lct_min = 0 
		self.lct_sec = 0 
		self.is_daylight_saving = False 
		self.zone_correction_hours = 0 
		self.local_date_day = 22 
		self.local_date_month = 11 
		self.local_date_year = 2003 
		self.planet_name = "Jupiter"

	def test_approximate_position_of_planet(self):
		planet_ra_hour, planet_ra_min, planet_ra_sec, planet_dec_deg, planet_dec_min, planet_dec_sec = PP.approximate_position_of_planet(self.lct_hour,self.lct_min,self.lct_sec,self.is_daylight_saving,self.zone_correction_hours,self.local_date_day,self.local_date_month,self.local_date_year,self.planet_name)

		print("Approximate position of planet: [Local Time] {lct_hour}:{lct_min}:{lct_sec} [DST?] {is_daylight_saving} [Zone Correction] {zone_correction_hours} [Local Date] {local_date_month}/{local_date_day}/{local_date_year} [Planet] {planet_name} = [Right Ascension] {planet_ra_hour}h {planet_ra_min}m {planet_ra_sec}s [Declination] {planet_dec_deg}d {planet_dec_min}m {planet_dec_sec}s".format(lct_hour=self.lct_hour,lct_min=self.lct_min,lct_sec=self.lct_sec,is_daylight_saving=self.is_daylight_saving,zone_correction_hours=self.zone_correction_hours,local_date_day=self.local_date_day,local_date_month=self.local_date_month,local_date_year=self.local_date_year,planet_name=self.planet_name, planet_ra_hour=planet_ra_hour,planet_ra_min=planet_ra_min,planet_ra_sec=planet_ra_sec, planet_dec_deg=planet_dec_deg,planet_dec_min=planet_dec_min,planet_dec_sec=planet_dec_sec))

		self.assertEqual(planet_ra_hour,11,"Planet Right Ascension (hour)")
		self.assertEqual(planet_ra_min,11,"Planet Right Ascension (minutes)")
		self.assertEqual(planet_ra_sec,13.8,"Planet Right Ascension (seconds)")
		self.assertEqual(planet_dec_deg,6,"Planet Declination (degrees)")
		self.assertEqual(planet_dec_min,21,"Planet Declination (minutes)")
		self.assertEqual(planet_dec_sec,25.1,"Planet Declination (seconds)")


if __name__ == '__main__':
	UT.main()
