#!/usr/bin/python3

import lib.pa_sun as PS
import unittest as UT

class test_position_of_sun(UT.TestCase):
	def setUp(self):
		self.lct_hours = 0
		self.lct_minutes = 0
		self.lct_seconds = 0
		self.local_day = 27
		self.local_month = 7
		self.local_year = 2003
		self.is_daylight_saving = False
		self.zone_correction = 0

	def test_approximate_position_of_sun(self):
		sun_ra_hour,sun_ra_min,sun_ra_sec,sun_dec_deg,sun_dec_min,sun_dec_sec = PS.approximate_position_of_sun(self.lct_hours, self.lct_minutes, self.lct_seconds, self.local_day, self.local_month, self.local_year, self.is_daylight_saving, self.zone_correction)

		print("Approximate position of the sun: [Local Time] {lct_hours}:{lct_minutes}:{lct_seconds} [Local Day] {local_month}/{local_day}/{local_year} [DST] {is_daylight_saving} [Zone Correction] {zone_correction} = [Sun] [RA] {sun_ra_hour}:{sun_ra_min}:{sun_ra_sec} [Dec] {sun_dec_deg}d {sun_dec_min}m {sun_dec_sec}s".format(lct_hours=self.lct_hours,lct_minutes=self.lct_minutes,lct_seconds=self.lct_seconds,local_month=self.local_month,local_day=self.local_day,local_year=self.local_year,is_daylight_saving=self.is_daylight_saving,zone_correction=self.zone_correction,sun_ra_hour=sun_ra_hour,sun_ra_min=sun_ra_min,sun_ra_sec=sun_ra_sec,sun_dec_deg=sun_dec_deg,sun_dec_min=sun_dec_min,sun_dec_sec=sun_dec_sec))

		self.assertEqual(sun_ra_hour,8,"Sun RA Hour")
		self.assertEqual(sun_ra_min,23,"Sun RA Minutes")
		self.assertEqual(sun_ra_sec,33.73,"Sun RA Seconds")
		self.assertEqual(sun_dec_deg,19,"Sun Dec Degrees")
		self.assertEqual(sun_dec_min,21,"Sun Dec Minutes")
		self.assertEqual(sun_dec_sec,14.33,"Sun Dec Seconds")

if __name__ == '__main__':
	UT.main()
