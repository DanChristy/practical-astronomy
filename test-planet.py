#!/usr/bin/python3

import lib.pa_planet as PP
import unittest as UT

class test_position_of_planet(UT.TestCase):
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

		print(f"Approximate position of planet: [Local Time] {self.lct_hour}:{self.lct_min}:{self.lct_sec} [DST?] {self.is_daylight_saving} [Zone Correction] {self.zone_correction_hours} [Local Date] {self.local_date_month}/{self.local_date_day}/{self.local_date_year} [Planet] {self.planet_name} = [Right Ascension] {planet_ra_hour}h {planet_ra_min}m {planet_ra_sec}s [Declination] {planet_dec_deg}d {planet_dec_min}m {planet_dec_sec}s")

		self.assertEqual(planet_ra_hour,11,"Planet Right Ascension (hour)")
		self.assertEqual(planet_ra_min,11,"Planet Right Ascension (minutes)")
		self.assertEqual(planet_ra_sec,13.8,"Planet Right Ascension (seconds)")
		self.assertEqual(planet_dec_deg,6,"Planet Declination (degrees)")
		self.assertEqual(planet_dec_min,21,"Planet Declination (minutes)")
		self.assertEqual(planet_dec_sec,25.1,"Planet Declination (seconds)")

	def test_precise_position_of_planet(self):
		planet_ra_hour, planet_ra_min, planet_ra_sec, planet_dec_deg, planet_dec_min, planet_dec_sec = PP.precise_position_of_planet(self.lct_hour,self.lct_min,self.lct_sec,self.is_daylight_saving,self.zone_correction_hours,self.local_date_day,self.local_date_month,self.local_date_year,self.planet_name)

		print(f"Precise position of planet: [Local Time] {self.lct_hour}:{self.lct_min}:{self.lct_sec} [DST?] {self.is_daylight_saving} [Zone Correction] {self.zone_correction_hours} [Local Date] {self.local_date_month}/{self.local_date_day}/{self.local_date_year} [Planet] {self.planet_name} = [Right Ascension] {planet_ra_hour}h {planet_ra_min}m {planet_ra_sec}s [Declination] {planet_dec_deg}d {planet_dec_min}m {planet_dec_sec}s")

		self.assertEqual(planet_ra_hour,11,"Planet Right Ascension (hour)")
		self.assertEqual(planet_ra_min,10,"Planet Right Ascension (minutes)")
		self.assertEqual(planet_ra_sec,30.99,"Planet Right Ascension (seconds)")
		self.assertEqual(planet_dec_deg,6,"Planet Declination (degrees)")
		self.assertEqual(planet_dec_min,25,"Planet Declination (minutes)")
		self.assertEqual(planet_dec_sec,49.46,"Planet Declination (seconds)")

	def test_visual_aspects_of_a_planet(self):
		distance_au, ang_dia_arcsec, phase, light_time_hour, light_time_minutes, light_time_seconds, pos_angle_bright_limb_deg, approximate_magnitude = PP.visual_aspects_of_a_planet(self.lct_hour, self.lct_min, self.lct_sec, self.is_daylight_saving, self.zone_correction_hours, self.local_date_day, self.local_date_month, self.local_date_year, self.planet_name)

		print(f"Visual aspects of planet: [Local Time] {self.lct_hour}:{self.lct_min}:{self.lct_sec} [DST?] {self.is_daylight_saving} [Zone Correction] {self.zone_correction_hours} [Local Date] {self.local_date_month}/{self.local_date_day}/{self.local_date_year} [Planet] {self.planet_name} = [Distance] {distance_au} au [Angular Diameter] {ang_dia_arcsec} arcsec [Phase] {phase} [Light Time] {light_time_hour}:{light_time_minutes}:{light_time_seconds} [Position Angle of Bright Limb] {pos_angle_bright_limb_deg}d [Magnitude] {approximate_magnitude}")

		self.assertEqual(distance_au,5.59829,"Distance - AU")
		self.assertEqual(ang_dia_arcsec,35.1,"Angular Diameter - arcsec")
		self.assertEqual(phase,0.99,"Phase")
		self.assertEqual(light_time_hour,0,"Light Time - hour part")
		self.assertEqual(light_time_minutes,46,"Light Time - minutes part")
		self.assertEqual(light_time_seconds,33.32,"Light Time - seconds part")
		self.assertEqual(pos_angle_bright_limb_deg,113.2,"Position Angle of Bright Limb - degrees")
		self.assertEqual(approximate_magnitude,-2,"Approximate Magnitude")


if __name__ == '__main__':
	UT.main()
