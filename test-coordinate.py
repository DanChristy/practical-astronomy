#!/usr/bin/python3

import lib.pa_coordinate as PC
import unittest as UT

def getDecimalDegrees(degrees,minutes,seconds):
	resultDecimalDegrees = round(PC.AngleToDecimalDegrees(degrees,minutes,seconds),7)

	return resultDecimalDegrees

class TestAngleDecimalDegrees(UT.TestCase):
	def setUp(self):
		self.degrees = 182
		self.minutes = 31
		self.seconds = 27

	def test_angle_to_decimal_degrees(self):
		resultDecimalDegrees = getDecimalDegrees(self.degrees,self.minutes,self.seconds)

		print("[Angle] {degrees}d {minutes}m {seconds}s = [Decimal Degrees] {decimalDegrees}".format(degrees=self.degrees,minutes=self.minutes,seconds=self.seconds,decimalDegrees=resultDecimalDegrees))

		self.assertEqual(resultDecimalDegrees,182.5241667,"Decimal Degrees")

	def test_decimal_degrees_to_angle(self):
		resultDecimalDegrees = getDecimalDegrees(self.degrees,self.minutes,self.seconds)

		revertDegrees,revertMinutes,revertSeconds = PC.DecimalDegreesToAngle(resultDecimalDegrees)

		print("[Decimal Degrees] {decimalDegrees} = [Angle] {degrees}d {minutes}m {seconds}s".format(decimalDegrees=resultDecimalDegrees,degrees=revertDegrees,minutes=revertMinutes,seconds=revertSeconds))

		self.assertEqual(revertDegrees,182,"Angle Degrees")
		self.assertEqual(revertMinutes,31,"Angle Minutes")
		self.assertEqual(revertSeconds,27,"Angle Seconds")

class test_right_ascension_hour_angle(UT.TestCase):
	def setUp(self):
		self.ra_hours = 18
		self.ra_minutes = 32
		self.ra_seconds = 21
		self.lct_hours = 14
		self.lct_minutes = 36
		self.lct_seconds = 51.67
		self.is_daylight_saving = False
		self.zone_correction = -4
		self.local_day = 22
		self.local_month = 4
		self.local_year = 1980
		self.geographical_longitude = -64

	def test_right_ascension_to_hour_angle(self):
		hour_angle_hours,hour_angle_minutes,hour_angle_seconds = PC.right_ascension_to_hour_angle(self.ra_hours,self.ra_minutes,self.ra_seconds,self.lct_hours,self.lct_minutes,self.lct_seconds,self.is_daylight_saving,self.zone_correction,self.local_day,self.local_month,self.local_year,self.geographical_longitude)

		print("[RA] {ra_hours}:{ra_minutes}:{ra_seconds} [LCT] {lct_hours}:{lct_minutes}:{lct_seconds} [DS] {is_daylight_saving} [ZC] {zone_correction} [LD] {local_month}/{local_day}/{local_year} [LON] {geographical_longitude} = [HA] {hour_angle_hours}:{hour_angle_minutes}:{hour_angle_seconds}".format(ra_hours=self.ra_hours,ra_minutes=self.ra_minutes,ra_seconds=self.ra_seconds,lct_hours=self.lct_hours,lct_minutes=self.lct_minutes,lct_seconds=self.lct_seconds,is_daylight_saving=self.is_daylight_saving,zone_correction=self.zone_correction,local_month=self.local_month,local_day=self.local_day,local_year=self.local_year,geographical_longitude=self.geographical_longitude,hour_angle_hours=hour_angle_hours,hour_angle_minutes=hour_angle_minutes,hour_angle_seconds=hour_angle_seconds))

		self.assertEqual(hour_angle_hours,9,"Hour Angle Hours")
		self.assertEqual(hour_angle_minutes,52,"Hour Angle Minutes")
		self.assertEqual(hour_angle_seconds,23.66,"Hour Angle Seconds")

	def test_hour_angle_to_right_ascension(self):
		hour_angle_hours,hour_angle_minutes,hour_angle_seconds = PC.right_ascension_to_hour_angle(self.ra_hours,self.ra_minutes,self.ra_seconds,self.lct_hours,self.lct_minutes,self.lct_seconds,self.is_daylight_saving,self.zone_correction,self.local_day,self.local_month,self.local_year,self.geographical_longitude)

		right_ascension_hours,right_ascension_minutes,right_ascension_seconds = PC.hour_angle_to_right_ascension(hour_angle_hours,hour_angle_minutes,hour_angle_seconds,self.lct_hours,self.lct_minutes,self.lct_seconds,self.is_daylight_saving,self.zone_correction,self.local_day,self.local_month,self.local_year,self.geographical_longitude)

		print("[HA] {hour_angle_hours}:{hour_angle_minutes}:{hour_angle_seconds} [LCT] {lct_hours}:{lct_minutes}:{lct_seconds} [DS] {is_daylight_saving} [ZC] {zone_correction} [LD] {local_month}/{local_day}/{local_year} [LON] {geographical_longitude} = [RA] {ra_hours}:{ra_minutes}:{ra_seconds}".format(hour_angle_hours=hour_angle_hours,hour_angle_minutes=hour_angle_minutes,hour_angle_seconds=hour_angle_seconds,lct_hours=self.lct_hours,lct_minutes=self.lct_minutes,lct_seconds=self.lct_seconds,is_daylight_saving=self.is_daylight_saving,zone_correction=self.zone_correction,local_month=self.local_month,local_day=self.local_day,local_year=self.local_year,geographical_longitude=self.geographical_longitude,ra_hours=right_ascension_hours,ra_minutes=right_ascension_minutes,ra_seconds=right_ascension_seconds))

		self.assertEqual(right_ascension_hours,18,"Right Ascension Hours")
		self.assertEqual(right_ascension_minutes,32,"Right Ascension Minutes")
		self.assertEqual(right_ascension_seconds,21,"Right Ascension Seconds")


if __name__ == '__main__':
	UT.main()
