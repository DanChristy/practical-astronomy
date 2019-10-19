#!/usr/bin/python3

import lib.pa_eclipses as PE
import unittest as UT

class test_lunar_eclipse_occurrence(UT.TestCase):
	def setUp(self):
		self.local_date_day = 1
		self.local_date_month = 4
		self.local_date_year = 2015
		self.is_daylight_saving = False
		self.zone_correction_hours = 10

	def test_lunar_eclipse_occurrence(self):
		status,event_date_day,event_date_month,event_date_year = PE.lunar_eclipse_occurrence(self.local_date_day,self.local_date_month,self.local_date_year,self.is_daylight_saving,self.zone_correction_hours)

		print(f"Lunar eclipse occurrence: [Local Date] {self.local_date_month}/{self.local_date_day}/{self.local_date_year} [DST?] {self.is_daylight_saving} [Zone Correction] {self.zone_correction_hours}h = [Status] {status} [Event Date] {event_date_month}/{event_date_day}/{event_date_year}")

		self.assertEqual(status,"Lunar eclipse certain","Lunar eclipse status")
		self.assertEqual(event_date_day,4,"Lunar eclipse event date (day)")
		self.assertEqual(event_date_month,4,"Lunar eclipse event date (month)")
		self.assertEqual(event_date_year,2015,"Lunar eclipse event date (year)")


if __name__ == '__main__':
	UT.main()
