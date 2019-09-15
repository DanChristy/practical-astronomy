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

class test_equatorial_coordinates_horizon_coordinates(UT.TestCase):
	def setUp(self):
		self.hour_angle_hours = 5
		self.hour_angle_minutes = 51
		self.hour_angle_seconds = 44
		self.declination_degrees = 23
		self.declination_minutes = 13
		self.declination_seconds = 10
		self.geographical_latitude = 52

	def test_equatorial_coordinates_to_horizon_coordinates(self):
		azimuth_degrees,azimuth_minutes,azimuth_seconds,altitude_degrees,altitude_minutes,altitude_seconds = PC.equatorial_coordinates_to_horizon_coordinates(self.hour_angle_hours,self.hour_angle_minutes,self.hour_angle_seconds,self.declination_degrees,self.declination_minutes,self.declination_seconds,self.geographical_latitude)

		print("[HA] {ha_hours}:{ha_minutes}:{ha_seconds} [DEC] {dec_degrees}d {dec_minutes}m {dec_seconds}s [LON] {geog_lat} = [AZ] {azimuth_degrees}d {azimuth_minutes}m {azimuth_seconds}s [ALT] {altitude_degrees}d {altitude_minutes}m {altitude_seconds}s".format(ha_hours=self.hour_angle_hours,ha_minutes=self.hour_angle_minutes,ha_seconds=self.hour_angle_seconds,dec_degrees=self.declination_degrees,dec_minutes=self.declination_minutes,dec_seconds=self.declination_seconds,geog_lat=self.geographical_latitude,azimuth_degrees=azimuth_degrees,azimuth_minutes=azimuth_minutes,azimuth_seconds=azimuth_seconds,altitude_degrees=altitude_degrees,altitude_minutes=altitude_minutes,altitude_seconds=altitude_seconds))

		self.assertEqual(azimuth_degrees,283,"Azimuth Degrees")
		self.assertEqual(azimuth_minutes,16,"Azimuth Minutes")
		self.assertEqual(azimuth_seconds,15.7,"Azimuth Seconds")
		self.assertEqual(altitude_degrees,19,"Altitude Degrees")
		self.assertEqual(altitude_minutes,20,"Altitude Minutes")
		self.assertEqual(altitude_seconds,3.64,"Altitude Seconds")

	def test_horizon_coordinates_to_equatorial_coordinates(self):
		azimuth_degrees,azimuth_minutes,azimuth_seconds,altitude_degrees,altitude_minutes,altitude_seconds = PC.equatorial_coordinates_to_horizon_coordinates(self.hour_angle_hours,self.hour_angle_minutes,self.hour_angle_seconds,self.declination_degrees,self.declination_minutes,self.declination_seconds,self.geographical_latitude)

		hour_angle_hours,hour_angle_minutes,hour_angle_seconds,declination_degrees,declination_minutes,declination_seconds = PC.horizon_coordinates_to_equatorial_coordinates(azimuth_degrees,azimuth_minutes,azimuth_seconds,altitude_degrees,altitude_minutes,altitude_seconds,self.geographical_latitude)

		print("[AZ] {azimuth_degrees}d {azimuth_minutes}m {azimuth_seconds}s [ALT] {altitude_degrees}d {altitude_minutes}m {altitude_seconds}s [LON] {geog_lat} = [HA] {ha_hours}:{ha_minutes}:{ha_seconds} [DEC] {dec_degrees}d {dec_minutes}m {dec_seconds}s)".format(azimuth_degrees=azimuth_degrees,azimuth_minutes=azimuth_minutes,azimuth_seconds=azimuth_seconds,altitude_degrees=altitude_degrees,altitude_minutes=altitude_minutes,altitude_seconds=altitude_seconds,geog_lat=self.geographical_latitude,ha_hours=hour_angle_hours,ha_minutes=hour_angle_minutes,ha_seconds=hour_angle_seconds,dec_degrees=declination_degrees,dec_minutes=declination_minutes,dec_seconds=declination_seconds))

		self.assertEqual(hour_angle_hours,5,"Hour Angle Hours")
		self.assertEqual(hour_angle_minutes,51,"Hour Angle Minutes")
		self.assertEqual(hour_angle_seconds,44,"Hour Angle Seconds")
		self.assertEqual(declination_degrees,23,"Declination Degrees")
		self.assertEqual(declination_minutes,13,"Declination Minutes")
		self.assertEqual(declination_seconds,10,"Declination Seconds")

class test_ecliptic(UT.TestCase):
	def setUp(self):
		pass

	def test_mean_obliquity_of_the_ecliptic(self):
		g_day = 6
		g_month = 7
		g_year = 2009

		obliquity = PC.mean_obliquity_of_the_ecliptic(g_day,g_month,g_year)
		obliquity = round(obliquity,8)

		print("[Greenwich Date] {g_month}/{g_day}/{g_year} = [Obliquity] {obliquity}".format(g_month=g_month,g_day=g_day,g_year=g_year,obliquity=obliquity))

		self.assertEqual(obliquity,23.43805531,"Obliquity")


if __name__ == '__main__':
	UT.main()
