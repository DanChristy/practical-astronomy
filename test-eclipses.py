#!/usr/bin/python3

import lib.pa_eclipses as PE
import unittest as UT

class test_lunar_eclipse(UT.TestCase):
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

	def test_lunar_eclipse_circumstances(self):
		lunar_eclipse_certain_date_day, lunar_eclipse_certain_date_month, lunar_eclipse_certain_date_year, ut_start_pen_phase_hour, ut_start_pen_phase_minutes, ut_start_umbral_phase_hour, ut_start_umbral_phase_minutes, ut_start_total_phase_hour, ut_start_total_phase_minutes, ut_mid_eclipse_hour, ut_mid_eclipse_minutes, ut_end_total_phase_hour, ut_end_total_phase_minutes, ut_end_umbral_phase_hour, ut_end_umbral_phase_minutes, ut_end_pen_phase_hour, ut_end_pen_phase_minutes, eclipse_magnitude = PE.lunar_eclipse_circumstances(self.local_date_day,self.local_date_month,self.local_date_year,self.is_daylight_saving,self.zone_correction_hours)

		print(f"Lunar eclipse circumstances: [Local Date] {self.local_date_month}/{self.local_date_day}/{self.local_date_year} [DST?] {self.is_daylight_saving} [Zone Correction] {self.zone_correction_hours} = [Eclipse Date] {lunar_eclipse_certain_date_month}/{lunar_eclipse_certain_date_day}/{lunar_eclipse_certain_date_year} [Start Penumbral Phase] {ut_start_pen_phase_hour}:{ut_start_pen_phase_minutes} [Start Umbral Phase] {ut_start_umbral_phase_hour}:{ut_start_umbral_phase_minutes} [Start Total Phase] {ut_start_total_phase_hour}:{ut_start_total_phase_minutes} [Mid Eclipse] {ut_mid_eclipse_hour}:{ut_mid_eclipse_minutes} [End Total Phase] {ut_end_total_phase_hour}:{ut_end_total_phase_minutes} [End Umbral Phase] {ut_end_umbral_phase_hour}:{ut_end_umbral_phase_minutes} [End Penumbral Phase] {ut_end_pen_phase_hour}:{ut_end_pen_phase_minutes} [Magnitude] {eclipse_magnitude}")

		self.assertEqual(lunar_eclipse_certain_date_day,4,"Eclipse Date (day)")
		self.assertEqual(lunar_eclipse_certain_date_month,4,"Eclipse Date (month)")
		self.assertEqual(lunar_eclipse_certain_date_year,2015,"Eclipse Date (year)")
		self.assertEqual(ut_start_pen_phase_hour,9,"Start Penumbral Phase (hour)")
		self.assertEqual(ut_start_pen_phase_minutes,0,"Start Penumbral Phase (minutes)")
		self.assertEqual(ut_start_umbral_phase_hour,10,"Start Umbral Phase (hour)")
		self.assertEqual(ut_start_umbral_phase_minutes,16,"Start Umbral Phase (minutes)")
		self.assertEqual(ut_start_total_phase_hour,11,"Start Total Phase (hour)")
		self.assertEqual(ut_start_total_phase_minutes,55,"Start Total Phase (minutes)")
		self.assertEqual(ut_mid_eclipse_hour,12,"Mid Eclipse (hour)")
		self.assertEqual(ut_mid_eclipse_minutes,1,"Mid Eclipse (minutes)")
		self.assertEqual(ut_end_total_phase_hour,12,"End Total Phase (hour)")
		self.assertEqual(ut_end_total_phase_minutes,7,"End Total Phase (minutes)")
		self.assertEqual(ut_end_umbral_phase_hour,13,"End Umbral Phase (hour)")
		self.assertEqual(ut_end_umbral_phase_minutes,46,"End Umbral Phase (minutes)")
		self.assertEqual(ut_end_pen_phase_hour,15,"End Penumbral Phase (hour)")
		self.assertEqual(ut_end_pen_phase_minutes,1,"End Penumbral Phase (minutes)")
		self.assertEqual(eclipse_magnitude,1.01,"Eclipse Magnitude")

class test_solar_eclipse(UT.TestCase):
	def setUp(self):
		self.local_date_day = 1
		self.local_date_month = 4
		self.local_date_year = 2015
		self.is_daylight_saving = False
		self.zone_correction_hours = 0

	def test_solar_eclipse_occurrence(self):
		status,event_date_day,event_date_month,event_date_year = PE.solar_eclipse_occurrence(self.local_date_day,self.local_date_month,self.local_date_year,self.is_daylight_saving,self.zone_correction_hours)

		print(f"Solar eclipse occurrence: [Local Date] {self.local_date_month}/{self.local_date_day}/{self.local_date_year} [DST?] {self.is_daylight_saving} [Zone Correction] {self.zone_correction_hours}h = [Status] {status} [Event Date] {event_date_month}/{event_date_day}/{event_date_year}")

		self.assertEqual(status,"Solar eclipse certain","Lunar eclipse status")
		self.assertEqual(event_date_day,20,"Solar eclipse event date (day)")
		self.assertEqual(event_date_month,3,"Solar eclipse event date (month)")
		self.assertEqual(event_date_year,2015,"Solar eclipse event date (year)")


if __name__ == '__main__':
	UT.main()
